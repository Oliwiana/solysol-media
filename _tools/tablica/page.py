import json,html
F='file:///home/claude/tools/node_modules/@fontsource'
def page(els,strings,cams,js,creds,BH,caps,hook,end,top_r,Wd=1080,Hd=1920,endT=99,hook_end=3.0,yt=True):
    css=f'''@font-face{{font-family:T;src:url({F}/special-elite/files/special-elite-latin-ext-400-normal.woff2)}}
@font-face{{font-family:T;src:url({F}/special-elite/files/special-elite-latin-400-normal.woff2)}}
@font-face{{font-family:I;font-weight:900;src:url({F}/inter/files/inter-latin-ext-900-normal.woff2)}}@font-face{{font-family:I;font-weight:900;src:url({F}/inter/files/inter-latin-900-normal.woff2)}}
@font-face{{font-family:I;font-weight:800;src:url({F}/inter/files/inter-latin-ext-800-normal.woff2)}}@font-face{{font-family:I;font-weight:800;src:url({F}/inter/files/inter-latin-800-normal.woff2)}}
@font-face{{font-family:CG;font-style:italic;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-ext-600-italic.woff2)}}@font-face{{font-family:CG;font-style:italic;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-600-italic.woff2)}}
@font-face{{font-family:CG;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-ext-600-normal.woff2)}}@font-face{{font-family:CG;font-weight:600;src:url({F}/cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff2)}}
html,body{{margin:0;width:{Wd}px;height:{Hd}px;overflow:hidden;background:#2a1e14;font-family:I}}
#board{{position:absolute;left:0;top:0;width:{Wd}px;height:{BH}px;transform-origin:{Wd//2}px 0;background:#2a1e14}}
#board:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
.e{{position:absolute;opacity:0}}
.pin{{position:absolute;width:26px;height:26px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-13px;z-index:2}}
.paper{{background:#efe6d2;color:#1d1a16;box-shadow:6px 14px 30px rgba(0,0,0,.6);font-family:T}}
.paper img{{filter:contrast(1.05) sepia(.12)}}
.dark{{background:#1d1a16;color:#efe6d2}}
.pc{{position:absolute;left:30px;right:30px;bottom:26px;font-size:38px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.li{{font-size:50px;margin-top:22px}}
.u{{width:70px;height:56px;background:#c0281b;border:2px solid #7a130b;border-radius:4px;opacity:0}}
.cnt{{position:absolute;right:46px;bottom:26px;font-family:I;font-weight:900;font-size:80px;color:#c0281b}}
.stamp{{font-family:I;font-weight:900;border:8px solid;padding:6px 26px;letter-spacing:.06em;border-radius:8px;mix-blend-mode:multiply;white-space:nowrap}}
#vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.75) 100%)}}
#top{{position:absolute;left:0;right:0;top:0;height:200px;background:linear-gradient(180deg,rgba(0,0,0,.7),transparent);display:flex;justify-content:space-between;align-items:flex-start;padding:62px 64px 0;box-sizing:border-box;color:#efe6d2;font-weight:800;font-size:24px;letter-spacing:.22em}}
#top .b{{font-family:CG;font-weight:600;font-size:40px;letter-spacing:.08em}}#top .b i{{color:#F6C343}}
#cap{{position:absolute;left:{'60px' if Hd>Wd else '260px'};right:{'60px' if Hd>Wd else '260px'};bottom:{'250px' if Hd>Wd else '50px'};text-align:center;font-weight:900;font-size:{'58px' if Hd>Wd else '40px'};line-height:1.15;text-transform:uppercase;background:rgba(15,10,6,.82);padding:22px 26px;border-radius:12px}}
#cr{{position:absolute;right:14px;top:{'300px' if Hd>Wd else '160px'};writing-mode:vertical-rl;font-size:15px;color:#efe6d2;opacity:.55;white-space:nowrap;letter-spacing:.08em}}
#hook{{position:absolute;inset:0;background-size:cover;background-position:center}}
#end{{position:absolute;left:{'80px' if Hd>Wd else '460px'};right:{'80px' if Hd>Wd else '460px'};top:{'700px' if Hd>Wd else '230px'};opacity:0;text-align:center;color:#efe6d2;background:rgba(15,10,6,.9);padding:60px 40px;border-radius:16px}}
'''
    YT='<div style="margin-top:26px;display:inline-block;background:#F6C343;color:#171513;font-weight:900;font-size:44px;padding:12px 26px">▶ DŁUŻSZY ODCINEK NA YOUTUBE</div><div style="font-size:38px;margin-top:16px;font-weight:800">youtube.com/@solysolpl</div>' if yt else '<div style="font-size:40px;margin-top:20px;font-weight:800">Nowy odcinek w każdą niedzielę o 18:00 · solysol.pl</div>'
    body=f'''<div id=board><svg width={Wd} height={BH} style="position:absolute;left:0;top:0;z-index:1">{''.join(strings)}</svg>{''.join(els)}</div>
<div id=vig></div><div id=top><span class=b>SOL <i>y</i> SÓL</span><span>{top_r}</span></div>
<div id=cr>FOT. WIKIMEDIA COMMONS (CC BY / BY-SA / CC0) · AUTORZY W OPISIE · ZDJĘCIA ILUSTRACYJNE</div>
<div id=cap></div><div id=hook style="background-image:url({hook})"></div>
<div id=end><div style="font-family:CG;font-weight:600;font-size:64px;letter-spacing:.06em">SOL <i style="color:#F6C343">y</i> SÓL</div><div style="font-weight:900;font-size:62px;margin-top:20px">{end}</div>{YT}</div>'''
    cams.sort(key=lambda q:q[0])
    script=f'''<script>
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
const typ=(id,txt,a,dur,t)=>{{const n=Math.floor(txt.length*Math.max(0,Math.min(1,(t-a)/dur)));const el=document.getElementById(id);el.style.opacity=t>=a?1:0;el.textContent=txt.slice(0,n)+(t>=a&&t<a+dur+0.6&&Math.floor(t*3)%2?'_':'')}};
function pop(id,a,t,sc0){{const el=document.getElementById(id);const k=E(a,0.35,t);el.style.opacity=k;const base=el.dataset.tr!==undefined?el.dataset.tr:(el.dataset.tr=el.style.transform||'');el.style.transform=base+' scale('+(sc0+(1-sc0)*k)+')'}}
function str(id,a,dur,t){{const p=document.getElementById(id);const L=p.getTotalLength();p.style.strokeDasharray=L;p.style.strokeDashoffset=L*(1-E(a,dur,t))}}
const C={json.dumps([[round(a,2),c] for a,c in cams])};for(const q of C){{if(typeof q[1]=='string'){{const el=document.getElementById(q[1]);const sb=document.getElementById(q[1]+'s');let h=el.offsetHeight;if(sb)h=Math.max(h,sb.offsetTop+sb.offsetHeight-el.offsetTop);q[1]=el.offsetTop+Math.min(h,{Hd}*0.8)/2}}}}const HC={Hd*0.42 if Hd>Wd else Hd*0.47};
function cam(t){{let c=C[0][1];for(let i=0;i<C.length;i++){{if(t>=C[i][0]){{const pc=i?C[i-1][1]:C[0][1];const k=E(C[i][0],0.45,t);c=pc+(C[i][1]-pc)*k}}}}const z={'1.02' if Hd>Wd else '0.98'}+0.03*Math.sin(t*0.25);document.getElementById('board').style.transform='translateY('+(HC-c*z)+'px) scale('+z+')'}}
const PH={json.dumps(caps,ensure_ascii=False)};
function caps(t){{const c=document.getElementById('cap');let p=null;for(const q of PH){{if(t>=q[0][1]-0.05&&t<=q[q.length-1][2]+0.25)p=q}}if(!p||t>{endT}){{c.innerHTML='';c.style.opacity=0;return}}c.style.opacity=1;c.innerHTML=p.map(w=>'<span style="color:'+(t>=w[1]-0.02?'#F6C343':'#fff')+'">'+w[0]+'</span>').join(' ')}}
window.setT=function(t){{cam(t);caps(t);
const hk=document.getElementById('hook');hk.style.opacity=1-E({hook_end},0.35,t);hk.style.transform='scale('+(1+0.03*t/3)+')';
{''.join(js)}
const en=document.getElementById('end');en.style.opacity=E({endT},0.4,t);en.style.transform='translateY('+(80*(1-E({endT},0.4,t)))+'px)'}};
</script>'''
    return f'<!DOCTYPE html><html><head><meta charset=utf-8><style>{css}</style></head><body>{body}{script}</body></html>'
