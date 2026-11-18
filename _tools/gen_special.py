# Sol y Sól – wydanie specjalne (np. dodatek świąteczny) w stylu magazynu. Karuzela 1080x1350.
# usage: python3 gen_special.py dane.json OUTDIR  (potem: cp shot.js OUTDIR && cd OUTDIR && node shot.js)
import json, sys, os, html
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_base.py')).read().split("P={}")[0])
d = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
PH = d.get('photos_dir', '/home/claude/photos_raw/')
GRN = '#0F3A27'; GRN2 = '#1F6B45'; RED = '#9E1B22'; RED2 = '#C62828'; GOLD = '#F2C14E'; CREAM = '#FFF6E5'
slides = d['slides']; N = len(slides)
E = lambda t: html.escape(t or '', quote=False)
SNOW = ('<div style="position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(rgba(255,255,255,.6) 1.6px,transparent 2.2px),'
        'radial-gradient(rgba(242,193,78,.55) 1.3px,transparent 1.8px);background-size:96px 96px,150px 150px;background-position:12px 22px,70px 80px;opacity:.5"></div>')
GARL = lambda pos: (f'<div style="position:absolute;left:0;right:0;{pos}:0;height:16px;background:repeating-linear-gradient(90deg,{RED2} 0 44px,{GOLD} 44px 56px,{GRN2} 56px 100px,{GOLD} 100px 112px)"></div>')
def img(p, x, y, w, h, pos='50% 50%', r=0, extra=''):
    return f'<img src="file://{PH}{p}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};border-radius:{r}px;{extra}">'
def credit(t, x, y, c='rgba(255,246,229,.8)', al='left'):
    return f'<div style="position:absolute;{al}:{x}px;top:{y}px;font-size:14px;color:{c}">{E(t)}</div>'
def mast(n, fg=CREAM):
    return (f'<div style="position:absolute;left:64px;right:64px;top:44px;display:flex;justify-content:space-between;align-items:center;color:{fg};z-index:5">'
            f'<div style="{CG}font-size:30px;font-weight:500;letter-spacing:.06em">S<span style="display:inline-block;width:20px;height:20px;border-radius:50%;background:{GOLD};margin:0 2px"></span>L <i style="color:{GOLD}">y</i> SÓL</div>'
            f'<div style="font-size:16px;font-weight:700;letter-spacing:.22em">{E(d["label"])}</div>'
            f'<div style="font-size:16px;font-weight:700;letter-spacing:.14em;opacity:.8">{n}/{N}</div></div>')
def foot(fg=CREAM):
    return (f'<div style="position:absolute;left:64px;right:64px;bottom:40px;display:flex;justify-content:space-between;font-size:17px;font-weight:700;letter-spacing:.16em;color:{fg};z-index:5">'
            f'<span style="opacity:.8">{E(d["foot"])}</span><span>SOLYSOL.PL</span></div>')
def chip(t, bg=RED2, fg='#fff'):
    return f'<span style="display:inline-block;background:{bg};color:{fg};font-size:18px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;padding:9px 16px">{E(t)}</span>'
def facts(rows, fg=CREAM):
    return ''.join(f'<div style="display:flex;gap:18px;padding:13px 0;border-top:1.5px solid rgba(242,193,78,.35)"><div style="min-width:150px;font-size:17px;font-weight:800;letter-spacing:.18em;color:{GOLD};text-transform:uppercase;padding-top:5px">{E(k)}</div><div style="font-size:25px;line-height:1.38;color:{fg}">{v}</div></div>' for k, v in rows)
def tip(title, text, bg=GOLD, fg=GRN):
    return (f'<div style="background:{bg};color:{fg};padding:22px 26px;border-radius:4px;position:relative">'
            f'<div style="font-size:16px;font-weight:800;letter-spacing:.22em;text-transform:uppercase">✦ {E(title)}</div>'
            f'<div style="font-size:23px;line-height:1.42;margin-top:8px">{text}</div></div>')

def page_out(name, body, bg):
    open(f'{out}/{name}.html', 'w').write(page(body, bg, CREAM))

for i, s in enumerate(slides):
    n = i + 1; t = s['type']; bg = GRN if i % 2 == 0 else RED
    if t == 'cover':
        lines = ''.join(f'<div style="border-left:5px solid {GOLD};padding:4px 0 4px 16px;margin-bottom:20px"><div style="font-size:15px;font-weight:800;letter-spacing:.22em;color:{GOLD}">{E(a)}</div><div style="{CG}font-size:33px;line-height:1.08;margin-top:4px">{E(b)}</div></div>' for a, b in s['lines'])
        body = (img(s['photo'], 0, 0, 1080, 1350, s.get('pos', '50% 50%')) +
                f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,30,20,.82) 0%,rgba(10,30,20,.25) 30%,rgba(10,30,20,.15) 52%,rgba(10,30,20,.88) 80%,rgba(10,30,20,.95) 100%)"></div>' + SNOW + GARL('top') + GARL('bottom') +
                f'<div style="position:absolute;left:64px;right:64px;top:50px;display:flex;justify-content:space-between;align-items:flex-end;color:{CREAM}">'
                f'<div style="{CG}font-size:92px;font-weight:500;letter-spacing:.04em;line-height:1">S<span style="display:inline-block;width:62px;height:62px;border-radius:50%;background:{GOLD};margin:0 4px"></span>L <i style="color:{GOLD}">y</i> SÓL</div>'
                f'<div style="text-align:right;font-size:16px;font-weight:800;letter-spacing:.2em;line-height:1.6">{E(s["issue"])}<br><span style="color:{GOLD}">{E(s["date"])}</span></div></div>'
                f'<div style="position:absolute;left:64px;top:178px;background:{RED2};color:#fff;font-size:20px;font-weight:800;letter-spacing:.26em;padding:10px 18px;transform:rotate(-2deg)">{E(s["kicker"])}</div>'
                f'<div style="position:absolute;left:60px;right:60px;top:760px;color:{CREAM}"><div style="{CG}font-size:150px;font-weight:600;line-height:.9;letter-spacing:-.01em">{s["title"]}</div>'
                f'<div style="font-size:27px;margin-top:18px;max-width:900px;line-height:1.35">{E(s["sub"])}</div></div>'
                f'<div style="position:absolute;right:56px;top:262px;width:420px;color:{CREAM};background:rgba(10,30,20,.78);padding:24px 24px 6px;border-top:6px solid {GOLD}">{lines}</div>'
                f'<div style="position:absolute;left:64px;bottom:56px;font-size:18px;font-weight:800;letter-spacing:.2em;color:{GOLD}">PRZESUŃ  →</div>'
                + credit(s.get('credit', ''), 64, 1290, al='right'))
        page_out(f'{n:02d}', body, GRN); continue
    if t == 'calendar':
        rows = ''.join(f'<div style="display:flex;align-items:center;gap:22px;padding:14px 0;border-top:1.5px solid rgba(242,193,78,.3)">'
                       f'<div style="min-width:150px;{CG}font-size:44px;font-weight:600;color:{GOLD};line-height:1">{E(a)}</div>'
                       f'<div><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:#F7D9A0;text-transform:uppercase">{E(b)}</div><div style="font-size:25px;line-height:1.3;margin-top:3px">{E(c)}</div></div></div>' for a, b, c in s['rows'])
        body = (SNOW + GARL('top') + mast(n) +
                f'<div style="position:absolute;left:64px;right:64px;top:130px;color:{CREAM}">{chip(s["chip"], GOLD, GRN)}'
                f'<div style="{CG}font-size:80px;font-weight:600;line-height:1;margin-top:20px">{s["title"]}</div>'
                f'<div style="margin-top:26px">{rows}</div></div>' + foot())
        page_out(f'{n:02d}', body, bg); continue
    if t == 'story':
        h = s.get('h', 650)
        pics = img(s['photo'], 0, 0, 1080, h, s.get('pos', '50% 50%'))
        if s.get('photo2'):
            pics += img(s['photo2'], 720, h - 170, 300, 300, s.get('pos2', '50% 50%'), 6, f'border:8px solid {CREAM};box-shadow:0 10px 30px rgba(0,0,0,.35);transform:rotate(3deg);z-index:3')
        body = (pics + f'<div style="position:absolute;left:0;top:0;width:1080px;height:{h}px;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 26%)"></div>' +
                credit(s.get('credit', ''), 64, h - 30) + GARL('top') + mast(n) + SNOW +
                f'<div style="position:absolute;left:64px;right:{400 if s.get("photo2") else 64}px;top:{h + 34}px;color:{CREAM}">'
                f'<div style="display:flex;gap:12px;align-items:center">{chip(s["town"], GOLD if bg == RED else RED2, GRN if bg == RED else "#fff")}<span style="font-size:17px;font-weight:800;letter-spacing:.2em;color:{GOLD};text-transform:uppercase">{E(s["cat"])}</span></div>'
                f'<div style="{CG}font-size:{s.get("ts", 60)}px;font-weight:600;line-height:1.02;margin-top:16px">{E(s["title"])}</div></div>'
                f'<div style="position:absolute;left:64px;right:64px;top:{h + 34 + 70 + s.get("tgap", 150)}px;color:{CREAM}">{facts(s["facts"])}'
                + (f'<div style="margin-top:20px">{tip(s["tip"][0], s["tip"][1])}</div>' if s.get('tip') else '') + '</div>' + foot())
        page_out(f'{n:02d}', body, bg); continue
    if t == 'facts':
        cards = ''.join(f'<div style="background:rgba(255,246,229,.08);border:1.5px solid rgba(242,193,78,.45);padding:20px 22px;display:flex;gap:18px;align-items:flex-start">'
                        f'<div style="{CG}font-size:54px;color:{GOLD};line-height:.9;min-width:46px">{k + 1}</div>'
                        f'<div><div style="font-size:24px;font-weight:700">{E(a)}</div><div style="font-size:21px;line-height:1.4;margin-top:5px;color:#F3E7D3">{E(b)}</div></div></div>' for k, (a, b) in enumerate(s['items']))
        body = (SNOW + GARL('top') + mast(n) +
                f'<div style="position:absolute;left:64px;right:64px;top:126px;color:{CREAM}">{chip(s["chip"], GOLD, GRN)}'
                f'<div style="{CG}font-size:76px;font-weight:600;line-height:1;margin-top:18px">{s["title"]}</div>'
                f'<div style="display:grid;gap:14px;margin-top:26px">{cards}</div></div>' + foot())
        page_out(f'{n:02d}', body, bg); continue
    if t == 'end':
        body = (SNOW + GARL('top') + GARL('bottom') + mast(n, GRN) +
                f'<div style="position:absolute;left:70px;right:70px;top:250px;color:{GRN}">'
                f'<div style="font-size:120px;line-height:1">🎄</div>'
                f'<div style="{CG}font-size:104px;font-weight:600;line-height:1;margin-top:20px;color:{RED}">Wesołych<br>Świąt!</div>'
                f'<div style="font-size:31px;line-height:1.45;margin-top:34px">{s["text"]}</div>'
                f'<div style="display:flex;gap:16px;margin-top:46px;font-size:20px;font-weight:800;letter-spacing:.16em">'
                f'<span style="background:{RED2};color:#fff;padding:15px 20px">🔔 WŁĄCZ POWIADOMIENIA</span><span style="border:2.5px solid {GRN};padding:13px 20px">ZAPISZ · UDOSTĘPNIJ</span></div></div>' + foot(GRN))
        page_out(f'{n:02d}', body.replace('rgba(255,255,255,.6)', 'rgba(198,40,40,.35)'), CREAM); continue

open(f'{out}/fb.html', 'w').write(open(f'{out}/01.html').read().replace('PRZESUŃ  →', 'CAŁY PRZEWODNIK W OPISIE'))
print('ok', N)
