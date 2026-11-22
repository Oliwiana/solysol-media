import sys; sys.path.insert(0,'/tmp/z9')
from genv import build
import json
O='/tmp/z9'
SPEC={
'reel':dict(segs=[(432,437),(438,446),(40,83),(304,332),(616,634)],
  hook='Ile pieniędzy wyprano <u>w Marbelli</u>?',hook_img=73,
  photos=[85,123,122,120,80,17,82,21,50,53,73,87,84,58,88,11,9,62,39,93,43,44,45,101,102],
  notes={0:'250 MLN €',4:'42 AUTA',8:'2 ODRZUTOWCE',11:'410 000 €',15:'DELAWARE',22:'14 Z 19'}),
'short1':dict(segs=[(275,359)],hook='Jak ukryć właściciela <u>willi</u>?',hook_img=162,
  photos=[160,120,39,31,30,11,10,9,94,93,88,62,89,90,98,14,181],notes={5:'DELAWARE',11:'BRAK NAZWISKA'},hook_lab='Ballena Blanca · Marbella'),
'short2':dict(segs=[(31,39),(40,99)],hook='Co policja znalazła <u>w Marbelli</u>?',hook_img=74,
  photos=[122,120,80,17,82,21,50,53,73,165,87,84,58,136,88,89],notes={2:'42 AUTA',6:'2 ODRZUTOWCE',10:'410 000 €'},hook_lab='Operacja Ballena Blanca · 2005'),
'short3':dict(segs=[(621,626),(546,601),(616,620),(627,634)],hook='Dlaczego <u>14 z 19</u> uniewinniono?',hook_img=42,
  photos=[43,44,147,148,155,33,112,45,116,117,30,101,102],notes={0:'ROK PROCESU',3:'PODSŁUCHY',8:'14 Z 19'},hook_lab='Proces Ballena Blanca'),
'short4':dict(segs=[(383,386),(387,478)],hook='Skąd pochodziły <u>te pieniądze</u>?',hook_img=175,
  photos=[177,168,108,107,104,85,172,139,87,6,5,4,2,93,89,165],notes={5:'250 MLN €',6:'500 MLN €?',7:'≈350 MLN €'},hook_lab='Ballena Blanca · Marbella'),
}
res={}
for k,s in SPEC.items():
    L,total=build(k,s['segs'],s['hook'],s['hook_img'],s['photos'],s['notes'],O,hook_lab=s.get('hook_lab','Zagadki Costa del Sol'),end2=('na YouTube · Sol y Sól' if k=='reel' else 'link pod filmem · Sol y Sól'))
    res[k]=dict(L=round(L,2),total=round(total,2),n=len(s['photos']),per=round((total-2.2)/len(s['photos']),2))
print(json.dumps(res,indent=0))
json.dump(res,open('/tmp/z9/vlen.json','w'))
