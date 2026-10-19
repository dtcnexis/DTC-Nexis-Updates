#!/usr/bin/env python3
"""No-publish owner recovery signer self-test, for isolated CI only.

A recovery private key is read at runtime from a protected runner environment
variable, never placed in the source tree or shown in output. No feed is signed.
"""
import os
import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature


def main():
    pem = os.environ.get("NEXIS_OWNER_RECOVERY_SIGNER_KEY_PEM")
    if not pem:
        sys.exit("FAIL: recovery signer not configured")
    try:
        signer = serialization.load_pem_private_key(pem.encode("utf-8"), password=None)
    except (ValueError, TypeError):
        sys.exit("FAIL: recovery signer secret is not an unencrypted PEM private key")
    if not isinstance(signer, ec.EllipticCurvePrivateKey) or not isinstance(signer.curve, ec.SECP256R1):
        sys.exit("FAIL: recovery signer must use P-256")
    payload = b"DTC-NEXIS-RC382-RECOVERY-TEST-ONLY-NO-FEED"
    signature = signer.sign(payload, ec.ECDSA(hashes.SHA256()))
    signer.public_key().verify(signature, payload, ec.ECDSA(hashes.SHA256()))
    try:
        signer.public_key().verify(signature, payload + b"-modified", ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
        pass
    else:
        sys.exit("FAIL: modified data accepted")
    print("PASS: configured recovery signer can sign and verify test bytes")
    print("PASS: modified bytes rejected")
    print("NO PUBLISH: no feed, update package, or installer was produced")


if __name__ == "__main__":
    main()
