import json
from shots import SHOTS
from words import W
S=1.12
F='file:///home/claude/tools/node_modules/@fontsource/'
def ff(fam,pkg,w,style='normal',name=None):
    n=name or pkg
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{style};src:url({F}{pkg}/files/{n}-{sub}-{w}-{style}.woff2)}}" for sub in ('latin','latin-ext'))
fonts=ff('O','oswald',600)+ff('CG','cormorant-garamond',500,'italic')+ff('CG','cormorant-garamond',600,'normal')+ff('I','inter',900)+ff('I','inter',800)+ff('I','inter',600)+ff('T','special-elite',400)
# captions: phrases
KEY={'70','razy.','1904','piątej','rano.','teoria,','100\u00a0000','100\u00a0000.','jedną','Wszędzie','wielokrotnie','więcej','Więcej','ciekawie.','Torreviei','dwa','lata','rzędu.','Malaga.','naraz.','Mit.','częściej.','nigdy.','komentarzu.','Doña','Manolita','szczęście.'}
words=[[('70' if w=='siedemdziesiąt' else w.replace('100 000','100\u00a0000')),a/S,b/S] for w,a,b in W]
# split into phrases at sentence ends or max 6 words
ph=[];cur=[]
for w in words:
    cur.append(w)
    if w[0][-1] in '.?!' or len(cur)>=6 and w[0] not in ('w','i','z','na','do','–','A','W'):
        ph.append(cur);cur=[]
if cur: ph.append(cur)
ph=[[[x[0],round(x[1],3),round(x[2],3),1 if x[0] in KEY else 0] for x in p] for p in ph]
shots=[[round(s[0]/S,3),'img/%02d.jpg'%i,s[2]] for i,s in enumerate(SHOTS)]
html=f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{fonts}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#2a1e14;font-family:I}}
#pols{{position:absolute;inset:0;z-index:1}}
.e{{z-index:5}}
#bd{{position:absolute;inset:0;background:#2a1e14}}
#bd:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
.pol{{position:absolute;left:90px;top:300px;width:880px;padding:20px 20px 74px;background:#efe6d2;box-shadow:8px 18px 36px rgba(0,0,0,.65);opacity:0}}
.pol .win{{width:880px;height:818px;overflow:hidden;position:relative;background:#111}}
.pol img{{position:absolute;left:0;top:0;width:880px;height:818px;transform-origin:50% 50%}}
.pol .lab{{position:absolute;left:24px;bottom:20px;font-family:T;font-size:36px;color:#1d1a16}}
.pin{{position:absolute;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-14px;z-index:3}}
.e{{position:absolute;opacity:0}}
.paper{{background:#efe6d2;color:#1d1a16;box-shadow:6px 14px 30px rgba(0,0,0,.6);font-family:T}}
.stamp{{font-family:I;font-weight:900;border:9px solid;padding:6px 26px;letter-spacing:.06em;border-radius:8px;background:rgba(239,230,210,.9)}}
.ybar{{background:#f2e35b;color:#171513;font-weight:900;box-shadow:6px 12px 24px rgba(0,0,0,.5);padding:12px 26px}}
#vig{{z-index:6;position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 42%,transparent 52%,rgba(0,0,0,.72) 100%)}}
#top{{z-index:7;position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(180deg,rgba(0,0,0,.75),transparent);}}
#brand{{z-index:8;position:absolute;left:64px;top:150px;font-family:CG;font-weight:600;font-size:46px;letter-spacing:.08em;color:#efe6d2}}
#brand i{{color:#f2e35b;font-style:italic}}
#sec{{z-index:8;position:absolute;right:150px;top:160px;background:#5b7cff;color:#fff;font-weight:800;font-size:26px;letter-spacing:.14em;padding:8px 16px}}
#cap{{z-index:8;position:absolute;left:56px;right:150px;top:1262px;background:rgba(12,9,6,.82);border-radius:18px;padding:22px 22px;text-align:center;font-family:I;font-weight:900;font-size:64px;line-height:1.12;color:#fff;text-transform:uppercase;letter-spacing:-.01em;opacity:0}}
#cap .k{{color:#f2e35b}}
#cr{{z-index:8;position:absolute;left:18px;top:520px;writing-mode:vertical-rl;transform:rotate(180deg);color:#efe6d2;font-size:15px;font-weight:600;letter-spacing:.1em;opacity:.55}}
/* hook */
#hook{{z-index:20;position:absolute;inset:0;background:#0d0d0f}}
#hbg{{position:absolute;left:-54px;top:-96px;width:1188px;height:2112px;filter:contrast(1.1) brightness(.8)}}
#hook .tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,20,.55),rgba(8,10,20,.3) 35%,rgba(8,10,20,.93) 70%)}}
.lb{{display:inline-block;font-family:I;font-weight:600;font-size:40px;line-height:1.05;padding:6px 14px 8px}}
.blue{{background:#5b7cff;color:#fff}}.yel{{background:#f2e35b;color:#2f45c9}}
.h{{font-family:O;font-weight:600;font-size:122px;line-height:.98;letter-spacing:-.025em;margin:24px 0 0;color:#f4f1ea}}
.h u{{text-decoration-thickness:7px;text-underline-offset:14px;text-decoration-color:#f2e35b}}
.h em{{font-family:CG;font-style:italic;font-weight:500;letter-spacing:-.01em}}
#verd{{left:100px;top:600px;width:830px;box-sizing:border-box;padding:40px 44px 44px;background:#1d1a16;color:#efe6d2;transform:rotate(-1.5deg);box-shadow:8px 18px 40px rgba(0,0,0,.7)}}
#end{{z-index:9;left:56px;right:150px;top:1030px;background:#f2e35b;padding:44px 46px;color:#171513}}
</style></head><body>
<div id=bd></div>
<div id=pols></div>
<div class="e paper" id=n1904 style="left:560px;top:930px;width:330px;padding:24px;text-align:center;transform:rotate(5deg)"><div class=pin></div><div style="font-size:30px">działa od</div><div style="font-family:I;font-weight:900;font-size:110px;line-height:1">1904</div></div>
<div class="e ybar" id=n5 style="left:120px;top:1010px;transform:rotate(-4deg);font-size:54px">KOLEJKA OD 5:00 RANO</div>
<div class="e paper" id=nteo style="left:110px;top:900px;width:780px;padding:30px 36px;transform:rotate(-2deg)"><div class=pin></div><div style="font-size:30px;opacity:.75">TEORIA:</div><div style="font-size:46px;line-height:1.2;margin-top:8px">„Niektóre kolektury przyciągają szczęście”</div></div>
<div class="e paper" id=n100 style="left:470px;top:930px;width:420px;padding:24px;text-align:center;transform:rotate(4deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:96px;line-height:1">100 000</div><div style="font-size:32px">numerów w El Gordo</div></div>
<div class="e stamp" id=n1 style="left:150px;top:960px;color:#c0281b;font-size:110px;transform:rotate(-7deg)">1 : 100 000</div>
<div class="e ybar" id=nall style="left:110px;top:1060px;transform:rotate(3deg);font-size:46px">TAK SAMO W KAŻDYM PUNKCIE</div>
<div class="e paper" id=nvol style="left:120px;top:900px;width:760px;padding:28px 34px;transform:rotate(2deg)"><div class=pin></div><div style="font-size:42px;line-height:1.25">więcej sprzedanych losów<br>= więcej numerów w grze</div></div>
<div class="e ybar" id=ntor style="left:110px;top:980px;transform:rotate(-3deg);font-size:64px">TORREVIEJA</div>
<div class="e stamp" id=n2223 style="left:300px;top:1040px;white-space:nowrap;color:#c0281b;font-size:56px;transform:rotate(6deg)">GORDO 2022 + 2023</div>
<div class="e paper" id=nmal style="left:460px;top:940px;width:430px;padding:24px;text-align:center;transform:rotate(-4deg)"><div class=pin></div><div style="font-size:30px">ten sam numer</div><div style="font-family:I;font-weight:900;font-size:58px;line-height:1.05;margin-top:6px">PROWINCJA MALAGA</div></div>
<div class="e paper" id=nmany style="left:110px;top:960px;width:780px;padding:26px 34px;transform:rotate(1.5deg)"><div class=pin></div><div style="font-size:44px;line-height:1.2">1 numer → wiele punktów sprzedaży naraz</div></div>
<div class=e id=verd><div style="font-family:I;font-weight:800;font-size:30px;letter-spacing:.2em;color:#f2e35b">WERDYKT</div><div style="font-family:O;font-weight:600;font-size:64px;line-height:1.02;margin-top:14px">„Szczęśliwe” kolektury</div>
<div id=vs class="stamp e" style="position:relative;display:inline-block;margin-top:26px;color:#c0281b;font-size:130px;transform:rotate(-6deg)">MIT</div>
<div id=v1 class=e style="position:relative;font-family:T;font-size:36px;line-height:1.3;margin-top:26px">Kolektura: częściej, bo sprzedaje więcej.<br>Twój los: zawsze 1 : 100 000.</div></div>
<div id=vig></div>
<div id=top></div><div id=brand>SOL <i>y</i> SÓL</div><div id=sec>TEORIA KONTRA FAKTY</div>
<div id=cr>FOT. WIKIMEDIA COMMONS (CC BY / CC BY-SA, M.IN. BARCEX, SERGEI GUSSEV) · ZDJĘCIA ILUSTRACYJNE · OPIS: AUTORZY W PODPISIE POSTA</div>
<div id=cap></div>
<div class=e id=end><div style="font-family:O;font-weight:600;font-size:96px;line-height:1">@solysol.pl</div><div style="font-family:CG;font-style:italic;font-weight:600;font-size:46px;margin-top:12px">Obserwuj – więcej takich historii z wybrzeża</div></div>
<div id=hook><img id=hbg src=img/hook.jpg><div class=tint></div>
<div style="position:absolute;left:64px;top:150px;font-family:CG;font-weight:600;font-size:46px;letter-spacing:.08em;color:#efe6d2">SOL <i style="color:#f2e35b">y</i> SÓL</div>
<div style="position:absolute;left:64px;right:150px;top:760px"><span class="lb blue">Teoria kontra fakty</span> <span class="lb yel">Madryt · El Gordo</span>
<h1 class=h>Ta kolektura<br>wygrała<br><u>ponad 70 razy</u>.<br><em>Przypadek?</em></h1></div></div>
<script>
const SH={json.dumps(shots,ensure_ascii=False)};
const PH={json.dumps(ph,ensure_ascii=False)};
const HOOKEND=3.6, VEND={round(53.6,2)};
const P=document.getElementById('pols');
SH.forEach((s,i)=>{{const d=document.createElement('div');d.className='pol';d.id='p'+i;d.innerHTML='<div class=pin></div><div class=win><img src="'+s[1]+'"></div><div class=lab>'+s[2]+'</div>';P.appendChild(d)}});
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
function pop(id,a,b,t,sc0){{const el=document.getElementById(id);const k=E(a,0.3,t)*(1-E(b,0.3,t));el.style.opacity=k;const base=el.dataset.tr||(el.dataset.tr=el.style.transform||'');el.style.transform=base+' scale('+(sc0+(1-sc0)*E(a,0.3,t))+')'}}
window.setT=function(t){{
 const h=document.getElementById('hook');h.style.opacity=1-E(HOOKEND,0.25,t);h.style.display=t>HOOKEND+0.3?'none':'block';
 document.getElementById('hbg').style.transform='scale('+(1+0.05*t/HOOKEND)+')';
 for(let i=0;i<SH.length;i++){{const a=SH[i][0],b=i+1<SH.length?SH[i+1][0]:99;const el=document.getElementById('p'+i);
  if(t<a-0.01||t>b+0.35){{el.style.display='none';continue}}el.style.display='block';
  const k=E(a,0.22,t);el.style.opacity=k;const rot=(i%2?2.2:-2.2);el.style.transform='rotate('+rot+'deg) scale('+(1.06-0.06*k)+')';el.style.zIndex=i;
  const u=Math.min(1,Math.max(0,(t-a)/(b-a+0.35)));const dir=i%4;const z=1.04+0.12*(dir<2?u:1-u);const tx=(dir%2?1:-1)*24*(u-0.5),ty=(dir==2?-1:1)*16*(u-0.5);
  el.querySelector('img').style.transform='translate('+tx+'px,'+ty+'px) scale('+z+')'}}
 const c=document.getElementById('cap');let p=null;for(const q of PH){{if(t>=q[0][1]-0.05&&t<=q[q.length-1][2]+0.3)p=q}}
 if(!p||t<HOOKEND||t>53.5){{c.style.opacity=0}}else{{c.style.opacity=1;c.innerHTML=p.filter(w=>t>=w[1]-0.04).map(w=>'<span class='+(w[3]?'k':'')+'>'+w[0]+'</span>').join(' ')}}
 pop('n1904',6.0,8.0,t,1.4);pop('n5',10.0,11.0,t,1.5);pop('nteo',11.1,12.9,t,1.1);pop('n100',16.2,17.6,t,1.3);pop('n1',18.6,19.7,t,2.0);pop('nall',20.6,22.7,t,1.3);
 pop('nvol',29.6,31.8,t,1.1);pop('ntor',34.0,35.8,t,1.4);pop('n2223',36.4,37.8,t,2.0);pop('nmal',39.0,41.2,t,1.2);pop('nmany',41.6,44.3,t,1.1);
 pop('verd',44.45,VEND,t,1.08);pop('vs',45.3,99,t,2.4);pop('v1',46.0,99,t,1.0);
 const en=document.getElementById('end');en.style.opacity=E(53.55,0.35,t);en.style.transform='translateY('+(60*(1-E(53.55,0.35,t)))+'px)';
}};
</script></body></html>'''
open('index.html','w').write(html)
print(len(ph),'phrases')
