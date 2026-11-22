import json
from shots import SHOTS
S=1.17
F='file:///home/claude/tools/node_modules/@fontsource/'
def ff(fam,pkg,w,style='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{style};src:url({F}{pkg}/files/{pkg}-{sub}-{w}-{style}.woff2)}}" for sub in ('latin','latin-ext'))
fonts=ff('O','oswald',600)+ff('CG','cormorant-garamond',500,'italic')+ff('CG','cormorant-garamond',600,'normal')+ff('CG','cormorant-garamond',600,'italic')+ff('I','inter',900)+ff('I','inter',800)+ff('I','inter',600)+ff('T','special-elite',400)
W=json.load(open('words_raw.json'))
# merge number words
MERGE=[(['dwa','tysiące','dwadzieścia','sześć.'],'2026.'),(['trzydzieści','sześć'],'36'),(['jedenaście'],'11'),(['Dziesięć'],'10'),(['Cztery'],'4')]
out=[];i=0
while i<len(W):
    for seq,rep in MERGE:
        if [w[0] for w in W[i:i+len(seq)]]==seq:
            out.append([rep,W[i][1],W[i+len(seq)-1][2]]);i+=len(seq);break
    else:
        out.append(W[i]);i+=1
KEY={'2026.','36','11','granatów','karabinów','Marbella.','dnia,','ranny,','trzech','gangów','10','Malaga.','ławce.','pomylili','4','twarz','Muelle','Uno.','Przeżył.','Chirurg','klinice','kulę','medalik','Plan','patroli,','kontroli.','redakcji','zamawia','strzały.','Sól','Lipiec.','Wrzesień.','Październik.','Listopad.','arsenał:'}
words=[[w,round(a/S,3),round(b/S,3)] for w,a,b in out]
ph=[];cur=[]
for w in words:
    cur.append(w)
    if w[0][-1] in '.?!:' or len(cur)>=4 and w[0] not in ('w','i','z','na','we','–','przy','go'):
        ph.append(cur);cur=[]
if cur: ph.append(cur)
ph=[[[x[0],x[1],x[2],1 if x[0] in KEY else 0] for x in p] for p in ph]
shots=[[round(s[0]/S,3),'img/%02d.jpg'%i,s[2]] for i,s in enumerate(SHOTS)]
t=lambda x:round(x/S,2)
HOOKEND=t(2.95); ENDT=t(58.75); VEND=t(62.9)
pops=[('narse',8.25,11.75,1.3),('nwrz',11.8,13.4,1.4),('n13',15.1,17.05,1.8),('ngang',19.25,21.3,1.1),('nmal',21.5,23.65,1.4),('npom',27.55,29.4,2.0),('n4',29.5,31.6,1.4),('nprz',35.4,36.3,2.2),('npaz',36.25,37.3,1.4),('nchir',38.2,40.8,1.1),('nlis',40.95,42.2,1.4),('nmed',46.9,48.35,1.6),('nplan',48.4,53.1,1.1),('nred',53.2,58.65,1.08)]
popjs=';'.join(f"pop('{a}',{t(b)},{t(c)},t,{d})" for a,b,c,d in pops)
html=f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{fonts}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#2a1e14;font-family:I}}
#pols{{position:absolute;inset:0;z-index:1}}
#bd{{position:absolute;inset:0;background:#2a1e14}}
#bd:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
.pol{{position:absolute;left:80px;top:290px;width:880px;padding:20px 20px 74px;background:#efe6d2;box-shadow:8px 18px 36px rgba(0,0,0,.65);opacity:0}}
.pol .win{{width:880px;height:818px;overflow:hidden;position:relative;background:#111}}
.pol img{{position:absolute;left:0;top:0;width:880px;height:818px;transform-origin:50% 50%}}
.pol .lab{{position:absolute;left:24px;bottom:20px;font-family:T;font-size:34px;color:#1d1a16}}
.pin{{position:absolute;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-14px;z-index:3}}
.e{{position:absolute;opacity:0;z-index:5}}
.paper{{background:#efe6d2;color:#1d1a16;box-shadow:6px 14px 30px rgba(0,0,0,.6);font-family:T}}
.stamp{{font-family:I;font-weight:900;border:9px solid;padding:6px 26px;letter-spacing:.06em;border-radius:8px;background:rgba(239,230,210,.92);white-space:nowrap}}
.ybar{{background:#f2e35b;color:#171513;font-weight:900;box-shadow:6px 12px 24px rgba(0,0,0,.5);padding:12px 26px;white-space:nowrap}}
#vig{{z-index:6;position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 42%,transparent 52%,rgba(0,0,0,.72) 100%)}}
#top{{z-index:7;position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(180deg,rgba(0,0,0,.75),transparent)}}
#brand{{z-index:8;position:absolute;left:64px;top:160px;font-family:CG;font-weight:600;font-size:46px;letter-spacing:.08em;color:#efe6d2}}
#brand i{{color:#f2e35b;font-style:italic}}
#sec{{z-index:8;position:absolute;right:150px;top:170px;background:#5b7cff;color:#fff;font-weight:800;font-size:26px;letter-spacing:.14em;padding:8px 16px}}
#cap{{z-index:8;position:absolute;left:56px;right:150px;top:1262px;background:rgba(12,9,6,.84);border-radius:18px;padding:22px 22px;text-align:center;font-family:I;font-weight:900;font-size:66px;line-height:1.12;color:#fff;text-transform:uppercase;letter-spacing:-.01em;opacity:0}}
#cap .k{{color:#f2e35b}}
#cr{{z-index:8;position:absolute;left:18px;top:420px;writing-mode:vertical-rl;transform:rotate(180deg);color:#efe6d2;font-size:15px;font-weight:600;letter-spacing:.1em;opacity:.55}}
#hook{{z-index:20;position:absolute;inset:0;background:#0d0d0f}}
#hbg{{position:absolute;left:-54px;top:-96px;width:1188px;height:2112px;filter:contrast(1.1) brightness(.85)}}
#hook .tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,20,.6),rgba(8,10,20,.35) 30%,rgba(8,10,20,.92) 62%)}}
.lb{{display:inline-block;font-family:I;font-weight:600;font-size:40px;line-height:1.05;padding:6px 14px 8px}}
.blue{{background:#5b7cff;color:#fff}}.yel{{background:#f2e35b;color:#2f45c9}}
.h{{font-family:O;font-weight:600;font-size:124px;line-height:.98;letter-spacing:-.025em;margin:24px 0 0;color:#f4f1ea}}
.h u{{text-decoration-thickness:7px;text-underline-offset:14px;text-decoration-color:#f2e35b}}
.h em{{font-family:CG;font-style:italic;font-weight:500;letter-spacing:-.01em}}
#end{{z-index:9;left:56px;right:150px;top:1000px;background:#f2e35b;padding:44px 46px;color:#171513}}
</style></head><body>
<div id=bd></div>
<div id=pols></div>
<div class="e paper" id=narse style="left:110px;top:880px;width:600px;padding:26px 34px;transform:rotate(-3deg)"><div class=pin></div><div style="font-size:30px;opacity:.75">LIPIEC · ARSENAŁ</div><div style="font-family:I;font-weight:900;font-size:84px;line-height:1.02;margin-top:6px">36 karabinów<br><span style="color:#c0281b">11 granatów</span></div></div>
<div class="e ybar" id=nwrz style="left:110px;top:1060px;transform:rotate(-4deg);font-size:58px">WRZESIEŃ · MARBELLA</div>
<div class="e stamp" id=n13 style="left:110px;top:1010px;color:#c0281b;font-size:64px;transform:rotate(-6deg)">1 RANNY · 3 ZATRZYMANYCH</div>
<div class="e paper" id=ngang style="left:110px;top:900px;width:760px;padding:28px 34px;transform:rotate(2deg)"><div class=pin></div><div style="font-size:28px;opacity:.75">PRZEDSTAWICIEL RZĄDU:</div><div style="font-size:48px;line-height:1.2;margin-top:8px">„porachunki gangów narkotykowych”</div></div>
<div class="e ybar" id=nmal style="left:120px;top:1060px;transform:rotate(3deg);font-size:62px">+10 DNI · MALAGA</div>
<div class="e stamp" id=npom style="left:330px;top:1020px;color:#c0281b;font-size:110px;transform:rotate(-8deg)">POMYŁKA?</div>
<div class="e ybar" id=n4 style="left:110px;top:1060px;transform:rotate(-3deg);font-size:58px">+4 DNI · MUELLE UNO</div>
<div class="e stamp" id=nprz style="left:380px;top:1020px;color:#1f7a3a;font-size:110px;transform:rotate(-7deg)">PRZEŻYŁ</div>
<div class="e ybar" id=npaz style="left:110px;top:1060px;transform:rotate(3deg);font-size:58px">PAŹDZIERNIK · MARBELLA</div>
<div class="e paper" id=nchir style="left:300px;top:900px;width:560px;padding:26px 32px;transform:rotate(-3deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:54px;line-height:1.05">CHIRURG<br>PLASTYCZNY</div><div style="font-size:34px;margin-top:10px">zastrzelony we własnej klinice</div></div>
<div class="e ybar" id=nlis style="left:110px;top:1060px;transform:rotate(-3deg);font-size:58px">LISTOPAD · MALAGA</div>
<div class="e paper" id=nmed style="left:470px;top:880px;width:420px;padding:24px;text-align:center;transform:rotate(5deg)"><div class=pin></div><div style="font-size:30px">kula w klatkę piersiową</div><div style="font-family:I;font-weight:900;font-size:76px;line-height:1.05;margin-top:6px;color:#c0281b">MEDALIK?</div><div style="font-size:28px;margin-top:6px">mógł złagodzić uderzenie</div></div>
<div class="e paper" id=nplan style="left:110px;top:880px;width:780px;padding:28px 34px;transform:rotate(-1.5deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:56px">PLAN COSTA DEL SOL</div><div style="font-size:40px;line-height:1.25;margin-top:8px">+ więcej patroli<br>+ więcej kontroli</div></div>
<div class="e" id=nred style="left:100px;top:720px;width:830px;box-sizing:border-box;padding:40px 44px 44px;background:#1d1a16;color:#efe6d2;transform:rotate(-1.5deg);box-shadow:8px 18px 40px rgba(0,0,0,.7)"><div style="font-family:I;font-weight:800;font-size:30px;letter-spacing:.2em;color:#f2e35b">ZDANIEM REDAKCJI</div><div style="font-family:O;font-weight:600;font-size:70px;line-height:1.02;margin-top:14px">Liczy się nie liczba patroli.<br><span style="color:#f2e35b">Kto zamawia te strzały?</span></div></div>
<div id=vig></div>
<div id=top></div><div id=brand>SOL <i>y</i> SÓL</div><div id=sec>TEMAT TYGODNIA</div>
<div id=cr>FOT. WIKIMEDIA COMMONS (CC BY / CC BY-SA / CC0 / PD) · ZDJĘCIA ILUSTRACYJNE · AUTORZY W OPISIE POSTA</div>
<div id=cap></div>
<div class=e id=end><div style="font-family:O;font-weight:600;font-size:100px;line-height:1">@solysol.pl</div><div style="font-family:CG;font-style:italic;font-weight:600;font-size:46px;margin-top:12px">Obserwuj – więcej takich historii z wybrzeża</div></div>
<div id=hook><img id=hbg src=img/hook.jpg><div class=tint></div>
<div style="position:absolute;left:64px;top:160px;font-family:CG;font-weight:600;font-size:46px;letter-spacing:.08em;color:#efe6d2">SOL <i style="color:#f2e35b">y</i> SÓL</div>
<div style="position:absolute;left:64px;right:150px;top:700px"><span class="lb blue">Temat tygodnia</span> <span class="lb yel">Costa del Sol · 2026</span>
<h1 class=h>Czy na<br>Costa del Sol<br>strzela się już<br><u>w biały</u> <em>dzień?</em></h1></div></div>
<script>
const SH={json.dumps(shots,ensure_ascii=False)};
const PH={json.dumps(ph,ensure_ascii=False)};
const HOOKEND={HOOKEND}, ENDT={ENDT};
const P=document.getElementById('pols');
SH.forEach((s,i)=>{{const d=document.createElement('div');d.className='pol';d.id='p'+i;d.innerHTML='<div class=pin></div><div class=win><img src="'+s[1]+'"></div><div class=lab>'+s[2]+'</div>';P.appendChild(d)}});
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
function pop(id,a,b,t,sc0){{const el=document.getElementById(id);const k=E(a,0.25,t)*(1-E(b,0.25,t));el.style.opacity=k;const base=el.dataset.tr||(el.dataset.tr=el.style.transform||'');el.style.transform=base+' scale('+(sc0+(1-sc0)*E(a,0.25,t))+')'}}
window.setT=function(t){{
 const h=document.getElementById('hook');h.style.opacity=1-E(HOOKEND,0.2,t);h.style.display=t>HOOKEND+0.25?'none':'block';
 document.getElementById('hbg').style.transform='scale('+(1+0.06*Math.min(t,HOOKEND)/HOOKEND)+')';
 for(let i=0;i<SH.length;i++){{const a=SH[i][0],b=i+1<SH.length?SH[i+1][0]:99;const el=document.getElementById('p'+i);
  if(t<a-0.01||t>b+0.3){{el.style.display='none';continue}}el.style.display='block';
  const k=E(a,0.18,t);el.style.opacity=k;const rot=(i%2?2.2:-2.2);el.style.transform='rotate('+rot+'deg) scale('+(1.06-0.06*k)+')';el.style.zIndex=i;
  const u=Math.min(1,Math.max(0,(t-a)/Math.min(4,(b-a+0.3))));const dir=i%4;const z=1.05+0.14*(dir<2?u:1-u);const tx=(dir%2?1:-1)*30*(u-0.5),ty=(dir==2?-1:1)*20*(u-0.5);
  el.querySelector('img').style.transform='translate('+tx+'px,'+ty+'px) scale('+z+')'}}
 const c=document.getElementById('cap');let p=null;for(const q of PH){{if(t>=q[0][1]-0.05&&t<=q[q.length-1][2]+0.25)p=q}}
 if(!p||t<HOOKEND||t>ENDT-0.05){{c.style.opacity=0}}else{{c.style.opacity=1;c.innerHTML=p.filter(w=>t>=w[1]-0.04).map(w=>'<span class='+(w[3]?'k':'')+'>'+w[0]+'</span>').join(' ')}}
 {popjs};
 const en=document.getElementById('end');en.style.opacity=E(ENDT,0.3,t);en.style.transform='translateY('+(60*(1-E(ENDT,0.3,t)))+'px)';
}};
</script></body></html>'''
open('index.html','w').write(html)
print(len(ph),'phrases; final dur',VEND)
