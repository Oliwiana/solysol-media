const p=require('/home/claude/tools/node_modules/puppeteer-core');
(async()=>{const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1350});
for(let i=1;i<=10;i++){await pg.goto('file:///tmp/p25b/p'+i+'.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await new Promise(r=>setTimeout(r,150));await pg.screenshot({path:'/tmp/p25b/post-'+i+'.jpg',type:'jpeg',quality:92})}
await b.close()})();
