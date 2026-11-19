import fs from 'node:fs';
import path from 'node:path';
import {createHash,generateKeyPairSync} from 'node:crypto';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {compile,publish} from '../ci/web-release.mjs';
export const root=fileURLToPath(new URL('../',import.meta.url));
const sha=text=>createHash('sha256').update(text).digest('hex');
const file='qa/web-fixtures/source.json';
const sourceText=fs.readFileSync(path.join(root,file),'utf8').replace(/\r\n/g,'\n');
const source=JSON.parse(sourceText);
function row(n,id,scope,revision){
  const label='TEST '+id+' '+revision;
  return {id,code:source.records[n].code,sourceRecordId:source.records[n].id,scope,text:{ar:label,en:label,sv:label},
    technical:{ar:{summary:'TEST notes '+revision,causes:['TEST cause'],tests:['TEST check']}},status:'approved',confidence:'technical',reviewedBy:'AUTOMATED TRIAL ONLY',
    source:{reference:'https://example.invalid/dtc-test',locator:'synthetic fixture',file,sha256:sha(sourceText),pointer:'/records/'+n}};
}
const makeBatch=(sequence,changes)=>({channel:'trial',sequence,date:'2026-11-'+(18+sequence)+'T00:00:00.000Z',changes});
export function trialBatches(){
  const volvo=row(1,'trial:volvo',{make:'Volvo',model:'V70',yearStart:2014,yearEnd:2016,engineCode:'D4204T5'},1);
  const correction={...volvo,text:{ar:'TEST VOLVO revised',en:'TEST VOLVO revised',sv:'TEST VOLVO revised'},replaces:sha(JSON.stringify(volvo))};
  return [makeBatch(1,[row(0,'trial:general',{},1),volvo,row(0,'trial:bmw',{make:'BMW'},1),row(2,'legacy:P0106',{},1),{id:'trial:pending',status:'pending',reason:'Missing technical evidence'}]),
    makeBatch(2,[correction]),{...makeBatch(3,[]),restore:1,reason:'Synthetic recovery exercise'}];
}
export async function generateTrial(directory,sequence){
  fs.mkdirSync(directory,{recursive:true});
  const keyFile=path.join(directory,'trial-private.pem');
  if(!fs.existsSync(keyFile)){
    const pair=generateKeyPairSync('ec',{namedCurve:'P-256'});
    fs.writeFileSync(keyFile,pair.privateKey.export({type:'pkcs8',format:'pem'}),{mode:0o600,flag:'wx'});
    fs.writeFileSync(path.join(directory,'public.pem'),pair.publicKey.export({type:'spki',format:'pem'}));
  }
  const batches=trialBatches().slice(0,sequence);
  const {states,pending}=compile({root,batches,channel:'trial'});
  await publish({out:path.join(directory,'feed'),states,channel:'trial',privateKey:fs.readFileSync(keyFile),commit:'0'.repeat(40)});
  return pending;
}
if(process.argv[1]&&import.meta.url===pathToFileURL(path.resolve(process.argv[1])).href){
  const n=Number(process.argv[3]);
  if(![1,2,3].includes(n))throw Error('Use a disposable directory and a trial sequence of 1, 2 or 3');
  await generateTrial(path.resolve(process.argv[2]),n);
}
