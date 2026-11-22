# Styl „barwna” Sol y Sól (od 22.11.2026) – KOLOROWA okładka jak wydanie specjalne „Święta 2026”:
# pełne kolorowe zdjęcie, duża winieta SOL Y SÓL, granatowa ramka + żółta ramka, czerwona pieczęć, tytuł Cormorant ze złotą kursywą.
# Użycie: from barwna import cover; html = cover(photo_url=..., head='Kiedy Marbella <i>była Hollywood</i>', ...)
# Pola opcjonalne: box1=[etykieta, tytuł], box2=[etykieta, WIELKI TEKST, dopisek], seal=[góra, kursywa, dół], more=[[etykieta, tytuł] x3]
import html as _h
F = 'file:///home/claude/tools/node_modules/@fontsource'
def _ff(fam, path, w, st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X', s)})}}" for s in ('latin', 'latin-ext'))
FONTS = (_ff('CG', 'cormorant-garamond/files/cormorant-garamond-X-600-normal.woff2', 600) + _ff('CG', 'cormorant-garamond/files/cormorant-garamond-X-600-italic.woff2', 600, 'italic')
         + _ff('IN', 'inter/files/inter-X-400-normal.woff2', 400) + _ff('IN', 'inter/files/inter-X-600-normal.woff2', 600) + _ff('IN', 'inter/files/inter-X-800-normal.woff2', 800)
         + _ff('IX', 'inter/files/inter-X-900-italic.woff2', 900, 'italic'))
GOLD = '#F2C14E'; RED = '#C62828'; NAVY = 'rgba(12,24,40,.74)'
CG = "font-family:CG,Georgia,serif;"
def cover(photo_url, pos='50% 50%', credit='', head='', teaser='', desk='', mast='MAGAZYN', date='', box1=None, box2=None, seal=None, more=(),
          hsize=100, htop=800, btop=440, stop=470, acc=GOLD, red=RED):
    head = head.replace('<i>', f'<i style="color:{acc}">')
    bx = ''
    if box1: bx += f'<div style="background:{NAVY};border-left:5px solid {acc};padding:16px 22px 18px;margin-bottom:16px;width:400px"><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:{acc}">{box1[0]}</div><div style="{CG}font-size:36px;font-weight:600;line-height:1.08;margin-top:6px">{box1[1]}</div></div>'
    if box2: bx += f'<div style="background:{acc};color:#171513;padding:14px 20px 16px;width:400px;transform:rotate(-2deg);box-shadow:0 14px 30px rgba(0,0,0,.45)"><div style="display:inline-block;background:#171513;color:{acc};font-size:13px;font-weight:800;letter-spacing:.18em;padding:4px 10px">{box2[0]}</div><div style="font-family:IX;font-style:italic;font-weight:900;font-size:36px;line-height:1.02;letter-spacing:-.02em;margin-top:8px;text-transform:uppercase">{box2[1]}</div><div style="font-size:16px;font-weight:600;margin-top:6px">{box2[2] if len(box2) > 2 else ""}</div></div>'
    sl = (f'<div style="position:absolute;right:58px;top:{stop}px;width:230px;height:230px;border-radius:50%;background:{red};color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-8deg);box-shadow:0 10px 30px rgba(0,0,0,.4);border:3px dashed {acc};text-align:center">'
          f'<div style="font-size:16px;font-weight:800;letter-spacing:.2em">{seal[0]}</div><div style="{CG}font-style:italic;font-size:44px;line-height:1;margin:4px 0">{seal[1]}</div><div style="width:110px;height:1px;background:rgba(255,255,255,.6);margin:4px 0 6px"></div><div style="font-size:14px;font-weight:800;letter-spacing:.14em;line-height:1.3">{seal[2]}</div></div>') if seal else ''
    low = ''.join(f'<div style="flex:1;text-align:center"><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:{acc}">{a}</div><div style="{CG}font-size:30px;font-weight:600;line-height:1.12;margin-top:8px">{b}</div></div>' for a, b in list(more)[:3])
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box;margin:0}}html,body{{width:1080px;height:1350px;overflow:hidden;font-family:IN,sans-serif;background:#0A1422;color:#FAF7F2}}</style></head><body>
<div style="position:absolute;inset:0;background:url('{photo_url}') {pos}/cover;filter:saturate(1.15)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,20,34,.72) 0%,rgba(10,20,34,.25) 26%,rgba(10,20,34,.12) 45%,rgba(10,20,34,.5) 62%,rgba(10,20,34,.92) 80%,#0A1422 100%)"></div>
<div style="position:absolute;left:64px;right:64px;top:40px;text-align:center">
<div style="display:flex;justify-content:space-between;font-size:16px;font-weight:600;letter-spacing:.18em;padding-bottom:12px;border-bottom:1px solid rgba(250,247,242,.5)"><span>{_h.escape(mast)}</span><span>{_h.escape(date)}</span><span>SOLYSOL.PL</span></div>
<div style="{CG}font-size:140px;font-weight:600;line-height:1;letter-spacing:.1em;margin-top:20px;padding-left:.1em;text-shadow:0 4px 24px rgba(0,0,0,.35)">SOL Y SÓL</div>
<div style="font-size:18px;font-weight:600;letter-spacing:.42em;margin-top:8px;padding-left:.42em">COSTA DEL SOL PO POLSKU</div></div>
<div style="position:absolute;left:64px;top:{btop}px">{bx}</div>{sl}
<div style="position:absolute;right:30px;top:{htop-40}px;font-size:13px;opacity:.8">{_h.escape(credit)}</div>
<div style="position:absolute;left:50px;right:50px;top:{htop}px;text-align:center">
<div style="font-size:17px;font-weight:600;letter-spacing:.24em;color:{acc}">{desk}</div>
<div style="{CG}font-size:{hsize}px;font-weight:600;line-height:.98;margin-top:12px">{head}</div>
<div style="font-size:24px;margin-top:16px;line-height:1.35">{teaser}</div></div>
{('<div style="position:absolute;left:64px;right:64px;top:1150px;border-top:1px solid rgba(250,247,242,.45);padding-top:18px;display:flex;gap:30px">' + low + '</div>') if low else ''}
<div style="position:absolute;left:64px;right:64px;bottom:22px;display:flex;justify-content:space-between;font-size:13px;letter-spacing:.16em;opacity:.75"><span>PRZESUŃ  →</span><span>SOLYSOL.PL</span></div>
</body></html>"""
