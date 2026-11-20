import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {createHash, createPublicKey, randomUUID, sign, verify} from 'node:crypto';
import {execFileSync} from 'node:child_process';
import {pathToFileURL} from 'node:url';
import {reviewedVehicle} from './web-vehicles.mjs';

const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const json = value => Buffer.from(JSON.stringify(value));
const string = value => typeof value === 'string' && value.trim() === value && !!value;
const norm = value => String(value ?? '').normalize('NFC').trim().replace(/\s+/g, ' ').toLowerCase();
const fields = ['make','model','yearStart','yearEnd','engineCode','ecu','market'];
const makeKey = value => ({'škoda':'skoda','citroen':'citroën'}[norm(value)] ?? norm(value));
// Use the same lookup identity as the web client. Keep the scanner spelling in the row.
const codeKey = value => {
  const spelling=value.toUpperCase().trim().replace(/\s+/g,' ').replace(/\s*([-:/_])\s*/g,'$1');
  const compact=spelling.replace(/ /g,'').replace(/^([PBCU])-([0-9A-F]{4})$/,'$1$2');
  return /^(?:[PBCU][0-9A-F]{4}|[0-9]+)$/.test(compact)?compact:spelling;
};
const scopeKey = row => JSON.stringify([codeKey(row.code),...fields.map(k=>k==='make'?makeKey(row.scope[k]):norm(row.scope[k]))]);
const rank = {technical:1,manufacturer:2};

const isTestEvidence=row=>/\bTEST (?:legacy|notes|cause|check)\b|synthetic fixture|example\.invalid|automated trial only/i.test(JSON.stringify(row));

function evidence(root, row, channel) {
  const ref = row.source;
  assert(ref && Object.keys(ref).every(k=>['reference','locator','file','sha256','pointer','commit'].includes(k)),'Unmapped source field');
  assert(ref && string(ref.reference) && string(ref.locator), 'Missing technical reference or locator');
  assert(/^https:\/\//.test(ref.reference) && new URL(ref.reference).protocol === 'https:', 'Reference must be HTTPS');
  assert(string(ref.file) && !ref.file.split('/').some(p=>!p || p==='.' || p==='..') && /^[\w./-]+\.json$/.test(ref.file), 'Invalid source path');
  const allowed = channel==='trial'?'qa/web-fixtures/':'data/master/';
  assert(ref.file.startsWith(allowed), 'Source outside channel');
  let bytes;
  if(channel==='stable'){
    assert(/^[a-f0-9]{40}$/.test(ref.commit),'Pin the evidence to its Git commit');
    execFileSync('git',['merge-base','--is-ancestor',ref.commit,'refs/remotes/origin/main'],{cwd:root});
    bytes=execFileSync('git',['show',ref.commit+':'+ref.file],{cwd:root,maxBuffer:128*1024*1024});
  }else bytes=fs.readFileSync(path.join(root,ref.file));
  // JSON evidence is tracked in Git. Canonical LF tolerates Windows checkout conversion.
  const sourceText = bytes.toString('utf8').replace(/\r\n/g,'\n');
  assert.equal(hash(sourceText),ref.sha256,'Source fingerprint changed');
  assert(/^\/(?:[^~/]|~[01])+(?:\/(?:[^~/]|~[01])+)*$/.test(ref.pointer),'Invalid JSON pointer');
  const document=JSON.parse(sourceText);
  let item = document;
  for(const token of ref.pointer.slice(1).split('/')) {
    const key=token.replace(/~1/g,'/').replace(/~0/g,'~');
    assert(item && Object.hasOwn(item,key),'Source row missing');
    item=item[key];
  }
  if(channel==='stable'){
    assert(!isTestEvidence(item),'Test evidence in central source row');
    const brand=item.brand ?? document.brand;
    if(typeof brand==='string' && brand.trim()){
      assert(makeKey(row.scope.make)===makeKey(brand),'Manufacturer evidence requires matching make');
    }
    if(item.ecu_context){
      const ecus=Array.isArray(item.ecu_context)?item.ecu_context:[item.ecu_context];
      if(ecus.length && ecus.every(string))assert(ecus.some(ecu=>norm(ecu)===norm(row.scope.ecu)),'Preserve original ECU context');
    }
  }
  assert.equal(String(item.code ?? item.raw_code ?? item.code_raw).trim(),row.code,'Source code mismatch');
  const originalId=item.original_record_id ?? item.id;
  if(originalId) assert.equal(row.sourceRecordId,originalId,'Original identifier lost');
}

function validate(root,row,channel) {
  const allowedFields=['id','sourceRecordId','code','scope','text','technical','status','confidence','reviewedBy','source','replaces'];
  assert(Object.keys(row).every(k=>allowedFields.includes(k)),'Unmapped record field');
  assert(string(row.id) && row.id.length<=180 && /^[\w:|.-]+$/.test(row.id),'Invalid ID');
  assert(string(row.code) && row.code.length<=32 && /^[A-Za-z0-9]+(?:[-:_/ ][A-Za-z0-9]+)*(?: ?\([A-Za-z0-9]+\))?$/.test(row.code),'Invalid code');
  if(channel==='stable')assert(!isTestEvidence(row),'Test evidence in stable release');
  assert(row.scope && Object.keys(row.scope).every(k=>fields.includes(k)), 'Unsupported applicability');
  const s=row.scope;
  assert(Object.keys(s).length===0 || string(s.make),'Specific scope requires make');
  assert(/^[PBCU][\dA-F]{4}$/.test(row.code) || string(s.make),'OEM code requires make');
  for(const k of ['make','model','engineCode','ecu','market']) if(k in s) assert(string(s[k]),'Empty context field');
  if('yearStart' in s || 'yearEnd' in s) assert(Number.isInteger(s.yearStart) && Number.isInteger(s.yearEnd) && s.yearStart>=1886 && s.yearEnd<=2200 && s.yearStart<=s.yearEnd,'Invalid years');
  assert(row.text && Object.keys(row.text).length && Object.entries(row.text).every(([k,v])=>['ar','en','sv'].includes(k)&&string(v)),'Invalid translation');
  assert(Object.hasOwn(rank,row.confidence) && string(row.reviewedBy),'Missing technical review');
  if(row.technical!==undefined){
    assert(row.technical && Object.keys(row.technical).every(k=>['ar','en','sv'].includes(k)),'Invalid notes language');
    for(const notes of Object.values(row.technical)){
      assert(notes && string(notes.summary) && Object.keys(notes).every(k=>['summary','causes','tests'].includes(k)),'Invalid summary');
      for(const k of ['causes','tests'])if(k in notes)assert(Array.isArray(notes[k]) && notes[k].length && notes[k].every(string),'Invalid diagnostic notes');
    }
  }
  assert(row.status==='approved','Only approved records may be distributed');
  evidence(root,row,channel);
}

function overlapping(a,b){
  for(const key of ['make','model','engineCode','ecu','market']){
    const normalize=key==='make'?makeKey:norm;
    if(a[key] && b[key] && normalize(a[key])!==normalize(b[key]))return false;
  }
  return !(a.yearStart && b.yearStart && (a.yearEnd<b.yearStart || b.yearEnd<a.yearStart));
}
function includesScope(a,b){
  return ['make','model','engineCode','ecu','market'].every(k=>!a[k]||b[k]) &&
    (!a.yearStart || (b.yearStart>=a.yearStart && b.yearEnd<=a.yearEnd));
}

export function compile({root, batches, channel}) {
  assert(['trial','stable'].includes(channel));
  const states=[], pending=new Map(), revisions=new Map(), identities=new Map(), scopesByCode=new Map();
  let records=new Map(), parent=null;
  let vehicles=new Map();
  const vehicleHistory=new Map(), sourceCache=new Map();
  for(const [index,batch] of batches.entries()) {
    assert.equal(batch.sequence,index+1,'Gap or duplicate release');
    assert(batch.channel===channel && typeof batch.date==='string' && new Date(batch.date).toISOString()===batch.date,'Invalid channel/date');
    assert(!index || batch.date>=batches[index-1].date,'Date regression');
    assert(Array.isArray(batch.changes),'Missing changes');
    const audit=[], seen=new Set();
    if(batch.restore!==undefined){
      assert(Number.isInteger(batch.restore)&&batch.restore>0&&batch.restore<=index&&batch.changes.length===0&&string(batch.reason),'Invalid restore');
      assert(!batch.vehicles?.length,'Restore must not add vehicle records');
      records=new Map(states[batch.restore-1].records);
      vehicles=new Map(states[batch.restore-1].vehicles);
    }
    assert(Array.isArray(batch.vehicles ?? []),'Invalid vehicle reviews');
    for(const review of batch.vehicles ?? []){
      assert(channel==='stable' && !seen.has(review.id),'Duplicate or unsupported vehicle review');
      seen.add(review.id);
      const vehicle=reviewedVehicle(root,review,sourceCache);
      const previous=vehicleHistory.get(vehicle.id);
      assert.equal(review.replaces,previous && hash(json(previous)),'Repeated or stale vehicle review');
      if(previous){
        assert(previous.vehicleId===vehicle.vehicleId && previous.make===vehicle.make && previous.model===vehicle.model,'Vehicle identity reassigned');
      }
      vehicles.set(vehicle.id,vehicle);
      vehicleHistory.set(vehicle.id,vehicle);
      audit.push({id:vehicle.id,operation:'vehicle',source:review.source,reviewedBy:review.reviewedBy,current:hash(json(vehicle))});
    }
    for(const row of batch.changes) {
      if(row.status==='candidate'){
        assert(string(row.id),'Candidate requires a durable review ID');
        const reasons=[];
        if(!row.source?.reference || !row.source?.locator)reasons.push('technical reference or locator missing');
        if(!row.text || !Object.values(row.text).some(string))reasons.push('definition missing');
        if(!row.scope)reasons.push('applicability not specified');
        reasons.push('technical approval pending');
        pending.set(row.id,{sequence:batch.sequence,id:row.id,source:row.source ?? null,reason:reasons.join(', ')});
        continue;
      }
      if(row.status==='pending'){
        assert(string(row.id) && string(row.reason),'Review entry needs ID and reason');
        pending.set(row.id,{sequence:batch.sequence,id:row.id,source:row.source ?? null,reason:row.reason});
        continue;
      }
      validate(root,row,channel);
      pending.delete(row.id);
      const key=scopeKey(row), previous=revisions.get(row.id);
      assert(!seen.has(row.id),'Repeated ID in batch');
      seen.add(row.id);
      assert(!identities.has(key)||identities.get(key)===row.id,'Duplicate code/context');
      if(previous) {
        assert.equal(scopeKey(previous),key,'Existing ID reassigned');
        if(previous.sourceRecordId)assert.equal(row.sourceRecordId,previous.sourceRecordId,'Original source ID changed');
        for(const [lang,notes] of Object.entries(previous.technical||{})){
          for(const field of Object.keys(notes))assert(row.technical?.[lang]?.[field],'Technical information removed');
        }
        assert.equal(row.replaces,hash(json(previous)),'Stale correction');
        assert(rank[row.confidence]>=rank[previous.confidence],'Evidence downgrade');
        for(const lang of Object.keys(previous.text)) assert(string(row.text[lang]),'Translation removed');
      } else assert(!row.replaces,'Correction has no predecessor');
      if(!previous){
        const related=scopesByCode.get(codeKey(row.code))||[];
        for(const other of related)assert(!overlapping(other,row.scope) || includesScope(other,row.scope) || includesScope(row.scope,other),'Ambiguous overlapping code contexts');
        related.push(row.scope);scopesByCode.set(codeKey(row.code),related);
      }
      identities.set(key,row.id);
      revisions.set(row.id,row);
      records.set(row.id,row);
      const changed=Object.keys(row).filter(k=>k!=='replaces' && JSON.stringify(previous?.[k])!==JSON.stringify(row[k]));
      audit.push({id:row.id,changed,operation:previous?'correct':'add',previous:previous?hash(json(previous)):null,current:hash(json(row)),source:row.source,reviewedBy:row.reviewedBy});
    }
    const digest=hash(json({parent,batch}));
    states.push({sequence:batch.sequence,date:batch.date,digest,parent,records:new Map(records),vehicles:new Map(vehicles),audit,restore:batch.restore??null,reason:batch.reason??null});
    parent=digest;
  }
  return {states,pending:[...pending.values()]};
}

function atomic(file,bytes) {
  fs.mkdirSync(path.dirname(file),{recursive:true});
  const tmp=file+'.'+randomUUID()+'.tmp';
  try { fs.writeFileSync(tmp,bytes,{flag:'wx'}); fs.renameSync(tmp,file); }
  finally { if(fs.existsSync(tmp)) fs.unlinkSync(tmp); }
}
function immutable(file,bytes){
  if(fs.existsSync(file)) assert(fs.readFileSync(file).equals(bytes),'Immutable artifact differs');
  else atomic(file,bytes);
}
export async function publish({out,channel,states,privateKey,commit,verifyDelivery}) {
  assert(states.length && /^[a-f0-9]{40}$/.test(commit),'Missing version or Git revision');
  assert(createPublicKey(privateKey).asymmetricKeyDetails?.namedCurve==='prime256v1','Use P-256 release key');
  fs.mkdirSync(out,{recursive:true});
  const lock=path.join(out,'.publish.lock');
  const fd=fs.openSync(lock,'wx');
  try {
    const current=path.join(out,'current.json');
    if(fs.existsSync(current)) {
      const old=JSON.parse(fs.readFileSync(current));
      const body=Buffer.from(old.payload,'base64');
      assert(verify('sha256',body,{key:createPublicKey(privateKey),dsaEncoding:'ieee-p1363'},Buffer.from(old.signature,'base64')),'Invalid previous signature');
      const prior=JSON.parse(body);
      assert(prior.channel===channel && states[prior.sequence-1]?.digest===prior.digest,'Release history rewritten or stale');
      if(prior.sequence===states.length)return;
      assert.equal(prior.sequence+1,states.length,'Publish each approved batch in order');
    }
    const state=states.at(-1), groups=new Map();
    for(const row of state.records.values()){
      const key=makeKey(row.scope.make)||'*';
      if(!groups.has(key))groups.set(key,[]);
      groups.get(key).push(row);
    }
    const packs=[];
    for(const [group,rows] of [...groups].sort(([a],[b])=>a.localeCompare(b))){
      rows.sort((a,b)=>a.id.localeCompare(b.id));
      const bytes=json(rows),sha256=hash(bytes);
      immutable(path.join(out,'packs',sha256+'.json'),bytes);
      packs.push({group,sha256,count:rows.length});
    }
    let vehiclePack;
    if(state.vehicles?.size){
      const vehicles=[...state.vehicles.values()].sort((a,b)=>a.id.localeCompare(b.id));
      const bytes=json(vehicles),sha256=hash(bytes);
      immutable(path.join(out,'packs',sha256+'.json'),bytes);
      vehiclePack={group:'vehicles',sha256,count:vehicles.length};
    }
    if(channel==='stable'){
      assert(typeof verifyDelivery==='function','Public delivery verification required');
      for(const pack of packs)await verifyDelivery(pack.sha256);
      if(vehiclePack)await verifyDelivery(vehiclePack.sha256);
    }
    const payload=json({schema:vehiclePack?2:1,channel,sequence:state.sequence,date:state.date,digest:state.digest,commit,packs,vehiclePack,restore:state.restore,reason:state.reason});
    const signature=sign('sha256',payload,{key:privateKey,dsaEncoding:'ieee-p1363'});
    const envelope=json({payload:payload.toString('base64'),signature:signature.toString('base64')});
    // A retry after an interrupted activation reuses the already signed envelope.
    const archived=path.join(out,'releases',state.sequence+'.json');
    if(fs.existsSync(archived)){
      const prior=JSON.parse(fs.readFileSync(archived)),body=Buffer.from(prior.payload,'base64');
      const archivedMeta=JSON.parse(body),requested=JSON.parse(payload);
      assert(JSON.stringify({...archivedMeta,commit:requested.commit})===JSON.stringify(requested)&&verify('sha256',body,{key:createPublicKey(privateKey),dsaEncoding:'ieee-p1363'},Buffer.from(prior.signature,'base64')),'Conflicting archived release');
    }else immutable(archived,envelope);
    immutable(path.join(out,'releases',state.sequence+'-changes.json'),json({sequence:state.sequence,date:state.date,restore:state.restore,reason:state.reason,changes:state.audit}));
    atomic(current,fs.readFileSync(archived));
  } finally {fs.closeSync(fd); fs.unlinkSync(lock);}
}

if(process.argv[1] && import.meta.url===pathToFileURL(path.resolve(process.argv[1])).href){
  const root=process.cwd(),dir=path.join(root,'data/web/batches');
  const batches=fs.readdirSync(dir).filter(n=>n.endsWith('.json')).sort().map(n=>JSON.parse(fs.readFileSync(path.join(dir,n))));
  const result=compile({root,batches,channel:'stable'});
  console.log(JSON.stringify({releases:result.states.length,pending:result.pending}));
  if(process.env.DTC_REVIEW_REPORT)fs.writeFileSync(process.env.DTC_REVIEW_REPORT,JSON.stringify(result.pending,null,2));
  if(process.argv[2]==='publish'){
    const commit=execFileSync('git',['rev-parse','HEAD'],{encoding:'utf8'}).trim();
    const out=process.env.DTC_DATA_ROOT, current=path.join(out,'current.json');
    const existing=fs.existsSync(current)?JSON.parse(Buffer.from(JSON.parse(fs.readFileSync(current)).payload,'base64')).sequence:0;
    assert(result.states.length && existing<=result.states.length,'No release or stale history');
    const origin=new URL(process.env.DTC_WEB_ORIGIN);
    assert(origin.protocol==='https:' && !origin.username && !origin.password,'HTTPS distribution origin required');
    async function verifyDelivery(sha){
      const url=new URL('/dtc-data/packs/'+sha+'.json',origin);
      const response=await fetch(url,{redirect:'error',cache:'no-store',signal:AbortSignal.timeout(30000)});
      assert(response.ok && hash(Buffer.from(await response.arrayBuffer()))===sha,'Public pack verification failed');
    }
    for(let end=Math.max(1,existing);end<=result.states.length;end++)
      await publish({out,channel:'stable',states:result.states.slice(0,end),privateKey:process.env.DTC_RELEASE_PRIVATE_KEY,commit,verifyDelivery});
  }
}
