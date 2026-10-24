#!/usr/bin/env python3
"""Conservative human-review staging export. Does not activate signed feeds.
Usage: python make_catalog_export.py MASTER.json OUTPUT_DIR
Never include owner workshop records or binary/third-party images.
"""
import hashlib,json,re,sys
from pathlib import Path

SECTIONS = ('vehicle_records','engine_powertrain_variants','dtc_legacy_candidates',
'engine_code_evidence','ecu_catalog_and_evidence','individual_vehicle_cases',
'observed_dtc_cases','general_dtc_reference','diagnostic_checkworkflows',
'wiring_and_location_requests','reviews_and_safety')
PRIVATE_FIELDS = {'vin','registration','reg_no','license_plate','customer','customer_name','customer_email','email','phone','telephone','address','api_key','private_key','token','password','secret','plate_number','workshop_visit','workshop_visits'}
CHUNK_LIMIT=45000
VIN_RE=re.compile(r'\b[A-HJ-NPR-Z0-9]{17}\b')
EMAIL_RE=re.compile(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b',re.I)

def sanitize(x):
 if isinstance(x,list):return [sanitize(v) for v in x]
 if isinstance(x,dict):
  return {k:sanitize(v) for k,v in x.items() if k.lower() not in PRIVATE_FIELDS and not k.lower().endswith('_vin')}
 if isinstance(x,str):
  return EMAIL_RE.sub('[EMAIL_REDACTED]',VIN_RE.sub('[VIN_REDACTED]',x))
 return x

def canon(x):return (json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False)+'\n').encode('utf-8')
def sha(b):return hashlib.sha256(b).hexdigest()

def main():
 src=Path(sys.argv[1]);out=Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
 data=json.loads(src.read_text(encoding='utf-8'));raw=data['catalog'];index=[];tot=0
 assert set(raw)==set(SECTIONS),('unexpected sections',set(raw)^set(SECTIONS))
 for section in SECTIONS:
  rows=sanitize(raw[section]); assert isinstance(rows,list);seen=set()
  for row in rows:
   assert isinstance(row,dict) and isinstance(row.get('ref'),str) and isinstance(row.get('data'),dict)
   assert row['ref'] not in seen,('duplicate',section,row['ref']);seen.add(row['ref'])
  chunks=[];buf=[]
  def flush():
   if not buf:return
   num=len(chunks)+1
   doc={'schema':'dtcnexis.staging.records.v1','make':'Volkswagen','section':section,'chunk':num,
        'disposition':'REVIEW_ONLY_NOT_RELEASED','records':list(buf)}
   content=canon(doc)
   assert len(content)<75000,(section,len(content))
   name=f'{section}-{num:03d}.json'
   (out/name).write_bytes(content)
   chunks.append({'path':name,'size':len(content),'sha256':sha(content),'records':len(buf)})
   buf.clear()
  for row in rows:
   nxt=buf+[row]
   if buf and len(canon({'schema':'dtcnexis.staging.records.v1','make':'Volkswagen','section':section,'chunk':1,'disposition':'REVIEW_ONLY_NOT_RELEASED','records':nxt}))>CHUNK_LIMIT: flush()
   buf.append(row)
  flush()
  index.append({'section':section,'records':len(rows),'chunks':chunks})
  tot+=len(rows)
 manifest={'schema':'dtcnexis.staging.manifest.v1','make':'Volkswagen','version':'VW022','status':'STAGING_ONLY_NO_AUTO_INSTALL',
   'source_sha256':sha(src.read_bytes()),'record_count':tot,'section_count':len(SECTIONS),
   'user_records_included':False,'binary_assets_included':False,'publication_license_cleared':False,
   'vin_ecu_fitment_approved':False,'signed_for_client':False,'client_update_ready':False,
   'notes':['Not a signed update-feed or executable release.','644 VAG legacy DTC candidates not approved for per-vehicle fitment.','Preserves evidence/status and quarantined info; clients must not auto-import.'],
   'sections':index}
 (out/'manifest.json').write_bytes(canon(manifest))
 assert tot==1699,tot
 for sec in index:
  assert sum(c['records'] for c in sec['chunks'])==sec['records']
  for c in sec['chunks']:
   b=(out/c['path']).read_bytes();assert sha(b)==c['sha256']
 print(json.dumps({'records':tot,'files':sum(len(x['chunks']) for x in index)+1,'size':sum(f.stat().st_size for f in out.glob('*.json')),'source_sha256':manifest['source_sha256'],'chunks_per_section':{x['section']:len(x['chunks']) for x in index}},indent=2))
if __name__=='__main__':main()