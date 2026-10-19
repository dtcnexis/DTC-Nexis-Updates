#!/usr/bin/env python3
"""Offline synthetic signer tests only; no owner private key in any source."""
import base64,json,pathlib,sys,tempfile,unittest
from cryptography.hazmat.primitives import hashes,serialization
from cryptography.hazmat.primitives.asymmetric import ec,utils
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from prepare_owner_v10_signed import prepare,open_envelope,OWNER_URL,CATALOG_URL

ROOT=pathlib.Path(__file__).resolve().parents[1]
def b64(x):return base64.urlsafe_b64encode(x.to_bytes(32,"big")).rstrip(b"=").decode()

class OwnerV10StagingTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=pathlib.Path(self.temp.name)
        self.key=ec.generate_private_key(ec.SECP256R1())
        self.second=ec.generate_private_key(ec.SECP256R1())
        numbers=self.key.public_key().public_numbers()
        self.jwk=self.root/"pinned.json"
        self.jwk.write_text(json.dumps({
            "kty":"EC","crv":"P-256","x":b64(numbers.x),"y":b64(numbers.y)
        }),encoding="utf-8")
        self.p=self.root/"signer.pem"
        self.p.write_bytes(self.key.private_bytes(serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,serialization.NoEncryption()))
        self.bad=self.root/"other.pem"
        self.bad.write_bytes(self.second.private_bytes(serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,serialization.NoEncryption()))
        self.prev=self.root/"signed-v9.json"
        payload=json.dumps({"app":"DTCNexis","versionCode":7,
            "catalog":{"versionCode":9}},separators=(",",":")).encode()
        der=self.key.sign(payload,ec.ECDSA(hashes.SHA256()))
        r,s=utils.decode_dss_signature(der)
        self.prev.write_text(json.dumps({
            "payload":base64.b64encode(payload).decode(),
            "signature":base64.b64encode(r.to_bytes(32,"big")+s.to_bytes(32,"big")).decode()
        }),encoding="utf-8")
        self.old=ROOT/"owner-tests/batch01/catalog-v9.json"
        self.new=ROOT/"owner-channel/packages/catalog-v10.json"
        self.out=self.root/"candidate-feed.json"

    def tearDown(self):self.temp.cleanup()

    def run_sign(self,**kw):
        args=dict(previous_feed=self.prev,old_catalog=self.old,
                  new_catalog=self.new,public_jwk=self.jwk,
                  private_pem=self.p,output=self.out)
        args.update(kw)
        return prepare(**args)

    def test_valid_staged_feed_matches_existing_public_key(self):
        report=self.run_sign()
        self.assertEqual(report["definitions"],26)
        self.assertEqual(report["feed_url"],OWNER_URL)
        feed=open_envelope(self.out,self.key.public_key())
        self.assertEqual(feed["catalog"]["versionCode"],10)
        self.assertEqual(feed["catalog"]["url"],CATALOG_URL)
        self.assertEqual(feed["versionCode"],7)
        self.assertNotIn("windows",feed)
        self.assertNotIn("images",feed)
        self.assertNotIn("PRIVATE KEY",self.out.read_text())
        self.assertEqual(json.loads(self.new.read_text())["items"][:18],
                         json.loads(self.old.read_text())["items"])

    def test_wrong_signer_is_blocked(self):
        with self.assertRaisesRegex(AssertionError,"Signer does not match"):
            self.run_sign(private_pem=self.bad)
        self.assertFalse(self.out.exists())

    def test_invalid_previous_signature_is_blocked(self):
        forged=json.loads(self.prev.read_text())
        forged["signature"]=base64.b64encode(bytes(64)).decode()
        self.prev.write_text(json.dumps(forged))
        with self.assertRaises(Exception):
            self.run_sign()
        self.assertFalse(self.out.exists())

    def test_modified_prior_definitions_cannot_be_signed(self):
        modified=json.loads(self.new.read_text())
        modified["items"][0]["en"]="Changed historical DTC"
        copied=self.root/"corrupted.json"
        copied.write_text(json.dumps(modified,ensure_ascii=False))
        with self.assertRaisesRegex(AssertionError,"Existing 18"):
            self.run_sign(new_catalog=copied)
        self.assertFalse(self.out.exists())

    def test_existing_feed_cannot_be_overwritten(self):
        with self.assertRaisesRegex(AssertionError,"Cannot overwrite"):
            self.run_sign(output=self.prev)

if __name__=="__main__":unittest.main(verbosity=2)
