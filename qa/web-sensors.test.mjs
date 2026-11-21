import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {createHash,generateKeyPairSync,verify} from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {compile,publish} from '../ci/web-release.mjs';
import {validateSensorCatalog} from '../ci/sensor-model.mjs';

const file='data/master/sensors/multimeter-v1.json';
const bytes=fs.readFileSync(file,'utf8').replace(/\r\n/g,'\n');
const hash=b=>createHash('sha256').update(b).digest('hex');

test('central guides and deferred evidence have durable, distinct identifiers',()=>{
  const catalog=validateSensorCatalog(JSON.parse(bytes));
  const queue=JSON.parse(fs.readFileSync('data/review/sensors/multimeter-pending.json'));
  const ids=new Set(catalog.sensors.map(s=>s.id));
  assert.equal(ids.size,11);
  assert.equal(new Set(queue.map(r=>r.id)).size,queue.length);
  assert(queue.every(r=>ids.has(r.sensorId)&&r.reason&&r.status==='pending'&&r.source.startsWith('https://')));
});

test('only pinned reviewed evidence enters a delivered signed sensor pack',async t=>{
  const root=fs.mkdtempSync(path.join(os.tmpdir(),'dtc-sensor-release-'));
  t.after(()=>fs.rmSync(root,{recursive:true,force:true}));
  const git=(...args)=>execFileSync('git',args,{cwd:root,encoding:'utf8'}).trim();
  fs.mkdirSync(path.dirname(path.join(root,file)),{recursive:true});
  fs.writeFileSync(path.join(root,file),bytes);
  git('init','--quiet');git('add','--',file);
  git('-c','user.name=Fixture','-c','user.email=qa@example.invalid','-c','commit.gpgsign=false','commit','--quiet','-m','Test input');
  const commit=git('rev-parse','HEAD');
  git('update-ref','refs/remotes/origin/main',commit);
  const review={file,commit,sha256:hash(bytes),reviewedBy:'test reviewer'};
  const batch={sequence:1,channel:'stable',date:'2026-11-21T00:00:00.000Z',changes:[],sensors:review};
  const build=sensors=>compile({root,channel:'stable',batches:[{...batch,sensors}]});
  assert.throws(()=>build({...review,sha256:'0'.repeat(64)}));
  assert.throws(()=>build({...review,reviewedBy:''}));
  const {states}=build(review);
  const incomplete=JSON.parse(bytes);
  incomplete.sensors.pop();
  const changed=JSON.stringify(incomplete);
  fs.writeFileSync(path.join(root,file),changed);
  git('add','--',file);
  git('-c','user.name=Fixture','-c','user.email=qa@example.invalid','-c','commit.gpgsign=false','commit','--quiet','-m','Test removal');
  const nextCommit=git('rev-parse','HEAD');
  git('update-ref','refs/remotes/origin/main',nextCommit);
  const next={...batch,sequence:2,sensors:{...review,commit:nextCommit,sha256:hash(changed)}};
  assert.throws(()=>compile({root,channel:'stable',batches:[batch,next]}),/Sensor guide removed/);
  const {privateKey,publicKey}=generateKeyPairSync('ec',{namedCurve:'prime256v1'});
  const out=path.join(root,'output');
  const input={out,channel:'stable',states,commit,privateKey:privateKey.export({type:'pkcs8',format:'pem'})};
  await assert.rejects(publish({...input,verifyDelivery:()=>{throw Error('unavailable');}}));
  assert.equal(fs.existsSync(path.join(out,'current.json')),false);
  await publish({...input,verifyDelivery:async sha=>{
    assert.equal(hash(fs.readFileSync(path.join(out,'packs',sha+'.json'))),sha);
  }});
  const env=JSON.parse(fs.readFileSync(path.join(out,'current.json')));
  const body=Buffer.from(env.payload,'base64');
  assert(verify('sha256',body,{key:publicKey,dsaEncoding:'ieee-p1363'},Buffer.from(env.signature,'base64')));
  const descriptor=JSON.parse(body).sensorPack;
  assert.equal(descriptor.count,1);
  assert.deepEqual(JSON.parse(fs.readFileSync(path.join(out,'packs',descriptor.sha256+'.json'))),[JSON.parse(bytes)]);
});
