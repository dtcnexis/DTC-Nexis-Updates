#!/usr/bin/env python3
"""Prepare owner-only Revision 10 catalog+Guide signed envelopes.
IMPORTANT: private review artifact only. NEVER write the live update-feed.json.
The signing private key must match the permanently pinned Revision 9 public key.
"""
from __future__ import annotations
import argparse,base64,hashlib,json,os,pathlib
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import ec,utils
from prepare_owner_v10_signed import key_from_jwk,open_envelope,check_catalog,CATALOG_URL
from check_owner_guide_v10_candidate import validate as guide_validate

ROOT=pathlib.Path(__file__).resolve().parents[1]
def sign(private,public,obj):
 payload=json.dumps(obj,ensure_ascii=False,separators=(",",":"),allow_nan=False).encode("utf-8")
 signature=private.sign(payload,ec.ECDSA(hashes.SHA256()))
 r,s=utils.decode_dss_signature(signature)
 raw=r.to_bytes(32,"big")+s.to_bytes(32,"big")
 public.verify(utils.encode_dss_signature(r,s),payload,ec.ECDSA(hashes.SHA256()))
 return {"payload":base64.b64encode(payload).decode(),"signature":base64.b64encode(raw).decode()}

def prepare(*,private_pem,output,previous_feed=None,public_jwk=None,old_catalog=None,
   catalog=None,guide=None,assets_root=None):
 old=pathlib.Path(old_catalog or ROOT/"owner-tests/batch01/catalog-v9.json")
 cat=pathlib.Path(catalog or ROOT/"owner-channel/packages/catalog-v10.json")
 guide_path=pathlib.Path(guide or ROOT/"owner-channel/review/guide-v10-unsigned.json")
 prev=pathlib.Path(previous_feed or ROOT/"owner-channel/update-feed.json")
 jwk_path=pathlib.Path(public_jwk or ROOT/"owner-tests/batch01/public-key.jwk.json")
 assets=pathlib.Path(assets_root or ROOT/"owner-channel/packages/guide-v10")
 out=pathlib.Path(output)
 key_file=pathlib.Path(private_pem)
 assert out.resolve()!=prev.resolve(),"Do not overwrite active signed owner feed"
 assert out.resolve()!=key_file.resolve(),"Do not overwrite private signing key"
 assert not out.exists(),"Refuse output overwrite"
 jwk=json.loads(jwk_path.read_text(encoding="utf-8"))
 public=key_from_jwk(jwk)
 old_feed=open_envelope(prev,public)
 assert old_feed["app"]=="DTCNexis" and old_feed["versionCode"]==7
 assert old_feed["catalog"]["versionCode"]==9 and "guide" not in old_feed
 source_catalog=cat.read_bytes()
 assert len(source_catalog)<2*1024*1024
 new=json.loads(source_catalog)
 count=check_catalog(new,json.loads(old.read_text(encoding="utf-8")))
 # Re-evaluate all metadata, immutable asset bytes and unmodified signed R9.
 g=guide_validate(guide_path,assets_root=assets)
 assert g["ready_to_sign"],"Missing approved Guide WebP files: "+",".join(g["missing"])
 guide_doc=json.loads(guide_path.read_text(encoding="utf-8"))
 private=serialization.load_pem_private_key(key_file.read_bytes(),password=None)
 assert isinstance(private,ec.EllipticCurvePrivateKey) and isinstance(private.curve,ec.SECP256R1),"Only P-256 private key accepted"
 assert private.public_key().public_numbers()==public.public_numbers(),(
  "Original pinned signing identity unavailable/mismatched; never rotate key silently")
 inner=sign(private,public,guide_doc)
 # Verify exact independent nested Guide R10 signature before creating output.
 raw_inner=base64.b64decode(inner["payload"])
 sig_inner=base64.b64decode(inner["signature"])
 r=int.from_bytes(sig_inner[:32],"big");s=int.from_bytes(sig_inner[32:],"big")
 public.verify(utils.encode_dss_signature(r,s),raw_inner,ec.ECDSA(hashes.SHA256()))
 assert json.loads(raw_inner)==guide_doc
 outer={"app":"DTCNexis","version":"RC3.8.2-owner-v10-catalog-and-guide",
  "versionCode":7,
  "catalog":{"versionCode":10,"url":CATALOG_URL,"sha256":hashlib.sha256(source_catalog).hexdigest()},
  "guide":inner,
  "notes":"OWNER TEST ONLY: 26 generic DTCs and four image-backed Vehicle Guide cards. No Windows installer."}
 envelope=sign(private,public,outer)
 out.parent.mkdir(parents=True,exist_ok=True)
 fd=os.open(out,os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
 with os.fdopen(fd,"w",encoding="utf-8") as handle:
  json.dump(envelope,handle,ensure_ascii=False,separators=(",",":"))
  handle.write("\n");handle.flush();os.fsync(handle.fileno())
 assert open_envelope(out,public)==outer
 return {"staged":True,"published":False,"catalog_codes":count,"guide_cards":len(guide_doc["cards"]),
         "output":str(out),"same_pinned_signer":True}

if __name__=="__main__":
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument("--private-pem",required=True)
 parser.add_argument("--out",required=True)
 parser.add_argument("--assets-root")
 a=parser.parse_args()
 print(json.dumps(prepare(private_pem=a.private_pem,output=a.out,assets_root=a.assets_root),ensure_ascii=False))
