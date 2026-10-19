#!/usr/bin/env python3
"""Sign one fixed, non-installable CI trust probe. Never a live feed or package."""
import base64
import hashlib
import json
import os
import sys
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils

def main():
    try:
        pem=os.environ.get("NEXIS_OWNER_RECOVERY_SIGNER_KEY_PEM")
        if not pem:raise ValueError()
        key=serialization.load_pem_private_key(pem.encode("utf-8"),password=None)
        if not isinstance(key,ec.EllipticCurvePrivateKey) or not isinstance(key.curve,ec.SECP256R1):raise ValueError()
        der=key.public_key().public_bytes(serialization.Encoding.DER,serialization.PublicFormat.SubjectPublicKeyInfo)
        if hashlib.sha256(der).hexdigest()!="6ed08e270c7e87c9c79377078a7d2f36689a047b8533b9f62842ff3ccfe3f45a":raise ValueError()
        document={"app":"DTCNexis","version":"PRIVATE-TRUST-PROBE-NO-INSTALL","versionCode":7,
          "ownerTrustEpoch":1,"ownerDataRevision":10,
          "catalog":{"versionCode":10,"url":"https://example.invalid/rc382-private-trust-probe.json",
          "sha256":hashlib.sha256(b"NOT AN INSTALLABLE CATALOG").hexdigest()},
          "notes":"CI public verification probe only. Reserved invalid hostname. No dataset, live Revision 10 or executable."}
        payload=json.dumps(document,separators=(",",":")).encode("utf-8")
        signature=key.sign(payload,ec.ECDSA(hashes.SHA256()))
        key.public_key().verify(signature,payload,ec.ECDSA(hashes.SHA256()))
        r,s=utils.decode_dss_signature(signature)
        envelope={"payload":base64.b64encode(payload).decode(),
          "signature":base64.b64encode(r.to_bytes(32,"big")+s.to_bytes(32,"big")).decode()}
    except Exception:
        sys.exit("FAIL: fixed public CI probe signing failed; no private material exported")
    print("PUBLIC_NONINSTALLABLE_PROBE_JSON="+json.dumps(envelope,separators=(",",":")))
    print("PASS: fixed public verification probe; no downloadable data, no live feed write, no publication")
if __name__=="__main__":
    main()
