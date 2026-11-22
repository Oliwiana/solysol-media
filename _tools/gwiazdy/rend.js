// node rend.js <id> [jpgs t1 t2 ...]  – renderuje /home/claude/gw/<id>/index.html do video.mp4 (bez audio) albo klatki podglądu
const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn}=require('child_process');const fs=require('fs');
(async()=>{const id=process.argv[2],dir='/home/claude/gw/'+id;const D=JSON.parse(fs.readFileSync(dir+'/timeline.json'));const FPS=24,DUR=D.total;
const b=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await b.newPage();await pg.setViewport({width:1080,height:1920});
await pg.goto('file://'+dir+'/index.html',{waitUntil:'networkidle0'});await pg.evaluate(()=>document.fonts.ready);
if(process.argv[3]==='jpgs'){for(const t of process.argv.slice(4)){await pg.evaluate(t=>setT(t),+t);await new Promise(r=>setTimeout(r,150));await pg.screenshot({path:dir+'/f_'+t+'.jpg',type:'jpeg',quality:80})}await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',''+FPS,'-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',dir+'/video.mp4']);
for(let f=0;f<Math.round(FPS*DUR);f++){await pg.evaluate(t=>setT(t),f/FPS);const buf=await pg.screenshot({type:'jpeg',quality:88});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await b.close()})();
