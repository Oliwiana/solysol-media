# Reel czywiesz-wraki-2412 – wersja 2 (więcej zdjęć, szybsze tempo, strefa TikToka)
# python3 gen.py  -> build/ (img/*.jpg, index.html, credits.json)
import json, os, re
from PIL import Image, ImageOps, ImageEnhance
from shots import SHOTS, HOOK
from words import W
S = 1.12          # przyspieszenie lektora (atempo)
ROOT = '/home/claude/solysol-media/'
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build')
os.makedirs(B + '/img', exist_ok=True)

def credit(src, fallback):
    if src.startswith('_photos'):
        d, f = src.rsplit('/', 1)
        c = [x for x in json.load(open(ROOT + d + '/credits.json')) if x['file'] == f][0]
        a = re.split(r' \(| –|, ', c['author'])[0].strip()
        return f"{a} ({c['license']})", c['title'], c['source']
    return fallback, '', ''

def prep(src, crop, out, w=1100, h=1024):
    im = Image.open(ROOT + src).convert('RGB')
    if crop:
        W0, H0 = im.size
        im = im.crop((int(crop[0]*W0), int(crop[1]*H0), int(crop[2]*W0), int(crop[3]*H0)))
    im = ImageOps.fit(im, (w, h), Image.LANCZOS)
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.15)
    g.convert('RGB').save(out, quality=86)

credits = []
shots = []
for i, s in enumerate(SHOTS):
    prep(s[1], s[3], f'{B}/img/{i:02d}.jpg')
    cr = credit(s[1], s[4])
    credits.append({'shot': i, 'src': s[1], 'credit': cr[0], 'title': cr[1], 'source': cr[2]})
    shots.append([round(s[0]/S, 3), f'img/{i:02d}.jpg', s[2]])
prep(HOOK, None, f'{B}/img/hook.jpg', 1188, 2112)
json.dump(credits, open(B + '/credits.json', 'w'), ensure_ascii=False, indent=1)

F = 'file:///home/claude/tools/node_modules/@fontsource/'
def ff(fam, pkg, w, style='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{style};src:url({F}{pkg}/files/{pkg}-{sub}-{w}-{style}.woff2)}}" for sub in ('latin', 'latin-ext'))
fonts = ff('O','oswald',600)+ff('CG','cormorant-garamond',500,'italic')+ff('CG','cormorant-garamond',600,'normal')+ff('CG','cormorant-garamond',600,'italic')+ff('I','inter',900)+ff('I','inter',800)+ff('I','inter',600)+ff('T','special-elite',400)

KEY = {'złota','Gibraltarem?','1694.','Sztorm','HMS','Sussex','dno.','500','dwóch.','10','ton','złotych','monet.','Tajna','Sabaudii.','2001','wrak','800','metrów','zablokowała','nikt','Sussex.','1891.','Utopia','pancernik','562','Maladze','1900','Gneisenau','falochron.','40','Mieszkańcy','domów.','„bardzo','gościnnej”.','Obserwuj'}
words = [[w, a/S, b/S] for w, a, b in W]
ph = []; cur = []
NOBR = ('w','i','z','na','do','o','A','W','Z','pod','dla','że','to','Do','Od','Na','nie')
for w in words:
    cur.append(w)
    if w[0][-1] in '.?!,' and len(cur) >= 2 or w[0][-1] in '.?!' or (len(cur) >= 4 and w[0] not in NOBR):
        ph.append(cur); cur = []
if cur: ph.append(cur)
ph = [[[x[0], round(x[1], 3), round(x[2], 3), 1 if x[0] in KEY else 0] for x in p] for p in ph]
T = lambda o: round(o/S, 3)
HOOKEND = T(2.9); ENDT = T(59.85)

html = f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{fonts}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#2a1e14;font-family:I}}
#bd{{position:absolute;inset:0;background:#2a1e14}}
#bd:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
#pols{{position:absolute;inset:0;z-index:1}}
.pol{{position:absolute;left:70px;top:280px;width:820px;padding:20px 20px 74px;background:#efe6d2;box-shadow:8px 18px 36px rgba(0,0,0,.65);opacity:0}}
.pol .win{{width:820px;height:780px;overflow:hidden;position:relative;background:#111}}
.pol img{{position:absolute;left:0;top:0;width:820px;height:780px;object-fit:cover;transform-origin:50% 50%}}
.pol .lab{{position:absolute;left:24px;right:20px;bottom:20px;font-family:T;font-size:36px;color:#1d1a16;white-space:nowrap;overflow:hidden}}
.pin{{position:absolute;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-14px;z-index:3}}
.e{{position:absolute;opacity:0;z-index:5}}
.paper{{background:#efe6d2;color:#1d1a16;box-shadow:6px 14px 30px rgba(0,0,0,.6);font-family:T}}
.stamp{{font-family:I;font-weight:900;border:9px solid;padding:6px 26px;letter-spacing:.06em;border-radius:8px;background:rgba(239,230,210,.9);white-space:nowrap}}
.ybar{{background:#f2e35b;color:#171513;font-weight:900;box-shadow:6px 12px 24px rgba(0,0,0,.5);padding:12px 26px;white-space:nowrap}}
#vig{{z-index:6;position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 42%,transparent 52%,rgba(0,0,0,.72) 100%)}}
#top{{z-index:7;position:absolute;left:0;right:0;top:0;height:300px;background:linear-gradient(180deg,rgba(0,0,0,.75),transparent)}}
#brand{{z-index:8;position:absolute;left:64px;top:160px;font-family:CG;font-weight:600;font-size:46px;letter-spacing:.08em;color:#efe6d2}}
#brand i{{color:#f2e35b;font-style:italic}}
#sec{{z-index:8;position:absolute;right:150px;top:168px;background:#5b7cff;color:#fff;font-weight:800;font-size:26px;letter-spacing:.14em;padding:8px 16px}}
#cap{{z-index:8;position:absolute;left:56px;right:150px;top:1250px;background:rgba(12,9,6,.84);border-radius:18px;padding:20px 22px;text-align:center;font-family:I;font-weight:900;font-size:62px;line-height:1.1;color:#fff;text-transform:uppercase;letter-spacing:-.01em;opacity:0}}
#cap .k{{color:#f2e35b}}
#cr{{z-index:8;position:absolute;left:18px;top:470px;writing-mode:vertical-rl;transform:rotate(180deg);color:#efe6d2;font-size:15px;font-weight:600;letter-spacing:.1em;opacity:.55}}
#hook{{z-index:20;position:absolute;inset:0;background:#0d0d0f;overflow:hidden}}
#hbg{{position:absolute;left:-54px;top:-96px;width:1188px;height:2112px;filter:contrast(1.1) brightness(1.05)}}
#hook .tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,20,.55),rgba(8,10,20,.25) 32%,rgba(8,10,20,.93) 66%)}}
.lb{{display:inline-block;font-family:I;font-weight:600;font-size:40px;line-height:1.05;padding:6px 14px 8px}}
.blue{{background:#5b7cff;color:#fff}}.yel{{background:#f2e35b;color:#2f45c9}}
.h{{font-family:O;font-weight:600;font-size:132px;line-height:.98;letter-spacing:-.025em;margin:26px 0 0;color:#f4f1ea}}
.h u{{text-decoration-thickness:8px;text-underline-offset:14px;text-decoration-color:#f2e35b}}
.h em{{font-family:CG;font-style:italic;font-weight:500;letter-spacing:-.01em}}
#end{{z-index:9;left:56px;right:150px;top:1000px;background:#f2e35b;padding:44px 46px;color:#171513}}
</style></head><body>
<div id=bd></div>
<div id=pols></div>
<div class="e paper" id=n500 style="left:440px;top:880px;width:400px;padding:24px;text-align:center;transform:rotate(4deg)"><div class=pin></div><div style="font-size:32px">ok. 500 na pokładzie</div><div style="font-family:I;font-weight:900;font-size:62px;line-height:1.05;margin-top:8px;color:#c0281b">PRZEŻYŁO 2</div></div>
<div class="e stamp" id=n10 style="left:100px;top:970px;color:#c0281b;font-size:76px;transform:rotate(-7deg)">10 TON ZŁOTA?</div>
<div class="e paper" id=nsab style="left:110px;top:920px;width:760px;padding:28px 34px;transform:rotate(-2deg)"><div class=pin></div><div style="font-size:30px;opacity:.75">PRZEZNACZENIE:</div><div style="font-size:46px;line-height:1.2;margin-top:8px">tajna zapłata dla księcia Sabaudii</div></div>
<div class="e ybar" id=n2001 style="left:110px;top:1010px;transform:rotate(-3deg);font-size:52px">2001 · FIRMA Z USA</div>
<div class="e paper" id=n800 style="left:460px;top:890px;width:380px;padding:24px;text-align:center;transform:rotate(4deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:100px;line-height:1">800 m</div><div style="font-size:32px">pod wodą</div></div>
<div class="e stamp" id=nblk style="left:120px;top:980px;color:#c0281b;font-size:76px;transform:rotate(-6deg)">ZABLOKOWANE</div>
<div class="e ybar" id=nq style="left:110px;top:1010px;transform:rotate(2deg);font-size:46px">CZY TO SUSSEX? BRAK DOWODU</div>
<div class="e ybar" id=n1891 style="left:110px;top:990px;transform:rotate(-3deg);font-size:64px">1891 · GIBRALTAR</div>
<div class="e paper" id=nutop style="left:110px;top:910px;width:760px;padding:26px 34px;transform:rotate(1.5deg)"><div class=pin></div><div style="font-size:42px;line-height:1.2">parowiec z emigrantami → pancernik na kotwicy</div></div>
<div class="e paper" id=n562 style="left:470px;top:890px;width:370px;padding:24px;text-align:center;transform:rotate(-4deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:110px;line-height:1;color:#c0281b">562</div><div style="font-size:34px">ofiary</div></div>
<div class="e ybar" id=n1900 style="left:110px;top:990px;transform:rotate(-3deg);font-size:58px">MALAGA · GRUDZIEŃ 1900</div>
<div class="e stamp" id=nfal style="left:180px;top:990px;color:#c0281b;font-size:80px;transform:rotate(5deg)">FALOCHRON</div>
<div class="e paper" id=n40 style="left:470px;top:890px;width:370px;padding:24px;text-align:center;transform:rotate(4deg)"><div class=pin></div><div style="font-family:I;font-weight:900;font-size:100px;line-height:1;color:#c0281b">40+</div><div style="font-size:34px">ofiar</div></div>
<div class="e stamp" id=nmh style="left:90px;top:970px;color:#1f5fa8;font-size:56px;transform:rotate(-5deg)">„MUY HOSPITALARIA”</div>
<div id=vig></div>
<div id=top></div><div id=brand>SOL <i>y</i> SÓL</div><div id=sec>CZY WIESZ</div>
<div id=cr>FOT. WIKIMEDIA COMMONS · OBRAZY I ZDJĘCIA ARCHIWALNE, CZĘŚĆ ILUSTRACYJNA · AUTORZY W OPISIE</div>
<div id=cap></div>
<div class=e id=end><div style="font-family:O;font-weight:600;font-size:100px;line-height:1">@solysol.pl</div><div style="font-family:CG;font-style:italic;font-weight:600;font-size:46px;margin-top:12px">Obserwuj – więcej takich historii z wybrzeża</div></div>
<div id=hook><img id=hbg src=img/hook.jpg><div class=tint></div>
<div style="position:absolute;left:64px;top:160px;font-family:CG;font-weight:600;font-size:46px;letter-spacing:.08em;color:#efe6d2">SOL <i style="color:#f2e35b">y</i> SÓL</div>
<div style="position:absolute;left:64px;right:150px;top:700px"><span class="lb blue">Czy wiesz</span> <span class="lb yel">Gibraltar · 1694</span>
<h1 class=h>Ile <u>złota</u><br>leży na dnie<br>pod <em>Gibraltarem?</em></h1></div></div>
<script>
const SH={json.dumps(shots, ensure_ascii=False)};
const PH={json.dumps(ph, ensure_ascii=False)};
const HOOKEND={HOOKEND}, ENDT={ENDT};
const P=document.getElementById('pols');
SH.forEach((s,i)=>{{const d=document.createElement('div');d.className='pol';d.id='p'+i;d.innerHTML='<div class=pin></div><div class=win><img src="'+s[1]+'"></div><div class=lab>'+s[2]+'</div>';P.appendChild(d)}});
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
const T=o=>o/{S};
function pop(id,a,b,t,sc0){{a=T(a);b=T(b);const el=document.getElementById(id);const k=E(a,0.22,t)*(1-E(b,0.22,t));el.style.opacity=k;const base=el.dataset.tr||(el.dataset.tr=el.style.transform||'');el.style.transform=base+' scale('+(sc0+(1-sc0)*E(a,0.22,t))+')'}}
window.setT=function(t){{
 const h=document.getElementById('hook');h.style.opacity=1-E(HOOKEND,0.2,t);h.style.display=t>HOOKEND+0.25?'none':'block';
 document.getElementById('hbg').style.transform='scale('+(1+0.06*t/HOOKEND)+')';
 for(let i=0;i<SH.length;i++){{const a=SH[i][0],b=i+1<SH.length?SH[i+1][0]:ENDT;const el=document.getElementById('p'+i);
  if(t<a-0.01||t>b+0.3){{el.style.display='none';continue}}el.style.display='block';
  const k=E(a,0.18,t);el.style.opacity=k;const rot=(i%2?2:-2);el.style.transform='rotate('+rot+'deg) scale('+(1.06-0.06*k)+')';el.style.zIndex=i;
  const u=Math.min(1,Math.max(0,(t-a)/(b-a+0.3)));const dir=i%4;const z=1.05+0.14*(dir<2?u:1-u);const tx=(dir%2?1:-1)*28*(u-0.5),ty=(dir==2?-1:1)*18*(u-0.5);
  el.querySelector('img').style.transform='translate('+tx+'px,'+ty+'px) scale('+z+')'}}
 const c=document.getElementById('cap');let p=null;for(const q of PH){{if(t>=q[0][1]-0.05&&t<=q[q.length-1][2]+0.25)p=q}}
 if(!p||t<HOOKEND||t>ENDT-0.1){{c.style.opacity=0}}else{{c.style.opacity=1;c.innerHTML=p.filter(w=>t>=w[1]-0.04).map(w=>'<span class='+(w[3]?'k':'')+'>'+w[0]+'</span>').join(' ')}}
 pop('n500',12.5,15.0,t,1.3);pop('n10',16.5,18.4,t,2.0);pop('nsab',18.5,20.7,t,1.1);pop('n2001',20.9,24.9,t,1.4);
 pop('n800',25.2,26.9,t,1.3);pop('nblk',27.6,29.2,t,2.2);pop('nq',29.9,32.1,t,1.3);
 pop('n1891',32.3,34.7,t,1.4);pop('nutop',35.0,40.6,t,1.1);pop('n562',41.2,43.3,t,1.5);
 pop('n1900',43.6,46.3,t,1.4);pop('nfal',49.1,50.0,t,2.0);pop('n40',50.6,52.0,t,1.4);pop('nmh',57.8,59.8,t,1.8);
 const en=document.getElementById('end');en.style.opacity=E(ENDT,0.3,t);en.style.transform='translateY('+(60*(1-E(ENDT,0.3,t)))+'px)';
}};
</script></body></html>'''
open(B + '/index.html', 'w').write(html)
print(len(shots), 'shots,', len(ph), 'phrases, end', ENDT)
