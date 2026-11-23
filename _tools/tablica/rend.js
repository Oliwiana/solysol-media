const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const [,,page,W,H,FPS,DUR,out,audio,...ts]=process.argv;
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:+W,height:+H});
await pg.goto('file://'+page,{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
if(out.endsWith('.jpg')){for(const t of ts){await pg.evaluate(t=>setT(t),+t);await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:70})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',FPS,'-i','-','-i',audio,'-map','0:v','-map','1:a','-c:v','libx264','-preset','veryfast','-crf','26','-pix_fmt','yuv420p','-c:a','aac','-b:a','128k','-shortest','-movflags','+faststart',out]);
const N=Math.round(+FPS*+DUR);for(let f=0;f<N;f++){await pg.evaluate(t=>setT(t),f/+FPS);const buf=await pg.screenshot({type:'jpeg',quality:85});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));if(f%300==0)console.log(f,N)}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
