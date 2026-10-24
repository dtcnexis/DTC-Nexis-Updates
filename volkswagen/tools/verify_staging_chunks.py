#!/usr/bin/env python3
"""Read-only verifier for review-only brand JSON chunks. Usage: python verify_staging_chunks.py <data-dir>"""
import hashlib,json,sys
from pathlib import Path

def digest(b):return hashlib.sha256(b).hexdigest()

def main():
 root=Path(sys.argv[1]);m=json.loads((root/'manifest.json').read_text(encoding='utf8'))
 assert m['schema']=='dtcnexis.staging.manifest.v1'
 assert m['status']=='STAGING_ONLY_NO_AUTO_INSTALL'
 assert m['signed_for_client'] is False and m['client_update_ready'] is False
 assert m['publication_license_cleared'] is False
 seen=set();rows=0;files=0
 for section in m['sections']:
  count=0
  for chk in section['chunks']:
   p=root/chk['path'];assert p.is_file() and not p.is_symlink()
   b=p.read_bytes();assert len(b)==chk['size'] and digest(b)==chk['sha256']
   obj=json.loads(b)
   assert obj['schema']=='dtcnexis.staging.records.v1'
   assert obj['section']==section['section'] and obj['make']==m['make']
   assert obj['disposition']=='REVIEW_ONLY_NOT_RELEASED'
   assert len(obj['records'])==chk['records']
   for entry in obj['records']:
    assert entry['ref'] not in seen,entry['ref'];seen.add(entry['ref'])
   count+=len(obj['records']);files+=1
  assert count==section['records'];rows+=count
 assert rows==m['record_count']
 assert len(list(root.glob('*.json')))==files+1
 print(f'PASS: {m["make"]} {rows} records / {files+1} JSON files; NOT a live update')
if __name__=='__main__':main()