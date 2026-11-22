# Seria „Gwiazdy na Costa del Sol” – karuzela: okładka BARWNA (barwna.cover) + slajdy w tej samej palecie.
# usage: python3 gen.py ep.json OUTDIR
import json, sys, os, re
sys.path.insert(0, '/home/claude/solysol-media/_tools')
from barwna import cover, FONTS, GOLD, RED
d = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    if f.endswith('.html') or f.endswith('.png'): os.remove(os.path.join(out, f))
PH = '/home/claude/solysol-media/_photos/commons/'
CG = "font-family:CG,Georgia,serif;"
NAVY = '#0A1422'; CREAM = '#FAF7F2'
N = len(d['slides']) + 1

def frame(x, y, w, h, note=''):
    return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border:4px dashed {GOLD};background:rgba(10,20,34,.62);'
            f'display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:{GOLD}">'
            f'<div style="font-size:22px;font-weight:800;letter-spacing:.18em">ZDJĘCIE</div><div style="font-size:18px;font-weight:800;letter-spacing:.18em;margin-top:6px">– DODA REDAKCJA –</div>'
            f'<div style="font-size:16px;font-weight:400;margin-top:10px;color:{CREAM};opacity:.8;padding:0 16px">{note}</div></div>')

# ---------- okładka ----------
c = d['cover']
html = cover(photo_url='file://' + PH + c['photo'], pos=c.get('pos', '50% 50%'), credit=c.get('credit', ''), head=c['head'], teaser=c['teaser'],
             desk=c['desk'], mast='GWIAZDY NA COSTA DEL SOL', date=d['date'], box1=c['box1'], box2=c['box2'], seal=['SERIA', 'gwiazdy', 'CO SOBOTĘ'],
             more=c['more'], hsize=c.get('hsize', 96), htop=c.get('htop', 800), btop=440, stop=c.get('stop', 360))
# mniejsza pieczęć + ramka na zdjęcie gwiazdy po prawej
html = html.replace('width:230px;height:230px', 'width:190px;height:190px').replace('right:58px;top', 'right:40px;top')
fr = frame(620, 470, 380, 290, c.get('framenote', ''))
html = html.replace('<div style="position:absolute;right:30px;top:', fr + '<div style="position:absolute;right:30px;top:', 1)
# pieczęć nad ramką
html = html.replace(fr, '').replace('<div style="position:absolute;right:40px;top', fr + '<div style="position:absolute;right:40px;top', 1)
open(f'{out}/s1.html', 'w').write(html)

# ---------- slajdy ----------
def page(inner, n, bgimg=None, pos='50% 50%'):
    bg = ''
    if bgimg:
        bg = (f'<div style="position:absolute;left:0;top:0;right:0;height:640px;background:url(\'file://{PH}{bgimg}\') {pos}/cover;filter:saturate(1.15)"></div>'
              f'<div style="position:absolute;left:0;top:0;right:0;height:642px;background:linear-gradient(180deg,rgba(10,20,34,.55) 0%,rgba(10,20,34,.05) 30%,rgba(10,20,34,.2) 70%,{NAVY} 100%)"></div>')
    top = (f'<div style="position:absolute;left:64px;right:64px;top:40px;display:flex;justify-content:space-between;align-items:center;font-size:16px;font-weight:600;letter-spacing:.18em;padding-bottom:12px;border-bottom:1px solid rgba(250,247,242,.45)">'
           f'<span style="{CG}font-size:28px;letter-spacing:.12em">SOL Y SÓL</span><span style="color:{GOLD}">GWIAZDY NA COSTA DEL SOL · ODC. {d["ep"]}</span><span>{n}/{N}</span></div>')
    foot = (f'<div style="position:absolute;left:64px;right:64px;bottom:26px;display:flex;justify-content:space-between;font-size:14px;letter-spacing:.16em;opacity:.75">'
            f'<span>{"PRZESUŃ  →" if n < N else "CO SOBOTĘ 18:00"}</span><span>SOLYSOL.PL</span></div>')
    return (f'<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box;margin:0}}html,body{{width:1080px;height:1350px;overflow:hidden;font-family:IN,sans-serif;background:{NAVY};color:{CREAM}}}'
            f'b{{color:{GOLD};font-weight:600}}</style></head><body>{bg}{top}{inner}{foot}</body></html>')

def chip(t, bg=GOLD, fg='#171513'):
    return f'<span style="display:inline-block;background:{bg};color:{fg};font-size:17px;font-weight:800;letter-spacing:.2em;padding:7px 14px">{t}</span>'

for i, s in enumerate(d['slides']):
    n = i + 2; t = s.get('type', 'text'); inner = ''
    if t == 'text':
        y = 700 if s.get('photo') else (180 if not s.get('frame') else 180)
        fr = ''
        if s.get('frame'):
            fx = s['frame']
            fr = frame(64, 150, 952, 470, fx); y = 680
        cr = f'<div style="position:absolute;right:24px;top:600px;font-size:13px;opacity:.8;text-align:right">{s.get("credit","")}</div>' if s.get('photo') else ''
        paras = ''.join(f'<p style="font-size:{s.get("fs",35)}px;line-height:1.42;margin-top:18px">{p}</p>' for p in s['body'])
        inner = (f'{fr}{cr}<div style="position:absolute;left:64px;right:64px;top:{y}px">{chip(s["kicker"])}'
                 f'<div style="{CG}font-size:{s.get("hs",80)}px;font-weight:600;line-height:1.02;margin-top:18px">{s["head"].replace("<i>", f"<i style=color:{GOLD}>")}</div>{paras}</div>')
        open(f'{out}/s{n}.html', 'w').write(page(inner, n, s.get('photo'), s.get('pos', '50% 50%')))
    elif t == 'numbers':
        rows = ''.join(f'<div style="display:flex;gap:30px;align-items:baseline;padding:40px 0;border-top:1.5px solid rgba(242,193,78,.4)"><div style="{CG}font-size:104px;font-weight:600;color:{GOLD};min-width:330px;line-height:1">{a}</div><div style="font-size:34px;line-height:1.35">{b}</div></div>' for a, b in s['rows'])
        inner = f'<div style="position:absolute;left:64px;right:64px;top:190px">{chip(s["kicker"])}<div style="{CG}font-size:84px;font-weight:600;line-height:1.02;margin:18px 0 26px">{s["head"].replace("<i>", f"<i style=color:{GOLD}>")}</div>{rows}</div>'
        open(f'{out}/s{n}.html', 'w').write(page(inner, n))
    elif t == 'where':
        rows = ''.join(f'<div style="display:flex;gap:20px;padding:20px 0;border-top:1.5px solid rgba(242,193,78,.4)"><div style="min-width:170px;font-size:16px;font-weight:800;letter-spacing:.18em;color:{GOLD};padding-top:6px">{a}</div><div style="font-size:29px;line-height:1.4">{b}</div></div>' for a, b in s['rows'])
        cr = f'<div style="position:absolute;right:24px;top:600px;font-size:13px;opacity:.8;text-align:right">{s.get("credit","")}</div>'
        inner = f'{cr}<div style="position:absolute;left:64px;right:64px;top:{s.get("y",560)}px">{chip("GDZIE TO DZIŚ ZOBACZYĆ", RED, "#fff")}<div style="{CG}font-size:62px;font-weight:600;line-height:1.02;margin:16px 0 18px">{s["head"].replace("<i>", f"<i style=color:{GOLD}>")}</div>{rows}</div>'
        open(f'{out}/s{n}.html', 'w').write(page(inner, n, s.get('photo'), s.get('pos', '50% 50%')))
    elif t == 'cta':
        eps = ''.join(f'<div style="display:flex;gap:24px;padding:16px 0;border-top:1.5px solid rgba(242,193,78,.4);{"opacity:.55" if e[2] else ""}"><div style="min-width:150px;font-size:18px;font-weight:800;letter-spacing:.18em;color:{GOLD};padding-top:8px">{e[0]}</div><div style="{CG}font-size:38px;font-weight:600;line-height:1.1">{e[1]}</div></div>' for e in s['eps'])
        inner = (f'<div style="position:absolute;left:64px;right:64px;top:200px;text-align:center">'
                 f'<div style="display:inline-block;width:230px;height:230px;border-radius:50%;background:{RED};border:3px dashed {GOLD};transform:rotate(-8deg);padding-top:58px"><div style="font-size:16px;font-weight:800;letter-spacing:.2em">CO SOBOTĘ</div><div style="{CG}font-style:italic;font-size:52px;line-height:1">18:00</div></div>'
                 f'<div style="{CG}font-size:84px;font-weight:600;line-height:1;margin-top:40px">Obserwuj – <i style="color:{GOLD}">co sobotę nowa gwiazda</i></div>'
                 f'<div style="font-size:26px;margin-top:22px;line-height:1.4">{s["sub"]}</div></div>'
                 f'<div style="position:absolute;left:64px;right:64px;top:{s.get("ey",820)}px">{eps}</div>'
                 f'<div style="position:absolute;left:64px;right:64px;bottom:70px;font-size:15px;opacity:.65;line-height:1.4">{s["note"]}</div>')
        open(f'{out}/s{n}.html', 'w').write(page(inner, n))
print('ok', N)
