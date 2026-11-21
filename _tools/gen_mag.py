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

def frame(n, total, section, inner, bg=None):
    bg = bg or PAPER
    foot = (f'<div style="position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #CFC5B5;padding-top:14px;font-size:15px;letter-spacing:.14em;color:{MUT}">'
            f'<span><b style="color:{INKK}">SOL Y SÓL</b> · WYDANIE SPECJALNE · ŚWIĘTA 2026</span><span>{E(section.upper())} · {n:02d}</span></div>')
    return page(GARL + SNOWD + inner + foot, bg, INKK)

def kick(t, c=None):
    c = c or RED
    return f'<div style="font-size:16px;font-weight:700;letter-spacing:.22em;color:{c};text-transform:uppercase">{E(t)}</div>'
def H(t, size=86, c=None):  # t may contain <i>
    c = c or INKK
    return f'<div style="{CG}font-size:{size}px;font-weight:600;line-height:1;color:{c};margin-top:10px">{t}</div>'
def rule(c=None, w=3):
    c = c or INKK
    return f'<div style="height:{w}px;background:{c};margin:18px 0"></div>'
PHOTO_STYLE = ['blob', 'fade']
def photo(p, x, y, w, h, pos='50% 50%', cap='', style=None):
    st = style or 'none'
    if st == 'blob':
        css = 'border-radius:48% 52% 44% 56% / 55% 45% 55% 45%;-webkit-mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 62%,transparent 100%)'
    elif st == 'fade':
        css = 'border-radius:40px 40px 160px 40px;-webkit-mask-image:linear-gradient(180deg,#000 60%,transparent 100%),linear-gradient(90deg,transparent 0%,#000 14%,#000 86%,transparent 100%);-webkit-mask-composite:source-in'
    else:
        css = ''
    c = f'<div style="position:absolute;left:{x}px;top:{y+h-18}px;width:{w}px;font-size:13px;color:{MUT};text-align:center">{E(cap)}</div>' if cap else ''
    return f'<img src="file://{PH}{p}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover;object-position:{pos};{css}">' + c
def stat(big, small, c=None, size=64):
    c = c or RED
    return f'<div><div style="{CG}font-size:{size}px;font-weight:600;line-height:1;color:{c}">{big}</div><div style="font-size:19px;line-height:1.35;margin-top:8px;color:{INKK}">{small}</div></div>'
def box(title, text, bg=None, fg='#fff', tc=None):
    bg = bg or GRN
    return (f'<div style="background:{bg};color:{fg};padding:22px 26px"><div style="font-size:15px;font-weight:800;letter-spacing:.2em;color:{tc or "#F2C14E"}">{E(title)}</div>'
            f'<div style="font-size:21px;line-height:1.45;margin-top:8px">{text}</div></div>')
def p(t, size=21):
    return f'<p style="font-size:{size}px;line-height:1.5;margin:0 0 14px">{t}</p>'
def hdr(t, size=30, c=None):
    c = c or INKK
    return f'<div style="{CG}font-size:{size}px;font-weight:600;line-height:1.1;color:{c};margin:4px 0 6px">{t}</div>'

def src(t):
    return f'<div style="position:absolute;left:64px;right:64px;bottom:84px;font-size:13px;color:{MUT}">Źródła: {E(t)}</div>'

THEMES = {
 'light': dict(PAPER='#FFFDF8', INKK='#1E1B18', MUT='#7A6F63', SAND='#F4ECDD', RED='#A4161A', GRN='#14452F', GOLD='#B8892B', LINE='#E2D8C6', SUB='#4A443D', ZEB='#FBF6EC', CARD='#FFFFFF'),
 'green': dict(PAPER='#123D2B', INKK='#FFF6E5', MUT='#BFD6C6', SAND='rgba(255,255,255,.09)', RED='#F2C14E', GRN='#E0574B', GOLD='#F2C14E', LINE='rgba(242,193,78,.35)', SUB='#E3EDE6', ZEB='rgba(255,255,255,.05)', CARD='rgba(255,255,255,.14)'),
 'red':   dict(PAPER='#8E1C22', INKK='#FFF6E5', MUT='#F1CFCB', SAND='rgba(255,255,255,.1)', RED='#F2C14E', GRN='#8EDDB0', GOLD='#F2C14E', LINE='rgba(242,193,78,.4)', SUB='#F8E6E3', ZEB='rgba(255,255,255,.06)', CARD='rgba(255,255,255,.15)'),
}
def build(PAGES, out, seq=('green', 'red')):
    os.makedirs(out, exist_ok=True); N = len(PAGES); g = globals()
    seq = g.get('THEME_SEQ', seq)
    for i, f in enumerate(PAGES):
        t = THEMES[seq[i % len(seq)] if seq[i % len(seq)] in THEMES else 'light']
        for k, v in t.items(): g[k] = v
        h = f(i + 1, N)
        for a, b in [('#CFC5B5', t['LINE']), ('#4A443D', t['SUB']), ('#D9CDB8', t['LINE']), ('rgba(239,230,214,.6)', t['ZEB']),
                     ('background:#fff;border', 'background:' + t['CARD'] + ';border'), ('rgba(0,0,0,.7) 100%', t['PAPER'] + ' 100%'),
                     ('rgba(0,0,0,.75) 100%', t['PAPER'] + ' 100%'), ('rgba(201,154,46,.35) 1.4px', 'rgba(255,255,255,.35) 1.4px' if t['PAPER'] != '#FFFDF8' else 'rgba(0,0,0,0) 1.4px')]:
            h = h.replace(a, b)
        open(f'{out}/{i+1:02d}.html', 'w').write(h)
    print('ok', N)

def dc(text, c=None):
    c = c or RED
    return f'<p style="font-size:21px;line-height:1.55;margin:0 0 14px"><span style="float:left;{CG}font-size:96px;line-height:.78;font-weight:600;color:{c};margin:8px 12px 0 0">{text[0]}</span>{text[1:]}</p>'
def pull(t, c=None):
    c = c or RED
    return f'<div style="border-top:3px solid {c};border-bottom:1px solid {c};padding:18px 0;margin:10px 0 18px"><div style="{CG}font-style:italic;font-size:36px;line-height:1.15;color:{c}">„{t}”</div></div>'
def cap(t, x, y, w, al='left'):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font-size:14px;font-style:italic;color:{MUT};text-align:{al}">{E(t)}</div>'

if __name__ == '__main__':
    exec(open(sys.argv[1]).read(), globals())
    build(globals()['PAGES'], sys.argv[2])
