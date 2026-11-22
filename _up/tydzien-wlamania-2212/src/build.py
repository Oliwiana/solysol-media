import json,os
from PIL import Image
S='/tmp/claude-0/-home-claude-solysol-media/98892a6c-d95e-562c-bf4b-9e84c4d82712/scratchpad'
C='/home/claude/solysol-media/_photos/commons/'
F=1.1
shots=[(0,'marbella-night/01',None),(2.9,'prison-bars/01',None),(4.4,'polic-a-nacional-spain/01','60% 50%'),(6.1,'gibralfaro-m-laga-vista/02',None),
(7.9,'marbella-villa/03',None),(9.6,'prison-bars/02',None),(11.4,'marbella-villa/02','50% 70%'),(13.2,'bricked-up-window-abandoned-house-spain/01',None),
(15.6,'underground-car-park-spain/06',None),(17.6,'file-folders-archive/03',None),(19.6,'gibralfaro-m-laga-vista/04',None),(20.4,'mijas-pueblo/01',None),
(21.1,'torre-de-maro-nerja/02',None),(21.9,'guardia-civil-patrol-car/03',None),(24.4,'milla-de-oro-marbella/04',None),(26.6,'luxury-villa-swimming-pool/01',None),
(28.4,'marbella-villa/04',None),(30.3,'balaclava/03','50% 30%'),(31.9,'handcuffs/03',None),(33.5,'handcuffs/02',None),(35.6,'polic-a-nacional-spain-car/03',None),
(37.4,'luxury-watches-display/04',None),(39.6,'luxury-watches-display/02',None),(41.4,'marbella-night/03',None),(43.0,'luxury-watches-display/01',None),
(45.2,'euro-banknotes/04',None),(47.9,'marbella-christmas-lights/02',None),(50.1,'malaga-airport-night/05',None),(51.9,'key-lock-box/03',None),
(54.2,'key-lock-box/01',None),(56.6,'yacht-marina-night/01',None),(58.4,'puerto-banus-night/03',None)]
KB=[[0,0,1.05,-25,-35,1.17],[-20,10,1.16,20,-20,1.06],[10,-20,1.06,-30,20,1.18],[0,30,1.18,0,-30,1.07]]
END_T=61.2
P=[];cred={};os.makedirs(S+'/wl/p',exist_ok=True)
for i,(st,f,pos) in enumerate(shots):
  en=shots[i+1][0] if i+1<len(shots) else END_T
  d,fn=f.split('/');src=f'p/{i:02d}.jpg'
  im=Image.open(C+f+'.jpg').convert('RGB');im.thumbnail((1500,2200));im.save(S+'/wl/'+src,quality=85)
  p={'src':src,'start':round(max(0,st/F-0.15 if i else 0),3),'end':round(en/F,3),'kb':KB[i%4]}
  if pos:p['pos']=pos
  P.append(p)
  for c in json.load(open(C+d+'/credits.json')):
    if c['file']==fn+'.jpg':cred[f]=c
W=json.load(open('/home/claude/words.json'))
W=[[w['text'],round(w['start']/F,3),round(w['end']/F,3)] for w in W]
W=[w for w in W if w[1]<56.7/F]   # "Obserwuj Sol y Sól..." – plansza końcowa
s=lambda x:round(x/F,3)
CARDS=[['c1',s(4.44),s(7.9),[['c1b',s(5.08)]]],['c2',s(7.94),s(13.1)],['c3',s(13.22),s(17.5),[['c3b',s(15.76)]]],
['c4',s(17.72),s(21.9),[['w0',s(19.64)],['w1',s(20.4)],['w2',s(21.16)]]],['c5',s(21.96),s(26.6)],['c6',s(26.78),s(30.3)],['c7',s(30.42),s(33.5)],
['c8',s(33.62),s(39.7)],['c9',s(39.8),s(43.0)],['c10',s(43.14),s(48.0)],['c11',s(48.14),s(56.6),[['k0',s(50.22)],['k1',s(51.96)],['k2',s(54.28)]]]]
open(S+'/wl/data.js','w').write('window.PHOTOS='+json.dumps(P)+';window.WORDS='+json.dumps(W,ensure_ascii=False)+';window.CARDS='+json.dumps(CARDS)+f';window.END={s(56.7)};')
json.dump(cred,open(S+'/cred.json','w'),ensure_ascii=False,indent=1)
print(len(P),'shots, distinct files',len(set(x[1] for x in shots)),'max dur',max(p['end']-p['start'] for p in P[:-2]))
