#!/usr/bin/env python3
"""Owner private R10 catalog+Guide signer regression: no real owner key is loaded."""
import base64,io,json,pathlib,tempfile,unittest,sys
from cryptography.hazmat.primitives.asymmetric import ec,utils
from cryptography.hazmat.primitives import hashes
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from prepare_owner_v10_guide_signed import sign,prepare
ROOT=pathlib.Path(__file__).resolve().parents[1]
class OwnerGuideSignerTests(unittest.TestCase):
 def test_two_layer_signature_matched_to_ephemeral_test_key(self):
  private=ec.generate_private_key(ec.SECP256R1())
  pub=private.public_key()
  inner={"schema":"dtcnexis.signed-guide.v1","revision":10,"cards":[{"id":"wiring_diagrams"}]}
  signed_inner=sign(private,pub,inner)
  outer={"app":"DTCNexis","versionCode":7,"guide":signed_inner}
  signed_outer=sign(private,pub,outer)
  for env,expected in ((signed_inner,inner),(signed_outer,outer)):
   payload=base64.b64decode(env["payload"],validate=True)
   sig=base64.b64decode(env["signature"],validate=True)
   self.assertEqual(len(sig),64)
   r=int.from_bytes(sig[:32],"big");s=int.from_bytes(sig[32:],"big")
   pub.verify(utils.encode_dss_signature(r,s),payload,ec.ECDSA(hashes.SHA256()))
   self.assertEqual(json.loads(payload),expected)
 def test_missing_real_assets_cannot_be_signed_even_with_bad_test_key_file(self):
  with tempfile.TemporaryDirectory() as d:
   key=pathlib.Path(d)/"empty-owner.pem";key.write_text("INTENTIONALLY NOT A SECRET")
   output=pathlib.Path(d)/"signed.json"
   with self.assertRaisesRegex(AssertionError,"Missing approved Guide WebP files"):
    prepare(private_pem=key,output=output)
   self.assertFalse(output.exists())
 def test_live_signed_r9_is_untouched(self):
  live=ROOT/"owner-channel/update-feed.json"
  env=json.loads(live.read_text(encoding="utf-8"))
  payload=json.loads(base64.b64decode(env["payload"],validate=True))
  self.assertEqual(payload["catalog"]["versionCode"],9)
  self.assertNotIn("guide",payload)
if __name__=="__main__":unittest.main(verbosity=2)
