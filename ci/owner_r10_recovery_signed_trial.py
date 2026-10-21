#!/usr/bin/env python3
"""DTC NEXIS RC3.8.2: R10 real WebP metadata and real recovery signer, CI ONLY.

Construct both owner R10 Guide and owner R10 DATA-ONLY feed signed envelopes in
MEMORY ONLY. Validate both using the independently pinned recovery public key.
NEVER export the envelopes, alter R9, publish, upload artifacts, change secrets,
or claim that the installed R9 program can accept the recovery key.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

from owner_r10_readiness import (
    APPROVED, ReadinessError, key_from_jwk, original_feed,
    review_candidate, sign, verify_envelope,
)
from owner_recovery_secret_attestation import (
    read_public, RECOVERY_X, RECOVERY_Y, RECOVERY_SHA256, LEGACY_X, LEGACY_Y,
)

ALLOWED_OUTER_FIELDS = frozenset((
    "app", "version", "versionCode", "notes", "ownerTrustEpoch",
    "ownerDataRevision", "catalog", "images", "guide",
))
SIGNED_GUIDE_SCHEMA = "dtcnexis.signed-guide.v1"
REQUIRED_CHANNEL = "owner-stable-data-channel/owner-channel/packages/guide-v10/"
LABEL = "OWNER TEST ONLY: R10 double signed data-only payload; NO DOWNLOAD, NO INSTALL"


def require(value: bool, msg: str) -> None:
    if not value:
        raise ReadinessError(msg)


def read_real_secret() -> ec.EllipticCurvePrivateKey:
    pem = os.environ.get("NEXIS_OWNER_RECOVERY_SIGNER_KEY_PEM", "")
    require(pem.startswith("-----BEGIN"), "Recovery signer Secret missing")
    try:
        private = serialization.load_pem_private_key(pem.encode("utf-8"), password=None)
    except (ValueError, TypeError):
        raise ReadinessError("Recovery signer unreadable") from None
    require(isinstance(private, ec.EllipticCurvePrivateKey)
            and isinstance(private.curve, ec.SECP256R1),
            "Recovery signer must be P-256")
    recovery = read_public(RECOVERY_X, RECOVERY_Y)
    legacy = read_public(LEGACY_X, LEGACY_Y)
    require(private.public_key().public_numbers() == recovery.public_numbers(),
            "GitHub Secret is NOT the approved recovery signer")
    require(private.public_key().public_numbers() != legacy.public_numbers(),
            "Recovery and original R9 signer unexpectedly identical")
    from cryptography.hazmat.primitives import serialization as s
    fingerprint = hashlib.sha256(recovery.public_bytes(
        s.Encoding.DER, s.PublicFormat.SubjectPublicKeyInfo)).hexdigest()
    require(fingerprint == RECOVERY_SHA256, "Unapproved recovery signer fingerprint")
    return private


def verify_candidate(envelope: dict, recovery: ec.EllipticCurvePublicKey, approved_doc: dict) -> dict:
    outer = verify_envelope(envelope, recovery)
    require(set(outer).issubset(ALLOWED_OUTER_FIELDS), "Unsupported R10 feed field")
    require(set(outer) == {"app", "version", "versionCode", "notes",
                          "ownerTrustEpoch", "ownerDataRevision", "guide"},
            "R10 trial must contain a guide and no executable, catalog or image update")
    require(outer["app"] == "DTCNexis" and type(outer["versionCode"]) is int
            and outer["versionCode"] == 7, "Unexpected app/versionCode")
    require(outer["ownerTrustEpoch"] == 1 and type(outer["ownerTrustEpoch"]) is int
            and type(outer["ownerDataRevision"]) is int
            and outer["ownerDataRevision"] == 10, "Recovery revision/epoch changed")
    require(isinstance(outer["version"], str) and isinstance(outer["notes"], str),
            "Missing feed label")
    nested = verify_envelope(outer["guide"], recovery)
    require(nested == approved_doc and nested["schema"] == SIGNED_GUIDE_SCHEMA
            and type(nested["revision"]) is int and nested["revision"] == 10,
            "Inner Guide signature or revision changed")
    require(len(nested["cards"]) == 4, "R10 four-card boundary changed")
    for card in nested["cards"]:
        require(REQUIRED_CHANNEL in card["url"], "Unexpected future image channel")
    return outer


def run(live: Path, legacy_jwk: Path, candidate: Path, assets: Path) -> None:
    # Verify the *actual* published R9 feed before any new signing.
    old_pub = key_from_jwk(json.loads(legacy_jwk.read_text(encoding="utf-8")))
    require(old_pub.public_numbers() == read_public(LEGACY_X, LEGACY_Y).public_numbers(),
            "Original R9 verification key changed")
    old = original_feed(live, old_pub)
    require(old.get("catalog", {}).get("versionCode") == 9,
            "Original R9 catalog reference changed")

    # Image bytes, lengths, SHA256, approval metadata, pixel dimensions,
    # future owner URL allowlist and staged review-branch image copies.
    guide, total_bytes = review_candidate(candidate, assets)
    require(total_bytes == 48882 and len(guide["cards"]) == len(APPROVED),
            "Four original WebP assets not byte-identical to owner-approved ones")
    require(guide["revision"] == 10 and guide["schema"] == SIGNED_GUIDE_SCHEMA,
            "Guide schema/revision mismatch")

    private = read_real_secret()
    recovery = read_public(RECOVERY_X, RECOVERY_Y)

    # No signed envelopes or PEMs are written to files, git, logs or artifacts.
    inner = sign(private, guide)
    outer = {
        "app": "DTCNexis",
        "version": "RC3.8.2-owner-r10-recovery-ci-rehearsal",
        "versionCode": 7,
        "notes": LABEL,
        "ownerTrustEpoch": 1,
        "ownerDataRevision": 10,
        "guide": inner,
    }
    feed = sign(private, outer)
    verified = verify_candidate(feed, recovery, guide)
    require(verified["ownerDataRevision"] > old["catalog"]["versionCode"],
            "R10 is not newer than R9")

    # Rejection proofs: tamper with each signed layer, and reject old signer.
    altered = json.loads(json.dumps(feed))
    altered["signature"] = base64.b64encode(b"\x00" * 64).decode("ascii")
    try:
        verify_candidate(altered, recovery, guide)
    except (ReadinessError, InvalidSignature):
        pass
    else:
        raise ReadinessError("Tampered outer feed was accepted")

    bad_guide = json.loads(json.dumps(inner))
    bad_guide["signature"] = base64.b64encode(b"\x00" * 64).decode("ascii")
    try:
        verify_envelope(bad_guide, recovery)
    except (ReadinessError, InvalidSignature):
        pass
    else:
        raise ReadinessError("Tampered inner guide was accepted")

    try:
        verify_envelope(feed, old_pub)
    except (ReadinessError, InvalidSignature):
        pass
    else:
        raise ReadinessError("R9 public key unexpectedly accepted recovery R10 feed")

    # An earlier/stale R9 client MUST reject this feed. No channel reset.
    require(old_pub.public_numbers() != recovery.public_numbers(),
            "Trust-rotation not isolated")

    print("PASS: actual signed owner R9 feed verified and preserved.")
    print("PASS: 4 owner-approved REAL WebPs; 48,882 bytes; checked pixels, hashes and future pinned URLs.")
    print("PASS: REAL GitHub recovery signer signed BOTH R10 Guide and R10 data-only feed in CI memory.")
    print("PASS: pinned recovery public JWK verifies BOTH signed layers; old R9 key rejects them.")
    print("PASS: tampered outer/inner signatures rejected; data revision 10 above original catalog 9.")
    print("BLOCKED BY DESIGN: R9-installed Windows client does not yet trust recovery signer.")
    print("BLOCKED BY DESIGN: stable-channel WebP asset paths not yet published.")
    print("NOT A RELEASE: no feed JSON, signed envelope, installer, artifact, or private key exported.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--live", type=Path, required=True)
    p.add_argument("--legacy-jwk", type=Path, required=True)
    p.add_argument("--candidate", type=Path,
                   default=Path("owner-review/rc382-guide-r10/guide-v10-unsigned.json"))
    p.add_argument("--assets", type=Path, default=Path("owner-review/rc382-guide-r10"))
    a = p.parse_args()
    try:
        run(a.live, a.legacy_jwk, a.candidate, a.assets)
    except (ValueError, TypeError, KeyError, OSError) as exc:
        # Do not emit PEM, signed data or a traceback sourced from Secret bytes.
        print("BLOCKED: isolated owner R10 signing readiness failed: " + str(exc), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
