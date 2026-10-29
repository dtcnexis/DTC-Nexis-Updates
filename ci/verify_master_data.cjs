#!/usr/bin/env node
/* Permanent owner DTC archive integrity check. NEVER publishes or signs files. */
'use strict';
const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.resolve(__dirname,'../data/master');
const load=p=>JSON.parse(fs.readFileSync(path.join(root,p),'utf8'));
const manifest=load('all_collected_catalog_manifest.json');
assert.equal(manifest.schema,'dtcnexis-permanent-collected-codes-manifest-v1');
assert.ok(manifest.current_saved_row_count>=7230,'Baseline permanently saved rows cannot decrease without owner approval');
assert.equal(manifest.file_count,manifest.collections.length,'Manifest file count inconsistent');
const all=new Set();let counted=0;
const groups={};
for(const record of manifest.collections){
 assert.ok(!all.has(record.path),'duplicate file listing');
 all.add(record.path);
 assert.ok(record.path.startsWith('data/master/'));
 const d=load(record.path.slice('data/master/'.length));
 const items=d.records||d.entries||d.items;
 assert.ok(Array.isArray(items),'Missing rows: '+record.path);
 assert.equal(items.length,record.rows,'Rows changed in '+record.path);
 for(const entry of items) {
  const code=String(entry.code??entry.raw_code??'');
  assert.ok(code.trim().length>0,'Blank code in '+record.path);
  assert.ok(!code.includes('\n'),'Invalid code in '+record.path);
 }
 counted+=items.length;
 groups[record.kind]=(groups[record.kind]||0)+items.length;
 if(record.kind==='manufacturer_batch02') assert.ok(d.source?.git_blob_sha,'Untraceable manufacturer: '+record.path);
 if(record.kind==='vag_original_numeric') assert.equal(d.source_parts?.length,8,'VAG source chunks missing');
 if(record.kind==='generic_trilingual') {
  for(const item of items){
   for(const lang of ['en','ar','sv'])assert.ok(item['translation_'+lang]||item[lang]||item['definition_'+lang]);
  }
 }
}
assert.equal(counted,manifest.current_saved_row_count);
assert.ok(groups.manufacturer_batch02>=934);
assert.ok(groups.vag_original_numeric>=644);
assert.ok(groups.multibrand_C_variants>=278);
assert.ok(groups.ds_automobiles_batch01>=798);
assert.ok(groups.legacy_generic_PBU>=2137);
assert.ok(groups.generic_trilingual>=26);
assert.ok(groups.nissan_batch02>=495);
assert.ok(groups.renault_batch01>=129);
assert.ok(groups.kia_batch01>=63);
assert.ok(groups.ford_batch01>=409);
assert.ok(groups.peugeot_legacy>=1317);
for(const e of manifest.enrichment_files||[]){const v=load(e.path.slice('data/master/'.length));assert.equal(v.records.length,e.original_rows);assert.equal(v.counts_towards_unique_ledger,false);}

const enhanced=load('legacy_enhanced_diagnostics.json');
assert.equal(enhanced.records.length,12);
const registry=load('source_registry.json');
assert.equal(registry.materialized_text_records,counted);
assert.equal(registry.manufacturer_originals.files.length,11);
assert.ok(!manifest.release_to_app,'Master archive must not be treated as published release');
console.log('PASS: '+counted+' archived records in '+all.size+' permanent source files; 12 enhanced diagnostic notes.');
console.log('PASS: no duplicate source-file paths; original manufacturer fingerprints preserved.');
console.log('No app install, signing, release, or owner channel changes.');
