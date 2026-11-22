import json
from shots import SHOTS
from words import W
S=1.2
F='file:///home/claude/tools/node_modules/@fontsource/'
def ff(fam,pkg,w,style='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{style};src:url({F}{pkg}/files/{pkg}-{sub}-{w}-{style}.woff2)}}" for sub in ('latin','latin-ext'))
fonts=ff('O','oswald',600)+ff('CG','cormorant-garamond',500,'italic')+ff('CG','cormorant-garamond',600,'normal')+ff('CG','cormorant-garamond',600,'italic')+ff('I','inter',900)+ff('I','inter',800)+ff('I','inter',600)+ff('T','special-elite',400)
KEY={'Trzy','miliony','2026','5','5.','4.','3.','2.','1?','rekord','794','Błękitne','Flagi.','45','Europejską','Stolicą','Gdańsku.','Starlite','15','Lenny','Kravitz,','Maroon','Deep','Purple.','ciekawie.','Lipiec.','3','pierwszy','Premios','Juventud','Ameryki.','września','Marbelli.','Shakira,','Karol','G','Bad','Bunny.','wybrzeża.','komentarzu.','numer','jeden.','Gastronomicznej.','Kultury'}
words=[[w,a/S,b/S] for w,a,b in W]
ph=[];cur=[]
SOFT=('w','i','z','na','do','–','A','W','I','to','Rok','Numer','numer')
for w in words:
    cur.append(w)
    if w[0][-1] in '.?!…' or w[0][-1]==',' and len(cur)>=2 or len(cur)>=4 and w[0] not in SOFT:
        ph.append(cur);cur=[]
if cur: ph.append(cur)
ph=[[[x[0],round(x[1],3),round(x[2],3),1 if x[0] in KEY else 0] for x in p] for p in ph]
shots=[[round(s[0]/S,3),'img/%02d.jpg'%i,s[1]] for i,s in enumerate(SHOTS)]
VEND=round(62.85/S,2)
html=f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{fonts}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#2a1e14;font-family:I}}
#bd{{position:absolute;inset:0;background:#2a1e14}}
#bd:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
#pols{{position:absolute;inset:0;z-index:1}}
.pol{{position:absolute;left:100px;top:230px;width:840px;padding:20px 20px 74px;background:#efe6d2;box-shadow:8px 18px 36px rgba(0,0,0,.65);opacity:0}}
.pol .win{{width:840px;height:560px;overflow:hidden;position:relative;background:#111}}
.pol img{{position:absolute;left:0;top:0;width:840px;height:560px;transform-origin:50% 50%}}
.pol .lab{{position:absolute;left:24px;bottom:20px;font-family:T;font-size:34px;color:#1d1a16;white-space:nowrap}}
.pin{{position:absolute;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-14px;z-index:3}}
.e{{position:absolute;opacity:0;z-index:5}}
.paper{{background:#efe6d2;color:#1d1a16;box-shadow:6px 14px 30px rgba(0,0,0,.6);font-family:T}}
.stamp{{font-family:I;font-weight:900;border:9px solid;padding:6px 26px;letter-spacing:.06em;border-radius:8px;background:rgba(239,230,210,.92);white-space:nowrap}}
.ybar{{background:#f2e35b;color:#171513;font-weight:900;box-shadow:6px 12px 24px rgba(0,0,0,.5);padding:12px 26px;white-space:nowrap}}
.num{{font-family:O;font-weight:600;color:#f2e35b;font-size:150px;line-height:1;text-shadow:4px 8px 20px rgba(0,0,0,.7)}}
#vig{{z-index:6;position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 42%,transparent 52%,rgba(0,0,0,.72) 100%)}}
#top{{z-index:7;position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(180deg,rgba(0,0,0,.75),transparent)}}
#brand{{z-index:8;position:absolute;left:64px;top:160px;font-family:CG;font-weight:600;font-size:44px;letter-spacing:.08em;color:#efe6d2}}
#brand i{{color:#f2e35b;font-style:italic}}
#sec{{z-index:8;position:absolute;right:150px;top:168px;background:#5b7cff;color:#fff;font-weight:800;font-size:26px;letter-spacing:.14em;padding:8px 16px}}
#cap{{z-index:8;position:absolute;left:56px;right:150px;top:1285px;background:rgba(12,9,6,.84);border-radius:18px;padding:20px 22px;text-align:center;font-family:I;font-weight:900;font-size:62px;line-height:1.12;color:#fff;text-transform:uppercase;letter-spacing:-.01em;opacity:0}}
#cap .k{{color:#f2e35b}}
#cr{{z-index:8;position:absolute;left:18px;top:420px;writing-mode:vertical-rl;transform:rotate(180deg);color:#efe6d2;font-size:15px;font-weight:600;letter-spacing:.1em;opacity:.55}}
#hook{{z-index:20;position:absolute;inset:0;background:#0d0d0f;overflow:hidden}}
#hbg{{position:absolute;left:-54px;top:-96px;width:1188px;height:2112px;object-fit:cover;filter:grayscale(1) contrast(1.15) brightness(.75)}}
#hook .tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,20,.6),rgba(8,10,20,.25) 35%,rgba(8,10,20,.93) 68%)}}
.lb{{display:inline-block;font-family:I;font-weight:600;font-size:40px;line-height:1.05;padding:6px 14px 8px}}
.blue{{background:#5b7cff;color:#fff}}.yel{{background:#f2e35b;color:#2f45c9}}
.h{{font-family:O;font-weight:600;font-size:124px;line-height:.98;letter-spacing:-.025em;margin:24px 0 0;color:#f4f1ea}}
.h u{{text-decoration-thickness:7px;text-underline-offset:14px;text-decoration-color:#f2e35b}}
.h em{{font-family:CG;font-style:italic;font-weight:500;letter-spacing:-.01em}}
#end{{z-index:9;left:56px;right:150px;top:820px;background:#f2e35b;padding:44px 46px;color:#171513}}
</style></head><body>
<div id=bd></div>
<div id=pols></div>
<div class=e id=k5 style="left:70px;top:945px"><div class=num>#5</div></div>
<div class="e paper" id=n794 style="left:330px;top:955px;width:500px;padding:22px 26px;text-align:center;transform:rotate(3deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:104px;line-height:1">794</div><div style="font-size:32px">rekord Błękitnych Flag</div></div>
<div class="e ybar" id=n45 style="left:110px;top:1160px;transform:rotate(-3deg);font-size:50px">45 W PROWINCJI MÁLAGA</div>
<div class=e id=k4 style="left:70px;top:945px"><div class=num>#4</div></div>
<div class="e paper" id=ngas style="left:300px;top:955px;width:560px;padding:24px 28px;transform:rotate(-2deg)"><div class=pin></div><div style="font-size:28px;opacity:.75">MÁLAGA 2026:</div><div style="font-size:40px;line-height:1.2;margin-top:6px">Europejska Stolica Kultury Gastronomicznej</div></div>
<div class="e stamp" id=ngd style="left:330px;top:1160px;color:#c0281b;font-size:80px;transform:rotate(-7deg)">GDAŃSK</div>
<div class=e id=k3 style="left:70px;top:945px"><div class=num>#3</div></div>
<div class="e paper" id=nst style="left:330px;top:955px;width:500px;padding:22px 26px;text-align:center;transform:rotate(4deg)"><div class=pin></div><div style="font-size:30px">Starlite · Marbella</div><div style="font-family:I;font-weight:900;font-size:96px;line-height:1">15 LAT</div></div>
<div class="e ybar" id=nkr style="left:110px;top:1160px;transform:rotate(-2deg);font-size:40px">KRAVITZ · MAROON 5 · DEEP PURPLE</div>
<div class=e id=k2 style="left:70px;top:945px"><div class=num>#2</div></div>
<div class="e paper" id=n3m style="left:300px;top:955px;width:560px;padding:22px 26px;text-align:center;transform:rotate(-3deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:92px;line-height:1">3 000 000</div><div style="font-size:32px">pasażerów · lipiec 2026</div></div>
<div class="e stamp" id=nrek style="left:180px;top:1160px;color:#c0281b;font-size:64px;transform:rotate(5deg)">PIERWSZY RAZ</div>
<div class=e id=k1 style="left:70px;top:945px"><div class=num>#1</div></div>
<div class="e paper" id=npj style="left:280px;top:955px;width:600px;padding:22px 26px;transform:rotate(2deg)"><div class=pin></div><div style="font-size:28px;opacity:.75">3 WRZEŚNIA 2026 · MARBELLA</div><div style="font-family:I;font-weight:900;font-size:52px;line-height:1.05;margin-top:6px;white-space:nowrap">PREMIOS JUVENTUD</div></div>
<div class="e stamp" id=npe style="left:120px;top:1160px;color:#c0281b;font-size:38px;transform:rotate(-4deg)">PIERWSZY RAZ POZA AMERYKĄ</div>
<div class="e paper" id=nred style="left:110px;top:955px;width:760px;padding:26px 32px;transform:rotate(-1.5deg);background:#1d1a16;color:#efe6d2"><div class=pin></div><div style="font-family:I;font-weight:800;font-size:28px;letter-spacing:.2em;color:#f2e35b">ZDANIEM REDAKCJI</div><div style="font-family:O;font-weight:600;font-size:76px;line-height:1.02;margin-top:10px">2026 – rok wybrzeża</div></div>
<div id=vig></div>
<div id=top></div><div id=brand>SOL <i>y</i> SÓL</div><div id=sec>TEMAT TYGODNIA</div>
<div id=cr>FOT. WIKIMEDIA COMMONS (CC BY / CC BY-SA) · ZDJĘCIA ILUSTRACYJNE · AUTORZY W OPISIE POSTA</div>
<div id=cap></div>
<div class=e id=end><div style="font-family:O;font-weight:600;font-size:96px;line-height:1">@solysol.pl</div><div style="font-family:CG;font-style:italic;font-weight:600;font-size:46px;margin-top:12px">Obserwuj – więcej dobrych wiadomości z wybrzeża</div></div>
<div id=hook><img id=hbg src=img/hook.jpg><div class=tint></div>
<div style="position:absolute;left:64px;top:160px;font-family:CG;font-weight:600;font-size:44px;letter-spacing:.08em;color:#efe6d2">SOL <i style="color:#f2e35b">y</i> SÓL</div>
<div style="position:absolute;left:64px;right:150px;top:780px"><span class="lb blue">Temat tygodnia</span> <span class="lb yel">Costa del Sol · 2026</span>
<h1 class=h><u>3 miliony</u> ludzi<br>w jeden miesiąc.<br><em>A to nie jest</em><br><em>numer jeden.</em></h1></div></div>
<script>
const SH={json.dumps(shots,ensure_ascii=False)};
const PH={json.dumps(ph,ensure_ascii=False)};
const HOOKEND={round(2.5/S,2)}, VEND={VEND};
const P=document.getElementById('pols');
SH.forEach((s,i)=>{{const d=document.createElement('div');d.className='pol';d.id='p'+i;d.innerHTML='<div class=pin></div><div class=win><img src="'+s[1]+'"></div><div class=lab>'+s[2]+'</div>';P.appendChild(d)}});
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
function pop(id,a,b,t,sc0){{const el=document.getElementById(id);const k=E(a,0.25,t)*(1-E(b,0.25,t));el.style.opacity=k;el.style.display=k>0?'block':'none';const base=el.dataset.tr!==undefined?el.dataset.tr:(el.dataset.tr=el.style.transform||'');el.style.transform=base+' scale('+(sc0+(1-sc0)*E(a,0.25,t))+')'}}
const T=x=>x/{S};
window.setT=function(t){{
 const h=document.getElementById('hook');h.style.opacity=1-E(HOOKEND,0.25,t);h.style.display=t>HOOKEND+0.3?'none':'block';
 document.getElementById('hbg').style.transform='scale('+(1+0.05*t/HOOKEND)+')';
 for(let i=0;i<SH.length;i++){{const a=SH[i][0],b=i+1<SH.length?SH[i+1][0]:VEND;const el=document.getElementById('p'+i);
  if(t<a-0.01||t>b+0.3){{el.style.display='none';continue}}el.style.display='block';
  const k=E(a,0.2,t);el.style.opacity=k;const rot=(i%2?2.2:-2.2);el.style.transform='rotate('+rot+'deg) scale('+(1.06-0.06*k)+')';el.style.zIndex=i;
  const u=Math.min(1,Math.max(0,(t-a)/(b-a+0.3)));const dir=i%4;const z=1.04+0.12*(dir<2?u:1-u);const tx=(dir%2?1:-1)*24*(u-0.5),ty=(dir==2?-1:1)*16*(u-0.5);
  el.querySelector('img').style.transform='translate('+tx+'px,'+ty+'px) scale('+z+')'}}
 const c=document.getElementById('cap');let p=null;for(const q of PH){{if(t>=q[0][1]-0.05&&t<=q[q.length-1][2]+0.3)p=q}}
 if(!p||t<HOOKEND||t>VEND){{c.style.opacity=0}}else{{c.style.opacity=1;c.innerHTML=p.filter(w=>t>=w[1]-0.04).map(w=>'<span class='+(w[3]?'k':'')+'>'+w[0]+'</span>').join(' ')}}
 pop('k5',T(11.6),T(20.5),t,1.6);pop('n794',T(14.6),T(20.5),t,1.3);pop('n45',T(17.6),T(20.5),t,1.3);
 pop('k4',T(20.6),T(28.4),t,1.6);pop('ngas',T(22.3),T(28.4),t,1.1);pop('ngd',T(27.4),T(28.4),t,2.0);
 pop('k3',T(28.5),T(37.0),t,1.6);pop('nst',T(29.6),T(37.0),t,1.3);pop('nkr',T(33.9),T(37.0),t,1.3);
 pop('k2',T(38.9),T(45.3),t,1.6);pop('n3m',T(43.1),T(45.3),t,1.3);pop('nrek',T(41.8),T(45.3),t,2.0);
 pop('k1',T(45.5),T(56.5),t,1.6);pop('npj',T(46.5),T(56.5),t,1.1);pop('npe',T(48.6),T(56.5),t,1.6);
 pop('nred',T(56.6),VEND,t,1.08);
 const en=document.getElementById('end');const ke=E(VEND,0.35,t);en.style.opacity=ke;en.style.display=ke>0?'block':'none';en.style.transform='translateY('+(60*(1-ke))+'px)';
}};
</script></body></html>'''
open('index.html','w').write(html)
print(len(ph),'phrases',len(shots),'shots',VEND)
