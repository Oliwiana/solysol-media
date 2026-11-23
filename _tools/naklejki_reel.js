// Nakłada animowane naklejki-wycinanki (kolaż) na gotowy reel.mp4. Użycie: node naklejki_reel.js spec.json wej.mp4 wyj.mp4
// spec: [{src:'/abs.png', t0, t1, x, y, w, r}] – współrzędne w 1080x1920; wejście „pyk” (skala 0→1.15→1, obrót), wyjście 0,18 s.
const p=require('/home/claude/tools/node_modules/puppeteer-core');const {spawn,execSync}=require('child_process');const fs=require('fs');
(async()=>{const [,,specF,inp,out]=process.argv;const S=JSON.parse(fs.readFileSync(specF));
const info=execSync(`ffprobe -v error -select_streams v:0 -show_entries stream=width,height,r_frame_rate,bit_rate -show_entries format=duration -of json "${inp}"`).toString();const J=JSON.parse(info);
const VBR=+J.streams[0].bit_rate||0;const W=J.streams[0].width,H=J.streams[0].height,[a,b]=J.streams[0].r_frame_rate.split('/'),FPS=a/b,DUR=+J.format.duration,k=W/1080;
const html=`<!doctype html><html><head><style>html,body{margin:0;width:${W}px;height:${H}px;background:transparent;overflow:hidden}img{filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))}</style></head><body>${S.map((s,i)=>`<div id=s${i} style="position:absolute;left:${s.x*k}px;top:${s.y*k}px;width:${s.w*k}px;opacity:0;transform-origin:50% 60%">${s.blob?`<div style="position:absolute;left:${(s.bx||-8)}%;top:${(s.by||-6)}%;width:${s.bs||100}%;aspect-ratio:1;border-radius:50%;background:${s.blob}"></div>`:''}<img src="file://${s.src}" style="position:relative;width:100%;display:block"></div>`).join('')}
<script>const S=${JSON.stringify(S)};function ease(x){return 1-Math.pow(1-x,3)}
function setT(t){S.forEach((s,i)=>{const e=document.getElementById('s'+i);if(t<s.t0||t>s.t1){e.style.opacity=0;return}
let a=t-s.t0,sc=1,op=1,rot=s.r||0;if(a<.28){const x=a/.28;sc=x<.7?ease(x/.7)*1.15:1.15-.15*((x-.7)/.3);rot+=(1-x)*-14}
const z=s.t1-t;if(z<.18){sc*=z/.18;op=z/.18}rot+=Math.sin((t-s.t0)*2.2)*1.2;sc*=1+.025*Math.sin((t-s.t0)*1.7);
e.style.opacity=op;e.style.transform='rotate('+rot+'deg) scale('+sc+')'})}</script></body></html>`;
fs.writeFileSync('/tmp/_nk_'+process.pid+'.html',html);
const br=await p.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox','--allow-file-access-from-files']});const pg=await br.newPage();await pg.setViewport({width:W,height:H});
await pg.goto('file:///tmp/_nk_'+process.pid+'.html',{waitUntil:'load'});
const blank=await pg.screenshot({type:'png',omitBackground:true});
const ff=spawn('ffmpeg',['-y','-loglevel','error','-i',inp,'-f','image2pipe','-framerate',''+FPS,'-c:v','png','-i','-','-filter_complex','[0:v][1:v]overlay=0:0:format=auto[v]','-map','[v]','-map','0:a?','-c:v','libx264','-preset','veryfast','-crf',process.env.CRF||'28',...(VBR&&!process.env.NOCAP?['-maxrate',''+Math.round(VBR*1.1),'-bufsize',''+Math.round(VBR*2)]:[]),'-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',out]);
const N=Math.round(FPS*DUR);for(let f=0;f<N;f++){const t=f/FPS;const vis=S.some(s=>t>=s.t0&&t<=s.t1);let buf;
if(vis){await pg.evaluate(t=>setT(t),t);buf=await pg.screenshot({type:'png',omitBackground:true})}else buf=blank;
if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r))}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await br.close()})();
