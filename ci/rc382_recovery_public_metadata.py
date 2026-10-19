#!/usr/bin/env python3
"""Export ONLY the P-256 recovery public JWK from an already-configured signer.

Owner-only, isolated branch. No feed signing, file publication, release, or
changes to the protected Windows RC3.8.0. Private PEM is never serialized.
"""
from __future__ import annotations
import base64
import hashlib
import json
import os
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec


def encode_axis(value: int) -> str:
    return base64.urlsafe_b64encode(value.to_bytes(32, "big")).rstrip(b"=").decode("ascii")


def public_metadata_from_private_pem(raw: bytes) -> dict:
    signer = serialization.load_pem_private_key(raw, password=None)
    if not isinstance(signer, ec.EllipticCurvePrivateKey) or not isinstance(signer.curve, ec.SECP256R1):
        raise ValueError("Recovery signing secret must be an EC P-256 private key")
    pub = signer.public_key()
    coords = pub.public_numbers()
    jwk = {
        "kty": "EC", "crv": "P-256", "x": encode_axis(coords.x),
        "y": encode_axis(coords.y), "ext": True,
    }
    encoded = pub.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
    fingerprint = hashlib.sha256(encoded).hexdigest()
    recovered_pub = ec.EllipticCurvePublicNumbers(
        int.from_bytes(base64.urlsafe_b64decode(jwk["x"] + "="), "big"),
        int.from_bytes(base64.urlsafe_b64decode(jwk["y"] + "="), "big"),
        ec.SECP256R1(),
    ).public_key()
    if recovered_pub.public_numbers() != coords:
        raise ValueError("Public JWK round-trip mismatch")
    return {
        "purpose": "DTC_NEXIS_OWNER_TRIAL_RECOVERY",
        "status": "NOT_ACTIVE_REQUIRES_TRUSTED_BOOTSTRAP",
        "public_jwk": jwk,
        "fingerprint_sha256": fingerprint,
    }


def main() -> None:
    raw = os.environ.get("NEXIS_OWNER_RECOVERY_SIGNER_KEY_PEM", "").encode("utf-8")
    if not raw:
        raise SystemExit("FAIL: recovery signing secret not available")
    try:
        metadata = public_metadata_from_private_pem(raw)
    except (ValueError, TypeError) as exc:
        raise SystemExit("FAIL: recovery public key derivation unsuccessful") from None
    path_text = os.environ.get("RECOVERY_PUBLIC_METADATA_PATH", "")
    runner_temp = os.environ.get("RUNNER_TEMP", "")
    if not path_text or not runner_temp:
        raise SystemExit("FAIL: public-only output path not set")
    parent = Path(runner_temp).resolve()
    destination = Path(path_text).resolve()
    if destination.parent != parent or destination.name != "owner-recovery-public.jwk.json":
        raise SystemExit("FAIL: public metadata must remain in the runner's temporary directory")
    with destination.open("x", encoding="utf-8") as handle:
        json.dump(metadata, handle, separators=(",", ":"))
        handle.write("\n")
    print("PASS: public-only P-256 recovery metadata derived from configured signer")
    print("PUBLIC_RECOVERY_METADATA=" + json.dumps(metadata, separators=(",", ":")))
    print("NOT ACTIVE: no update feed or Windows trust anchor changed")


if __name__ == "__main__":
    main()
