import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import assert from 'node:assert/strict';

const base=process.argv[2],destination=process.argv[3];
if(!base)throw Error('Pass website dist/data followed by an optional JSON output path');
const read=file=>JSON.parse(fs.readFileSync(file));
const archive=read('data/master/all_collected_catalog_manifest.json');
const byCode=new Map();
for(const source of archive.collections){
  const doc=read(source.path);
  for(const [index,row] of (doc.records||doc.entries||doc.items).entries()){
    const code=String(row.code??row.raw_code??row.code_raw).trim().toUpperCase();
    if(!byCode.has(code))byCode.set(code,[]);
    byCode.get(code).push({file:source.path,index,originalId:row.original_record_id??row.id??null});
  }
}
const fromBase=name=>read(path.join(base,name+'.json'));
const definitions=fromBase('definitions'),oem=fromBase('oem');
const inventory=[...definitions.map(r=>({id:'legacy:'+r.code,code:r.code})),
  ...Object.entries(oem).map(([code,r])=>({id:'legacy-oem:'+code,code,makes:r.makes}))];
assert.equal(new Set(inventory.map(r=>r.id)).size,inventory.length,'Duplicate bundled ID');
for(const row of inventory) row.candidates=byCode.get(row.code)||[];
const files={};
for(const name of ['definitions','oem','enhanced','swedish']){
  const data=fromBase(name);
  files[name]={entries:Object.keys(data).length,contentSHA256:createHash('sha256').update(JSON.stringify(data)).digest('hex')};
}
const summary={archived:archive.current_saved_row_count,bundled:inventory.length,
  withSourceCodeCandidate:inventory.filter(r=>r.candidates.length).length,
  withoutSourceCodeCandidate:inventory.filter(r=>!r.candidates.length).length};
if(destination)fs.writeFileSync(destination,JSON.stringify({summary,files,inventory},null,2));
console.log(JSON.stringify(summary));
