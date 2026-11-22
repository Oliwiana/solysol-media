# Styl „noir” Sol y Sól (od 22.11.2026) – okładki: czarno-białe zdjęcie na całość, ziarno,
# niebieskie/żółte etykiety, wąski nagłówek (Oswald) z podkreśleniem <u> i szeryfową kursywą <i>/<em>,
# podtytuł szeryfową kursywą, opcjonalny „skrawek” (drugie zdjęcie przypięte jak w kolażu).
import re, html as _h
F = 'file:///home/claude/tools/node_modules/@fontsource'
def _ff(fam, path, w, st='normal'):
    return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};font-style:{st};src:url({F}/{path.replace('X', s)})}}" for s in ('latin', 'latin-ext'))
FONTS = (_ff('NO', 'oswald/files/oswald-X-600-normal.woff2', 600) + _ff('NS', 'cormorant-garamond/files/cormorant-garamond-X-500-italic.woff2', 500, 'italic')
         + _ff('NS', 'cormorant-garamond/files/cormorant-garamond-X-600-normal.woff2', 600) + _ff('NI', 'inter/files/inter-X-600-normal.woff2', 600)
         + _ff('NI', 'inter/files/inter-X-400-normal.woff2', 400))
CSS = FONTS + '''
html,body{margin:0;width:1080px;height:1350px;overflow:hidden;background:#0d0d0f;color:#f4f1ea}
.nbg{position:absolute;inset:0;background-size:cover;filter:grayscale(1) contrast(1.15) brightness(.8)}
.ntint{position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,14,30,.35) 0%,rgba(10,14,30,.05) 30%,rgba(8,10,20,.82) 66%,rgba(8,10,20,.96) 100%)}
.ngrain{position:absolute;inset:0;opacity:.22;mix-blend-mode:overlay}
.nscrap{position:absolute;background:#efe9dc;padding:14px 14px 40px;box-shadow:0 18px 40px rgba(0,0,0,.55)}
.nscrap img{display:block;filter:grayscale(1) contrast(1.1)}
.nlab{display:inline-block;font-family:NI;font-weight:600;font-size:32px;line-height:1.05;padding:6px 14px 8px;margin:0 8px 8px 0}
.nblue{background:#5b7cff;color:#fff}.nyel{background:#f2e35b;color:#2f45c9}
.nh{font-family:NO;font-weight:600;line-height:.98;letter-spacing:-.025em;margin:14px 0 0;color:#f4f1ea}
.nh u{text-decoration-thickness:6px;text-underline-offset:12px}
.nh i,.nh em{font-family:NS;font-style:italic;font-weight:500;letter-spacing:-.01em;color:#f4f1ea}
.nsub{font-family:NS;font-style:italic;font-size:44px;line-height:1.15;opacity:.92;margin-top:24px}
.nbrand{position:absolute;left:64px;top:56px;font-family:NS;font-weight:600;font-size:36px;letter-spacing:.08em}
.nbrand i{color:#f2e35b;font-style:italic}
.ncr{position:absolute;right:28px;bottom:22px;font-family:NI;font-weight:400;font-size:17px;opacity:.6}
.nfoot{position:absolute;left:64px;right:64px;bottom:58px;display:flex;justify-content:space-between;font-family:NI;font-weight:600;font-size:22px;letter-spacing:.14em;text-transform:uppercase;opacity:.8}
'''
GRAIN = '<svg class=ngrain width=1080 height=1350><filter id=nn><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=3 stitchTiles=stitch/></filter><rect width=100% height=100% filter=url(#nn)/></svg>'

def clean_head(h):
    h = re.sub(r'<i\b[^>]*>', '<i>', h or ''); h = re.sub(r'<span\b[^>]*>|</span>', '', h)
    return h

def head_size(h):
    n = len(re.sub(r'<[^>]+>', '', h))
    return 112 if n <= 28 else 98 if n <= 44 else 86 if n <= 62 else 74

def cover(photo_url, pos='50% 50%', credit='', labels=(), head='', sub='', foot_left='Przesuń →', foot_right='solysol.pl', scrap_url=None, scrap_pos='50% 50%', hsize=None):
    head = clean_head(head); hs = hsize or head_size(head)
    labs = ''.join(f'<span class="nlab n{c}">{_h.escape(t)}</span>' for t, c in labels if t)
    scrap = f'<div class=nscrap style="right:70px;top:170px;transform:rotate(4deg)"><img src="{scrap_url}" style="width:330px;height:230px;object-fit:cover;object-position:{scrap_pos}"></div>' if scrap_url else ''
    body = f'''<div class=nbg style="background-image:url('{photo_url}');background-position:{pos}"></div><div class=ntint></div>{GRAIN}
<div class=nbrand>SOL <i>y</i> SÓL</div>{scrap}
<div style="position:absolute;left:64px;right:64px;bottom:150px">{labs}
<h1 class=nh style="font-size:{hs}px">{head}</h1>
{f'<div class=nsub>{_h.escape(sub)}</div>' if sub else ''}</div>
<div class=nfoot><span>{_h.escape(foot_left)}</span><span>{_h.escape(foot_right)}</span></div><div class=ncr>{_h.escape(credit)}</div>'''
    return f'<!DOCTYPE html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{body}</body></html>'
