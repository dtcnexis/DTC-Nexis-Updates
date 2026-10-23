#!/usr/bin/env python3
"""DTC NEXIS RC3.8.2 owner R11 signing rehearsal, NO PUBLISH.

Use the existing owner RECOVERY signer secret only in CI memory.
Verify five exact approved WebPs, the existing signed R9 feed, then
sign/verify nested Guide and outer feed. Never write a signature, signed feed,
key, certificate, artifact or changed channel file. The installed R9 client
does NOT yet trust this recovery identity: publication is forbidden.
"""
from __future__ import annotations
import argparse, base64, hashlib, io, json, sys
from pathlib import Path

from PIL import Image
from cryptography.exceptions import InvalidSignature
from owner_r10_readiness import (
    ReadinessError, key_from_jwk, original_feed, sign, verify_envelope,
)
from owner_r10_recovery_signed_trial import read_real_secret
from owner_recovery_secret_attestation import read_public, LEGACY_X, LEGACY_Y, RECOVERY_X, RECOVERY_Y

ROOT=Path(__file__).resolve().parents[1]
STAGED=ROOT/"owner-review"/"rc382-guide-r11"
APPROVED={
 "wiring_diagrams":("db81eb1c202a2ea3f09213be747b13b0ac4990e74a8ca7956cc7f372495b5c3e",15884),
 "remote_key_maintenance":("87ba05e803921537a765c38b58891dbd80f1047f8b057e901895eb7dea38f9e0",9754),
 "timing_belt_chain":("fa6a68a32435357fe3e25a6d5794835390b0e7c957b519a8dce6268e508fde46",12322),
 "torque_specifications":("05fa800456753aec254d673e73b5e67719487a9b2bbb1f17ae456e6e0bea2014",10922),
 "ecu_list":("a1a8ac63ab958a7160912c8a99ed494f909c15eb43ec437ffd7e66bd2f952cd7",42274),
}
EXPECTED_IDS=list(APPROVED)
PREFIX="https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/owner-stable-data-channel/owner-channel/owner-guide-cards/"
NOTES="PRIVATE OWNER R11 DRY RUN ONLY. Recovery trust bootstrap missing. Never install or publish."

def ensure(value,msg):
 if not value:raise ReadinessError(msg)

def validate_candidate():
 manifest=json.loads((STAGED/"manifest.json").read_text(encoding="utf-8"))
 doc=json.loads((STAGED/"guide-r11-unsigned-payload.json").read_text(encoding="utf-8"))
 ensure(manifest.get("status")=="OWNER_REVIEWED_UNSIGNED_NOT_DELIVERED","Unapproved candidate")
 ensure(manifest.get("release_gates",{}).get("real_five_image_edge_test") is True,"Real five-photo Edge QA missing")
 ensure(manifest["release_gates"].get("owner_original_p256_signed") is False,"Candidate status unexpectedly signed")
 ensure(manifest["release_gates"].get("stable_feed_unchanged") is True,"Stable feed must stay unchanged")
 ensure(set(doc)=={"schema","revision","cards"} and doc["schema"]=="dtcnexis.signed-guide.v1"
        and type(doc["revision"]) is int and doc["revision"]==11,"Invalid R11 guide schema/revision")
 cards=doc["cards"]
 ensure(isinstance(cards,list) and [r.get("id") for r in cards]==EXPECTED_IDS,"Exactly five R11 cards and order required")
 manifest_images={r["id"]:r for r in manifest["images"]}
 ensure(set(manifest_images)==set(APPROVED),"Incorrect image-review manifest")
 total=0
 for card in cards:
  ident=card["id"]; sha,n=APPROVED[ident]
  ensure(set(card)=={"id","label","topic","sha256","bytes","mime","url","buttons"},"Unsupported card field")
  ensure((card["sha256"],card["bytes"],card["mime"],card["url"])==
         (sha,n,"image/webp",PREFIX+ident+".webp"),"Hash, bytes, mime or owner URL changed")
  ensure(card["buttons"]==["google","youtube","pdf"],"Guide action identifiers changed")
  ensure(set(card["label"])=={"ar","en","sv"} and
         all(isinstance(card["label"][lang],str) and len(card["label"][lang])>=3
             for lang in ("ar","en","sv")),"Missing Guide localization")
  ensure(isinstance(card["topic"],str) and 12<=len(card["topic"])<=160,"Unsupported search topic")
  row=manifest_images[ident]
  ensure((row["sha256"],row["bytes"],row["width"],row["height"])==(sha,n,352,272),
         "Manifest fingerprint/size changed")
  src=(STAGED if ident=="ecu_list" else ROOT/"owner-review"/"rc382-guide-r10")/"images"/(ident+".webp")
  ensure(src.is_file() and not src.is_symlink(),"Missing staged approved WebP")
  raw=src.read_bytes()
  ensure(len(raw)==n and hashlib.sha256(raw).hexdigest()==sha,"Actual approved WebP changed")
  ensure(raw[:4]==b"RIFF" and raw[8:12]==b"WEBP","Invalid WebP magic")
  with Image.open(io.BytesIO(raw)) as photo:
   ensure(photo.format=="WEBP" and photo.size==(352,272),"Wrong WebP dimensions")
   photo.verify()
  total+=n
 ensure(total==91156,"Wrong aggregate owner image sizes")
 return doc,total

def must_reject(envelope,key,label):
 try:verify_envelope(envelope,key)
 except (ReadinessError,InvalidSignature):return
 raise ReadinessError("Fail-open signature verification: "+label)

def rehearse(live,legacy_pub):
 original=key_from_jwk(json.loads(Path(legacy_pub).read_text(encoding="utf-8")))
 ensure(original.public_numbers()==read_public(LEGACY_X,LEGACY_Y).public_numbers(),
        "Original R9 trust anchor changed")
 old=original_feed(live,original)
 ensure(old["catalog"]["versionCode"]==9,"Unexpected original R9 data revision")
 guide,total=validate_candidate()
 recovery=read_public(RECOVERY_X,RECOVERY_Y)
 private=read_real_secret() # Verified against pinned recovery JWK; secret remains CI memory
 inner=sign(private,guide)
 ensure(verify_envelope(inner,recovery)==guide,"Nested R11 Guide signature rejected")
 outer={
  "app":"DTCNexis","version":"RC3.8.2-R11-private-dry-run",
  "versionCode":7,"notes":NOTES,"ownerTrustEpoch":1,
  "ownerDataRevision":11,"guide":inner,
 }
 signed=sign(private,outer)
 checked=verify_envelope(signed,recovery)
 ensure(checked==outer and verify_envelope(checked["guide"],recovery)==guide,
        "Recovery R11 double signature invalid")
 must_reject(signed,original,"legacy trust boundary")
 corrupted=json.loads(json.dumps(signed))
 corrupted["signature"]=base64.b64encode(bytes(64)).decode()
 must_reject(corrupted,recovery,"outer tamper")
 corrupted_inner=json.loads(json.dumps(inner))
 corrupted_inner["signature"]=base64.b64encode(bytes(64)).decode()
 must_reject(corrupted_inner,recovery,"inner tamper")
 ensure(outer["ownerDataRevision"]>old["catalog"]["versionCode"],"R11 rollback")
 ensure("windows" not in outer and "exe" not in outer and "download" not in outer,
        "No binary executable may enter the Guide feed")
 print("PASS PRIVATE R11: five REAL approved WebPs, 91,156 bytes, SHA-256 and 352x272 verified.")
 print("PASS PRIVATE R11: existing recovery GitHub Secret signed inner Guide and outer feed in MEMORY only.")
 print("PASS PRIVATE R11: verified both signatures; modified layers and original R9 key rejected.")
 print("BLOCKED FOR LIVE UPDATE: R9-installed owner app has NOT been proven to trust recovery signer.")
 print("NOT A RELEASE: no signature/feed file, artifact, installer, new channel or secret exported.")

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--live",required=True,type=Path)
 parser.add_argument("--legacy-jwk",required=True,type=Path)
 a=parser.parse_args()
 try:rehearse(a.live,a.legacy_jwk)
 except Exception:
  # Do not print exception texts or secret-derived tracebacks in public CI.
  print("BLOCKED: private R11 rehearsal validation failed; NO feed published.",file=sys.stderr)
  raise SystemExit(2)

if __name__=="__main__":
 main()
