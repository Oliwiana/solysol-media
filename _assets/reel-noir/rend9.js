const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const FPS=+process.argv[2]||24,DUR=+process.argv[3]||41,out=process.argv[4];
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file:///tmp/bondv/index9.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
if(out.endsWith('.jpg')){for(const t of process.argv.slice(5)){await pg.evaluate(t=>setT(t),+t);await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:80})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-i','/tmp/bondv/audio8.m4a','-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','24','-maxrate','1.2M','-bufsize','2.4M','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',out]);
for(let f=0;f<FPS*DUR;f++){{const ts=f/FPS*1.15;const tv=ts<20.56?ts:(ts<24.08?20.56+(ts-20.56)*(3.08/3.52):ts-0.44);await pg.evaluate(t=>setT(t),tv)};const buf=await pg.screenshot({type:'jpeg',quality:88});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
