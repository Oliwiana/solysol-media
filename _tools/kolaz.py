# Okładka-kolaż Sol y Sól („składanka”, od 22.11.2026) – soczyste tło, koło z cz-b zdjęciem w rastrze,
# wycinanki z białym obrysem (naklejka.py), nagłówek Anton, biała etykieta z italikiem szeryfowym, pieczątka.
# cover(spec) -> HTML 1080 x H. Spec: bg, blob (kolor koła), photo (ścieżka, robi raster), head (linie, <u> podkreślenie),
# sub (biała etykieta), tag (żółta), tag2 (niebieska), stamp [tekst, x, y, rot], stickers [[png, x, y, w, rot, z]], H (1920/1350)
import base64, io, os, numpy as np, cv2
from PIL import Image, ImageOps, ImageEnhance
F = 'file:///home/claude/tools/node_modules/@fontsource'
def _ff(fam, path, w=400, st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X', s)})}}" for s in ('latin', 'latin-ext'))
FONTS = (_ff('AN', 'anton/files/anton-X-400-normal.woff2') + _ff('CG', 'cormorant-garamond/files/cormorant-garamond-X-600-italic.woff2', 600, 'italic')
         + _ff('IN', 'inter/files/inter-X-600-normal.woff2', 600) + _ff('IN', 'inter/files/inter-X-800-normal.woff2', 800) + _ff('IN', 'inter/files/inter-X-400-normal.woff2', 400))
def halftone(src, out, size=900, cell=9, contrast=1.3):
    im = Image.open(src).convert('L'); im = ImageOps.fit(im, (size, size)); im = ImageOps.autocontrast(im, cutoff=2); im = ImageEnhance.Contrast(im).enhance(contrast)
    a = np.array(im, np.float32) / 255; o = np.full(a.shape, 255, np.uint8)
    for y in range(0, size, cell):
        for x in range(0, size, cell):
            r = (1 - a[y:y + cell, x:x + cell].mean()) * cell * .74
            if r > .5: cv2.circle(o, (x + cell // 2, y + cell // 2), int(round(r)), 0, -1, cv2.LINE_AA)
    Image.fromarray(o).save(out); return out
def _u(p): return 'file://' + os.path.abspath(p)
def cover(bg='#F2E35B', blob='#E8562A', photo=None, blobxy=(330, 360, 760), head='', hsize=150, htop=1080, sub='', tag='', tag2='', stamp=None,
          stickers=(), H=1920, brand=True, note='', grain=True):
    st = ''.join(f'<img src="{_u(p)}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg);z-index:{z}">' for p, x, y, w, r, z in stickers)
    bx, by, bd = blobxy
    ph = f'<div style="position:absolute;left:{bx}px;top:{by}px;width:{bd}px;height:{bd}px;border-radius:50%;background:{blob};overflow:hidden;z-index:1">' + \
         (f'<img src="{_u(photo)}" style="width:100%;height:100%;object-fit:cover;mix-blend-mode:multiply;opacity:.92">' if photo else '') + '</div>'
    sp = (f'<div style="position:absolute;left:{stamp[1]}px;top:{stamp[2]}px;transform:rotate({stamp[3]}deg);border:8px solid #C0281B;color:#C0281B;font-family:AN;font-size:{stamp[4] if len(stamp) > 4 else 96}px;'
          f'padding:0 22px;border-radius:10px;z-index:6;background:rgba(255,255,255,.35);letter-spacing:.02em">{stamp[0]}</div>') if stamp else ''
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box;margin:0}}
html,body{{width:1080px;height:{H}px;overflow:hidden;background:{bg};font-family:IN,sans-serif}}
.hd{{font-family:AN;font-size:{hsize}px;line-height:1.06;color:#141210;text-transform:uppercase;letter-spacing:-.005em}}
.hd u{{text-decoration-thickness:10px;text-underline-offset:12px;text-decoration-color:#C0281B}}
.lab{{display:inline-block;font-family:IN;font-weight:800;font-size:34px;padding:6px 16px 8px;letter-spacing:.01em}}
</style></head><body>
<div style="position:absolute;inset:0;background:radial-gradient(circle at 20% 15%,rgba(255,255,255,.25),transparent 45%)"></div>
{ph}{st}{sp}
{f'<div style="position:absolute;left:60px;top:{htop - 90}px;z-index:7">' + (f'<span class=lab style="background:#2F45C9;color:#fff;transform:rotate(-2deg)">{tag2}</span> ' if tag2 else '') + (f'<span class=lab style="background:#141210;color:#F2E35B">{tag}</span>' if tag else '') + '</div>'}
<div class=hd style="position:absolute;left:56px;right:56px;top:{htop}px;z-index:7">{head}</div>
{f'<div style="position:absolute;left:60px;top:{htop + 40}px;z-index:8" id=sub><span style="display:inline-block;background:#fff;color:#141210;font-family:CG;font-style:italic;font-weight:600;font-size:62px;padding:2px 22px 8px;box-shadow:0 8px 20px rgba(0,0,0,.25);transform:rotate(-1.5deg)">{sub}</span></div>' if sub else ''}
{f'<div style="position:absolute;left:60px;right:60px;bottom:{(H - 1350) // 2 + 40 if H > 1350 else 40}px;font-family:IN;font-weight:600;font-size:30px;color:#141210;z-index:8">{note}</div>' if note else ''}
{f'<div style="position:absolute;left:0;right:0;top:{(H - 1350) // 2 + 26 if H > 1350 else 26}px;text-align:center;z-index:9"><span style="display:inline-block;background:#141210;color:#fff;font-family:IN;font-weight:800;font-size:26px;letter-spacing:.32em;padding:8px 18px 8px 26px">SOL Y SÓL</span></div>' if brand else ''}
{'<svg style="position:absolute;inset:0;z-index:20;opacity:.22;mix-blend-mode:multiply" width=1080 height=' + str(H) + '><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=2 stitchTiles=stitch /><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 0"/></filter><rect width=100% height=100% filter=url(#n) /></svg>' if grain else ''}
</body></html>"""

def cover_h(bg='#F2E35B', blob='#E8562A', photo=None, head='', hsize=110, tag='', tag2='', stickers=(), W=1280, H=720, grain=True):
    """Miniatura YouTube 1280x720: nagłówek po lewej, koło ze zdjęciem po prawej, wycinanki."""
    st = ''.join(f'<img src="{_u(p)}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;transform:rotate({r}deg);z-index:{z}">' for p, x, y, w, r, z in stickers)
    ph = f'<div style="position:absolute;left:700px;top:60px;width:600px;height:600px;border-radius:50%;background:{blob};overflow:hidden;z-index:1">' + \
         (f'<img src="{_u(photo)}" style="width:100%;height:100%;object-fit:cover;mix-blend-mode:multiply;opacity:.92">' if photo else '') + '</div>'
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{box-sizing:border-box;margin:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{bg};font-family:IN,sans-serif}}
.hd{{font-family:AN;font-size:{hsize}px;line-height:.98;color:#141210;text-transform:uppercase}}
.hd u{{text-decoration-thickness:8px;text-underline-offset:10px;text-decoration-color:#C0281B}}
.lab{{display:inline-block;font-family:IN;font-weight:800;font-size:26px;padding:5px 12px 7px}}</style></head><body>
<div style="position:absolute;inset:0;background:radial-gradient(circle at 20% 15%,rgba(255,255,255,.25),transparent 45%)"></div>
{ph}{st}
<div style="position:absolute;left:48px;top:40px;z-index:9"><span style="display:inline-block;background:#141210;color:#fff;font-weight:800;font-size:22px;letter-spacing:.3em;padding:6px 14px 6px 20px">SOL Y SÓL</span></div>
<div style="position:absolute;left:48px;top:120px;z-index:7">{f'<span class=lab style="background:#2F45C9;color:#fff">{tag2}</span> ' if tag2 else ''}{f'<span class=lab style="background:#141210;color:#F2E35B">{tag}</span>' if tag else ''}</div>
<div class=hd style="position:absolute;left:44px;width:760px;top:200px;z-index:7">{head}</div>
{'<svg style="position:absolute;inset:0;z-index:20;opacity:.22;mix-blend-mode:multiply" width=' + str(W) + ' height=' + str(H) + '><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=2 stitchTiles=stitch /><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 0"/></filter><rect width=100% height=100% filter=url(#n) /></svg>' if grain else ''}
</body></html>"""
