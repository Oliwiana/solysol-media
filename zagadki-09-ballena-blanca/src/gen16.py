#!/usr/bin/env python3
# Generuje /tmp/z9/v16/index.html – plansze 16:9 w stylu noir pod lektora (setT(t) w sekundach filmu)
import json, html, os, sys, shutil
sys.path.insert(0, '/tmp/z9')
from slides import S
from PIL import Image
INTRO = 13.0
W = json.load(open('/tmp/z9/words.json'))
items = json.load(open('/tmp/w/items.json')); cred = json.load(open('/tmp/w/cred.json'))
R = '/home/claude/solysol-media/'
os.makedirs('/tmp/z9/v16/img', exist_ok=True)
F = 'file:///home/claude/tools/node_modules/@fontsource'
def ff(fam, path, w, st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X', s)})}}" for s in ('latin', 'latin-ext'))
FONTS = (ff('O', 'oswald/files/oswald-X-600-normal.woff2', 600) + ff('S', 'cormorant-garamond/files/cormorant-garamond-X-500-italic.woff2', 500, 'italic')
         + ff('S', 'cormorant-garamond/files/cormorant-garamond-X-600-normal.woff2', 600) + ff('I', 'inter/files/inter-X-600-normal.woff2', 600)
         + ff('I', 'inter/files/inter-X-400-normal.woff2', 400) + ff('I', 'inter/files/inter-X-800-normal.woff2', 800)
         + ff('T', 'special-elite/files/special-elite-X-400-normal.woff2', 400))

def prep(i, maxw=2300):
    """kopiuje zdjęcie, zwraca nazwę pliku"""
    src = R + items[i]; dst = f'/tmp/z9/v16/img/{i}.jpg'
    if not os.path.exists(dst):
        im = Image.open(src).convert('RGB'); im.thumbnail((maxw, maxw)); im.save(dst, quality=88)
    return f'img/{i}.jpg'

def credit(i):
    c = cred[items[i]]; a = html.unescape(c.get('author') or '').replace('Unknown authorUnknown author', 'autor nieznany').replace('AnonymousUnknown author', 'autor nieznany').strip()
    return f"Fot. {a[:48]} / Wikimedia Commons, {c['license']} · zdjęcie ilustracyjne"

def build(S, W, offset=INTRO, end=None):
    sl = []
    for k, (wi, kind, img, p) in enumerate(S):
        t0 = W[wi]['s'] + offset - (0.25 if k else 0)
        if k == 0: t0 = offset
        sl.append(dict(t0=round(t0, 3), kind=kind, img=img, p=p))
    for k in range(len(sl)):
        sl[k]['t1'] = sl[k + 1]['t0'] if k + 1 < len(sl) else (end or W[-1]['e'] + offset + 2.5)
    return sl

def labs(p):
    out = ''
    for j, t in enumerate(p.get('lab', [])):
        out += f'<span class="lab {"blue" if j == 0 else "yel"}">{html.escape(t)}</span>'
    return out

def slide_html(k, s):
    p = s['p']; kind = s['kind']; img = s['img']
    bg = f'<div class=bg style="background-image:url({prep(img)})"></div>' if img is not None else ''
    cr = f'<div class=cr>{html.escape(credit(img))}</div>' if img is not None else ''
    scrap = ''
    if p.get('scrap') is not None:
        scrap = f'<div class="scrap a" style="right:120px;top:150px;transform:rotate(4deg)"><div class=pin></div><img src="{prep(p["scrap"], 900)}"><div class=sc>zdjęcie ilustracyjne</div></div>'
    body = ''
    if kind in ('photo', 'title', 'next'):
        fs = 96 if kind == 'photo' else 120
        body = f'<div class="txt a">{labs(p)}<h1 class=h style="font-size:{fs}px">{p.get("head","")}</h1>' + (f'<div class=sub>{html.escape(p["sub"])}</div>' if p.get('sub') else '') + '</div>'
    elif kind in ('num', 'date'):
        fs = 120 if p.get('small') else (230 if kind == 'num' else 210)
        body = f'<div class="txt a mid">{labs(p)}<div class=big style="font-size:{fs}px">{html.escape(p["big"])}</div>' + (f'<div class=sub>{html.escape(p["sub"])}</div>' if p.get('sub') else '') + '</div>'
    elif kind == 'paper':
        body = f'''<div class="paper a"><div class=pin></div><div class=pn>{html.escape(p["paper"])}</div><div class=pl></div><div class=ph>{html.escape(p["phead"])}</div><div class=ps>{html.escape(p["psub"])}</div><div class=plines>{"<i></i>"*9}</div><div class=rek>nagłówek odtworzony przez redakcję</div></div>'''
    elif kind == 'list':
        body = f'<div class="txt a mid">{labs(p)}' + ''.join(f'<div class="li" style="--d:{j*0.35}s">{html.escape(x)}</div>' for j, x in enumerate(p['items'])) + '</div>'
    elif kind == 'stamp':
        body = '<div class="stampbox a"><div class=stamp>' + html.escape(p['stamp']) + '</div></div>'
    elif kind == 'chain':
        boxes = [('Willa w Marbelli', 'nieruchomość'), ('Spółka w Hiszpanii', 'właściciel na papierze'), ('Spółka w Delaware', 'właściciel spółki'), ('?', 'prawdziwy właściciel')]
        body = '<div class=chain>' + ''.join(f'<div class="cb" style="--d:{j*0.9}s"><b>{html.escape(a)}</b><span>{html.escape(b)}</span></div>' + ('<div class="arr" style="--d:%ss">→</div>' % (j*0.9+0.45) if j < 3 else '') for j, (a, b) in enumerate(boxes)) + '</div><div class="txt a" style="bottom:120px"><span class="lab blue">Mechanizm według śledczych</span><span class="lab yel">schemat redakcji</span></div>'
    elif kind == 'end':
        body = '<div class="txt a mid" style="text-align:center;left:0;right:0"><div class=big style="font-size:150px;font-family:S;font-weight:600;letter-spacing:.06em">SOL <i style="color:#f2e35b">y</i> SÓL</div><div class=sub>Wszystko, co ważne na Costa del Sol · solysol.pl</div></div>'
    dark = ' dark' if kind in ('num', 'date', 'list', 'stamp', 'chain', 'paper', 'end') else ''
    return f'<div class="sl{dark}" id=s{k}>{bg}<div class=tint></div>{scrap}{body}{cr}</div>'

CSS = FONTS + '''
html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#0d0d0f;color:#f4f1ea}
.sl{position:absolute;inset:0;opacity:0;overflow:hidden;background:#0d0d0f}
.bg{position:absolute;inset:-2%;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.72);will-change:transform}
.dark .bg{filter:grayscale(1) contrast(1.1) brightness(.38)}
.tint{position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,10,20,.78) 0%,rgba(8,10,20,.35) 45%,rgba(8,10,20,.1) 100%),linear-gradient(0deg,rgba(8,10,20,.85) 0%,rgba(8,10,20,0) 45%)}
.txt{position:absolute;left:110px;right:520px;bottom:130px}
.txt.mid{bottom:auto;top:300px;right:200px}
.lab{display:inline-block;font-family:I;font-weight:600;font-size:30px;padding:5px 14px 7px;margin:0 10px 14px 0}
.blue{background:#5b7cff;color:#fff}.yel{background:#f2e35b;color:#2f45c9}
.h{font-family:O;font-weight:600;line-height:1;letter-spacing:-.02em;margin:6px 0 0}
.h u{text-decoration-thickness:6px;text-underline-offset:14px}
.h i{font-family:S;font-style:italic;font-weight:500}
.big{font-family:O;font-weight:600;line-height:1;letter-spacing:-.02em}
.sub{font-family:S;font-style:italic;font-size:48px;line-height:1.15;margin-top:22px;opacity:.92}
.cr{position:absolute;right:28px;bottom:20px;font-family:I;font-size:17px;opacity:.55}
.scrap{position:absolute;background:#efe9dc;padding:16px 16px 44px;box-shadow:0 18px 40px rgba(0,0,0,.6)}
.scrap img{display:block;width:430px;height:300px;object-fit:cover;filter:grayscale(1) contrast(1.1)}
.sc{position:absolute;left:16px;bottom:12px;font-family:T;font-size:20px;color:#333}
.pin{position:absolute;width:26px;height:26px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-13px}
.paper{position:absolute;left:300px;top:170px;width:1260px;background:#efe6d2;color:#1d1a16;padding:50px 70px 60px;box-shadow:0 30px 60px rgba(0,0,0,.7);transform:rotate(-2deg)}
.pn{font-family:S;font-weight:600;font-size:46px;letter-spacing:.04em}
.pl{height:4px;background:#1d1a16;margin:14px 0 26px}
.ph{font-family:O;font-weight:600;font-size:84px;line-height:1.02}
.ps{font-family:S;font-style:italic;font-size:40px;margin-top:20px}
.plines{columns:3;column-gap:40px;margin-top:30px}.plines i{display:block;height:14px;background:#b9ae98;margin:0 0 16px}
.rek{position:absolute;right:30px;top:24px;font-family:I;font-weight:600;font-size:20px;letter-spacing:.12em;text-transform:uppercase;color:#a3150c}
.li{font-family:O;font-weight:600;font-size:96px;line-height:1.08;opacity:0}
.stampbox{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.stamp{font-family:I;font-weight:800;font-size:110px;color:#e0473a;border:12px solid #e0473a;padding:20px 50px;border-radius:14px;transform:rotate(-7deg);letter-spacing:.04em;background:rgba(10,10,10,.35)}
.chain{position:absolute;left:90px;right:90px;top:330px;display:flex;align-items:center;justify-content:space-between}
.cb{width:340px;background:#efe6d2;color:#1d1a16;padding:30px 24px;text-align:center;box-shadow:0 20px 40px rgba(0,0,0,.6);opacity:0}
.cb b{display:block;font-family:O;font-weight:600;font-size:46px;line-height:1.05}.cb span{display:block;font-family:S;font-style:italic;font-size:32px;margin-top:10px}
.arr{font-family:O;font-size:90px;color:#f2e35b;opacity:0}
#brand{position:absolute;left:56px;top:40px;font-family:S;font-weight:600;font-size:34px;letter-spacing:.08em;z-index:9}
#brand i{color:#f2e35b}
#ep{position:absolute;right:56px;top:48px;font-family:I;font-weight:600;font-size:20px;letter-spacing:.2em;opacity:.8;z-index:9}
#grain{position:absolute;inset:0;width:1920px;height:1080px;opacity:.10;mix-blend-mode:overlay;z-index:8;pointer-events:none}
#vig{position:absolute;inset:0;z-index:7;pointer-events:none;background:radial-gradient(ellipse at 50% 50%,transparent 55%,rgba(0,0,0,.6) 100%)}
'''
JS = r'''
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
function setT(t){
  for(let k=0;k<SL.length;k++){const s=SL[k],el=EL[k];
    const fadeIn=k?0.6:0.01;
    if(t<s.t0-0.01||t>s.t1+0.6){el.style.opacity=0;continue}
    let o=t<s.t0+fadeIn?(t-s.t0)/fadeIn:1; if(t>s.t1) o=Math.max(0,1-(t-s.t1)/0.6); if(t>s.t1) o=1;
    el.style.opacity=Math.max(0,Math.min(1,o)); el.style.zIndex=k;
    const d=Math.max(0.1,s.t1-s.t0+0.6), u=Math.min(1,Math.max(0,(t-s.t0)/d));
    const bg=el.querySelector('.bg'); if(bg){const z=(k%2?1.13-0.11*u:1.02+0.11*u); const px=(k%3-1)*30*u; bg.style.transform=`scale(${z}) translateX(${px}px)`}
    const lt=t-s.t0;
    el.querySelectorAll('.a').forEach(a=>{const e=ease(lt/0.7); a.style.opacity=e; a.style.translate=`0 ${40*(1-e)}px`});
    el.querySelectorAll('.li,.cb,.arr').forEach(a=>{const dl=parseFloat(a.style.getPropertyValue('--d'))||0;const e=ease((lt-0.3-dl)/0.5);a.style.opacity=e;a.style.translate=`0 ${30*(1-e)}px`});
    const st=el.querySelector('.stamp'); if(st){const e=ease((lt-0.2)/0.35); st.style.transform=`rotate(-7deg) scale(${2.2-1.2*e})`; st.style.opacity=e}
  }
}
'''

def page(sl, brand_ep):
    body = ''.join(slide_html(k, s) for k, s in enumerate(sl))
    grain = '<img id=grain src=grain.png>'
    data = json.dumps([dict(t0=s['t0'], t1=s['t1']) for s in sl])
    return f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}<div id=vig></div>{grain}<div id=brand>SOL <i>y</i> SÓL</div><div id=ep>{brand_ep}</div>
<script>const SL={data};const EL=SL.map((s,k)=>document.getElementById('s'+k));{JS};setT(0)</script></body></html>'''

if __name__ == '__main__':
    sl = build(S, W)
    open('/tmp/z9/v16/index.html', 'w').write(page(sl, 'ZAGADKI COSTA DEL SOL · #9'))
    json.dump(sl, open('/tmp/z9/v16/sl.json', 'w'), ensure_ascii=False)
    used = sorted({s['img'] for s in sl if s['img'] is not None} | {s['p']['scrap'] for s in sl if s['p'].get('scrap') is not None})
    json.dump(used, open('/tmp/z9/used.json', 'w'))
    print(len(sl), 'plansz,', len(used), 'zdjęć, koniec', sl[-1]['t1'])
    d = [round(s['t1'] - s['t0'], 1) for s in sl]; print('min', min(d), 'max', max(d))
