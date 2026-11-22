import json, os
R='/home/claude/solysol-media/_photos/commons/'
SP=1.07
# (start_orig, photo, rot, card_html or None)
S=[
(0.0,'macaca-sylvanus/05.jpg',0,'HOOK'),
(2.1,'rock-of-gibraltar/01.jpg',-2,'<b>GIBRALTAR</b><span>II wojna światowa</span>'),
(3.68,'gibraltar-1942/02.jpg',2,None),
(5.5,'gibraltar-1942/01.jpg',-1.5,None),
(7.2,'gibraltar-upper-rock/06.jpg',1.5,'<i>Legenda:</i><b>gdy znikną małpy, znikną Brytyjczycy</b>'),
(8.9,'rock-of-gibraltar/05.jpg',-2,None),
(10.0,'gibraltar-main-street/02.jpg',2,None),
(11.6,'barbary-macaque-gibraltar/02.jpg',-1.5,'<b>JEDYNE</b><span>dzikie małpy w Europie</span>'),
(13.5,'treaty-of-utrecht-1713/02.jpg',1.5,'<b>1713</b><span>traktat z Utrechtu</span>'),
(15.2,'rock-of-gibraltar/04.jpg',-1,None),
(16.7,'gibraltar-1942/03.jpg',2,'<b>1939–1945</b>'),
(18.4,'gibraltar-world-war-ii-tunnels/04.jpg',-2,None),
(19.8,'macaca-sylvanus/01.jpg',1.5,'<i>zostało ok.</i><b class=big>7</b>'),
(21.0,'great-siege-tunnels-gibraltar/02.jpg',-1.5,None),
(22.8,'typewriter-old/03.jpg',2,'<b>WRZESIEŃ 1944</b>'),
(24.2,'typewriter-vintage-letter/01.jpg',-2,None),
(25.5,'file-folders-archive/03.jpg',1.5,'<i>Winston Churchill</i><b>notatka do ministra kolonii</b>'),
(27.0,'archivo-legajos-documentos/04.jpg',-1.5,None),
(28.4,'typewriter-old/04.jpg',1,'QUOTE'),
(30.85,'strait-of-gibraltar-map/02.jpg',-2,'<b>AFRYKA PŁN.</b><span>nowe samice</span>'),
(32.0,'atlas-mountains-morocco-forest/05.jpg',2,None),
(33.4,'gibraltar-1942/05.jpg',-1.5,'<b>ARMIA</b><span>opiekunem małp</span>'),
(35.2,'barbary-macaque-gibraltar/05.jpg',1.5,'<i>małpy miały</i><b>własnego sierżanta</b>'),
(36.5,'gibraltar-ape-baby/01.jpg',-2,'<b>JEDZENIE</b><span>w wojskowym budżecie</span>'),
(38.3,'great-siege-tunnels-gibraltar/05.jpg',2,None),
(40.0,'gibraltar-upper-rock/05.jpg',-1,'<i>wojsko oddało je</i><b>1991–1992</b>'),
(41.3,'macaca-sylvanus/04.jpg',1.5,'<i>dziś</i><b class=big>200+</b>'),
(43.1,'rock-of-gibraltar/05.jpg',0,'VERDICT'),
(45.3,'treaty-of-utrecht-1713/04.jpg',0,'VERDICT'),
(47.2,'macaca-sylvanus/02.jpg',-1.5,'<i>ale Churchill</i><b>wolał nie sprawdzać</b>'),
(49.2,'barbary-macaque-gibraltar/03.jpg',0,'ASK'),
(51.5,'rock-of-gibraltar/04.jpg',0,'END'),
]
END=53.2
words=[]
for it in open('/tmp/mk/words.txt').read().strip().split('|'):
    w,t=it.rsplit(' ',1); words.append([w,round(float(t)/SP,3)])
YEL={'Siedem','małp.','śmiertelnie','legenda:','Skały','Brytyjczycy.','jedyne','dzikie','trzystu','kilka.','dziwnie.','czterdziesty','czwarty.','Churchill','dwadzieścia','cztery.','Afryki','Północnej','samice.','armia.','sierżanta','budżecie.','dziewięćdziesiątych.','dwieście.','Mit.','traktaty,','sprawdzać.','wierzysz?','komentarzu.'}
# chunk captions: break at punctuation or 4 words
chunks=[];cur=[]
for w,t in words:
    cur.append([w,t,w in YEL])
    if w[-1] in '.,?:' or len(cur)>=4 or w=='–':
        chunks.append(cur);cur=[]
if cur: chunks.append(cur)
for i,c in enumerate(chunks):
    c_end = chunks[i+1][0][1] if i+1<len(chunks) else 49.0
    for x in c: pass
    chunks[i]={'s':c[0][1],'e':c_end,'w':[[x[0].rstrip(':'),x[1],x[2]] for x in c]}
shots=[]
for i,(s,p,r,card) in enumerate(S):
    e = S[i+1][0] if i+1<len(S) else END
    shots.append({'s':round(s/SP,3),'e':round(e/SP,3),'p':'file://'+R+p,'r':r,'c':card,'k':p})
json.dump({'shots':shots,'caps':chunks,'dur':round(END/SP,2)},open('/tmp/mk/data.json','w'),ensure_ascii=False)
mx=max(x['e']-x['s'] for x in shots); print(len(shots),len(set(s[1] for s in S)),'maxshot',mx,'dur',END/SP)
# credits
cr={}
for s in S:
    d,f=s[1].split('/'); c=([x for x in json.load(open(R+d+'/credits.json')) if x['file']==f] or [{'author':'??','license':'??'}])[0]
    cr[s[1]]=c
json.dump(cr,open('/tmp/mk/credits.json','w'),ensure_ascii=False,indent=1)

CR={k:(v['author'].split('\n')[0].replace('This Photo was taken by ','').rstrip('. ')[:50]+' / Wikimedia Commons, '+v['license']) for k,v in cr.items()}
h=open('/tmp/mk/index.html').read().replace('__DATA__',json.dumps({'shots':shots,'caps':chunks},ensure_ascii=False)).replace('__CR__',json.dumps(CR,ensure_ascii=False))
open('/tmp/mk/page.html','w').write(h)
