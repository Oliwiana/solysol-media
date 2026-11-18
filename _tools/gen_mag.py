# Sol y Sól – strony w stylu magazynu (jak Nr 1), wersja świąteczna. 1080x1350 (IG), te same strony do druku.
# usage: python3 gen_mag.py pages.py OUTDIR  – pages.py definiuje listę PAGES (funkcje z tego pliku)
import sys, os, html
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen_base.py')).read().split("P={}")[0])
PH = '/home/claude/photos_raw/'
PAPER = '#FAF6EE'; INKK = '#2B2926'; RED = '#B3262B'; GRN = '#1F5C3F'; GOLD = '#C99A2E'; SAND = '#EFE6D6'; MUT = '#6E665C'
E = lambda t: html.escape(t, quote=False)
ISSUE = 'SOL Y SÓL · WYDANIE SPECJALNE · ŚWIĘTA 2026'
GARL = (f'<div style="position:absolute;left:0;right:0;top:0;height:10px;background:repeating-linear-gradient(90deg,{RED} 0 38px,{GOLD} 38px 48px,{GRN} 48px 86px,{GOLD} 86px 96px)"></div>')
SNOWD = ('<div style="position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(rgba(201,154,46,.35) 1.4px,transparent 1.9px);background-size:120px 120px;background-position:30px 40px"></div>')

def frame(n, total, section, inner, bg=PAPER):
    foot = (f'<div style="position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #CFC5B5;padding-top:14px;font-size:15px;letter-spacing:.14em;color:{MUT}">'
            f'<span><b style="color:{INKK}">SOL Y SÓL</b> · WYDANIE SPECJALNE · ŚWIĘTA 2026</span><span>{E(section.upper())} · {n:02d}</span></div>')
    return page(GARL + SNOWD + inner + foot, bg, INKK)

def kick(t, c=RED):
    return f'<div style="font-size:16px;font-weight:700;letter-spacing:.22em;color:{c};text-transform:uppercase">{E(t)}</div>'
def H(t, size=86, c=INKK):  # t may contain <i>
    return f'<div style="{CG}font-size:{size}px;font-weight:600;line-height:1;color:{c};margin-top:10px">{t}</div>'
def rule(c=INKK, w=3):
    return f'<div style="height:{w}px;background:{c};margin:18px 0"></div>'
def photo(p, x, y, w, h, pos='50% 50%', cap=''):
    c = f'<div style="position:absolute;left:{x}px;top:{y+h+6}px;width:{w}px;font-size:13px;color:{MUT}">{E(cap)}</div>' if cap else ''
    return f'<img src="file://{PH}{p}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos}">' + c
def stat(big, small, c=RED, size=64):
    return f'<div><div style="{CG}font-size:{size}px;font-weight:600;line-height:1;color:{c}">{big}</div><div style="font-size:19px;line-height:1.35;margin-top:8px;color:{INKK}">{small}</div></div>'
def box(title, text, bg=GRN, fg='#fff', tc=None):
    return (f'<div style="background:{bg};color:{fg};padding:22px 26px"><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:{tc or "#F2C14E"}">{E(title)}</div>'
            f'<div style="font-size:21px;line-height:1.45;margin-top:8px">{text}</div></div>')
def p(t, size=21):
    return f'<p style="font-size:{size}px;line-height:1.5;margin:0 0 14px">{t}</p>'
def hdr(t, size=30, c=INKK):
    return f'<div style="{CG}font-size:{size}px;font-weight:600;line-height:1.1;color:{c};margin:4px 0 6px">{t}</div>'

def src(t):
    return f'<div style="position:absolute;left:64px;right:64px;bottom:84px;font-size:13px;color:{MUT}">Źródła: {E(t)}</div>'

def build(PAGES, out):
    os.makedirs(out, exist_ok=True); N = len(PAGES)
    for i, f in enumerate(PAGES):
        h = f(i + 1, N)
        open(f'{out}/{i+1:02d}.html', 'w').write(h)
    print('ok', N)

if __name__ == '__main__':
    exec(open(sys.argv[1]).read(), globals())
    build(globals()['PAGES'], sys.argv[2])
