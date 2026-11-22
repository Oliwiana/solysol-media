import json
shots=json.load(open('/home/claude/w/shots.json'));groups=json.load(open('/home/claude/w/groups.json'))
F='/home/claude/tools/node_modules/@fontsource'
ff=''
for fam,dir_,w,st in [('O','oswald',600,'normal'),('O','oswald',700,'normal'),('I','inter',600,'normal'),('I','inter',800,'normal'),('I','inter',900,'normal'),('S','cormorant-garamond',500,'italic'),('S','cormorant-garamond',600,'normal')]:
  for sub in ['latin','latin-ext']:
    ff+=f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url(file://{F}/{dir_}/files/{dir_}-{sub}-{w}-{st}.woff2)}}"
imgs=''.join(f'<img class=ph id=p{i} src="file://{s["src"]}">' for i,s in enumerate(shots))
html=f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{ff}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#0d0d0f;color:#f4f1ea;font-family:I}}
#tint,#vig,.grain,.brand,.cr,#slab,#hook,.stamp,#ver,#cap,#end{{z-index:5}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:1920px;opacity:0;will-change:transform}}
#tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,20,.62) 0%,rgba(8,10,20,.12) 22%,rgba(8,10,20,.1) 45%,rgba(8,10,20,.72) 70%,rgba(8,10,20,.9) 100%)}}
#vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,transparent 55%,rgba(0,0,0,.6) 100%)}}
.grain{{position:absolute;inset:0;opacity:.2;mix-blend-mode:overlay}}
.brand{{position:absolute;left:64px;top:160px;font-family:S;font-weight:600;font-size:40px;letter-spacing:.08em}}
.brand i{{color:#f2e35b}}
.cr{{position:absolute;left:66px;top:212px;font-family:I;font-weight:600;font-size:19px;letter-spacing:.06em;opacity:.6;text-transform:uppercase}}
.lab{{display:inline-block;font-family:I;font-weight:600;font-size:38px;line-height:1.05;padding:7px 16px 9px;letter-spacing:-.01em}}
.blue{{background:#5b7cff;color:#fff}}.yel{{background:#f2e35b;color:#2f45c9}}
#slab{{position:absolute;left:64px;top:270px;opacity:0}}
#hook{{position:absolute;left:64px;right:150px;top:560px}}
.h{{font-family:O;font-weight:600;font-size:132px;line-height:.98;letter-spacing:-.025em;margin:26px 0 0}}
.h u{{text-decoration-thickness:7px;text-underline-offset:14px}}
.h em{{font-family:S;font-style:italic;font-weight:500;font-size:1.04em}}
#cap{{position:absolute;left:64px;right:150px;top:1190px;height:300px;display:block;text-align:center;font-family:O;font-weight:700;font-size:84px;line-height:1.04;text-transform:uppercase;text-shadow:0 4px 0 #000,0 0 30px rgba(0,0,0,.9);letter-spacing:-.01em}}
#cap span{{display:inline}}
.stamp{{position:absolute;font-family:O;font-weight:700;border:9px solid;padding:4px 30px;letter-spacing:.06em;opacity:0}}
#ver{{position:absolute;left:64px;right:150px;top:430px;opacity:0}}
#ver .big{{font-family:O;font-weight:700;font-size:118px;line-height:1;margin-top:24px;color:#0d0d0f;background:#f2e35b;display:inline-block;padding:10px 26px 16px;transform:rotate(-2deg)}}
#ver .ln{{font-family:I;font-weight:800;font-size:50px;line-height:1.2;margin-top:34px;opacity:0;background:rgba(10,10,14,.8);padding:14px 22px;display:inline-block}}
#end{{position:absolute;inset:0;background:#0d0d0f;opacity:0;display:flex;flex-direction:column;justify-content:center;padding:0 64px;box-sizing:border-box}}
</style></head><body>
{imgs}
<div id=tint></div><div id=hdim style="position:absolute;inset:0;background:#000;z-index:4"></div><div id=vig></div>
<svg class=grain width=1080 height=1920><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch /></filter><rect width=100% height=100% filter=url(#n) /></svg>
<div class=brand>SOL <i>y</i> SÓL</div><div class=cr>Zdjęcia ilustracyjne · Wikimedia Commons</div>
<div id=slab><span class="lab yel" id=slabt></span></div>
<div id=hook><span class="lab blue">Teoria kontra fakty</span> <span class="lab yel">Hiszpania · Sylwester</span>
<h1 class=h>12 winogron<br>o północy –<br><u>marketing</u><br>czy <em>kpina</em>?</h1></div>
<div class=stamp id=st1 style="left:330px;top:640px;color:#f2e35b;font-size:120px;transform:rotate(-8deg)">TEORIA</div>
<div class=stamp id=st2 style="left:300px;top:640px;color:#f4f1ea;font-size:120px;transform:rotate(6deg)">FAKTY</div>
<div class=stamp id=st3 style="left:180px;top:560px;color:#f2e35b;font-size:190px;border-width:12px;transform:rotate(-6deg)">1882</div>
<div id=ver><span class="lab blue">Teoria kontra fakty · werdykt</span><br><div class=big>CZĘŚCIOWO<br>PRAWDA</div><br>
<div class=ln id=l1>✔ Rolnicy rozsławili zwyczaj</div><br><div class=ln id=l2 style="color:#f2e35b">✘ Ale go nie wymyślili</div></div>
<div id=cap></div>
<div id=end><div class=brand style="position:static;font-size:64px">SOL <i>y</i> SÓL</div>
<div style="font-family:O;font-weight:700;font-size:150px;line-height:1;margin-top:30px">@solysol.pl</div>
<div style="font-family:S;font-style:italic;font-weight:500;font-size:58px;margin-top:26px;opacity:.9">Obserwuj – więcej historii z wybrzeża.</div>
<div style="font-family:O;font-weight:600;font-size:64px;margin-top:70px">A Ty jesz <span style="color:#f2e35b">12 winogron</span>?</div></div>
<script>
const SH={json.dumps([[s['t'],s['lab']] for s in shots],ensure_ascii=False)};
const G={json.dumps(groups,ensure_ascii=False)};
const END=48.75;
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
function stamp(id,a,b,t){{const el=document.getElementById(id);const k=E(a,0.18,t)*(1-E(b,0.2,t));el.style.opacity=k;el.dataset.r=el.dataset.r||el.style.transform;el.style.transform=el.dataset.r+' scale('+(1+1.4*(1-E(a,0.18,t)))+')'}}
window.setT=function(t){{
 let cur=0;for(let i=0;i<SH.length;i++)if(t>=SH[i][0])cur=i;
 for(let i=0;i<SH.length;i++){{const el=document.getElementById('p'+i);
  if(i==cur||(i==cur-1&&t<SH[cur][0]+0.15)){{const a=SH[i][0],b=(SH[i+1]?SH[i+1][0]:END+2);const k=(t-a)/(b-a);
   const dir=i%4;const z=1.04+0.10*k;const dx=(dir==1?-1:dir==3?1:0)*30*k,dy=(dir==2?-1:0)*30*k;
   el.style.transform='translate('+dx+'px,'+dy+'px) scale('+(dir==0?1.16-0.10*k:z)+')';
   el.style.opacity=i==cur?Math.min(1,(t-a)/0.15+ (i==0?1:0)):1;el.style.zIndex=i==cur?2:1;}}else el.style.opacity=0}}
 const lab=SH[cur][1];const sl=document.getElementById('slab');sl.style.opacity=lab&&t>2.2?E(SH[cur][0],0.15,t):0;document.getElementById('slabt').textContent=lab;
 const hk=document.getElementById('hook');hk.style.opacity=1-E(2.05,0.15,t);document.getElementById('hdim').style.opacity=0.45*(1-E(2.05,0.15,t));
 stamp('st1',3.95,5.3,t);stamp('st2',14.95,16.4,t);stamp('st3',23.25,25.0,t);
 const v=document.getElementById('ver');v.style.opacity=E(39.75,0.2,t)*(1-E(45.2,0.25,t));
 document.getElementById('l1').style.opacity=E(41.85,0.2,t);document.getElementById('l2').style.opacity=E(43.8,0.2,t);
 const c=document.getElementById('cap');let g=null;
 if(t>2.1&&t<END){{for(const q of G){{if(t>=q[0][1]-0.05)g=q}}}}
 if(g&&t>g[g.length-1][1]+1.2)g=null;
 c.innerHTML=g?g.filter(w=>t>=w[1]-0.04).map(w=>'<span style="color:'+(w[2]?'#f2e35b':'#fff')+'">'+w[0]+'</span>').join(' '):'';
 document.getElementById('end').style.opacity=E(END,0.25,t);
}};
</script></body></html>'''
open('/home/claude/w/reel.html','w').write(html)
