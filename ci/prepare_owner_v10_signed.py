#!/usr/bin/env python3
"""Prepare an offline, owner-only signed v10 feed; NEVER publish automatically.

Accepts the private P-256 signer from an external protected file. Rejects a
replacement signing identity, rollback, changed prior records, and extra
executable/image fields. No signing secret is written to any output.
"""
import argparse
import base64
import hashlib
import json
import os
import pathlib
import re
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import ec,utils

OWNER_URL = ("https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/"
             "owner-stable-data-channel/owner-channel/update-feed.json")
CATALOG_URL = ("https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/"
               "owner-stable-data-channel/owner-channel/packages/catalog-v10.json")
REQUIRED_NEW = {"P0171","P0172","P0128","P0133","P0301","P0441","U0101","U0155"}
EXPECTED_SYSTEMS = {"P","B","C","U"}

def key_from_jwk(jwk):
    assert isinstance(jwk,dict) and jwk.get("kty")=="EC" and jwk.get("crv")=="P-256"
    assert "d" not in jwk
    points=[]
    for name in ("x","y"):
        value=jwk[name]
        assert isinstance(value,str) and re.fullmatch(r"[A-Za-z0-9_-]{43}",value)
        data=base64.urlsafe_b64decode(value+"=")
        assert len(data)==32
        points.append(int.from_bytes(data,"big"))
    return ec.EllipticCurvePublicNumbers(*points,ec.SECP256R1()).public_key()

def open_envelope(path,public_key):
    envelope=json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    payload=base64.b64decode(envelope["payload"],validate=True)
    signature=base64.b64decode(envelope["signature"],validate=True)
    assert 0<len(payload)<131072 and len(signature)==64
    r=int.from_bytes(signature[:32],"big")
    s=int.from_bytes(signature[32:],"big")
    public_key.verify(utils.encode_dss_signature(r,s),payload,ec.ECDSA(hashes.SHA256()))
    return json.loads(payload)

def check_catalog(catalog,old):
    assert set(catalog)=={"versionCode","items"} and catalog["versionCode"]==10
    assert old["versionCode"]==9 and len(old["items"])==18
    items=catalog["items"]
    assert isinstance(items,list) and len(items)==26
    assert items[:18]==old["items"],"Existing 18 DTC records must be unchanged"
    seen=set()
    for row in items:
        assert isinstance(row,dict) and set(row)=={"code","system","en","ar","sv","source"}
        code=row["code"]
        assert isinstance(code,str) and re.fullmatch(r"[PBCU][0-9A-F]{4}",code)
        assert code not in seen and row["system"]==code[0]
        seen.add(code)
        for key in ("en","ar","sv","source"):
            assert isinstance(row[key],str) and 3<=len(row[key])<=250
        assert "Generic" in row["source"],"Only trial generic DTC definitions permitted"
    assert seen-set(r["code"] for r in old["items"])==REQUIRED_NEW
    return len(items)

def prepare(*,previous_feed,old_catalog,new_catalog,public_jwk,private_pem,output):
    previous_feed=pathlib.Path(previous_feed)
    new_catalog=pathlib.Path(new_catalog)
    private_pem=pathlib.Path(private_pem)
    output=pathlib.Path(output)
    assert output.resolve()!=previous_feed.resolve(),"Cannot overwrite active channel directly"
    assert output.resolve()!=private_pem.resolve(),"Cannot overwrite private key"
    assert not output.exists(),"Refuse overwriting signed stage artifacts"
    pub=key_from_jwk(json.loads(pathlib.Path(public_jwk).read_text(encoding="utf-8")))
    previous=open_envelope(previous_feed,pub)
    assert previous["app"]=="DTCNexis" and previous["versionCode"]==7
    assert previous["catalog"]["versionCode"]==9
    assert "images" not in previous and "windows" not in previous
    old=json.loads(pathlib.Path(old_catalog).read_text(encoding="utf-8"))
    raw=new_catalog.read_bytes()
    assert len(raw)<2*1024*1024
    catalog=json.loads(raw)
    count=check_catalog(catalog,old)
    private=serialization.load_pem_private_key(private_pem.read_bytes(),password=None)
    assert hasattr(private,"curve") and isinstance(private.curve,ec.SECP256R1) and callable(getattr(private,"sign",None)) and callable(getattr(private,"public_key",None)), "Only an EC P-256 private signing key is accepted"
    assert private.public_key().public_numbers()==pub.public_numbers(),(
        "Signer does not match original permanently pinned public key; trust rotation forbidden"
    )
    manifest={
        "app":"DTCNexis",
        "version":"RC3.8.2-owner-v10-data",
        "versionCode":7,
        "catalog":{
            "versionCode":10,
            "url":CATALOG_URL,
            "sha256":hashlib.sha256(raw).hexdigest()
        },
        "notes":"OWNER TEST ONLY: 26 generic training DTCs. No new images or executable."
    }
    payload=json.dumps(manifest,ensure_ascii=False,separators=(",",":"),allow_nan=False).encode("utf-8")
    signature=private.sign(payload,ec.ECDSA(hashes.SHA256()))
    r,s=utils.decode_dss_signature(signature)
    envelope={
        "payload":base64.b64encode(payload).decode(),
        "signature":base64.b64encode(r.to_bytes(32,"big")+s.to_bytes(32,"big")).decode()
    }
    # Verify using the exact original embedded public key before any artifact is produced.
    check_r,check_s=utils.decode_dss_signature(signature)
    pub.verify(utils.encode_dss_signature(check_r,check_s),payload,ec.ECDSA(hashes.SHA256()))
    output.parent.mkdir(parents=True,exist_ok=True)
    fd=os.open(output,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,"w",encoding="utf-8") as handle:
        json.dump(envelope,handle,separators=(",",":"))
        handle.write("\n")
    assert open_envelope(output,pub)==manifest
    return {
        "ready_for_manual_owner_trial_activation":True,
        "feed_url":OWNER_URL,
        "next_catalog_version":10,
        "definitions":count,
        "data_sha256":manifest["catalog"]["sha256"],
        "signed_artifact_file":str(output)
    }

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--previous-feed",default="owner-channel/update-feed.json")
    parser.add_argument("--old-catalog",default="owner-tests/batch01/catalog-v9.json")
    parser.add_argument("--new-catalog",default="owner-channel/packages/catalog-v10.json")
    parser.add_argument("--public-jwk",default="owner-tests/batch01/public-key.jwk.json")
    parser.add_argument("--private-pem",required=True)
    parser.add_argument("--out",required=True)
    args=parser.parse_args()
    info=prepare(previous_feed=args.previous_feed,old_catalog=args.old_catalog,
                 new_catalog=args.new_catalog,public_jwk=args.public_jwk,
                 private_pem=args.private_pem,output=args.out)
    print(json.dumps(info,ensure_ascii=False))
