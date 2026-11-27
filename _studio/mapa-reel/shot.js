const p=require('/home/claude/tools/node_modules/puppeteer-core');
(async()=>{const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file:///tmp/kp/pro.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
const ts=process.argv.slice(2).map(Number);
// warm timeline smoothing
for(const t of ts){for(let k=60;k>=0;k--)await pg.evaluate(x=>setT(x),Math.max(0,t-k/30));await pg.screenshot({path:'/tmp/kp/f_'+t+'.jpg',type:'jpeg',quality:80})}
await b.close()})();
