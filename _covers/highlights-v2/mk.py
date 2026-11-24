import sys; sys.path.insert(0,'/tmp/sm/_tools')
from kolaz import FONTS,_u
SUN=_u('/tmp/g/logo/sunA.png')
clock='<svg width="380" height="380" viewBox="0 0 100 100"><circle cx="50" cy="50" r="40" fill="none" stroke="{c}" stroke-width="8"/><path d="M50 26 V50 L66 60" fill="none" stroke="{c}" stroke-width="8" stroke-linecap="round"/></svg>'
star='<svg width="400" height="400" viewBox="0 0 100 100"><path d="M50 8 L61 38 L93 39 L68 58 L77 90 L50 71 L23 90 L32 58 L7 39 L39 38 Z" fill="{c}"/></svg>'
cal='<svg width="380" height="380" viewBox="0 0 100 100"><rect x="12" y="18" width="76" height="70" rx="8" fill="none" stroke="{c}" stroke-width="8"/><path d="M12 38 H88 M32 8 V26 M68 8 V26" stroke="{c}" stroke-width="8" stroke-linecap="round"/><text x="50" y="80" text-anchor="middle" font-family="AN" font-size="38" fill="{c}">7</text></svg>'
G={'pilne':('txt','!'),'wiadomosci':('svg',clock),'tydzien':('svg',cal),'zagadki':('txt','?'),'gwiazdy':('svg',star),'czywiesz':('txt','i')}
def page(n,style):
    t,g=G[n]
    if style=='dark': bg,c,circ='#2a2723','#f3eee6',f'<img src="{SUN}" style="position:absolute;left:190px;top:610px;width:700px;height:700px;opacity:.95">'
    else: bg,c,circ='#f3eee6','#2a2723',f'<img src="{SUN}" style="position:absolute;left:190px;top:610px;width:700px;height:700px">'
    if style=='dark': gc='#f3eee6'
    else: gc='#f3eee6'
    inner=(f'<div style="position:absolute;left:0;right:0;top:640px;text-align:center;font-family:{"CG" if n=="czywiesz" else "AN"};font-style:{"italic" if n=="czywiesz" else "normal"};font-size:{560 if n!="czywiesz" else 600}px;line-height:1.1;color:{gc}">{g}</div>' if t=='txt'
           else f'<div style="position:absolute;left:0;right:0;top:770px;text-align:center">{g.format(c=gc)}</div>')
    return f'<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{margin:0}}html,body{{width:1080px;height:1920px;overflow:hidden;background:{bg}}}</style></head><body>{circ}{inner}</body></html>'
for st in ('dark','cream'):
    for n in G: open(f'{st}_{n}.html','w').write(page(n,st))
