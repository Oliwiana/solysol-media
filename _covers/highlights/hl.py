import sys; sys.path.insert(0,'/tmp/sm/_tools')
from kolaz import FONTS,_u
N='/tmp/sm/_assets/naklejki/'
D=[('wiadomosci','WIADOMOŚCI','#F2E35B','#E8562A','telefon.png'),
   ('tydzien','TYDZIEŃ','#2F45C9','#F2E35B','zegarek.png'),
   ('zagadki','ZAGADKI','#E8562A','#141210','ksiega.png'),
   ('gwiazdy','GWIAZDY','#9FD8C8','#E8562A','klaps.png'),
   ('czywiesz','CZY WIESZ','#141210','#E8562A','latarnia.png')]
for n,t,bg,blob,st in D:
    fg='#fff' if bg in('#2F45C9','#141210','#E8562A') else '#141210'
    h=f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{margin:0}}html,body{{width:1080px;height:1920px;overflow:hidden;background:{bg}}}</style></head><body>
<div style="position:absolute;left:190px;top:470px;width:700px;height:700px;border-radius:50%;background:{blob}"></div>
<img src="{_u(N+st)}" style="position:absolute;left:240px;top:470px;width:600px;height:600px;object-fit:contain;transform:rotate(-6deg)">
<div style="position:absolute;left:0;right:0;top:1090px;text-align:center"><span style="display:inline-block;background:{'#F2E35B' if bg=='#141210' else '#141210'};color:{'#141210' if bg=='#141210' else '#fff'};font-family:AN;font-size:150px;padding:4px 30px;transform:rotate(-2deg)">{t}</span></div>
<svg style="position:absolute;inset:0;opacity:.22;mix-blend-mode:multiply" width=1080 height=1920><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=2 stitchTiles=stitch /><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 0"/></filter><rect width=100% height=100% filter=url(#n) /></svg>
</body></html>"""
    open(f'{n}.html','w').write(h)
