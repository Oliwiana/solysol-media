# cover.py <id> <photo> <pos> <head> <teaser> <box1label> <box1title> <seal1> <seal2> <seal3> <person> <credit>
import sys; sys.path.insert(0,'/home/claude/solysol-media/_tools'); from barwna import cover
a=sys.argv[1:]; id,photo,pos,head,teaser,b1l,b1t,s1,s2,s3,person,credit=a
h=cover('file:///home/claude/solysol-media/_photos/commons/'+photo,pos=pos,credit=credit,head=head,teaser=teaser,desk='GWIAZDY NA COSTA DEL SOL',
  mast='SERIA SPECJALNA',date='REELS',box1=[b1l,b1t],seal=[s1,s2,s3],hsize=100,htop=1210,btop=640,stop=1000)
h=h.replace('height:1350px','height:1920px').replace('left:64px;right:64px;top:40px;text-align:center','left:64px;right:64px;top:300px;text-align:center')
h=h.replace('<span>PRZESUŃ  →</span>','<span>▶ REELS</span>').replace('bottom:22px;display:flex','bottom:300px;display:flex')
fr0=1
fr=f'<div style="position:absolute;right:64px;top:630px;width:400px;height:380px;border:5px dashed #F2C14E;background:rgba(10,20,34,.55);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transform:rotate(2deg)"><div style="font-weight:800;font-size:30px;letter-spacing:.06em;color:#F2C14E;line-height:1.15">ZDJĘCIE –<br>DODA REDAKCJA</div><div style="font-family:CG;font-style:italic;font-size:34px;margin-top:14px;padding:0 20px">{person}</div></div>'
h=h.replace('right:58px;top:1000px','left:90px;top:840px').replace('height:470px','height:380px')
h=h.replace('</body>',fr+'</body>')
# winieta-gradient rozciągnięty
open(f'/home/claude/gw/{id}/cover.html','w').write(h)
