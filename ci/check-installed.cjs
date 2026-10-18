'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs');
const {chromium}=require('playwright');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 try{
  const page=await browser.newPage();
  await page.goto('http://127.0.0.1:8873/',{waitUntil:'load',timeout:60000});
  await page.waitForFunction(()=>window.NexisUpdates&&window.RC2,{timeout:30000});
  const result=await page.evaluate(async()=>{
   for(const dialog of document.querySelectorAll('dialog[open]'))dialog.close();
   await new Promise(resolve=>setTimeout(resolve,3000));
   for(let attempt=0;attempt<50&&document.getElementById('updateBtn').disabled;attempt++)
    await new Promise(resolve=>setTimeout(resolve,500));
   if(document.getElementById('updateBtn').disabled)throw Error('Automatic update check did not settle');
   const messages=[],original=window.RC2.toast;
   window.RC2.toast=(text)=>{messages.push(String(text));original(text);};
   await window.NexisUpdates.check(true);
   return {messages,current:window.NexisUpdates.currentVersionCode,url:window.NEXIS_CONFIG.updateUrl,
     key:window.NEXIS_CONFIG.updatePublicKey};
  });
  const expected=JSON.parse(fs.readFileSync('verified-manifest.json','utf8'));
  const key=JSON.parse(fs.readFileSync('update-public-key.json','utf8'));
  assert.equal(result.current,expected.versionCode);
  assert.equal(result.url,'https://raw.githubusercontent.com/dtcnexis/DTC-Nexis-Updates/main/update-feed.json');
  assert.deepEqual(result.key,key);
  assert(result.messages.some(text=>/الأحدث|latest version|senaste versionen/.test(text)), 'Installed update button did not confirm the current signed release');
  fs.writeFileSync('installed-channel-verification.json',JSON.stringify({passed:true,revision:result.current,pinnedPublicKey:true,signedFeedChecked:true,currentVersionConfirmed:true},null,2));
  console.log('PASS: installed Windows program verified its public signed channel and confirmed the current version');
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
