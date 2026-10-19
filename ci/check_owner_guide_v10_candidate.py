#!/usr/bin/env python3
"""Validate private owner Guide R10 proposal, never sign or publish a feed."""
from __future__ import annotations
import base64,hashlib,json,pathlib,re
from urllib.parse import urlsplit
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec,utils

ROOT=pathlib.Path(__file__).resolve().parents[1]
PREFIX="https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/owner-stable-data-channel/owner-channel/packages/guide-v10/"
EXPECTED={
 "wiring_diagrams":("770a586f9d744bc36be665dd353edf628cd27cbcb8b2fad727b78617c65d5fcc",36872),
 "remote_key_maintenance":("dbcafcfc5342ddd4cfd6c89377f286f16390068c0ebd91139b7b8db47647d785",25312),
 "timing_belt_chain":("9209fea4a869d57642a903c9599cf37b932d54d30447c45dc6289fa2b4ac1b7f",31374),
 "torque_specifications":("ef0d27dd804197a60b2a03db879ca78f667488d3b2022e78a31780984debc371",23002)
}
def public_jwk():
 obj=json.loads((ROOT/"owner-tests/batch01/public-key.jwk.json").read_text(encoding="utf-8"))
 assert obj.get("kty")=="EC" and obj.get("crv")=="P-256" and "d" not in obj
 def decode(s):return base64.urlsafe_b64decode(s+"="*((-len(s))%4))
 return ec.EllipticCurvePublicNumbers(int.from_bytes(decode(obj["x"]),"big"),
   int.from_bytes(decode(obj["y"]),"big"),ec.SECP256R1()).public_key()
def validate(path=None,assets_root=None):
 p=pathlib.Path(path) if path else ROOT/"owner-channel/review/guide-v10-unsigned.json"
 doc=json.loads(p.read_text(encoding="utf-8"))
 assert set(doc)=={"schema","revision","cards"} and doc["schema"]=="dtcnexis.signed-guide.v1"
 assert type(doc["revision"]) is int and doc["revision"]==10
 cards=doc["cards"]
 assert isinstance(cards,list) and len(cards)==4
 assert {c["id"] for c in cards}==set(EXPECTED)
 total=0;missing=[]
 root=pathlib.Path(assets_root) if assets_root else ROOT/"owner-channel/packages/guide-v10"
 for c in cards:
  ident=c["id"]
  assert set(c)=={"id","label","topic","sha256","bytes","mime","url","buttons"}
  sha,size=EXPECTED[ident]
  assert c["sha256"]==sha and type(c["bytes"]) is int and c["bytes"]==size
  assert c["mime"]=="image/webp" and c["buttons"]==["google","youtube","pdf"]
  assert c["url"]==PREFIX+ident+".webp"
  url=urlsplit(c["url"])
  assert url.scheme=="https" and url.hostname=="raw.githubusercontent.com"
  assert not (url.fragment or url.query or url.username or url.password)
  assert set(c["label"])=={"ar","en","sv"}
  for lang in ("ar","en","sv"):
   label=c["label"][lang]
   assert isinstance(label,str) and 3<=len(label)<=100
  assert isinstance(c["topic"],str) and 12<=len(c["topic"])<=159 and "\n" not in c["topic"]
  asset=root/(ident+".webp")
  if asset.is_file():
   assert not asset.is_symlink()
   data=asset.read_bytes()
   assert len(data)==size and hashlib.sha256(data).hexdigest()==sha,"Asset changed: "+ident
   assert data[:4]==b"RIFF" and data[8:12]==b"WEBP","Invalid WebP: "+ident
  else:missing.append(ident)
  total+=size
 assert total==116560
 # Check the authenticated, unchanged owner trial feed is still R9.
 envelope=json.loads((ROOT/"owner-channel/update-feed.json").read_text(encoding="utf-8"))
 payload=base64.b64decode(envelope["payload"],validate=True)
 sig=base64.b64decode(envelope["signature"],validate=True)
 assert len(sig)==64
 r=int.from_bytes(sig[:32],"big");s=int.from_bytes(sig[32:],"big")
 public_jwk().verify(utils.encode_dss_signature(r,s),payload,ec.ECDSA(hashes.SHA256()))
 active=json.loads(payload)
 assert active["app"]=="DTCNexis" and active["versionCode"]==7
 assert active["catalog"]["versionCode"]==9 and "guide" not in active
 return {"revision":10,"cards":4,"image_bytes":total,
  "assets_present":4-len(missing),"missing":missing,"live_revision":9,
  "ready_to_sign":not missing}
if __name__=="__main__":
 report=validate()
 print("PASS: owner Guide R10 schema/labels/buttons/URLs/SHA256 metadata; live signed R9 unchanged")
 print(json.dumps(report,ensure_ascii=False))
 if report["missing"]:
  print("STAGING ONLY: missing "+", ".join(report["missing"])+"; do not sign or activate.")
