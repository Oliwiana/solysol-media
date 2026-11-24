import json
C='/tmp/sm/_photos/commons/'
def cr(p, ilu=False):
    c=[x for x in json.load(open(C+p.split('/')[0]+'/credits.json')) if x['file']==p.split('/')[1]][0]
    s=f"Fot. {c['author']} / Wikimedia Commons, {c['license']}"
    return s+(' · zdjęcie ilustracyjne' if ilu else '')
EPS=[('ODC. 1','Marbella Club i książę Alfonso'),('ODC. 2','Hemingway w Churrianie'),('ODC. 3','Torremolinos i hotel Pez Espada'),('ODC. 4','Banderas i Málaga'),('ODC. 5','Andersen w Maladze')]
def eps(k): return [[a,b,i<k-1] for i,(a,b) in enumerate(EPS) if i>=k][:3] or [[a,b,True] for a,b in EPS[:3]]
def more(k):
    nxt=[(a,b) for i,(a,b) in enumerate(EPS) if i>=k]
    if not nxt: nxt=[(a.replace('ODC.','BYŁO: ODC.'),b) for a,b in EPS[1:4]]
    return [[a,b.replace(' i ',' i<br>',1) if len(b)>22 else b] for a,b in nxt[:3]]
NOTE='Źródła sprawdzone 22.11.2026 (min. 2 niezależne na fakt) – lista w opisie posta w aplikacji. Tekst własny redakcji.'
P={}
# ---------- 1 ----------
P[1]=dict(ep=1,date='28.11.2026',cover=dict(photo='marbella-club-hotel/01.jpg',pos='20% 80%',credit=cr('marbella-club-hotel/01.jpg'),
 head='Jak książę <i>wymyślił Marbellę</i>',teaser='Rolls-Royce, rodzinna finca i 20 pokoi, które ściągnęły gwiazdy',desk='GWIAZDY NA COSTA DEL SOL · ODC. 1',
 box1=['CZY WIESZ, ŻE…','Marbella Club otworzył się w 1954 r. z 20 pokojami'],box2=['KTO TU PRZYJEŻDŻAŁ?','AVA, GRACE I AUDREY','w jednym ogrodzie nad morzem'],
 framenote='Książę Alfonso von Hohenlohe (archiwum)',more=more(1)),
 slides=[
 dict(kicker='1946 · PODRÓŻ NA POŁUDNIE',head='Rolls-Royce <i>na drodze do Marbelli</i>',frame='Książę Max lub Alfonso von Hohenlohe – zdjęcie archiwalne',
  body=['W 1946 r. niemiecki arystokrata, książę <b>Max von Hohenlohe</b>, wyruszył Rolls-Royce’em na południe Hiszpanii. Gdzieś na wybrzeżu przy Marbelli podróż się zatrzymała – i to był początek legendy.',
        'Jego syn, książę <b>Alfonso</b>, wrócił tu i kupił posiadłość <b>Santa Margarita</b> – wiejski dom wśród pinii, tuż przy plaży. Marbella była wtedy cichą wioską rybacką.']),
 dict(kicker='1954 · OTWARCIE',head='Z domu dla rodziny <i>– hotel dla świata</i>',photo='marbella-club-hotel/04.jpg',credit=cr('marbella-club-hotel/04.jpg'),pos='50% 55%',
  body=['Rodzinna posiadłość zmieniła się w hotel. W <b>1954 r.</b> ruszył <b>Marbella Club</b>: <b>20 pokoi</b>, jadalnia i bar w starym wiejskim domu.',
        'Zdaniem redakcji to był pomysł genialny w swojej prostocie: nie wielki hotel, tylko dom, do którego „wypada” przyjechać.']),
 dict(kicker='KTO TU BYWAŁ',head='Gwiazdy <i>w ogrodzie księcia</i>',frame='Kolaż: Ava Gardner, Grace Kelly, Audrey Hepburn',
  body=['W ogrodach klubu wypoczywały <b>Ava Gardner</b>, <b>Grace Kelly</b> i <b>Audrey Hepburn</b>. Gościem bywała też Brigitte Bardot.',
        'Zdaniem redakcji tak z jednej posiadłości zrobił się magnes: Marbella zaczęła się kojarzyć z luksusem, zanim powstała tu większość dzisiejszych willi.']),
 dict(type='numbers',kicker='W LICZBACH',head='Marbella Club <i>w 4 liczbach</i>',rows=[['1946','podróż księcia Maxa na południe Hiszpanii'],['1954','otwarcie Marbella Club'],['20','pokoi na start – w dawnym domu rodziny'],['70','lat hotel świętował w 2024 r.']]),
 dict(type='where',head='Bulwar <i>imienia księcia</i>',photo='marbella-club-hotel/03.jpg',credit=cr('marbella-club-hotel/03.jpg'),pos='50% 50%',y=600,
  rows=[['ADRES','Bulevar Príncipe Alfonso von Hohenlohe s/n, Marbella – ulica nosi imię założyciela'],['CO DZIŚ','Hotel działa do dziś, z beach clubem nad morzem'],['ZDANIEM REDAKCJI','Najprościej poczuć klimat, rezerwując stolik w restauracji hotelu – albo spacerując bulwarem do morza']]),
 dict(type='cta',sub='Kolejne odcinki serii – historie gwiazd i miejsc, które możesz dziś odwiedzić',eps=eps(1),note=NOTE)])
# ---------- 2 ----------
P[2]=dict(ep=2,date='05.12.2026',cover=dict(photo='churriana-m-laga/01.jpg',pos='50% 50%',credit=cr('churriana-m-laga/01.jpg',True),
 head='Ostatnie <i>wielkie lato</i> Hemingwaya',teaser='Churriana 1959: corrida, fajerwerki i 60. urodziny noblisty',desk='GWIAZDY NA COSTA DEL SOL · ODC. 2',
 box1=['CZY WIESZ, ŻE…','Na urodziny noblisty szampan przyleciał z Francji'],box2=['KTO TU MIESZKAŁ?','NOBLISTA W CHURRIANIE','lato 1959, La Cónsula'],
 framenote='Ernest Hemingway, 1959 (archiwum)',more=more(2)),
 slides=[
 dict(kicker='1 MAJA 1959 · ALGECIRAS',head='Noblista <i>schodzi ze statku</i>',frame='Ernest Hemingway – zdjęcie archiwalne z 1959 r.',
  body=['<b>1 maja 1959 r.</b> do portu w Algeciras wpływa liniowiec „Constitution”. Na pokładzie <b>Ernest Hemingway</b> z żoną <b>Mary Welsh</b>.',
        'Zamieszkają w <b>La Cónsuli</b> – posiadłości Amerykanów <b>Billa i Annie Davisów</b> w <b>Churrianie</b>, dziś dzielnicy Málagi. Spędzą tu całe lato.']),
 dict(kicker='MANO A MANO',head='Dwóch torreadorów, <i>jeden pisarz</i>',frame='Hemingway na corridzie – zdjęcie archiwalne',
  body=['Latem 1959 r. Hiszpania żyje pojedynkiem dwóch torreadorów: <b>Antonio Ordóñeza</b> i <b>Luisa Miguela Dominguína</b> – szwagrów i rywali.',
        'Hemingway śledzi ten pojedynek z bliska. Magazyn „Life” zamówił u niego reportaż – z tego materiału powstanie potem książka.']),
 dict(kicker='LIPIEC 1959 · 60. URODZINY',head='Przyjęcie <i>na 60. urodziny</i>',frame='Hemingway w La Cónsuli, lato 1959 – zdjęcie archiwalne',
  body=['Hemingway urodził się 21 lipca 1899 r., więc tego lata kończył <b>60 lat</b>. Davisowie wydali dla niego przyjęcie w La Cónsuli.',
        '<b>Szampan z Francji, jedzenie z Londynu</b>, pokaz fajerwerków, budki jak na jarmarku i orkiestra na żywo. Wśród gości – torreador <b>Antonio Ordóñez</b>.']),
 dict(type='numbers',kicker='W LICZBACH',head='Lato w Churrianie <i>w 4 liczbach</i>',rows=[['1959','lato Hemingwaya w La Cónsuli'],['60','urodziny świętowane w Churrianie'],['2','torreadorów w pojedynku mano a mano'],['1985','wydanie „Niebezpiecznego lata” – już po śmierci autora']]),
 dict(type='where',head='La Cónsula <i>dziś</i>',photo='churriana-m-laga/01.jpg',credit=cr('churriana-m-laga/01.jpg',True),pos='50% 70%',y=600,
  rows=[['GDZIE','Churriana – dzielnica Málagi, przy drodze do Alhaurín de la Torre'],['CO DZIŚ','W dawnej posiadłości Davisów działa szkoła hotelarsko-gastronomiczna (Escuela de Hostelería La Cónsula)'],['W CHURRIANIE','Mieszkał tu też pisarz Gerald Brenan – Hemingway odwiedził go pod koniec maja 1959 r.'],['DO CZYTANIA','„Niebezpieczne lato” – Hemingway o sezonie 1959']]),
 dict(type='cta',sub='Kolejne odcinki serii – historie gwiazd i miejsc, które możesz dziś odwiedzić',eps=eps(2),note=NOTE)])
# ---------- 3 ----------
P[3]=dict(ep=3,date='12.12.2026',cover=dict(photo='hotel-pez-espada-torremolinos/01.jpg',pos='50% 40%',credit=cr('hotel-pez-espada-torremolinos/01.jpg'),
 head='Torremolinos, <i>gdzie nocowało kino</i>',teaser='Hotel Pez Espada i gwiazdy, które przyjeżdżały tu od 1959 r.',desk='GWIAZDY NA COSTA DEL SOL · ODC. 3',
 box1=['CZY WIESZ, ŻE…','Hotel otwarto 31 maja 1959 r. jako pięciogwiazdkowy'],box2=['KTO TU NOCOWAŁ?','SINATRA, GARDNER, CONNERY','i Brigitte Bardot'],
 framenote='Frank Sinatra / Ava Gardner (archiwum)',more=more(3)),
 slides=[
 dict(kicker='31 MAJA 1959 · OTWARCIE',head='Pięć gwiazdek <i>nad plażą</i>',photo='hotel-pez-espada-torremolinos/03.jpg',credit=cr('hotel-pez-espada-torremolinos/03.jpg'),pos='50% 45%',
  body=['<b>31 maja 1959 r.</b> w Torremolinos otwiera się <b>Pez Espada</b> – hotel z <b>pięcioma gwiazdkami</b>. Zaprojektowali go architekci <b>Manuel Muñoz Monasterio</b> i <b>Juan Jáuregui Briales</b>.',
        'Dla dawnej wioski rybaków to skok w inną epokę: luksus, nowoczesna architektura i goście z całego świata.']),
 dict(kicker='KTO TU NOCOWAŁ',head='Lista gości <i>jak z gali Oscarów</i>',frame='Kolaż gwiazd: Sinatra, Gardner, Connery, Bardot',
  body=['W hotelu bywali m.in. <b>Frank Sinatra</b>, <b>Ava Gardner</b>, <b>Sean Connery</b>, <b>Elizabeth Taylor</b>, <b>Brigitte Bardot</b>, <b>Orson Welles</b>, <b>Anthony Quinn</b>, <b>Sophia Loren</b>, <b>Rita Hayworth</b> i <b>Ingrid Bergman</b>.',
        'Na wieczorach w hotelu występowali Julio Iglesias, Raphael i Massiel.']),
 dict(kicker='BAZA NA PLANIE',head='Tu się spało, <i>kręciło się obok</i>',frame='Frank Sinatra – zdjęcie z planu (archiwum)',
  body=['Gwiazdy rzadko grały w samym hotelu – mieszkały tu w czasie zdjęć w okolicy.',
        '<b>Frank Sinatra</b> nocował w Pez Espada, kręcąc „<b>Ekspres von Ryana</b>” w wąwozie El Chorro – tam, gdzie dziś jest Caminito del Rey. <b>Dirk Bogarde</b> i <b>John Mills</b> mieszkali tu przy filmie kręconym w Alhaurín el Grande.']),
 dict(type='numbers',kicker='W LICZBACH',head='Pez Espada <i>w 4 liczbach</i>',rows=[['1959','otwarcie – 31 maja'],['5★','kategoria hotelu na otwarcie'],['2','architektów: Muñoz Monasterio i Jáuregui Briales'],['10+','wielkich gwiazd kina na liście gości']]),
 dict(type='where',head='Pez Espada <i>dziś</i>',photo='playa-de-la-carihuela/01.jpg',credit=cr('playa-de-la-carihuela/01.jpg'),pos='50% 60%',y=600,
  rows=[['ADRES','Avenida Salvador Allende 11, 29620 Torremolinos'],['CO DZIŚ','Hotel działa – stoi przy samej plaży, obok dzielnicy La Carihuela'],['ZDANIEM REDAKCJI','Najlepiej dojść promenadą wzdłuż La Carihueli i zjeść rybę w jednym z chiringuitos']]),
 dict(type='cta',sub='Kolejne odcinki serii – historie gwiazd i miejsc, które możesz dziś odwiedzić',eps=eps(3),note=NOTE)])
# ---------- 4 ----------
P[4]=dict(ep=4,date='19.12.2026',cover=dict(photo='teatro-del-soho-malaga/01.jpg',pos='50% 40%',credit=cr('teatro-del-soho-malaga/01.jpg'),
 head='Gwiazda Hollywood <i>wraca do Málagi</i>',teaser='Własny teatr i Niedziela Palmowa, której nie opuszcza',desk='GWIAZDY NA COSTA DEL SOL · ODC. 4',
 box1=['CZY WIESZ, ŻE…','Od ponad 20 lat prowadzi tron Matki Bożej w procesji'],box2=['KTO TU WRÓCIŁ?','BANDERAS U SIEBIE','teatr na calle Córdoba'],
 framenote='Antonio Banderas (zdjęcie z licencją)',more=more(4)),
 slides=[
 dict(kicker='MÁLAGA · MIASTO RODZINNE',head='Hollywood, <i>a potem powrót</i>',photo='gibralfaro-m-laga-vista/01.jpg',credit=cr('gibralfaro-m-laga-vista/01.jpg',True),pos='50% 50%',
  body=['<b>Antonio Banderas</b> urodził się i wychował w Maladze. Zrobił karierę w Hollywood, ale do rodzinnego miasta wraca nie tylko na wakacje.',
        'W listopadzie 2019 r. otworzył tu własny teatr, a co roku w Niedzielę Palmową jest w centrum Málagi – w procesji.']),
 dict(kicker='15 LISTOPADA 2019',head='Teatr <i>w dawnym kinie</i>',photo='teatro-del-soho-malaga/01.jpg',credit=cr('teatro-del-soho-malaga/01.jpg'),pos='50% 40%',
  body=['<b>Teatro del Soho CaixaBank</b> powstał w odnowionym dawnym kinie. Ma <b>ponad 800 miejsc</b>.',
        'Na otwarcie Banderas wystawił musical „<b>A Chorus Line</b>” – współreżyserował i zagrał w nim Zacha. Dyrektorem artystycznym został Lluís Pasqual. Po Maladze spektakl ruszył do Bilbao, Barcelony i Madrytu.']),
 dict(kicker='NIEDZIELA PALMOWA',head='Tron, dzwonek <i>i pierwsza świeca</i>',photo='semana-santa-malaga/04.jpg',credit=cr('semana-santa-malaga/04.jpg',True),pos='50% 40%',
  body=['Banderas jest <b>mayordomo</b> tronu Matki Bożej w bractwie <b>Lágrimas y Favores</b>. Procesja wychodzi w <b>Niedzielę Palmową</b> z parafii <b>San Juan Bautista</b>.',
        'Zapala pierwszą świecę na tronie, a potem dzwonkiem prowadzi niosących go mężczyzn. Robi to od <b>ponad 20 lat</b> – w 2024 r. procesję odwołano przez deszcz.']),
 dict(type='numbers',kicker='W LICZBACH',head='Banderas i Málaga <i>w 4 liczbach</i>',rows=[['2019','otwarcie Teatro del Soho CaixaBank'],['800+','miejsc na widowni'],['20+','lat jako mayordomo w Niedzielę Palmową'],['4','miasta trasy „A Chorus Line”: Málaga, Bilbao, Barcelona, Madryt']]),
 dict(type='where',head='Málaga <i>Banderasa</i>',photo='plaza-de-la-marina-malaga/04.jpg',credit=cr('plaza-de-la-marina-malaga/04.jpg',True),pos='50% 50%',y=600,
  rows=[['TEATR','Teatro del Soho CaixaBank, calle Córdoba – centrum Málagi, kilka minut pieszo od Plaza de la Marina'],['PROCESJA','Lágrimas y Favores – Niedziela Palmowa, parafia San Juan Bautista. W 2027 r. to 21 marca'],['ZDANIEM REDAKCJI','Na procesję przyjdź wcześnie – w centrum są wtedy tłumy']]),
 dict(type='cta',sub='Kolejne odcinki serii – historie gwiazd i miejsc, które możesz dziś odwiedzić',eps=eps(4),note=NOTE)])
# ---------- 5 ----------
P[5]=dict(ep=5,date='26.12.2026',cover=dict(photo='plaza-de-la-marina-malaga/05.jpg',pos='50% 40%',credit=cr('plaza-de-la-marina-malaga/05.jpg'),
 head='Andersen: <i>tu byłem najszczęśliwszy</i>',teaser='Málaga, jesień 1862 – co autor baśni napisał o mieście',desk='GWIAZDY NA COSTA DEL SOL · ODC. 5',
 box1=['CZY WIESZ, ŻE…','Jego słowa o Maladze wyryto na cokole pomnika'],box2=['KTO TU MIESZKAŁ?','BAŚNIOPISARZ Z DANII','jesień 1862'],
 framenote='Hans Christian Andersen (portret, domena publiczna)',more=more(5)),
 slides=[
 dict(kicker='JESIEŃ 1862',head='Statkiem <i>do Málagi</i>',photo='malaga-port-19th-century/01.jpg',credit=cr('malaga-port-19th-century/01.jpg',True),pos='50% 50%',
  body=['Jesienią <b>1862 r.</b> do Málagi przypływa statkiem <b>Hans Christian Andersen</b> – autor „Brzydkiego kaczątka” i „Małej syrenki”, który podróżuje po Hiszpanii.',
        'Zatrzymuje się w <b>Fonda del Oriente</b>, hotelu z widokiem na <b>Alamedę</b>. Z okna obserwuje życie ulicy – i to ono zachwyca go bardziej niż zabytki.']),
 dict(kicker='CO NAPISAŁ',head='„Tak szczęśliwy <i>i tak u siebie”</i>',photo='alameda-principal-malaga/05.jpg',credit=cr('alameda-principal-malaga/05.jpg'),pos='50% 50%',
  body=['W książce o podróży Andersen napisał, że <b>w żadnym innym hiszpańskim mieście nie czuł się tak szczęśliwy i tak u siebie</b> jak w Maladze.',
        'Te słowa są dziś wyryte na cokole jego pomnika – Málaga nosi je jak wizytówkę.']),
 dict(kicker='MIASTO OCZAMI BAŚNIOPISARZA',head='Katedra, <i>cmentarz i Alameda</i>',photo='catedral-de-m-laga/04.jpg',credit=cr('catedral-de-m-laga/04.jpg'),pos='50% 30%',
  body=['Katedrę – z niedokończoną wieżą, przez którą mieszkańcy nazywają ją <b>La Manquita</b> – porównał do ogromnej arki na skamieniałym morzu.',
        '<b>Cmentarz Angielski</b> nazwał uroczym ogrodem, małym rajem. Na Alamedzie zachwycała go mieszanka ludzi i codzienne życie miasta.']),
 dict(type='numbers',kicker='W LICZBACH',head='Andersen w Maladze <i>w 4 liczbach</i>',rows=[['1862','jesień – pobyt w Maladze'],['1863','wydanie książki „W Hiszpanii”'],['2005','odsłonięcie pomnika Andersena'],['1','miasto w Hiszpanii, w którym czuł się „u siebie”']]),
 dict(type='where',head='Andersen <i>w Maladze dziś</i>',photo='cementerio-ingles-malaga/01.jpg',credit=cr('cementerio-ingles-malaga/01.jpg'),pos='50% 50%',y=600,
  rows=[['POMNIK','Plaza de la Marina – siedzący Andersen, na cokole jego słowa o Maladze. Autor: José María Córdoba'],['ALAMEDA','Alameda Principal – tu stał jego hotel Fonda del Oriente'],['CMENTARZ','Cementerio Inglés – „mały raj”, który odwiedził w 1862 r.'],['ZDANIEM REDAKCJI','Zrób zdjęcie obok Andersena – plac jest między portem a centrum']]),
 dict(type='cta',sub='To ostatni odcinek pierwszej serii – kolejne gwiazdy już w przygotowaniu',eps=[[a,b,False] for a,b in EPS[:4]],ey=780,note=NOTE)])
for k,v in P.items(): json.dump(v,open(f'/tmp/g/ep{k}.json','w'),ensure_ascii=False,indent=1)
print('ok')
