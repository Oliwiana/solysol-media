#!/usr/bin/env python3
# Generator reela „Gwiazdy na Costa del Sol" – styl NOIR wg wzor-bond.mp4 (tablica, polaroidy, napisy słowo po słowie)
# Użycie: python3 gen.py <data.py>  -> /home/claude/gw/<id>/index.html + timeline.json
import json, sys, os, re, math, runpy
P = '/home/claude/solysol-media/_photos/commons/'
F = 'file:///home/claude/tools/node_modules/@fontsource'
def ff(fam, path, w, st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X', s)})}}" for s in ('latin', 'latin-ext'))
FONTS = (ff('O', 'oswald/files/oswald-X-600-normal.woff2', 600) + ff('S', 'cormorant-garamond/files/cormorant-garamond-X-500-italic.woff2', 500, 'italic')
         + ff('S', 'cormorant-garamond/files/cormorant-garamond-X-600-normal.woff2', 600) + ff('I', 'inter/files/inter-X-600-normal.woff2', 600)
         + ff('I', 'inter/files/inter-X-800-normal.woff2', 800) + ff('I', 'inter/files/inter-X-900-normal.woff2', 900)
         + ff('T', 'special-elite/files/special-elite-X-400-normal.woff2', 400))

def wdur(w):
    w = w.replace('*', '')
    return 0.10 + 0.042 * len(w) + (0.18 if w[-1:] in '.?!' else 0.08 if w[-1:] in ',–:' else 0)

def credits(d):
    fs = sorted({d['hook']['bg']} | {s[0] for L in d['lines'] for s in L['shots'] if not s[0].startswith('PH:')})
    au = []; full = []
    for f in fs:
        dd, fn = f.split('/'); c = [x for x in json.load(open(P + dd + '/credits.json')) if x['file'] == fn][0]
        a = re.sub(r'\s+from\s+.*$', '', c['author']).replace('&amp;', '&').strip()
        a = re.sub(r'^This Photo was taken by ', '', a)
        a = a[:40]
        if a and a not in au: au.append(a)
        full.append({'file': f, 'author': c['author'], 'license': c['license'], 'source': c['source']})
    return au, full

def build(d):
    au, full = credits(d); d.setdefault('credits', 'FOT. WIKIMEDIA COMMONS (CC BY / BY-SA / CC0): ' + ', '.join(au).upper() + ' · ZDJĘCIA ILUSTRACYJNE')
    out = f"/home/claude/gw/{d['id']}"; os.makedirs(out, exist_ok=True)
    t = 0.15; words = []; chunks = []; shots = []; tags = []
    HOOK_END = d.get('hook_end', 2.6)
    for li, L in enumerate(d['lines']):
        ws0 = L['text'].split(); ws = []
        for w in ws0:
            if w == '–' and ws: ws[-1] += ' –'
            else: ws.append(w)
        t0 = t
        # podział na kawałki napisów max 4 słowa
        cur = []
        for w in ws:
            dd = wdur(w)
            word = {'w': w.replace('*', ''), 'k': w.startswith('*') or w.count('*') > 0, 'a': round(t, 3), 'b': round(t + dd, 3)}
            cur.append(word); t += dd
            if len(cur) >= 4 or w[-1:] in '.?!:' or (w[-1:] in ',–' and len(cur) >= 2):
                chunks.append(cur); cur = []
        if cur: chunks.append(cur)
        t += 0.22
        t1 = t
        if 'tag' in L: tags.append({'txt': L['tag'], 'a': round(t0, 2), 'b': round(t1, 2)})
        if li == 0 and d.get('hook'): continue
        sh = L['shots']; dur = t1 - t0
        n = max(len(sh), math.ceil(dur / 2.4))
        for k in range(n):
            s = sh[k % len(sh)]
            shots.append({'src': s[0], 'cap': s[1], 'a': round(t0 + dur * k / n, 3), 'v': (k // len(sh)) + li})
    END = t + 0.1; TOTAL = END + 3.2
    # hook-ujęcie trwa do końca 1. linii (min. HOOK_END)
    first_board = shots[0]['a'] if shots else HOOK_END
    js = {'chunks': chunks, 'shots': shots, 'tags': tags, 'hookEnd': first_board, 'end': END, 'total': TOTAL}
    def img(src):
        return src if src.startswith('PH:') else 'file://' + P + src
    for s in shots: s['src'] = img(s['src'])
    hk = d['hook']
    html = f"""<!DOCTYPE html><html><head><meta charset=utf-8><style>{FONTS}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#2a1e14;font-family:I}}
#board{{position:absolute;inset:0;background:#2a1e14}}
#board:before{{content:"";position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#000 1px,transparent 1.6px);background-size:7px 7px}}
.card{{position:absolute;left:80px;top:250px;width:900px;height:1000px;background:#efe6d2;box-shadow:8px 18px 40px rgba(0,0,0,.65);opacity:0}}
.card .ph{{position:absolute;left:22px;top:22px;right:22px;height:880px;overflow:hidden;background:#111}}
.card .ph img{{position:absolute;left:0;top:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.15) brightness(.92)}}
.card .cp{{position:absolute;left:30px;right:30px;bottom:22px;font-family:T;font-size:40px;color:#1d1a16;white-space:nowrap;overflow:hidden}}
.pin{{position:absolute;width:28px;height:28px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff6b5a,#a3150c);box-shadow:2px 4px 6px rgba(0,0,0,.6);left:50%;top:-12px;margin-left:-14px;z-index:3}}
.phd{{position:absolute;inset:0;background:#1d1a16;border:6px dashed #f2e35b;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#f2e35b}}
.phd b{{font-family:I;font-weight:900;font-size:62px;line-height:1.05;letter-spacing:.01em}}
.phd i{{font-family:T;font-style:normal;color:#efe6d2;font-size:46px;margin-top:30px;padding:0 40px}}
.grain{{position:absolute;inset:0;opacity:.14;mix-blend-mode:overlay;pointer-events:none}}
#vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,transparent 50%,rgba(0,0,0,.75) 100%)}}
#top{{position:absolute;left:0;right:0;top:0;height:250px;background:linear-gradient(180deg,rgba(0,0,0,.75),transparent);color:#efe6d2;z-index:20}}
#top .b{{position:absolute;left:64px;top:150px;font-family:S;font-weight:600;font-size:44px;letter-spacing:.08em}}
#top .b i{{color:#f2e35b;font-style:normal}}
#top .r{{position:absolute;right:150px;top:166px;font-weight:800;font-size:22px;letter-spacing:.2em}}
#capw{{position:absolute;left:50px;right:150px;top:1290px;text-align:center;z-index:21}}
#cap{{display:inline-block;max-width:880px;background:rgba(12,9,6,.85);border-radius:18px;padding:20px 26px;text-align:center;font-weight:900;font-size:66px;line-height:1.12;color:#fff;text-transform:uppercase;letter-spacing:-.01em;text-shadow:0 4px 0 #000;z-index:21;box-sizing:border-box}}
#cap span{{display:inline-block;margin:0 .05em}}
.tag{{position:absolute;right:150px;top:1150px;transform:rotate(-4deg);background:#f2e35b;color:#171513;font-weight:900;font-size:58px;padding:12px 28px;box-shadow:6px 12px 24px rgba(0,0,0,.5);z-index:22;opacity:0}}
#hook{{position:absolute;inset:0;z-index:30;background:#0d0d0f;color:#f4f1ea}}
#hook .bg{{position:absolute;inset:-40px;background-size:cover;background-position:center;filter:grayscale(1) contrast(1.15) brightness(.78)}}
#hook .tint{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,10,20,.6),rgba(8,10,20,.3) 35%,rgba(8,10,20,.9) 70%)}}
.lab{{display:inline-block;font-weight:600;font-size:40px;line-height:1.05;padding:6px 14px 8px}}
.blue{{background:#5b7cff;color:#fff}}.yel{{background:#f2e35b;color:#2f45c9}}
.h{{hyphens:none;font-family:O;font-weight:600;font-size:118px;line-height:.98;letter-spacing:-.025em;margin:24px 0 26px}}
.h u{{text-decoration-thickness:7px;text-underline-offset:12px}}
.h em{{font-family:S;font-style:italic;font-weight:500;letter-spacing:-.01em;font-size:1.04em;color:#f2e35b}}
#end{{position:absolute;left:60px;right:150px;top:760px;background:#f2e35b;color:#171513;padding:50px 50px;z-index:40;opacity:0;box-shadow:0 20px 50px rgba(0,0,0,.6)}}
#cr{{position:absolute;left:14px;top:300px;height:1150px;writing-mode:vertical-rl;transform:rotate(180deg);color:#efe6d2;font-size:13px;line-height:1.25;font-weight:600;letter-spacing:.1em;opacity:.55;z-index:25}}
</style></head><body>
<div id=board></div><div id=cards></div>
<svg class=grain width=1080 height=1920><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/></filter><rect width=100% height=100% filter=url(#n)/></svg>
<div id=vig></div>
<div id=top><div class=b>SOL <i>y</i> SÓL</div><div class=r>{d['label_top']}</div></div>
<div id=tags></div>
<div id=capw><div id=cap></div></div>
<div id=cr>{d['credits']}</div>
<div id=hook><div class=bg style="background-image:url({img(hk['bg'])})"></div><div class=tint></div>
<div style="position:absolute;left:64px;top:150px;font-family:S;font-weight:600;font-size:44px;letter-spacing:.08em">SOL <i style="color:#f2e35b;font-style:normal">y</i> SÓL</div>
<div style="position:absolute;left:64px;right:150px;top:{hk.get('top', 640)}px"><span class="lab blue">{d['label_blue']}</span>
<h1 class=h style="font-size:{hk.get('size', 118)}px">{hk['html']}</h1><span class="lab yel">{d['label_yel']}</span></div></div>
<div id=end><div style="font-family:I;font-weight:900;font-size:40px;letter-spacing:.06em">{d['label_blue'].upper()}</div>
<div style="font-family:O;font-weight:600;font-size:96px;line-height:1;margin-top:16px">{d['end_title']}</div>
<div style="font-family:S;font-style:italic;font-weight:500;font-size:52px;margin-top:22px">Obserwuj @solysol.pl</div></div>
<script>
const D={json.dumps(js, ensure_ascii=False)};
const E=(a,b,t)=>{{let x=Math.max(0,Math.min(1,(t-a)/b));return x*x*(3-2*x)}};
const cards=document.getElementById('cards');
D.shots.forEach((s,i)=>{{const c=document.createElement('div');c.className='card';c.id='c'+i;
 const ph=s.src.startsWith('PH:')?'<div class=phd><b>ZDJĘCIE –<br>DODA REDAKCJA</b><i>'+s.src.slice(3)+'</i></div>':'<img src="'+s.src+'">';
 c.innerHTML='<div class=pin></div><div class=ph>'+ph+'</div><div class=cp>'+s.cap+'</div>';cards.appendChild(c)}});
const tg=document.getElementById('tags');D.tags.forEach((g,i)=>{{const e=document.createElement('div');e.className='tag';e.id='g'+i;e.textContent=g.txt;tg.appendChild(e)}});
window.setT=function(t){{
 const hk=document.getElementById('hook');hk.style.opacity=t<D.hookEnd?1:0;
 hk.querySelector('.bg').style.transform='scale('+(1.04+0.05*t/D.hookEnd)+')';
 const h1=hk.querySelector('.h');h1.style.transform='translateY('+(30*(1-E(0,0.35,t)))+'px)';h1.style.opacity=E(0,0.25,t);
 let cur=-1;D.shots.forEach((s,i)=>{{if(t>=s.a)cur=i}});
 D.shots.forEach((s,i)=>{{const c=document.getElementById('c'+i);
  if(i===cur||i===cur-1){{const rot=((i%2)?2.2:-2.0)+((i%3)-1)*0.8;const k=i===cur?E(s.a,0.28,t):1;
   const dx=(i%2?14:-14);c.style.opacity=i===cur?k:(1-E(D.shots[cur].a+0.2,0.25,t));c.style.zIndex=i===cur?5:4;
   c.style.transform='translate('+dx+'px,'+(i===cur?(-40*(1-k)):0)+'px) rotate('+rot+'deg) scale('+(i===cur?1.06-0.06*k:0.97)+')';
   const im=c.querySelector('img');if(im){{const nx=i+1<D.shots.length?D.shots[i+1].a:D.end;const p=Math.max(0,Math.min(1,(t-s.a)/Math.max(1,nx-s.a)));
    const v=s.v%4;const z=v%2?1.18-0.1*p:1.06+0.12*p;const ox=[-1,1,0,0][v]*28*(p-0.5),oy=[0,0,-1,1][v]*28*(p-0.5);
    im.style.transform='scale('+z+') translate('+ox+'px,'+oy+'px)'}}}}
  else c.style.opacity=0}});
 D.tags.forEach((g,i)=>{{const e=document.getElementById('g'+i);const k=E(g.a,0.25,t)*(1-E(g.b,0.25,t));e.style.opacity=k;e.style.transform='rotate(-4deg) scale('+(1.6-0.6*E(g.a,0.25,t))+')'}});
 const cap=document.getElementById('cap');let ch=null;
 if(t>=D.hookEnd-0.01&&t<D.end+0.2)for(const c of D.chunks){{if(t>=c[0].a-0.02&&t<=c[c.length-1].b+0.25)ch=c}}
 if(!ch){{cap.style.opacity=0}}else{{cap.style.opacity=1;cap.innerHTML=ch.map(w=>'<span style="display:'+(t>=w.a-0.03?'inline-block':'none')+';color:'+(w.k?'#f2e35b':'#fff')+';transform:scale('+(t>=w.a&&t<w.a+0.12?1.04:1)+')">'+w.w+'</span>').join(' ')}}
 const en=document.getElementById('end');const ke=E(D.end+0.1,0.35,t);en.style.opacity=ke;en.style.transform='translateY('+(60*(1-ke))+'px) rotate(-1.5deg)';
}};
</script></body></html>"""
    open(f'{out}/index.html', 'w').write(html)
    json.dump(js, open(f'{out}/timeline.json', 'w'), ensure_ascii=False, indent=0)
    json.dump({'authors': au, 'photos': full}, open(f'{out}/credits.json', 'w'), ensure_ascii=False, indent=1)
    files = sorted({s['src'] for s in shots if not s['src'].startswith('PH:')} | {img(hk['bg'])})
    nwords = sum(len(L['text'].split()) for L in d['lines'])
    print(d['id'], 'words', nwords, 'total', round(TOTAL, 1), 's  shots', len(shots), 'distinct files', len(files), 'placeholders', sum(1 for s in shots if s['src'].startswith('PH:')))
    for s in shots:
        if s['src'].startswith('PH:'): print('  PH @', s['a'], s['src'])
    mx = max((shots[i + 1]['a'] - shots[i]['a']) for i in range(len(shots) - 1)); print('  max shot', round(mx, 2), 'hookEnd', first_board)
    return js

if __name__ == '__main__':
    build(runpy.run_path(sys.argv[1])['D'])
