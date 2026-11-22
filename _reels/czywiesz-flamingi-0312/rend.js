const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const [FPS,DUR,out,audio]=[+process.argv[2],+process.argv[3],process.argv[4],process.argv[5]];const SP=1.08;
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file:///home/claude/work/r/index.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
if(out.endsWith('.jpg')){for(const t of process.argv.slice(5)){await pg.evaluate(t=>setT(t),+t);await new Promise(r=>setTimeout(r,50));await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:85})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-i',audio,'-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','28','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',out]);
for(let f=0;f<FPS*DUR;f++){await pg.evaluate(t=>setT(t),f/FPS*SP);const buf=await pg.screenshot({type:'jpeg',quality:88});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
