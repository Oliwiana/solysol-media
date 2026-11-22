// node rend.js <html> <W> <H> <fps> <t0> <t1> <out.mp4|shot.jpg> [times...]
const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const [html,W,H,FPS,T0,T1,out]=process.argv.slice(2);const w=+W,h=+H,fps=+FPS,t0=+T0,t1=+T1;
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files','--disable-web-security']});
const pg=await b.newPage();await pg.setViewport({width:w,height:h});await pg.goto('file://'+html,{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);
await new Promise(r=>setTimeout(r,500));
if(out.endsWith('.jpg')){for(const t of process.argv.slice(9)){await pg.evaluate(t=>setT(t),+t);await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:80})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+fps,'-i','-','-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',out]);
const n=Math.round((t1-t0)*fps);
for(let f=0;f<n;f++){await pg.evaluate(t=>setT(t),t0+f/fps);const buf=await pg.screenshot({type:'jpeg',quality:82,optimizeForSpeed:true});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));if(f%500==0)console.error(f,'/',n)}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
