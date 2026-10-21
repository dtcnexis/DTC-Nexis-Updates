#!/usr/bin/env python3
"""Isolated owner recovery Secret -> pinned public key attestation.

Reads only NEXIS_OWNER_RECOVERY_SIGNER_KEY_PEM from job memory.
Signs a synthetic, non-installable message; never creates a feed, release,
data package, Windows installer, private-key file or signed artifact.
"""
from __future__ import annotations

import base64
import hashlib
import os
import sys

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

# The approved owner recovery public JWK is already pinned in the App's
# ci/owner_recovery_public_trial.jwk.json and recovery runtime.
RECOVERY_X = "hMttwEHK_1Ni8qj4NFbIs71O0dfAK_cKw8LsmyLwUf4"
RECOVERY_Y = "RKxaGcPmrGDgL7vCF6Im93nxtk9uEpdmMFfJbVNADPc"
RECOVERY_SHA256 = "6ed08e270c7e87c9c79377078a7d2f36689a047b8533b9f62842ff3ccfe3f45a"
LEGACY_X = "JIetTxXdoW4RP-wu8gYoBzTTFT-CSkWbG1XRz_stPu4"
LEGACY_Y = "cngeyubF_hsBftfTYK59wbpvmZPe9XXD-p933_EnIJI"
CHALLENGE = b"DTC-NEXIS-OWNER|RECOVERY-KEY-TEST-ONLY|NOT-A-FEED|2026-10-21"


def read_public(x: str, y: str) -> ec.EllipticCurvePublicKey:
    def number(s: str) -> int:
        if len(s) != 43:
            raise ValueError("Incorrect pinned key length")
        raw = base64.b64decode(s + "=", altchars=b"-_", validate=True)
        if len(raw) != 32:
            raise ValueError("Incorrect pinned key coordinate")
        return int.from_bytes(raw, "big")
    return ec.EllipticCurvePublicNumbers(
        number(x), number(y), ec.SECP256R1()
    ).public_key()


def attest() -> None:
    pem = os.environ.get("NEXIS_OWNER_RECOVERY_SIGNER_KEY_PEM", "")
    if not pem.startswith("-----BEGIN"):
        raise ValueError("Recovery signer GitHub Secret is missing or unsupported")

    key = serialization.load_pem_private_key(pem.encode("utf-8"), password=None)
    if not isinstance(key, ec.EllipticCurvePrivateKey) or not isinstance(key.curve, ec.SECP256R1):
        raise ValueError("Recovery signing key must be ECDSA P-256")

    approved = read_public(RECOVERY_X, RECOVERY_Y)
    legacy = read_public(LEGACY_X, LEGACY_Y)
    if key.public_key().public_numbers() != approved.public_numbers():
        raise ValueError("Recovery Secret does not match approved owner recovery JWK")
    if key.public_key().public_numbers() == legacy.public_numbers():
        raise ValueError("Recovery signer unexpectedly equals original R9 signer")

    der = approved.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    if hashlib.sha256(der).hexdigest() != RECOVERY_SHA256:
        raise ValueError("Recovery public key fingerprint does not match the approved checkpoint")

    signature = key.sign(CHALLENGE, ec.ECDSA(hashes.SHA256()))
    approved.verify(signature, CHALLENGE, ec.ECDSA(hashes.SHA256()))
    try:
        approved.verify(signature, CHALLENGE + b"|TAMPERED", ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
        pass
    else:
        raise ValueError("Tampered challenge was not rejected")

    try:
        legacy.verify(signature, CHALLENGE, ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
        pass
    else:
        raise ValueError("Old R9 anchor incorrectly accepted recovery signer")

    print("PASS: existing owner Recovery GitHub Secret matches approved P-256 public JWK.")
    print("PASS: in-memory synthetic signature verifies, tamper and legacy anchor reject.")
    print("PASS: original R9 private key not needed; NO feed, installer or artifact signed/published.")


if __name__ == "__main__":
    try:
        attest()
    except Exception:
        # Never print exception values, PEM content, or environment variables.
        print("BLOCKED: recovery signer attestation failed; no update was published.", file=sys.stderr)
        sys.exit(2)
