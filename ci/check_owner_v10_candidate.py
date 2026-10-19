#!/usr/bin/env python3
"""Owner-only Revision 10 content QA. Do not sign, publish or modify live feed."""
import base64,hashlib,json,pathlib,re
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec,utils

ROOT=pathlib.Path(__file__).resolve().parents[1]
old_path=ROOT/"owner-tests/batch01/catalog-v9.json"
draft_path=ROOT/"owner-channel/review/catalog-v10-unsigned.json"
package_path=ROOT/"owner-channel/packages/catalog-v10.json"
live_path=ROOT/"owner-channel/update-feed.json"
jwk=json.loads((ROOT/"owner-tests/batch01/public-key.jwk.json").read_text())
def dec(s):return base64.urlsafe_b64decode(s+"="*((-len(s))%4))
pub=ec.EllipticCurvePublicNumbers(int.from_bytes(dec(jwk['x']),"big"),int.from_bytes(dec(jwk['y']),"big"),ec.SECP256R1()).public_key()
envelope=json.loads(live_path.read_text(encoding="utf8"))
payload=base64.b64decode(envelope["payload"],validate=True)
signature=base64.b64decode(envelope["signature"],validate=True)
assert len(signature)==64,"Invalid active signature"
r=int.from_bytes(signature[:32],"big");s=int.from_bytes(signature[32:],"big")
pub.verify(utils.encode_dss_signature(r,s),payload,ec.ECDSA(hashes.SHA256()))
manifest=json.loads(payload)
assert manifest["app"]=="DTCNexis" and manifest["versionCode"]==7
assert manifest["catalog"]["versionCode"]==9,"Live feed must remain at last authorized revision"
assert "images" not in manifest,"No unreviewed image batches are published"
assert manifest["catalog"]["url"]!= "https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/owner-stable-data-channel/owner-channel/packages/catalog-v10.json", "Unsigned Revision 10 package must never be active"
old=json.loads(old_path.read_text(encoding="utf8"))
candidate=json.loads(draft_path.read_text(encoding="utf8"))
assert package_path.read_bytes()==draft_path.read_bytes(),"Staged package must match reviewed candidate exactly"
assert old["versionCode"]==9 and candidate["versionCode"]==10
assert len(old["items"])==18 and len(candidate["items"])==26
assert candidate["items"][:18]==old["items"],"Old 18 codes cannot be silently changed"
seen=set()
for item in candidate["items"]:
    assert isinstance(item,dict) and set(item)=={"code","system","en","ar","sv","source"}
    code=item["code"]
    assert re.fullmatch(r"[PBCU][0-9A-F]{4}",code)
    assert item["system"]==code[0] and code not in seen
    seen.add(code)
    for k in ("en","ar","sv","source"):
        assert isinstance(item[k],str) and 3<=len(item[k])<=250
    assert "Generic reference for trial only" in item["source"] or "Generic training/reference" in item["source"]
assert seen==set(x["code"] for x in old["items"])|{"P0171","P0172","P0128","P0133","P0301","P0441","U0101","U0155"}
assert len(draft_path.read_bytes())<2*1024*1024
print("PASS: signed, unchanged Revision 9 remains live on permanent owner endpoint")
print("PASS: unsigned Revision 10 candidate includes 26 records, 8 new generic P/U descriptions, preserves all 18 prior rows")
print("RELEASE BLOCKED: no authorized signature for Revision 10; zero reviewed new DTC PNGs")
