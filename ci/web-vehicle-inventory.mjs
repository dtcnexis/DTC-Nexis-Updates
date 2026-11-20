import fs from 'node:fs';
import path from 'node:path';
import {execFileSync} from 'node:child_process';
import {modelYears} from './web-vehicles.mjs';

// Count structured source tables once. DTC applicability and bulletin references
// are evidence about a diagnostic condition, not a second vehicle catalogue.
const paths=execFileSync('git',['ls-files','data/master'],{encoding:'utf8'}).trim().split(/\r?\n/);
const read=file=>JSON.parse(fs.readFileSync(file,'utf8').replace(/^\uFEFF/,''));
const records=[];
const modelYearValues=new Set(), productionYearValues=new Set(), modelYearPairs=new Set();
const models=new Set(), makes=new Set();
const groups={vehicles:0,engines:0,vehicle_engine_variants:0};
const batchFiles=fs.readdirSync('data/web/batches').filter(name=>name.endsWith('.json')).sort();
const {compile}=await import('./web-release.mjs');
const {states}=compile({root:process.cwd(),channel:'stable',batches:batchFiles.map(n=>read('data/web/batches/'+n))});
const released=states.at(-1)?.vehicles ?? new Map();
for(const file of paths.filter(f=>f.endsWith('.json'))){
  const doc=read(file);
  let tables=doc.related_datasets ?? doc.related, prefix=doc.related_datasets?'/related_datasets':'/related';
  const kind=doc.section ?? path.basename(file,'.json');
  if(!tables && ['vehicles','engines','vehicle_engine_variants'].includes(kind)){
    tables={[kind]:Array.isArray(doc)?doc:doc.records};
    prefix=Array.isArray(doc)?'':'/records';
  }
  if(!tables)continue;
  for(const type of Object.keys(groups)){
    for(const [i,row] of (tables[type] ?? []).entries()){
      const pointer=prefix+(tables===doc.related_datasets || tables===doc.related?'/'+type:'')+'/'+i;
      const id=row.id ?? (type==='vehicles'?row.vehicle_id:row.engine_id);
      const car=type==='vehicles'?row:tables.vehicles?.find(r=>r.id===row.vehicle_id);
      const make=car?.brand ?? row.brand ?? doc.brand ?? (file.includes('/byd_')?'BYD':file.includes('/dacia_')?'Dacia':undefined);
      const model=car?.model ?? row.model;
      let years=modelYears(row.model_year_scope ?? row.model_years);
      if(!years && row.model_year_start && row.model_year_end)years=modelYears(row.model_year_start+'-'+row.model_year_end);
      const first=row.production_start_year ?? row.production_year_start;
      const last=row.production_end_year ?? row.production_year_end;
      const productionYears=first && last ? modelYears(first+'-'+last) : null;
      const decision=released.get(id);
      const reasons=[];
      if(!decision)reasons.push('No active stable web review for this source ID');
      if(!model)reasons.push('No directly linked vehicle model');
      if(!years)reasons.push('No bounded model years on this row');
      if(type==='engines' && !row.vehicle_id)reasons.push('Engine family without direct vehicle ID');
      if(type==='vehicle_engine_variants' && !row.engine_id)reasons.push('Engine family ID unconfirmed');
      const status=row.verification_status ?? null;
      records.push({file,pointer,id,type,make,model,vehicleId:row.vehicle_id,engineId:row.engine_id,
        engineName:row.commercial_engine_name ?? row.engine_display_name ?? row.description,
        code:row.engine_code ?? row.engine_code_family,codeVerified:row.engine_code_verified,
        years,productionYears,status,sourceIds:row.source_ids,reasons});
      groups[type]++;
      if(make)makes.add(make);
      if(make && model)models.add(JSON.stringify([make,model]));
      if(years)for(let y=years[0];y<=years[1];y++){
        modelYearValues.add(y);
        if(make && model)modelYearPairs.add(JSON.stringify([make,model,y]));
      }
      if(productionYears)for(let y=productionYears[0];y<=productionYears[1];y++)productionYearValues.add(y);
    }
  }
}
const summary={groups,makes:[...makes].sort(),makeModels:models.size,
  modelYears:[...modelYearValues].sort(),makeModelYears:modelYearPairs.size,
  productionYears:[...productionYearValues].sort(),stableVehicleIds:released.size};
const report={masterTree:execFileSync('git',['rev-parse','HEAD:data/master'],{encoding:'utf8'}).trim(),summary,records};
if(process.argv[2])fs.writeFileSync(process.argv[2],JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify(summary));
