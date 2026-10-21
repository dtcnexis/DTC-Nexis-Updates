#!/usr/bin/env python3
"""R10 readiness regression: no owner secrets, no feed publication, synthetic test key."""
import base64
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

sys.path.insert(0, str(Path(__file__).resolve().parent))
import owner_r10_readiness as m

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "owner-review/rc382-guide-r10"
CANDIDATE = ASSETS / "guide-v10-unsigned.json"


def public_jwk(private):
    n = private.public_key().public_numbers()
    enc = lambda v: base64.urlsafe_b64encode(v.to_bytes(32, "big")).rstrip(b"=").decode()
    return {"kty": "EC", "crv": "P-256", "x": enc(n.x), "y": enc(n.y), "ext": True}


class R10OwnerSigningReadiness(unittest.TestCase):
    def setUp(self):
        t = tempfile.TemporaryDirectory()
        self.addCleanup(t.cleanup)
        self.root = Path(t.name)
        self.key = ec.generate_private_key(ec.SECP256R1())
        self.public = public_jwk(self.key)
        self.jwk = self.root / "pinned-public.json"
        self.jwk.write_text(json.dumps(self.public))
        self.old = {
            "app": "DTCNexis", "version": "RC3.8.2-owner-v9-data",
            "versionCode": 7,
            "catalog": {"versionCode": 9, "url": "https://example.invalid/old.json", "sha256": "a" * 64},
            "notes": "Original unchanged catalog",
        }
        self.feed = self.root / "signed-r9.json"
        self.feed.write_text(json.dumps(m.sign(self.key, self.old)))
        self.pem = self.key.private_bytes(
            serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption()).decode()

    def test_original_review_bytes_and_contract(self):
        actual, amount = m.review_candidate(CANDIDATE, ASSETS)
        self.assertEqual(actual["revision"], 10)
        self.assertEqual(amount, 48882)
        self.assertEqual(set(m.APPROVED), {c["id"] for c in actual["cards"]})

    def test_sign_two_layers_only_when_original_matches(self):
        report = m.audit(self.feed, self.jwk, CANDIDATE, ASSETS, secret=self.pem)
        self.assertTrue(report["original_signer_attested"])
        self.assertFalse(report["signed_and_published"])
        self.assertFalse(report["ready_for_in_app_install"])

    def test_without_secret_does_not_sign(self):
        report = m.audit(self.feed, self.jwk, CANDIDATE, ASSETS)
        self.assertFalse(report["original_signer_attested"])
        self.assertTrue(report["validated_v9_signed_feed"])

    def test_recovery_or_different_key_rejected(self):
        replacement = ec.generate_private_key(ec.SECP256R1())
        raw = replacement.private_bytes(serialization.Encoding.PEM,
             serialization.PrivateFormat.PKCS8, serialization.NoEncryption()).decode()
        with self.assertRaisesRegex(m.ReadinessError, "NOT original"):
            m.audit(self.feed, self.jwk, CANDIDATE, ASSETS, secret=raw)

    def test_revision_replay_rollback_rejected(self):
        with self.assertRaisesRegex(m.ReadinessError, "replay/rollback"):
            m.audit(self.feed, self.jwk, CANDIDATE, ASSETS, installed_revision=10)

    def test_original_feed_tamper_rejected(self):
        envelope = json.loads(self.feed.read_text())
        envelope["signature"] = base64.b64encode(b"X" * 64).decode()
        self.feed.write_text(json.dumps(envelope))
        with self.assertRaisesRegex(m.ReadinessError, "Signature failed"):
            m.audit(self.feed, self.jwk, CANDIDATE, ASSETS)

    def test_approved_webp_tamper_rejected(self):
        other = self.root / "asset-copy"
        shutil.copytree(ASSETS, other)
        target = other / "images" / "wiring_diagrams.webp"
        b = bytearray(target.read_bytes())
        b[26] ^= 1
        target.write_bytes(b)
        with self.assertRaisesRegex(m.ReadinessError, "bytes changed"):
            m.audit(self.feed, self.jwk, other / "guide-v10-unsigned.json", other)

    def test_bad_metadata_download_url_rejected(self):
        doc = json.loads(CANDIDATE.read_text(encoding="utf-8"))
        doc["cards"][0]["url"] = "https://attacker.invalid/wiring_diagrams.webp"
        invalid = self.root / "invalid.json"
        invalid.write_text(json.dumps(doc))
        with self.assertRaisesRegex(m.ReadinessError, "Unexpected owner channel URL"):
            m.audit(self.feed, self.jwk, invalid, ASSETS)


if __name__ == "__main__":
    unittest.main(verbosity=2)
