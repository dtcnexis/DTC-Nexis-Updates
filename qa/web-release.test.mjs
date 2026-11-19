import test from 'node:test';
import {createHash,generateKeyPairSync} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {compile,publish} from '../ci/web-release.mjs';
import {root,trialBatches,generateTrial} from './web-fixture.mjs';

test('publication replaces one pack, preserves IDs, defers incomplete evidence, restores the prior records',async t=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'dtc-feed-'));
  t.after(()=>fs.rmSync(dir,{recursive:true,force:true}));
  const manifest=()=>JSON.parse(Buffer.from(JSON.parse(fs.readFileSync(path.join(dir,'feed','current.json'))).payload,'base64'));
  assert.equal((await generateTrial(dir,1)).length,1);
  const first=manifest();
  await generateTrial(dir,2);
  const second=manifest();
  assert.deepEqual(first.packs.map(p=>p.count),second.packs.map(p=>p.count));
  assert.deepEqual(first.packs.find(p=>p.group==='*'),second.packs.find(p=>p.group==='*'));
  assert.deepEqual(first.packs.find(p=>p.group==='bmw'),second.packs.find(p=>p.group==='bmw'));
  assert.notEqual(first.packs.find(p=>p.group==='volvo').sha256,second.packs.find(p=>p.group==='volvo').sha256);
  await assert.rejects(()=>generateTrial(dir,1),/stale/);
  assert.deepEqual(manifest(),second);
  await generateTrial(dir,3);
  assert.deepEqual(manifest().packs,first.packs);
  await generateTrial(dir,3);
  assert.equal(manifest().sequence,3);
});
test('invalid, duplicate, conflicting, untraceable and weaker records fail the build',()=>{
  const build=batches=>compile({root,batches,channel:'trial'});
  for(const mutate of [
    r=>r.scope.yearEnd=1900,r=>r.scope.unsupported='?',r=>r.text={},r=>r.code='INVALID!',r=>r.source.sha256='0',
    r=>r.source.pointer='/records/0',r=>r.sourceRecordId='wrong',r=>r.status='draft',r=>r.replaces='0',r=>r.reviewedBy=''
  ]){
    const batches=trialBatches();mutate(batches[1].changes[0]);assert.throws(()=>build(batches));
  }
  const duplicate=trialBatches();duplicate[0].changes.push({...duplicate[0].changes[1],id:'duplicate'});assert.throws(()=>build(duplicate),/Duplicate/);
  const lost=trialBatches();delete lost[1].changes[0].text.ar;assert.throws(()=>build(lost),/removed/);
  const weaker=trialBatches();weaker[0].changes[1].confidence='manufacturer';
  const approved=weaker[0].changes[1];
  weaker[1].changes[0].replaces=createHash('sha256').update(JSON.stringify(approved)).digest('hex');
  assert.throws(()=>build(weaker),/downgrade/);
  assert.throws(()=>compile({root,batches:trialBatches(),channel:'stable'}),/channel/);
});



test('incompletely documented candidates remain in the review queue and overlaps fail closed',()=>{
  const batches=trialBatches();
  batches[0].changes.push({id:'candidate:missing',status:'candidate'});
  const {pending,states}=compile({root,batches,channel:'trial'});
  assert.match(pending.find(r=>r.id==='candidate:missing').reason,/reference.*missing/);
  assert(!states.at(-1).records.has('candidate:missing'));
  batches[0].changes.push({...batches[0].changes[1],id:'ambiguous',scope:{make:'Volvo',yearStart:2016,yearEnd:2019}});
  assert.throws(()=>compile({root,batches,channel:'trial'}),/overlapping/);
});

test('a stable-channel build pins source history and activates only after delivery verification',async t=>{
  const dir=fs.mkdtempSync(path.join(os.tmpdir(),'dtc-stable-simulation-'));
  t.after(()=>fs.rmSync(dir,{recursive:true,force:true}));
  const out=path.join(dir,'distribution'),file='data/master/sample.json';
  fs.mkdirSync(path.dirname(path.join(dir,file)),{recursive:true});
  const source=fs.readFileSync(path.join(root,'qa/web-fixtures/source.json'));
  fs.writeFileSync(path.join(dir,file),source);
  const git=(...args)=>execFileSync('git',args,{cwd:dir,windowsHide:true,encoding:'utf8',stdio:['ignore','pipe','pipe']}).trim();
  git('init','--quiet');git('add',file);
  git('-c','user.name=Trial','-c','user.email=trial@example.invalid','-c','commit.gpgsign=false','commit','-qm','Synthetic test only');
  const commit=git('rev-parse','HEAD'),batch=trialBatches()[0];batch.channel='stable';
  for(const row of batch.changes)if(row.source)Object.assign(row.source,{file,commit});
  fs.writeFileSync(path.join(dir,file),'{}');
  const {states}=compile({root:dir,batches:[batch],channel:'stable'});
  const key=generateKeyPairSync('ec',{namedCurve:'P-256'}).privateKey;
  const args={channel:'stable',states,out,privateKey:key,commit};
  await assert.rejects(()=>publish({...args,verifyDelivery:async()=>{throw Error('unreachable')}}),/unreachable/);
  assert(!fs.existsSync(path.join(out,'current.json')));
  await publish({...args,verifyDelivery:async sha=>assert.equal(createHash('sha256').update(fs.readFileSync(path.join(out,'packs',sha+'.json'))).digest('hex'),sha)});
  assert(fs.existsSync(path.join(out,'current.json')));
});
