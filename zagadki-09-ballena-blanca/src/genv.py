#!/usr/bin/env python3
# Pionowe filmy (reel / Shorty) w stylu wzor-bond: hak, korkowa tablica ze zdjęciami (zmiana co ~2 s), napisy słowo po słowie
import json, html, os, sys, subprocess
sys.path.insert(0, '/tmp/z9')
from gen16 import prep, credit, FONTS, items
W = json.load(open('/tmp/z9/words.json'))
CAP = {0:'Biały wieloryb',2:'Ballena Blanca',4:'„biały wieloryb”',5:'wierzchołek góry lodowej',6:'góra lodowa',9:'Delaware, USA',10:'Delaware z lotu ptaka',11:'Wilmington, Delaware',14:'raje podatkowe',17:'ferrari',21:'porsche',30:'pieczęć',31:'pieczęć notarialna',33:'podsłuch',39:'księga',42:'Ciudad de la Justicia',43:'sąd w Maladze',44:'sąd · Málaga',45:'sąd · Málaga',48:'policja francuska',49:'Francja · 2003',50:'prywatny odrzutowiec',53:'wnętrze odrzutowca',58:'skarbiec',62:'zniszczone akta',67:'Puerto Banús',69:'Puerto Banús',73:'jachty · Puerto Banús',74:'Puerto Banús z góry',80:'rolls-royce',82:'rolls-royce',84:'gotówka',85:'banknoty',87:'410 000 € w gotówce',88:'segregatory',89:'akta',90:'archiwum',93:'teczki',94:'dokumenty',98:'maszyna do pisania',101:'kajdanki',102:'kajdanki',104:'Policía Nacional',105:'Policía Nacional',107:'radiowóz',108:'radiowóz',112:'Ciudad de la Justicia',116:'Sąd Najwyższy',117:'Sąd Najwyższy · Madryt',118:'Sąd Najwyższy',119:'Madryt',120:'willa',121:'wybrzeże',122:'Costa del Sol',123:'Marbella nocą',124:'Marbella nocą',133:'Gibraltar',136:'liczarka banknotów',139:'sztabka złota',147:'magnetofon',148:'nagrania',155:'telefon',160:'willa',162:'willa z basenem',165:'Puerto Banús nocą',168:'port nocą',172:'dolary',175:'nocne morze',177:'port nocą',181:'Marbella · stare miasto',183:'Złota Mila'}

def segs_to_words(segs, gap=0.25):
    """segs: lista (i0,i1) indeksów słów; zwraca nowe słowa z czasem w nowym klipie i listę (src_start, src_end)"""
    out = []; cuts = []; t = 0
    for (a, b) in segs:
        s0 = max(0, W[a]['s'] - 0.08); s1 = W[b]['e'] + 0.12
        for w in W[a:b + 1]: out.append(dict(t=w['t'], s=w['s'] - s0 + t, e=w['e'] - s0 + t))
        cuts.append((s0, s1)); t += (s1 - s0) + gap
    return out, cuts, t - gap

def audio(cuts, total, out, hook_pad=0.0, tail=2.8):
    # wycina fragmenty z voice.wav, dokłada podkład noir (0.3) i normalizuje
    fl = []; ins = ''
    for k, (a, b) in enumerate(cuts):
        fl.append(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,aformat=channel_layouts=mono[c{k}]")
    parts = []
    for k in range(len(cuts)):
        parts.append(f'[c{k}]')
        if k < len(cuts) - 1: fl.append(f"anullsrc=r=44100:cl=mono,atrim=0:0.25[g{k}]"); parts.append(f'[g{k}]')
    fl.append(''.join(parts) + f"concat=n={len(parts)}:v=0:a=1,adelay={int(hook_pad*1000)},apad=pad_dur={tail}[v]")
    L = total + hook_pad + tail
    fl.append(f"[1:a]atrim=0:{L:.2f},volume=0.3,afade=t=out:st={L-2:.2f}:d=2[b]")
    fl.append("[v][b]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5[o]")
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', '/tmp/z9/voice.wav', '-i', '/tmp/z9/bedloop.wav', '-filter_complex', ';'.join(fl), '-map', '[o]', '-t', f'{L:.2f}', '-ar', '44100', '-ac', '2', out], check=True)
    return L

CSS = FONTS + '''
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#2a1e14;font-family:I}
#board{position:absolute;inset:0;background:#2a1e14}
#board:before{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}
.card{position:absolute;left:90px;top:300px;width:900px;opacity:0;background:#efe6d2;padding:22px 22px 90px;box-shadow:8px 20px 40px rgba(0,0,0,.65)}
.card .ph{width:856px;height:700px;overflow:hidden;position:relative}
.card .ph div{position:absolute;inset:-3%;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.92)}
.card .cap{position:absolute;left:30px;bottom:26px;font-family:T;font-size:40px;color:#1d1a16}
.card .il{position:absolute;right:26px;bottom:30px;font-family:T;font-size:20px;color:#6b6252}
.pin{position:absolute;width:30px;height:30px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-14px;margin-left:-15px;z-index:3}
.note{position:absolute;opacity:0;background:#f2e35b;color:#1d1a16;font-family:I;font-weight:800;font-size:54px;padding:14px 26px;box-shadow:4px 10px 20px rgba(0,0,0,.5)}
#top{position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(0,0,0,.75),transparent);display:flex;justify-content:space-between;padding:70px 64px 0;box-sizing:border-box;color:#efe6d2;font-weight:800;font-size:24px;letter-spacing:.22em;z-index:20}
#top b{font-family:S;font-style:italic;font-weight:600;letter-spacing:.08em;font-size:34px}#top b i{color:#f2e35b}
#capt{position:absolute;left:60px;right:60px;top:1330px;text-align:center;font-family:I;font-weight:800;font-size:66px;line-height:1.12;text-transform:uppercase;color:#fff;text-shadow:0 4px 14px rgba(0,0,0,.9);z-index:20}
#capt span{display:inline-block;margin:0 10px}#capt .on{color:#f2e35b}
#cr{position:absolute;left:0;right:0;bottom:250px;text-align:center;font-family:I;font-size:20px;color:#efe6d2;opacity:.55;z-index:20}
#hook{position:absolute;inset:0;z-index:30;background:#0d0d0f}
#hook .hb{position:absolute;inset:-3%;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.55)}
#hook .ht{position:absolute;left:70px;right:70px;top:560px}
#hook h1{font-family:O;font-weight:600;font-size:150px;line-height:.98;letter-spacing:-.02em;color:#f4f1ea;margin:20px 0 0}
#hook h1 u{text-decoration-thickness:9px;text-underline-offset:18px}#hook h1 i{font-family:S;font-style:italic;font-weight:500}
.lab{display:inline-block;font-family:I;font-weight:600;font-size:38px;padding:6px 16px 8px;margin-right:10px}.blue{background:#5b7cff;color:#fff}.yel{background:#f2e35b;color:#2f45c9}
#end{position:absolute;inset:0;z-index:40;background:#0d0d0f;opacity:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
#end .e1{font-family:O;font-weight:600;font-size:120px;color:#f4f1ea;line-height:1}
#end .e2{font-family:S;font-style:italic;font-size:62px;color:#f2e35b;margin-top:30px}
#end .e3{font-family:S;font-weight:600;font-size:60px;letter-spacing:.08em;color:#f4f1ea;margin-top:80px}#end .e3 i{color:#f2e35b}
#vig{position:absolute;inset:0;z-index:19;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.75) 100%)}
'''
JS = r'''
const ease=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
function setT(t){
 const hk=document.getElementById('hook'); const ho=t<HOOK?1:Math.max(0,1-(t-HOOK)/0.35); hk.style.opacity=ho; hk.querySelector('.hb').style.transform=`scale(${1.04+0.05*Math.min(1,t/HOOK)})`;
 hk.querySelector('.ht').style.transform=`scale(${1+0.03*Math.min(1,t/HOOK)})`;
 for(let k=0;k<C.length;k++){const c=C[k],el=CE[k];
  if(t<c.t0||t>c.t1+0.4){el.style.opacity=0;continue}
  const lt=t-c.t0,e=ease(lt/0.35); el.style.opacity=t>c.t1?1:e; el.style.zIndex=k+1;
  el.style.transform=`translateY(${(1-e)*-60}px) rotate(${c.r}deg) scale(${1.06-0.06*e})`;
  const u=Math.min(1,lt/(c.t1-c.t0+0.4)); el.querySelector('.ph div').style.transform=`scale(${k%2?1.14-0.1*u:1.04+0.1*u}) translateX(${(k%3-1)*20*u}px)`;
  const n=el.querySelector('.note'); if(n){const e2=ease((lt-0.4)/0.3); n.style.opacity=e2; n.style.transform=`rotate(-4deg) scale(${1.4-0.4*e2})`}
  document.getElementById('cr').textContent=c.cr;
 }
 let line=null; for(const L of LINES){if(t>=L.s-0.05&&t<L.e+0.25)line=L}
 const cp=document.getElementById('capt');
 if(t<HOOK-0.1||!line){cp.innerHTML=''}else{cp.innerHTML=line.w.map(w=>`<span class="${t>=w.s-0.03?'on':''}">${w.t}</span>`).join(' ')}
 const en=document.getElementById('end'); en.style.opacity=t<END?0:ease((t-END)/0.4);
}
'''

def build(name, segs, hook_html, hook_img, photos, notes, out_dir, hook_lab='Zagadki Costa del Sol', end1='Cały odcinek', end2='na YouTube · Sol y Sól'):
    words, cuts, total = segs_to_words(segs)
    HOOK = 2.2   # hak – pierwsze 2 s: duży napis + pytanie lektora (pierwszy segment to pytanie)
    L = audio(cuts, total, f'{out_dir}/{name}.m4a', hook_pad=0.0)
    END = total + 0.35
    # kartki zdjęć od końca haka, co ~2 s
    n = len(photos); span = END - HOOK; dt = span / n
    C = []
    for k, ph in enumerate(photos):
        t0 = HOOK + k * dt; C.append(dict(t0=round(t0, 3), t1=round(t0 + dt, 3), r=[-2.5, 2, -1, 3, -3, 1.5][k % 6], img=ph, cr=credit(ph)))
    # linie napisów (2–4 słowa)
    LINES = []; cur = []
    for i, w in enumerate(words):
        cur.append(w); ln = sum(len(x['t']) for x in cur)
        if w['t'][-1] in '.?!:,' or ln > 18 or len(cur) >= 4 or i == len(words) - 1:
            LINES.append(dict(s=cur[0]['s'], e=cur[-1]['e'], w=[dict(t=html.escape(x['t'].rstrip(',.:').upper() if x['t'] not in ('—',) else x['t']), s=x['s']) for x in cur])); cur = []
    cards = ''
    for k, c in enumerate(C):
        note = notes.get(k)
        nh = f'<div class=note style="right:-30px;top:560px">{html.escape(note)}</div>' if note else ''
        cards += f'<div class=card id=c{k}><div class=pin></div><div class=ph><div style="background-image:url(img/{c["img"]}.jpg)"></div></div><div class=cap>{html.escape(CAP.get(c["img"], ""))}</div><div class=il>zdjęcie ilustracyjne</div>{nh}</div>'
        prep(c['img'])
    prep(hook_img)
    page = f'''<!DOCTYPE html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div id=board></div>{cards}<div id=vig></div>
<div id=top><b>SOL <i>y</i> SÓL</b><span>ZAGADKA KRYMINALNA</span></div><div id=capt></div><div id=cr></div>
<div id=hook><div class=hb style="background-image:url(img/{hook_img}.jpg)"></div><div class=ht><span class="lab yel">🔊 włącz dźwięk</span><h1>{hook_html}</h1><div style="margin-top:34px"><span class="lab blue">{html.escape(hook_lab)}</span></div></div></div>
<div id=end><div class=e1>{html.escape(end1)}</div><div class=e2>{html.escape(end2)}</div><div class=e3>SOL <i>y</i> SÓL</div></div>
<script>const HOOK={HOOK},END={END:.3f},C={json.dumps(C, ensure_ascii=False)},LINES={json.dumps(LINES, ensure_ascii=False)};const CE=C.map((c,k)=>document.getElementById('c'+k));{JS};setT(0)</script></body></html>'''
    open(f'/tmp/z9/v16/{name}.html', 'w').write(page)
    return L, total
