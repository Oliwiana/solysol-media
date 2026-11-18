# Przegląd dnia Sol y Sól – karuzela IG (okładka + 1 slajd na wiadomość + zakończenie) i grafika FB.
# usage: python3 gen_digest.py dane.json OUTDIR   (potem: cp /home/claude/social/posty10/shot.js OUTDIR && cd OUTDIR && node shot.js)
# dane.json: {"id","edition":"rano"|"wieczor","date":"DD.MM.RRRR","photo","pos","credit",
#             "items":[{"town","cat","title","text","src","photo","pos","credit"}]}   (3–8 items)
import json, sys, os, html
exec(open('/home/claude/social/posty10/gen.py').read().split("P={}")[0])
d = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
ED = {'rano': ('Poranek', 'na wybrzeżu', 'PORANEK', '19:00', 'wieczorem'),
      'wieczor': ('Wieczór', 'na wybrzeżu', 'WIECZÓR', '8:00', 'jutro rano')}[d.get('edition', 'rano')]
items = d['items'][:8]; N = len(items) + 2; DATE = d['date']
PH = '/home/claude/photos_raw/'
def esc(t): return html.escape(t or '', quote=False)
def mast(n, fg=IV, line='rgba(246,241,232,.35)'):
    return (f'<div style="position:absolute;left:70px;right:70px;top:56px;display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:1.5px solid {line};color:{fg}">'
            f'<div style="{CG}font-size:34px;font-weight:500;letter-spacing:.06em">S<span style="display:inline-block;width:22px;height:22px;border-radius:50%;background:{ORL};margin:0 2px"></span>L <i style="color:{ORL}">y</i> SÓL</div>'
            f'<div style="font-size:19px;font-weight:600;letter-spacing:.2em">{ED[2]} · {DATE}</div>'
            f'<div style="font-size:19px;font-weight:600;letter-spacing:.14em;opacity:.75">{n}/{N}</div></div>')
def foot(txt, fg=IV, line='rgba(246,241,232,.3)'):
    return (f'<div style="position:absolute;left:70px;right:70px;bottom:52px;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid {line};padding-top:20px;color:{fg};font-size:20px;letter-spacing:.12em;font-weight:600">'
            f'<span style="opacity:.75">{txt}</span><span>SOLYSOL.PL</span></div>')
def tag(t): return f'<span style="display:inline-block;background:{ORG};color:#fff;font-size:20px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;padding:9px 16px">{esc(t)}</span>'
def write(name, body, bg=INK, fg=IV): open(f'{out}/{name}.html', 'w').write(page(body, bg, fg))

# 1. okładka – spis wiadomości
lst = ''.join(f'<div style="display:flex;gap:22px;align-items:baseline;padding:15px 0;border-top:1px solid rgba(246,241,232,.22)">'
              f'<span style="{CG}font-size:34px;color:{ORL};min-width:34px">{i+1}</span>'
              f'<div><div style="font-size:16px;font-weight:700;letter-spacing:.2em;color:{ORL};text-transform:uppercase">{esc(it["town"])}</div>'
              f'<div style="font-size:27px;line-height:1.25;margin-top:4px">{esc(it["title"])}</div></div></div>' for i, it in enumerate(items))
write('01', f'''<img src="file://{PH}{d["photo"]}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{d.get("pos","50% 50%")}">
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,21,19,.7) 0%,rgba(23,21,19,.35) 18%,rgba(23,21,19,.85) 36%,{INK} 52%)"></div>
{mast(1)}
<div style="position:absolute;left:70px;right:70px;top:170px">
<div style="{CG}font-size:118px;font-weight:500;line-height:.95">{ED[0]} <i style="color:{ORL}">{ED[1]}</i></div>
<div style="font-size:24px;letter-spacing:.16em;font-weight:600;margin-top:18px;color:#E6DED1">{len(items)} NAJWAŻNIEJSZYCH SPRAW · {DATE}</div></div>
<div style="position:absolute;left:70px;right:70px;top:{470 if len(items)<=6 else 420}px">{lst}</div>
<div style="position:absolute;right:70px;top:400px;font-size:15px;color:rgba(246,241,232,.65)">{esc(d.get("credit",""))}</div>
{foot('PRZESUŃ  →')}''')

# 2..N-1 – po jednej wiadomości
for i, it in enumerate(items):
    n = i + 2
    img = (f'<img src="file://{PH}{it["photo"]}" style="position:absolute;left:0;top:0;width:1080px;height:520px;object-fit:cover;object-position:{it.get("pos","50% 50%")}">'
           f'<div style="position:absolute;left:0;top:0;width:1080px;height:520px;background:linear-gradient(180deg,rgba(23,21,19,.75) 0%,rgba(23,21,19,0) 30%,rgba(23,21,19,0) 70%,rgba(23,21,19,.55) 100%)"></div>'
           f'<div style="position:absolute;right:70px;top:486px;font-size:15px;color:rgba(246,241,232,.8)">{esc(it.get("credit",""))}</div>') if it.get('photo') else ''
    top = 560 if it.get('photo') else 190
    tsize = 54 if len(it['title']) < 70 else 46
    write(f'{n:02d}', f'''{img}{mast(n)}
<div style="position:absolute;left:70px;right:70px;top:{top}px">
<div style="display:flex;gap:12px;align-items:center">{tag(it["town"])}<span style="font-size:18px;font-weight:700;letter-spacing:.2em;color:{ORL};text-transform:uppercase">{esc(it.get("cat",""))}</span></div>
<div style="{CG}font-size:{tsize}px;font-weight:500;line-height:1.05;margin-top:20px">{esc(it["title"])}</div>
<div style="font-size:{25 if len(it["text"])>420 else 27}px;line-height:1.48;margin-top:20px;color:#E6DED1">{esc(it["text"])}</div>
<div style="font-size:16px;margin-top:18px;color:rgba(246,241,232,.55)">Źródło: {esc(it.get("src",""))}</div></div>
{foot(f'{ED[2]} · {n-1}/{len(items)}')}''')

# ostatni slajd
write(f'{N:02d}', f'''{mast(N, INK, 'rgba(23,21,19,.25)')}
<div style="position:absolute;left:70px;right:70px;top:300px;color:{INK}">
<div style="{CG}font-size:92px;font-weight:500;line-height:1">To wszystko<br><i style="color:{ORG}">na {('teraz' if ED[2]=='PORANEK' else 'dziś')}.</i></div>
<div style="font-size:32px;line-height:1.45;margin-top:40px">Kolejne wydanie – <b>{ED[4]}, o {ED[3]}</b>.<br>Pilne sprawy publikujemy od razu.</div>
<div style="font-size:30px;line-height:1.45;margin-top:34px">Szczegóły każdej wiadomości – na <b>solysol.pl</b></div>
<div style="display:flex;gap:18px;margin-top:56px;font-size:21px;font-weight:700;letter-spacing:.16em">
<span style="border:2px solid {INK};padding:14px 20px">🔔 WŁĄCZ POWIADOMIENIA</span><span style="border:2px solid {INK};padding:14px 20px">ZAPISZ · UDOSTĘPNIJ</span></div></div>
{foot('OBSERWUJ @SOLYSOL.PL', INK, 'rgba(23,21,19,.25)')}''', IV, INK)

# FB – jedna grafika: okładka ze spisem (bez numeru slajdu)
open(f'{out}/fb.html', 'w').write(open(f'{out}/01.html').read().replace(f'>1/{N}<', '><').replace('PRZESUŃ  →', 'WSZYSTKIE WIADOMOŚCI W OPISIE'))
print('ok', N, 'slajdów')
