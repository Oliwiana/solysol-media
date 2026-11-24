import sys; sys.path.insert(0,'/tmp/sm/_tools')
from kolaz import FONTS,_u
N='/tmp/sm/_assets/naklejki/'
D=[('pilne','#C0281B','#F2E35B',None),('wiadomosci','#F2E35B','#E8562A','telefon.png'),('tydzien','#2F45C9','#F2E35B','zegarek.png'),
   ('zagadki','#E8562A','#141210','ksiega.png'),('gwiazdy','#9FD8C8','#E8562A','klaps.png'),('czywiesz','#141210','#E8562A','latarnia.png')]
G='<svg style="position:absolute;inset:0;opacity:.22;mix-blend-mode:multiply" width=1080 height=1920><filter id=n><feTurbulence type=fractalNoise baseFrequency=.9 numOctaves=2 stitchTiles=stitch /><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .5 0"/></filter><rect width=100% height=100% filter=url(#n) /></svg>'
for n,bg,blob,st in D:
    inner=(f'<img src="{_u(N+st)}" style="position:absolute;left:215px;top:635px;width:650px;height:650px;object-fit:contain;transform:rotate(-6deg)">' if st else
           '<div style="position:absolute;left:0;right:0;top:600px;text-align:center;font-family:AN;font-size:640px;line-height:1.1;color:#141210">!</div>')
    h=f'<!doctype html><html><head><meta charset=utf-8><style>{FONTS}*{{margin:0}}html,body{{width:1080px;height:1920px;overflow:hidden;background:{bg}}}</style></head><body><div style="position:absolute;left:170px;top:590px;width:740px;height:740px;border-radius:50%;background:{blob}"></div>{inner}{G}</body></html>'
    open(n+'.html','w').write(h)
