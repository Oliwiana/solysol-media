const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const FPS=24,S=1.2,DUR=+process.argv[2],out=process.argv[3];
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file:///tmp/nz/index.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await new Promise(r=>setTimeout(r,500));
if(out.endsWith('.jpg')){for(const t of process.argv.slice(4)){await pg.evaluate(t=>setT(t),+t);await new Promise(r=>setTimeout(r,100));await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:85})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',out]);
for(let f=0;f<FPS*DUR;f++){await pg.evaluate(t=>setT(t),f/FPS*S);const buf=await pg.screenshot({type:'jpeg',quality:88});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
