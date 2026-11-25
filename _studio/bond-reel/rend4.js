const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const FPS=30,DUR=64.6,out=process.argv[2];
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file:///tmp/bm/pro.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-c:v','libx264','-preset','veryfast','-crf','22','-pix_fmt','yuv420p','-movflags','+faststart',out]);
for(let f=0;f<FPS*DUR;f++){await pg.evaluate(t=>setT(t),f/FPS);const buf=await pg.screenshot({type:'jpeg',quality:90});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
