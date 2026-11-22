const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const FPS=+process.argv[2],DUR=+process.argv[3],out=process.argv[4];
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files','--disable-dev-shm-usage','--disable-gpu']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file:///tmp/claude-0/-home-claude-solysol-media/7abeb8da-1b3f-526a-874f-667401aac922/scratchpad/mdma/index.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await new Promise(r=>setTimeout(r,500));
if(out.endsWith('.jpg')){for(const t of process.argv.slice(5)){await pg.evaluate(t=>setT(t),+t);await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:85})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',out]);
const F0=+(process.argv[5]||0);for(let f=F0;f<Math.min(FPS*DUR,F0+(+(process.argv[6]||1e9)));f++){await pg.evaluate(t=>setT(t),f/FPS);const buf=await pg.screenshot({type:'jpeg',quality:85});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
