// node rendv.js <html> <dur> <audio.m4a> <out.mp4> [crf]
const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');
(async()=>{const [html,DUR,AUD,out,CRF]=process.argv.slice(2);const fps=24,dur=+DUR;
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});
const pg=await b.newPage();await pg.setViewport({width:1080,height:1920,deviceScaleFactor:2/3});await pg.goto('file://'+html,{waitUntil:'load'});await pg.evaluate(()=>document.fonts.ready);await new Promise(r=>setTimeout(r,500));
if(out.endsWith('.jpg')){for(const t of process.argv.slice(7)){await pg.evaluate(t=>setT(t),+t);await pg.screenshot({path:out.replace('.jpg','_'+t+'.jpg'),type:'jpeg',quality:85})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+fps,'-i','-','-i',AUD,'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf',CRF||'28','-maxrate','420k','-bufsize','840k','-pix_fmt','yuv420p','-c:a','aac','-b:a','96k','-shortest','-movflags','+faststart',out]);
const n=Math.round(dur*fps);for(let f=0;f<n;f++){await pg.evaluate(t=>setT(t),f/fps);const buf=await pg.screenshot({type:'jpeg',quality:85,optimizeForSpeed:true});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
