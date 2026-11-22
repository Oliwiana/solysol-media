import json
R='/home/claude/solysol-media/_photos/commons/'
T='/home/claude/solysol-media/_tts/'
SP=1.25
# (start_orig, photo, rot, card)
S=[
(0.0,'T:ufo-UFO-1.jpg',0,'HOOK'),
(3.0,'radar-military-antenna/03.jpg',-2,'<i>Krąży teoria:</i><b>armia ma dowody</b>'),
(5.6,'radar-military-antenna/02.jpg',2,None),
(7.3,'T:ufo-night--10.jpg',-1.5,'<b>OBCE STATKI?</b>'),
(8.4,'night-sea-waves/01.jpg',1.5,'<b>10.08.1989</b><span>wieczór nad wybrzeżem</span>'),
(10.4,'T:ufo-night--17.jpg',-2,None),
(12.4,'puerto-deportivo-de-estepona/01.jpg',2,'<b>ESTEPONA · KADYKS</b>'),
(14.2,'sevilla-triana-night/02.jpg',-1.5,'<b>SEWILLA</b>'),
(16.5,'stratospheric-balloon/04.jpg',1.5,'<b>JASNA KULA</b><span>tysiące świadków</span>'),
(18.6,'rotary-telephone/03.jpg',-2,'<i>lotnisko w Sewilli:</i><b>urywają się telefony</b>'),
(21.44,'eclipse-solar/05.jpg',2,'<i>nagle</i><b>dzieli się na dwa</b>'),
(24.72,'stratospheric-balloon/03.jpg',-1.5,'<b>WYJAŚNIENIE?</b>'),
(26.3,'T:ufo-strato-2.jpg',1.5,'<b>BALON</b><span>stratosferyczny</span>'),
(28.3,'sicily-trapani/01.jpg',-2,'<i>z Sycylii</i><b>do prowincji Sewilla</b>'),
(31.28,'file-folders-archive/03.jpg',2,'<b>TAJNE AKTA?</b>'),
(33.2,'typewriter-old/03.jpg',-1.5,'<b>2016</b><span>ministerstwo obrony</span>'),
(35.2,'archivo-legajos-documentos/04.jpg',1.5,None),
(37.0,'file-folders-archive/05.jpg',-2,'<i>raporty o UFO</i><b class=big>80</b>'),
(38.96,'archivo-legajos-documentos/03.jpg',2,'<i>stron</i><b class=big>1900+</b>'),
(41.2,'file-folders-archive/06.jpg',-1.5,'<b>1962–1995</b>'),
(43.5,'typewriter-vintage-letter/01.jpg',1.5,None),
(45.68,'mor-n-air-base/01.jpg',-2,'<b>MORÓN</b><span>baza pod Sewillą</span>'),
(47.4,'stratospheric-balloon/01.jpg',2,'<i>pilot widzi</i><b>owalny, szary obiekt</b>'),
(49.3,'malaga-airport-control-tower/01.jpg',-1.5,None),
(51.1,'T:ufo-strato-3.jpg',1.5,'<b>ODLATUJE I ZNIKA</b>'),
(53.28,'shredded-paper-documents/01.jpg',-2,'<b>NOWSZE AKTA?</b>'),
(55.4,'file-folders-archive/02.jpg',2,'<i>wojsko trzyma je jako</i><b>POUFNE</b>'),
(57.28,'eclipse-solar/02.jpg',0,'VERDICT'),
(59.5,'typewriter-old/04.jpg',0,'VERDICT'),
(61.2,'T:ufo-radar--15.jpg',-1.5,'<i>niewyjaśnione</i><b>≠ kosmiczne</b>'),
(64.16,'mediterranean-sea-night/01.jpg',0,'ASK'),
(66.9,'eclipse-solar/01.jpg',0,'END'),
]
END=69.4
TC={  # credits for _tts files (from original record)
'ufo-UFO-1.jpg':{'author':'George Stock','license':'Public domain','source':'https://commons.wikimedia.org/wiki/File:Supposed_UFO,_Passaic,_New_Jersey.jpg'},
'ufo-night--10.jpg':{'author':'Gaudencio Garcinuño','license':'CC BY-SA 2.0','source':'https://commons.wikimedia.org/wiki/File:Startrails_(4984557938).jpg'},
'ufo-night--17.jpg':{'author':'NASA Johnson Space Center','license':'Public domain','source':'https://commons.wikimedia.org/wiki/File:Night_Lights_Along_the_Mediterranean_Sea_(iss072e000922).jpg'},
'ufo-strato-2.jpg':{'author':'NASA Goddard','license':'Public domain','source':'https://commons.wikimedia.org/wiki/File:High-altitude-balloon-1041.jpg'},
'ufo-strato-3.jpg':{'author':'Naval Information Warfare Center Pacific','license':'Public domain','source':'https://commons.wikimedia.org/wiki/File:Aerostar_Stratospheric_Balloon_Carrying_the_SOLD_Payload.jpg'},
'ufo-radar--15.jpg':{'author':'NASA','license':'Public domain','source':'https://commons.wikimedia.org/wiki/File:C-band_Radar-dish_Antenna.jpg'},
}
W=json.load(open(T+'teoria-ufo-andaluzja-1712-words.json'))['words']
words=[[x['text'],round(x['start']/SP,3)] for x in W if x['type']=='word']
YEL={'UFO','Andaluzją?','dowody','obce','statki','Dziesiąty','sierpnia','jasna','kula.','Tysiące','telefony.','dwa','znika.','balon','stratosferyczny,','Sycylii.','tajne','akta?','osiemdziesiąt','raportów','tysiąc','dziewięćset','stron,','Morón','owalny,','szary','poufne.','częściowo','prawda.','istnieją.','kosmiczne.','wierzysz?','komentarzu.'}
chunks=[];cur=[]
for w,t in words:
    cur.append([w,t,w in YEL])
    if w[-1] in '.,?:' or len(cur)>=4:
        chunks.append(cur);cur=[]
if cur: chunks.append(cur)
for i,c in enumerate(chunks):
    c_end=chunks[i+1][0][1] if i+1<len(chunks) else c[-1][1]+1.2
    chunks[i]={'s':c[0][1],'e':c_end,'w':[[x[0].rstrip(':'),x[1],x[2]] for x in c]}
def path(p): return (T+p[2:]) if p.startswith('T:') else R+p
shots=[]
for i,(s,p,r,card) in enumerate(S):
    e=S[i+1][0] if i+1<len(S) else END
    shots.append({'s':round(s/SP,3),'e':round(e/SP,3),'p':'file://'+path(p),'r':r,'c':card,'k':p})
cr={}
for s in S:
    p=s[1]
    if p.startswith('T:'): c=TC[p[2:]]
    else:
        d,f=p.split('/'); c=[x for x in json.load(open(R+d+'/credits.json')) if x['file']==f][0]
    cr[p]={'author':c['author'].split('\n')[0].replace('This Photo was taken by ','').rstrip('. ')[:60],'license':c['license'],'source':c['source']}
json.dump(cr,open('/tmp/mk/credits.json','w'),ensure_ascii=False,indent=1)
CR={k:(v['author'][:50]+' / Wikimedia Commons, '+v['license']) for k,v in cr.items()}
dur=round(END/SP,2)
D={'shots':shots,'caps':chunks,'hookEnd':round(3.0/SP,3)}
h=open('/tmp/mk/index.html').read().replace('__DATA__',json.dumps(D,ensure_ascii=False)).replace('__CR__',json.dumps(CR,ensure_ascii=False))
open('/tmp/mk/page.html','w').write(h)
lens=[x['e']-x['s'] for x in shots]
print('shots',len(shots),'unique',len(set(s[1] for s in S)),'max',round(max(lens),2),'min',round(min(lens),2),'dur',dur)
