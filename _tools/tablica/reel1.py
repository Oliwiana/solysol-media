import json,sys
sys.path.insert(0,'/tmp/kb'); import board,page
T=json.load(open('/tmp/sm/_reels/gwiazdy-01-reel/timeline.json'))
caps=[[[w['w'],w['a'],w['b']] for w in c] for c in T['chunks']]
S=dict(beats=[
 dict(k='head',t=3.21,a='MARBELLA',b='1946',tb=4.35),
 dict(k='photo',t=5.75,f='rolls-royce-phantom/05',cap='Rolls-Royce Phantom',sub=dict(f='rolls-royce-phantom/03',cap='W drodze na południe',t=7.3)),
 dict(k='sticker',t=6.3,text='→ KSIĄŻĘ MAX HOHENLOHE I SYN',dy=-30,x=60),
 dict(k='photo',t=9.31,f='marbella-1950s/02',cap='Marbella – dawniej'),
 dict(k='stamp',t=10.25,text='RYBACKA WIOSKA',dx=520,dy=30),
 dict(k='photo',t=11.43,f='torre-ladrones-marbella/02',cap='Sosny i pusta plaża',sub=dict(f='marbella-beach/03',cap='Morze',t=12.3)),
 dict(k='note',t=13.42,lab='Rok później wraca syn:',text='ALFONSO · 1947',tt=14.2,td=1.0,h=260),
 dict(k='photo',t=16.4,f='fig-tree-andalusia/01',cap='Figi i sosny',sub=dict(f='fig-tree-andalusia/02',cap='Stara finca',t=17.4)),
 dict(k='photo',t=18.72,f='marbella-club-hotel/02',cap='Ogrody dawnej finki'),
 dict(k='stamp',t=19.4,text='SANTA MARGARITA',dx=600,dy=30,fs=44),
 dict(k='photo',t=20.44,f='marbella-club-hotel/01',cap='Marbella Club',sub=dict(f='marbella-club-hotel/05',cap='Wejście do hotelu',t=21.6)),
 dict(k='stamp',t=22.3,text='OTWARTY · 1954',dx=480,dy=40),
 dict(k='count',t=24.55,title='HOTEL NA START',n=20,unit='pokoi'),
 dict(k='sticker',t=27.6,text='NAZWA? MARBELLA CLUB',dy=-30),
 dict(k='note',t=28.57,text='I tu robi się ciekawie…',tt=28.7,td=1.2,h=200,fs=58),
 dict(k='photo',t=30.56,f='venice-grand-canal/01',cap='Wenecja · 1955',sub=dict(f='venice-wedding-gondola/03',cap='Wenecja',t=31.8)),
 dict(k='note',t=33.04,lab='Panna młoda:',text='księżniczka Ira von Fürstenberg',tt=33.5,td=1.0,h=300),
 dict(k='sticker',t=35.3,text='→ MÓWI O NICH CAŁA EUROPA',dy=-30,x=200),
 dict(k='photo',t=36.83,f='marbella-beach/05',cap='Do Marbelli zjeżdżają gwiazdy',sub=dict(f='hollywood-sign/02',cap='Hollywood',t=38.0)),
 dict(k='list',t=39.43,title='LISTA GOŚCI',items=[('Ava Gardner',39.5),('Grace Kelly',40.3),('Audrey Hepburn',41.0),('Brigitte Bardot',42.5)]),
 dict(k='photo',t=44.13,f='sierra-blanca-marbella/05',cap='Marbella',sub=dict(f='nagueles-marbella/01',cap='Wybrzeże',t=45.0)),
 dict(k='dark',t=45.6,lab='Zdaniem redakcji:',text='to tu narodziła się Marbella, jaką znamy.',tt=46.0,td=1.6,h=320),
 dict(k='sticker',t=47.75,text='KOGO CHCIAŁBYŚ TAM SPOTKAĆ? NAPISZ W KOMENTARZU',dy=-20,x=110,fs=40),
 dict(k='photo',t=50.63,f='hotel-marbella-club-marbella-m-laga/03',cap='Marbella Club dziś',sub=dict(f='milla-de-oro-marbella/03',cap='Złota Mila',t=51.5)),
 dict(k='photo',t=52.31,f='rolls-royce-phantom/02',cap='Tu wszystko się zaczęło'),
])
els,strings,cams,js,creds,BH=board.build(S,'/tmp/kb')
open('/tmp/kb/index.html','w').write(page.page(els,strings,cams,js,creds,BH,caps,'hook.jpg','Obserwuj @solysol.pl','GWIAZDY NA COSTA DEL SOL',endT=54.8,hook_end=3.0))
print('ok',BH,len(creds))
