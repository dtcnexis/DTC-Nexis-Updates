import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import path from 'node:path';

const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const text = value => typeof value === 'string' && value.length && value.trim() === value;
const unique = (rows, id) => {
  const matches = rows.filter(row => (row.id ?? row.source_id ?? row.vehicle_id) === id);
  assert.equal(matches.length, 1, 'Missing or ambiguous source ID: '+id);
  return matches[0];
};

export function modelYears(value) {
  const match = /^(\d{4})(?:[-–](\d{4}))?$/.exec(String(value));
  if (!match) return null;
  const start = Number(match[1]), end = Number(match[2] ?? match[1]);
  return start >= 1886 && end <= 2200 && end >= start ? [start,end] : null;
}

// Derive the delivered facts from the original row and its foreign keys.
// A batch author selects a row and signs off its scope, without retyping specifications.
export function reviewedVehicle(root, review, cache) {
  const {file, commit, pointer, sha256} = review.source ?? {};
  assert(Object.keys(review).every(key=>['id','source','status','reviewedBy','replaces'].includes(key)), 'Unmapped vehicle review field');
  assert(review.status === 'approved' && text(review.reviewedBy), 'Missing vehicle release review');
  assert(/^data\/master\/(?:[\w-]+\/)*[\w-]+\.json$/.test(file) && /^[a-f0-9]{40}$/.test(commit), 'Invalid vehicle source');
  function read(sourceFile) {
    const key = commit+':'+sourceFile;
    if (!cache.has(key)) {
      execFileSync('git',['merge-base','--is-ancestor',commit,'refs/remotes/origin/main'],{cwd:root});
      const bytes = execFileSync('git',['show',key],{cwd:root,encoding:'utf8',maxBuffer:64*1024*1024}).replace(/\r\n/g,'\n');
      cache.set(key,{sha256:hash(bytes),document:JSON.parse(bytes)});
    }
    return cache.get(key);
  }
  const saved = read(file);
  assert.equal(saved.sha256,sha256,'Vehicle source fingerprint changed');
  const doc = saved.document;
  const match = /^\/(related_datasets|related)\/(vehicles|engines|vehicle_engine_variants)\/(0|[1-9]\d*)$/.exec(pointer);
  let tables, table, index;
  if(match){
    tables=doc[match[1]];table=match[2];index=Number(match[3]);
  }else if(doc.section==='vehicles' && /^\/records\/(0|[1-9]\d*)$/.test(pointer)){
    tables={vehicles:doc.records,sources:read(path.posix.join(path.posix.dirname(file),'sources_part01.json')).document.records};
    table='vehicles';index=Number(pointer.slice(9));
  }else if(Array.isArray(doc) && file.endsWith('/vehicles.json') && /^\/(0|[1-9]\d*)$/.test(pointer)){
    tables={vehicles:doc,sources:read(path.posix.join(path.posix.dirname(file),'sources.json')).document};
    table='vehicles';index=Number(pointer.slice(1));
  }
  assert(Array.isArray(tables?.[table]), 'Unsupported vehicle source shape');
  const src=tables[table][index], id=src?.id ?? src?.vehicle_id;
  assert(text(id) && unique(tables[table],id) === src && review.id === id,'Original vehicle record ID mismatch');
  const isVariant = table === 'vehicle_engine_variants';
  const isEngine = table !== 'vehicles';
  const car = isEngine ? unique(tables.vehicles,src.vehicle_id) : src;
  const market=car.market ?? car.markets_confirmed_listed?.join(' / ');
  assert(text(car.brand) && (!doc.brand || car.brand===doc.brand) && text(car.model) && text(market),'Incomplete vehicle identity');
  const carYears = modelYears(car.model_years ?? (car.model_year_start && car.model_year_end ? car.model_year_start+'-'+car.model_year_end : ''));
  const engineYears=src.model_year_scope ?? (src.model_year_start && src.model_year_end ? src.model_year_start+'-'+src.model_year_end : '');
  const years = isEngine ? modelYears(engineYears) : carYears;
  if(isEngine)assert(years && carYears && years[0]>=carYears[0] && years[1]<=carYears[1], 'Explicit, compatible model-year bounds required');
  const refs = (src.source_ids ?? []).map(id=>unique(tables.sources,id));
  assert(refs.length && refs.every(ref=>/^https:\/\//.test(ref.url)), 'Missing vehicle technical reference');
  const record = {id,make:car.brand,model:car.model,...(years?{yearStart:years[0],yearEnd:years[1]}:{}),
    scope:[market,car.generation,car.body_styles ?? car.body_style,car.trim_scope].filter(Boolean).join(' · '),
    source:refs[0].url,references:refs.map(ref=>ref.url),upstreamCommit:commit,provenance:review.source,vehicleId:car.id ?? car.vehicle_id};
  if (isEngine) {
    const name=isVariant ? src.engine_display_name : src.commercial_engine_name;
    const status=isVariant ? 'manufacturer_explicit' : 'manufacturer_documented_specs';
    assert(src.verification_status===status && text(name),'Named engine evidence required');
    const family=isVariant && src.engine_id ? unique(tables.engines,src.engine_id) : src;
    if(isVariant && src.engine_id){
      assert(!family.brand || family.brand===car.brand,'Conflicting engine family make');
      assert(!src.engine_code || src.engine_code===family.engine_code,'Conflicting engine family code');
      record.engineId=family.id;
    }
    Object.assign(record,{name,yearBasis:src.model_year_scope?'model_year_scope':'model_year_start/end',fuel:src.fuel ?? family.fuel_type});
    if (src.engine_code_verified === true) {
      const code=family.engine_code;
      assert(text(code) && /^[A-Z0-9][A-Z0-9 ._-]{1,39}$/.test(code), 'Invalid verified engine code');
      record.engineCodes=[code];
      record.engineCodeEvidence=[{code,source:record.source,scope:record.scope}];
    }
  }
  return record;
}
