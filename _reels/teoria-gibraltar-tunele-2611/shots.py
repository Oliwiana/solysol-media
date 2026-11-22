import json,os
from PIL import Image,ImageOps,ImageEnhance
C='_photos/commons/'
# (orig_time, file, mode, label, ill, extra)
SH=[
 (4.0,'rock-of-gibraltar/05.jpg','full','Skała Gibraltaru',0,{}),
 (6.45,'great-siege-tunnels-gibraltar/06.jpg','pol','Wnętrze Skały',0,{}),
 (7.9,'gibraltar-world-war-ii-tunnels/03.jpg','full','Gibraltar · lata 40.',0,{}),
 (10.75,'great-siege-tunnels-gibraltar/02.jpg','full','',0,{'card':['55 KM','tuneli przecina Skałę'],'cx':80,'cy':760,'cr':-2}),
 (12.9,'gibraltar-world-war-ii-tunnels/07.jpg','pol','Drążenie tuneli · II wojna',0,{}),
 (14.7,'great-siege-tunnels-gibraltar/05.jpg','full','Tunele Wielkiego Oblężenia',0,{'card':['1782','pierwsze tunele w Skale'],'cx':80,'cy':760,'cr':2}),
 (16.9,'gibraltar-harbour-warship/02.jpg','pol','Oblężenie Gibraltaru · rycina',0,{}),
 (18.75,'gibraltar-1942/06.jpg','full','',0,{'stamp':['1941',150,330,700,-8]}),
 (21.0,'gibraltar-1942/01.jpg','pol','Działo na Skale · 1942',0,{}),
 (23.2,'heinkel-he-111/04.jpg','full','Strach przed Niemcami',1,{}),
 (25.25,'file-folders-archive/05.jpg','pol','tajny plan',1,{'stamp':['TAJNE',110,330,620,-9]}),
 (26.85,'typewriter-vintage-letter/01.jpg','full','',1,{'card':['OPERACJA TRACER','1941–1942'],'cx':80,'cy':760,'cr':-1.5}),
 (28.35,'gibraltar-world-war-ii-tunnels/05.jpg','full','',0,{'card':['6 LUDZI','dowódca · 2 lekarzy<br>3 radiotelegrafistów'],'cx':80,'cy':760,'cr':2}),
 (30.3,'stethoscope-doctor-hospital/01.jpg','pol','dwóch lekarzy',1,{}),
 (31.65,'vintage-radio-microphone-1930s/03.jpg','full','trzech radiotelegrafistów',1,{}),
 (33.15,'great-siege-tunnels-gibraltar/01.jpg','pol','komora w Skale',1,{'stamp':['ZAMUROWANI',92,140,640,-10]}),
 (35.1,'jebel-musa-morocco/05.jpg','full','Cieśnina Gibraltarska',0,{}),
 (36.55,'strait-of-gibraltar-map/02.jpg','pol','meldunki o statkach',0,{}),
 (38.0,'gibraltar-world-war-ii-tunnels/01.jpg','full','',1,{'card':['7 LAT','zapasów w komorze'],'cx':80,'cy':760,'cr':-2}),
 (40.05,'typewriter-vintage-letter/02.jpg','pol','„podobno” – Ian Fleming',1,{}),
 (42.55,'file-folders-archive/03.jpg','full','',1,{'card':['007','późniejszy twórca<br>Jamesa Bonda'],'cx':80,'cy':760,'cr':1.5}),
 (44.7,'rock-of-gibraltar/06.jpg','full','',0,{'stamp':['NIGDY NIEUŻYTA',72,110,700,-8]}),
 (46.7,'st-michael-s-cave-gibraltar/04.jpg','pol','grotołazi · koniec lat 90.',0,{}),
 (48.6,'cave-stalactites-lake/04.jpg','full','',1,{'card':['LATA 90.','odkrycie komory'],'cx':80,'cy':760,'cr':-2}),
 (49.95,'archivo-legajos-documentos/04.jpg','pol','potwierdzenie lekarza',1,{'card':['2008','świadek potwierdza'],'cx':480,'cy':900,'cr':3}),
 (52.0,'great-siege-tunnels-gibraltar/03.jpg','full','Dziś: muzeum tuneli',0,{}),
 (53.7,'strait-of-gibraltar-satellite/07.jpg','full','Europa · Afryka',0,{}),
 (55.55,'barbary-macaque-gibraltar/03.jpg','pol','Makak berberyjski',0,{}),
 (57.05,'st-michael-s-cave-gibraltar/01.jpg','full','Jaskinia Św. Michała',0,{'stamp':['LEGENDA',120,260,760,-8]}),
 (58.9,'jebel-musa-morocco/02.jpg','full','',0,{}),
 (61.0,'macaca-sylvanus/06.jpg','full','',0,{}),
 (62.9,'strait-of-gibraltar-satellite/08.jpg','full','',0,{}),
 (64.1,'europa-point-lighthouse/02.jpg','full','',0,{'card':['A TY?','wierzysz?'],'cx':80,'cy':760,'cr':-2}),
]
HOOK=['rock-of-gibraltar/01.jpg','gibraltar-1942/02.jpg','gibraltar-world-war-ii-tunnels/04.jpg']
F=1.18
def prep(src,dst,maxw=1300):
    im=Image.open(C+src).convert('L');im=ImageOps.autocontrast(im,cutoff=1);im=ImageEnhance.Contrast(im).enhance(1.12);im=im.point(lambda v:int(255*((v/255)**0.8)))
    im.thumbnail((maxw,maxw*2));im.convert('RGB').save(dst,quality=85)
cred={}
def credit(path):
    d,f=path.split('/');cj=json.load(open(C+d+'/credits.json'))
    items=cj if isinstance(cj,list) else cj.get('files',cj.get('items',list(cj.values()) if isinstance(cj,dict) else []))
    for it in items:
        if isinstance(it,dict) and (it.get('file')==f or str(it.get('path','')).endswith(path) or it.get('local')==f): return it
    return {'_raw':str(cj)[:200]}
out=[];crs=[]
for k,h in enumerate(HOOK):
    prep(h,f'/tmp/gt/img/h{k}.jpg');c=credit(h);crs.append(c);out.append(('h%d'%k,h,c))
sh=[]
for k,(t,f,m,lab,ill,ex) in enumerate(SH):
    prep(f,f'/tmp/gt/img/s{k}.jpg');c=credit(f);out.append(('s%d'%k,f,c))
    s={'t':round(t/F,3),'m':m,'lab':lab,'ill':ill};s.update(ex);sh.append(s)
json.dump({'sh':sh,'cred':out},open('/tmp/gt/data.json','w'),ensure_ascii=False)
ts=[s['t'] for s in sh]+[67.0/F]
print('hook end',4.0/F,'max',max(b-a for a,b in zip(ts,ts[1:])),'min',min(b-a for a,b in zip(ts,ts[1:])),'n files',len(set(HOOK+[s[1] for s in SH])))
for o in out[:3]: print(o)
