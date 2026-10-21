#!/usr/bin/env python3
"""RC3.8.2 R10 owner Guide readiness. Test branch only; never publishes or saves signed feed.

On manual owner authorization, attest the ORIGINAL P-256 signer using
NEXIS_OWNER_TRIAL_SIGNER_KEY_PEM in memory. Recovery keys are NEVER accepted.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils
from PIL import Image

PREFIX = ("https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/"
          "owner-stable-data-channel/owner-channel/packages/guide-v10/")
SCHEMA = "dtcnexis.signed-guide.v1"
APPROVED = {
    "wiring_diagrams": ("db81eb1c202a2ea3f09213be747b13b0ac4990e74a8ca7956cc7f372495b5c3e", 15884),
    "remote_key_maintenance": ("87ba05e803921537a765c38b58891dbd80f1047f8b057e901895eb7dea38f9e0", 9754),
    "timing_belt_chain": ("fa6a68a32435357fe3e25a6d5794835390b0e7c957b519a8dce6268e508fde46", 12322),
    "torque_specifications": ("05fa800456753aec254d673e73b5e67719487a9b2bbb1f17ae456e6e0bea2014", 10922),
}


class ReadinessError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise ReadinessError(message)


def key_from_jwk(doc):
    require(isinstance(doc, dict) and doc.get("kty") == "EC"
            and doc.get("crv") == "P-256" and "d" not in doc, "Untrusted public key")
    try:
        coordinates = []
        for axis in ("x", "y"):
            part = doc[axis]
            require(isinstance(part, str) and len(part) == 43, "Invalid public key coordinate")
            coordinates.append(int.from_bytes(base64.urlsafe_b64decode(part + "="), "big"))
        return ec.EllipticCurvePublicNumbers(
            *coordinates, ec.SECP256R1()).public_key()
    except (KeyError, TypeError, ValueError) as e:
        raise ReadinessError("Invalid pinned owner P-256 JWK") from e


def verify_envelope(envelope, public):
    require(isinstance(envelope, dict) and set(envelope) == {"payload", "signature"},
            "Invalid signed envelope shape")
    try:
        payload = base64.b64decode(envelope["payload"], validate=True)
        signature = base64.b64decode(envelope["signature"], validate=True)
        require(0 < len(payload) < 100_000 and len(signature) == 64,
                "Invalid signature or payload length")
        r, s = int.from_bytes(signature[:32], "big"), int.from_bytes(signature[32:], "big")
        public.verify(utils.encode_dss_signature(r, s), payload, ec.ECDSA(hashes.SHA256()))
        return json.loads(payload)
    except (ValueError, TypeError, InvalidSignature, KeyError, UnicodeError) as e:
        raise ReadinessError("Signature failed verification against original pinned key") from e


def original_feed(path, public):
    signed = json.loads(Path(path).read_text(encoding="utf-8"))
    old = verify_envelope(signed, public)
    require(old.get("app") == "DTCNexis" and old.get("versionCode") == 7,
            "Unexpected live owner feed format")
    require(isinstance(old.get("catalog"), dict)
            and old["catalog"].get("versionCode") == 9
            and "guide" not in old and "windows" not in old,
            "Original live R9 contract changed; no automatic update")
    return old


def review_candidate(path, assets_root, *, installed_revision=9):
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    require(isinstance(doc, dict) and set(doc) == {"schema", "revision", "cards"}
            and doc["schema"] == SCHEMA, "Unsupported R10 guide contract")
    require(type(doc["revision"]) is int and doc["revision"] == 10
            and doc["revision"] > installed_revision, "R10 replay/rollback rejected")
    cards = doc["cards"]
    require(isinstance(cards, list) and len(cards) == 4,
            "Exactly four approved cards are required")
    require({c.get("id") for c in cards if isinstance(c, dict)} == set(APPROVED),
            "Missing or duplicated approved card")
    total = 0
    for card in cards:
        ident = card["id"]
        require(set(card) == {"id", "label", "topic", "sha256", "bytes", "mime",
                             "url", "buttons"}, "Unexpected executable or card property")
        digest, size = APPROVED[ident]
        require(card["sha256"] == digest and type(card["bytes"]) is int
                and card["bytes"] == size and card["mime"] == "image/webp",
                "Owner-approved SHA-256 mismatch")
        require(card["url"] == PREFIX + ident + ".webp", "Unexpected owner channel URL")
        # Transport uses these action identifiers; UI independently presents YouTube, Google, PDF.
        require(card["buttons"] == ["google", "youtube", "pdf"],
                "Changed transport action identifiers")
        label = card["label"]
        require(isinstance(label, dict) and set(label) == {"ar", "en", "sv"}
                and all(isinstance(label[k], str) and 3 <= len(label[k]) <= 100
                        for k in ("ar", "en", "sv")), "Incomplete localization")
        require(isinstance(card["topic"], str) and 12 <= len(card["topic"]) < 160,
                "Invalid card search topic")
        asset = Path(assets_root) / "images" / (ident + ".webp")
        require(asset.is_file() and not asset.is_symlink(), "Approved WebP missing")
        raw = asset.read_bytes()
        require(len(raw) == size and hashlib.sha256(raw).hexdigest() == digest,
                "Approved WebP bytes changed")
        require(raw[:4] == b"RIFF" and raw[8:12] == b"WEBP", "Non-WebP image rejected")
        try:
            with Image.open(io.BytesIO(raw)) as img:
                require(img.format == "WEBP" and img.mode in ("RGB", "RGBA")
                        and img.size == (352, 272), "Unexpected image format/dimensions")
                img.verify()
        except (OSError, Image.DecompressionBombError) as e:
            raise ReadinessError("Corrupt WebP image") from e
        total += len(raw)
    manifest = json.loads((Path(assets_root) / "manifest.json").read_text(encoding="utf-8"))
    require(manifest.get("owner_review", {}).get("status")
            == "approved_for_private_rc382_testing", "Review status not approved")
    require(manifest.get("status") == "NOT_SIGNED_NOT_PUBLISHED",
            "Review files must not claim release")
    require({x["id"]: (x["sha256"], x["bytes"]) for x in manifest["images"]}
            == APPROVED, "Independent image review fingerprint changed")
    return doc, total


def sign(private, obj):
    raw = json.dumps(obj, ensure_ascii=False, separators=(",",":"),
                     allow_nan=False).encode("utf-8")
    der = private.sign(raw, ec.ECDSA(hashes.SHA256()))
    r, s = utils.decode_dss_signature(der)
    return {"payload": base64.b64encode(raw).decode(),
            "signature": base64.b64encode(r.to_bytes(32, "big") + s.to_bytes(32, "big")).decode()}


def attest_private_signer(pem, public, old, guide):
    """In-memory only: no PEM, signed envelope or private details printed or stored."""
    require(isinstance(pem, str) and pem.startswith("-----BEGIN"),
            "Original signing credential unavailable")
    try:
        private = serialization.load_pem_private_key(pem.encode("utf-8"), password=None)
    except (ValueError, TypeError) as e:
        raise ReadinessError("Signing credential cannot be opened") from e
    require(isinstance(private, ec.EllipticCurvePrivateKey)
            and isinstance(private.curve, ec.SECP256R1),
            "Only original P-256 owner signing identity allowed")
    require(private.public_key().public_numbers() == public.public_numbers(),
            "Owner signer NOT original R9 key; trust rotation forbidden")
    nested = sign(private, guide)
    require(verify_envelope(nested, public) == guide, "Inner Guide signing test failed")
    outer = dict(old)
    outer["version"] = "RC3.8.2-owner-r10-guide-private-stage"
    outer["guide"] = nested
    outer["notes"] = "Owner-only R10 review; no executable or Windows installer"
    signed = sign(private, outer)
    verified = verify_envelope(signed, public)
    require(verified == outer and verified["catalog"] == old["catalog"]
            and verified["versionCode"] == old["versionCode"]
            and verify_envelope(verified["guide"], public) == guide,
            "Nested envelope or prior catalog changed")
    return True


def audit(live, jwk, candidate, asset_root, secret=None, installed_revision=9):
    public = key_from_jwk(json.loads(Path(jwk).read_text(encoding="utf-8")))
    old = original_feed(live, public)
    guide, total = review_candidate(candidate, asset_root,
                                     installed_revision=installed_revision)
    signed = False
    if secret is not None:
        signed = attest_private_signer(secret, public, old, guide)
    return {"validated_v9_signed_feed": True, "guide_revision": guide["revision"],
            "approved_webp_count": 4, "approved_webp_bytes": total,
            "rollback_guard": "PASS", "original_signer_attested": signed,
            "signed_and_published": False,
            "live_image_urls_exist": "NOT_VERIFIED; DO NOT ACTIVATE",
            "ready_for_in_app_install": False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--live", required=True, help="Unmodified owner-stable signed R9 JSON")
    p.add_argument("--jwk", required=True, help="Original pinned public key, never recovery key")
    p.add_argument("--candidate", default="owner-review/rc382-guide-r10/guide-v10-unsigned.json")
    p.add_argument("--assets", default="owner-review/rc382-guide-r10")
    p.add_argument("--attest-secret", action="store_true", help="Manual owner-approved CI only")
    args = p.parse_args()
    try:
        out = audit(args.live, args.jwk, args.candidate, args.assets,
                    secret=os.environ.get("NEXIS_OWNER_TRIAL_SIGNER_KEY_PEM")
                    if args.attest_secret else None)
    except (ReadinessError, ValueError, KeyError, OSError) as e:
        print("BLOCKED:", str(e))
        raise SystemExit(2)
    print(json.dumps(out, sort_keys=True))
    if not args.attest_secret:
        print("CHECK ONLY: original private signer was not accessed; R10 is NOT signed/published.")


if __name__ == "__main__":
    main()
