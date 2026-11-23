import json,sys,re
sys.path.insert(0,'/tmp/kb'); sys.path.insert(0,'/tmp/ks')
import board,page
from shots import S
T=json.load(open('/tmp/ks/tl.json')); P=T['paras']; off=T['off']
tr=json.load(open('/tmp/ks/tr.json'))
# captions chunks from transcript (display words, original spelling)
import scen
def disp(n): 
    return scen.part(n).split()
caps=[]
for n in range(3):
    ws=[w for w in tr[n]['words'] if w['type']=='word']; dw=disp(n+1)
    if len(dw)!=len(ws): print('wc mismatch',n,len(dw),len(ws))
    cur=[]
    for i,w in enumerate(ws):
        txt=dw[i] if len(dw)==len(ws) else w['text']
        cur.append([txt,round(w['start']+off[n],2),round(w['end']+off[n],2)])
        if len(cur)>=6 or re.search(r'[.?!:]$',txt): caps.append(cur);cur=[]
    if cur: caps.append(cur)
chap={'Syn księcia':('Rozdział 1','Syn księcia · Madryt 1924'),'Dwadzieścia pokoi':('Rozdział 2','Dwadzieścia pokoi · 1954'),'Ślub w Wenecji':('Rozdział 3','Ślub w Wenecji · 1955'),'Hrabia Rudi':('Rozdział 4','Hrabia Rudi · 1956'),'Gwiazdy przyjeżdżają':('Rozdział 5','Gwiazdy przyjeżdżają'),'Ostatnie lata':('Rozdział 6','Ostatnie lata · Ronda'),'Zakończenie':('Epilog','70 lat później · 2024')}
extra={8:[dict(k='count',title='MARBELLA CLUB · 1954',n=20,unit='pokoi')],
 10:[dict(k='note',lab='Panna młoda:',text='księżniczka Ira von Fürstenberg, 15 lat',h=300)],
 16:[dict(k='list',title='GOŚCIE KLUBU',items=['Ava Gardner','Audrey Hepburn','Brigitte Bardot'])],
 9:[dict(k='dark',lab='Zdaniem redakcji:',text='to miał być klub dla znajomych.',h=300)],
 21:[dict(k='dark',lab='Zdaniem redakcji:',text='pierwszy zobaczył w rybackiej wiosce coś więcej.',h=320)],
 23:[dict(k='dark',lab='Zdaniem redakcji:',text='to tu narodziła się Marbella, jaką znamy.',h=320)]}
beats=[dict(k='head',t=1.5,a='MARBELLA',b='1946',tb=2.6)]
for i,(p,shots) in enumerate(zip(P,S)):
    t0=p['t']; span=p['end']-t0
    items=[]
    if p['first'] and p['ch'] in chap:
        a,b=chap[p['ch']]; items.append(dict(k='dark',lab=a,text=b,h=260,fs=60))
    if i==3: items=[dict(k='dark',lab='Gwiazdy na Costa del Sol · odcinek 1',text='Książę, który wymyślił Marbellę',h=330,fs=66)]
    if i==24: items=[]
    ph=[s for s in shots]
    # pair photos: main + sub
    j=0
    while j<len(ph):
        f,c,y=ph[j]; it=dict(k='photo',f=f,cap=c or 'Marbella')
        if j+1<len(ph): it['sub']=dict(f=ph[j+1][0],cap=ph[j+1][1] or 'Marbella'); j+=2
        else: j+=1
        items.append(it)
        if y: items.append(dict(k='stamp',text=str(y),fs=70,dx=330,dy=40))
    for e in extra.get(i,[]): items.insert(1 if items and items[0]['k']=='dark' and i not in(9,21,23) else len(items),e)
    big=[x for x in items if x['k']!='stamp']; n=len(big); q=0
    for x in items:
        if x['k']=='stamp': x['t']=round(last+1.0,2)
        else:
            x['t']=round(t0+span*q/n+(0.3 if q==0 and x['k']!='dark' else 0),2); last=x['t']
            if x.get('sub'): x['sub']['t']=round(x['t']+min(2.5,span/n*0.45),2)
            if x['k'] in('note','dark'): x['tt']=round(x['t']+0.4,2); x['td']=min(2.0,span/n*0.5)
            if x['k']=='list': x['items']=[(nm,round(x['t']+0.6+k*1.2,2)) for k,nm in enumerate(x['items'])]
            q+=1
        beats.append(x)
els,strings,cams,js,creds,BH=board.build(dict(beats=beats,y0=200),'/tmp/kb/L',Wd=1920,Hd=1080)
open('/tmp/kb/L/index.html','w').write(page.page(els,strings,cams,js,creds,BH,caps,'hook.jpg','Subskrybuj @solysolpl','GWIAZDY NA COSTA DEL SOL · ODCINEK 1',Wd=1920,Hd=1080,endT=P[24]['t']+0.5,hook_end=-1,yt=False))
json.dump(sorted(set(creds)),open('/tmp/kb/L/creds.json','w'),ensure_ascii=False)
print(len(beats),BH,len(creds))
