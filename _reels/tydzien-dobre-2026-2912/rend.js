const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
const DIR=process.argv[2],mode=process.argv[3];
(async()=>{const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file://'+DIR+'/index.html',{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await new Promise(r=>setTimeout(r,500));
if(mode=='shots'){for(const t of process.argv.slice(4)){await pg.evaluate(t=>setT(t),+t);await pg.screenshot({path:DIR+'/prev_'+t+'.jpg',type:'jpeg',quality:80})}await b.close();return}
const FPS=25,DUR=+process.argv[4],out=process.argv[5];
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',out]);
for(let f=0;f<FPS*DUR;f++){await pg.evaluate(t=>setT(t),f/FPS);const buf=await pg.screenshot({type:'jpeg',quality:90});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
