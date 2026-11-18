# Dodatek świąteczny Sol y Sól – strony magazynu
def P_cover(n, N):
    return open('/home/claude/swieta_up/cover_A.html').read()

def P_liczby(n, N):
    g = lambda a, b, c=RED: f'<div style="border-top:2px solid {INKK};padding-top:14px">{stat(a, b, c)}</div>'
    stats = (g('2,8 mln', 'lampek LED w centrum Malagi – włączenie 27.11') + g('3,8 mln', 'lampek w Marbelli i San Pedro', GRN) +
             g('20 €', 'kosztuje décimo, czyli los El Gordo', GOLD) + g('1812', 'rok pierwszego losowania loterii świątecznej') +
             g('12', 'winogron o północy w Sylwestra', GRN) + g('ok. 17°C', 'średnio w dzień w grudniu w Maladze', GOLD))
    short = ''.join(f'<div style="border-top:1px solid #CFC5B5;padding:12px 0"><div style="{CG}font-size:25px;font-weight:600">{a}</div><div style="font-size:18px;line-height:1.4;color:{MUT};margin-top:3px">{b}</div></div>' for a, b in [
        ('Málaga – koncert na start', 'Po włączeniu świateł 27.11 o 18:30 gra El Kanka, wstęp wolny.'),
        ('Marbella – anioły', 'Nowy pokaz na Plaza de los Naranjos, 3 razy dziennie.'),
        ('Fuengirola – jarmark', 'Drewniane domki na Plaza de la Constitución do ok. 21.12.'),
        ('Estepona – churros', '1.12 o 19:00 na Plaza del Ajedrez, z flashmobem 30 muzyków.')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Na start")}{H("Święta w liczbach", 88)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px 40px;width:560px">{stats}</div></div>'
             f'<div style="position:absolute;left:668px;right:64px;top:222px">{hdr("Krótko", 34)}{short}</div>'
             + photo('x_hp2.jpg', 64, 760, 560, 360, '50% 40%', 'Calle Larios w Maladze. Fot. Hernán Piñera / Wikimedia Commons, CC BY-SA 2.0')
             + f'<div style="position:absolute;left:668px;right:64px;top:790px">' + box('Czy wiesz, że…', 'W Hiszpanii święta trwają aż do 6 stycznia – najważniejszy dzień dla dzieci to Trzech Króli, a nie Wigilia.', RED) + '</div>'
             + src('Ayuntamiento de Málaga, Marbella, Fuengirola, Estepona; Loterías y Apuestas del Estado; AEMET (średnie klimatyczne). Stan na 18.11.2026.'))
    return frame(n, N, 'Na start', inner)

def P_kalendarz(n, N):
    rows = [('27.11', 'pt', 'Málaga · Fuengirola', 'Włączenie świateł. W Maladze o 18:30, potem koncert El Kanki.'),
            ('28.11', 'sob', 'Málaga', 'Rusza mapping na wieży katedry – 19:00, 20:30, 22:00.'),
            ('1.12', 'wt', 'Estepona', 'Światła, kolędy pastorales, churros z czekoladą i flashmob.'),
            ('8.12', 'wt', 'Cała Hiszpania', 'Święto Niepokalanego Poczęcia – dzień wolny.'),
            ('ok. 21.12', '', 'Fuengirola', 'Ostatnie dni jarmarku na Plaza de la Constitución.'),
            ('22.12', 'wt', 'Cała Hiszpania', 'El Gordo – losowanie od rana na żywo w TVE.'),
            ('24.12', 'czw', 'Nochebuena', 'Wigilia. Sklepy otwarte, ale zamykają wcześniej.'),
            ('25.12', 'pt', 'Navidad', 'Boże Narodzenie – dzień wolny, sklepy zamknięte.'),
            ('28.12', 'pn', 'Día de los Inocentes', 'Hiszpański prima aprilis – uważaj na żarty.'),
            ('31.12', 'czw', 'Nochevieja', '12 winogron o północy. W Maladze na Plaza de la Constitución.'),
            ('5.01', 'wt', 'Cabalgata de Reyes', 'Wieczorne pochody Trzech Króli w miastach.'),
            ('6.01', 'śr', 'Reyes', 'Dzień wolny i prezenty dla dzieci.')]
    rr = ''.join(f'<div style="display:grid;grid-template-columns:170px 1fr;gap:24px;padding:17px 0;border-top:1px solid #CFC5B5">'
                 f'<div><span style="{CG}font-size:40px;font-weight:600;color:{RED if i % 2 == 0 else GRN};line-height:1">{a}</span> <span style="font-size:15px;color:{MUT};letter-spacing:.1em">{b.upper()}</span></div>'
                 f'<div><div style="font-size:15px;font-weight:800;letter-spacing:.18em;color:{GOLD};text-transform:uppercase">{E(c)}</div><div style="font-size:21px;line-height:1.35;margin-top:2px">{E(d)}</div></div></div>' for i, (a, b, c, d) in enumerate(rows))
    inner = f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Kalendarz świąt")}{H("Daty, których <i style=\'color:"+RED+"\'>nie przegap</i>", 80)}{rule()}{rr}</div>'
    return frame(n, N, 'Kalendarz', inner)

def P_malaga(n, N):
    inner = (photo('x_hp2.jpg', 0, 10, 1080, 470, '50% 35%') +
             f'<div style="position:absolute;left:0;right:0;top:10px;height:470px;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.7) 100%)"></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:330px;color:#fff">{kick("Málaga · Temat numeru", "#F2C14E")}{H("Calle Larios <i style=\'color:#F2C14E\'>zapala święta</i>", 74, "#fff")}</div>'
             f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.8)">Fot. Hernán Piñera / Wikimedia Commons, CC BY-SA 2.0</div>'
             f'<div style="position:absolute;left:64px;top:520px;width:560px">'
             + p('<b>Święta na Costa del Sol zaczynają się w Maladze.</b> W piątek 27.11 o 18:30 przy wejściu na calle Larios zapalą się świąteczne światła – w centrum to w sumie <b>2,8 mln lampek LED</b>. Zaraz potem darmowy koncert El Kanki.')
             + p('Główna atrakcja to pokaz światła i muzyki „Natividad de Luz”: lampki nad calle Larios zmieniają się w rytm muzyki. Pokazy trwają do 4.01, trzy razy wieczorem. Nie ma ich tylko 24 i 31.12.')
             + p('Od 28.11 warto też podejść pod katedrę. Na jej wieży wyświetlany jest mapping – barwne obrazy na kamiennej fasadzie.')
             + f'</div><div style="position:absolute;left:666px;right:64px;top:520px">'
             + box('Pokazy na Larios', '<b style="font-size:30px">18:30 · 20:30 · 22:00</b><br>codziennie do 4.01<br>(bez 24 i 31.12)', RED)
             + '<div style="height:16px"></div>'
             + box('Mapping na katedrze', '<b style="font-size:30px">19:00 · 20:30 · 22:00</b><br>od 28.11', GRN)
             + '<div style="height:16px"></div>'
             + box('Czy wiesz, że…', 'Oświetlenie calle Larios co roku przyciąga do Malagi turystów z całej Europy – a o Maladze mówi się, że ma jedne z najpiękniejszych świątecznych świateł w Hiszpanii.', SAND, INKK, RED)
             + '</div>' + src('Ayuntamiento de Málaga; que.es; malagaes.com; marbella-sanpedro.com. Stan na 18.11.2026.'))
    return frame(n, N, 'Málaga', inner)

def P_marbella(n, N):
    nums = ''.join(f'<div style="background:{c};color:#fff;padding:18px 20px"><div style="{CG}font-size:52px;font-weight:600;line-height:1">{a}</div><div style="font-size:17px;margin-top:6px;line-height:1.3">{b}</div></div>' for a, b, c in [
        ('3,8 mln', 'lampek LED', RED), ('532', 'świetlne łuki', GRN), ('146', 'oświetlonych drzew', GOLD), ('2 421', 'girland', INKK)])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Marbella · San Pedro")}{H("Anioły nad <i style=\'color:"+RED+"\'>Plaza de los Naranjos</i>", 74)}{rule()}</div>'
             + photo('xmas_naranjos.jpg', 64, 290, 470, 560, '50% 0%', 'Plaza de los Naranjos. Fot. Berthold Werner / Wikimedia Commons, CC BY-SA 3.0')
             + f'<div style="position:absolute;left:570px;right:64px;top:290px">'
             + p('W tym roku Marbella stawia na <b>pokazy muzyczne</b>. Na Plaza de los Naranjos, najbardziej znanym placu starego miasta, staną <b>cztery wielkie anioły</b>. Pokazy – trzy razy dziennie.', 21)
             + p('San Pedro Alcántara dostanie własną atrakcję: <b>świetlny las</b> na Marqués del Duero, też z trzema pokazami dziennie.', 21)
             + box('Kiedy włączenie świateł?', 'Ratusz jeszcze nie podał daty. Rok temu San Pedro zaczęło w piątek, a Marbella dzień później. Damy znać od razu.', SAND, INKK, RED)
             + '</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:900px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{nums}</div>'
             + f'<div style="position:absolute;left:64px;right:64px;top:1060px">{box("Czy wiesz, że…", "Plac Pomarańczy powstał pod koniec XV wieku, a drzewa pomarańczowe, od których wziął nazwę, posadzono w 1941 roku.", GRN)}</div>'
             + src('Ayuntamiento de Marbella; Marbella Directo; La Noción; Área Costa del Sol; Wikipedia (Plaza de los Naranjos). Stan na 18.11.2026.'))
    return frame(n, N, 'Marbella', inner)

def P_fue_est(n, N):
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Fuengirola · Estepona")}{H("Jarmark, churros <i style=\'color:"+GRN+"\'>i 2,77 mln lampek</i>", 74)}{rule()}</div>'
             + photo('xmas_fue.jpg', 64, 290, 455, 330, '50% 60%', 'Fuengirola. Fot. Javi Masa / Wikimedia Commons, CC BY 3.0')
             + photo('est2.jpg', 561, 290, 455, 330, '50% 50%', 'Estepona. Fot. Christian Hergesell / Unsplash')
             + f'<div style="position:absolute;left:64px;top:670px;width:455px">{hdr("Fuengirola", 40, RED)}'
             + p('Światła zapalają się w piątek 27.11 i świecą do 6.01. Najbardziej ozdobiona będzie <b>Plaza de España</b>.', 20)
             + p('Na <b>Plaza de la Constitución</b> staje świąteczny jarmark z drewnianymi domkami: ozdoby, prezenty, rękodzieło – od końca listopada do ok. 21.12.', 20)
             + f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:6px">{stat("446","łuków",RED,44)}{stat("164","latarni",GRN,44)}{stat("63","figury",GOLD,44)}</div></div>'
             + f'<div style="position:absolute;left:561px;top:670px;width:455px">{hdr("Estepona", 40, GRN)}'
             + p('Estepona włącza światła we <b>wtorek 1.12 o 19:00</b> na Plaza del Ajedrez.', 20)
             + p('W programie kolędy grup <i>pastorales</i>, <b>churros z czekoladą</b> dla wszystkich i flashmob ponad 30 muzyków na żywo.', 20)
             + box('Słowo na dziś', '<b>Pastorales</b> – grupy, które śpiewają tradycyjne andaluzyjskie kolędy przy tamburynach i zambombach.', SAND, INKK, RED)
             + '</div>' + src('Ayuntamiento de Fuengirola (fuengirola.es); Área Costa del Sol; Ayuntamiento de Estepona; Al Sol de la Costa; Diario Costa. Stan na 18.11.2026.'))
    return frame(n, N, 'Fuengirola · Estepona', inner)

def P_gordo(n, N):
    tl = ''.join(f'<div style="display:grid;grid-template-columns:120px 1fr;gap:18px;padding:18px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:44px;font-weight:600;color:{RED}">{a}</div><div><b style="font-size:24px">{b}</b><div style="font-size:21px;line-height:1.4;color:{MUT}">{c}</div></div></div>' for a, b, c in [
        ('1812', 'Pierwsze losowanie', 'Loteria świąteczna działa od ponad 200 lat – to jedna z najstarszych loterii na świecie.'),
        ('22.12', 'Dzień losowania', 'Od rana cały kraj ogląda transmisję w TVE. Wielu Hiszpanów uważa ten dzień za początek świąt.'),
        ('20 €', 'Décimo', 'Tyle kosztuje dziesiąta część losu. Pełny los (billete) to 10 décimos.')])
    inner = (photo('xmas_loteria.jpg', 0, 10, 1080, 420, '50% 35%') +
             f'<div style="position:absolute;left:0;right:0;top:10px;height:420px;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.75) 100%)"></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:290px;color:#fff">{kick("Tradycja · 22 grudnia", "#F2C14E")}{H("El Gordo – loteria, <i style=\'color:#F2C14E\'>którą żyje cały kraj</i>", 64, "#fff")}</div>'
             f'<div style="position:absolute;right:30px;top:20px;font-size:13px;color:rgba(255,255,255,.85)">Obraz: Christian Franzen, ok. 1900 / Wikimedia Commons, domena publiczna</div>'
             f'<div style="position:absolute;left:64px;top:470px;width:560px">{tl}'
             + p('<br>Los kupuje się w punktach <b>Loterías y Apuestas del Estado</b> – często wspólnie: z rodziną, w pracy albo w ulubionym barze. Gdy numer wygra, cieszy się cała ulica.', 20) + '</div>'
             f'<div style="position:absolute;left:666px;right:64px;top:470px">'
             + box('Czy wiesz, że…', 'Wylosowane numery i kwoty nie są odczytywane, tylko <b>śpiewane</b> – robią to dzieci ze szkoły San Ildefonso w Madrycie.', RED)
             + '<div style="height:16px"></div>'
             + box('El Gordo, czyli…', '„Gruby” – tak nazywa się główną nagrodę. Stąd potoczna nazwa całego losowania.', GRN)
             + '<div style="height:16px"></div>'
             + box('Uwaga', 'Duże wygrane są w Hiszpanii opodatkowane. Szczegóły sprawdź na stronie Loterías y Apuestas del Estado.', SAND, INKK, RED)
             + '</div>' + src('Loterías y Apuestas del Estado; RTVE. Stan na 18.11.2026.'))
    return frame(n, N, 'Tradycje', inner)

def P_mit(n, N):
    cards = [('„W Hiszpanii prezenty przynosi Mikołaj.”', 'TO ZALEŻY', 'Coraz więcej rodzin daje prezenty 25.12, ale tradycyjnie przynoszą je Trzej Królowie 6.01.'),
             ('„Na święta w Maladze może spaść śnieg.”', 'MIT', 'W grudniu w dzień jest średnio ok. 17°C. Śnieg zobaczysz najwyżej w górach.'),
             ('„26 grudnia jest wolne.”', 'MIT', 'W Andaluzji drugi dzień świąt to zwykły dzień pracy.'),
             ('„W Wigilię wszystko jest zamknięte.”', 'MIT', 'Sklepy zwykle działają, ale zamykają wcześniej niż zwykle.'),
             ('„28 grudnia nie wierz w każdą wiadomość.”', 'FAKT', 'To Día de los Inocentes – żartują znajomi, a czasem nawet gazety.'),
             ('„Hiszpanie też chodzą na pasterkę.”', 'FAKT', 'Nazywa się Misa del Gallo – „msza koguta” – i odbywa się w noc wigilijną.')]
    cc = ''.join(f'<div style="background:{SAND if i % 3 != 1 else "#fff"};border:1px solid #D9CDB8;padding:28px 26px"><div style="{CG}font-style:italic;font-size:31px;font-weight:600;line-height:1.15">{E(a)}</div>'
                 f'<div style="display:inline-block;border:2px solid {RED if b == "MIT" else GRN};color:{RED if b == "MIT" else GRN};font-size:15px;font-weight:800;letter-spacing:.2em;padding:5px 10px;margin:12px 0 8px">{b}</div>'
                 f'<div style="font-size:22px;line-height:1.4">{E(c)}</div></div>' for i, (a, b, c) in enumerate(cards))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Sprawdzamy")}<div style="display:flex;justify-content:space-between;align-items:flex-end">{H("Mit <i style=\'color:"+RED+"\'>czy fakt?</i>", 88)}<div style="{CG}font-style:italic;font-size:24px;text-align:right;color:{MUT}">Sześć rzeczy, które każdy „wie”<br>o świętach w Hiszpanii</div></div>{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{cc}</div></div>' + src('BOE i kalendarz świąt Junta de Andalucía 2026; AEMET; Conferencia Episcopal Española.'))
    return frame(n, N, 'Sprawdzamy', inner)

def P_pl_es(n, N):
    rows = [('Główny wieczór', '24.12 – Wigilia', '24.12 – Nochebuena'),
            ('Prezenty', '24.12, od Mikołaja lub Gwiazdora', 'Głównie 6.01 od Trzech Króli; coraz częściej też 25.12'),
            ('Na stole', '12 potraw, karp, barszcz, pierogi', 'Owoce morza, pieczona jagnięcina lub indyk, turrón'),
            ('Opłatek', 'Tak – dzielimy się przed kolacją', 'Nie ma tej tradycji'),
            ('Pasterka', 'Tak', 'Tak – Misa del Gallo'),
            ('Kolędy', 'Kolędy i pastorałki', 'Villancicos, w Andaluzji z zambombą'),
            ('26 grudnia', 'Drugi dzień świąt – wolne', 'W Andaluzji dzień pracy'),
            ('Sylwester', 'Szampan o północy', '12 winogron, potem cava'),
            ('Koniec świąt', '2.02 – Matki Bożej Gromnicznej', '6.01 – Trzech Króli')]
    head = f'<div style="display:grid;grid-template-columns:210px 1fr 1fr;gap:18px;padding-bottom:10px"><div></div><div style="font-size:18px;font-weight:800;letter-spacing:.2em;color:{RED}">🇵🇱 POLSKA</div><div style="font-size:18px;font-weight:800;letter-spacing:.2em;color:{GOLD}">🇪🇸 HISZPANIA</div></div>'
    rr = ''.join(f'<div style="display:grid;grid-template-columns:210px 1fr 1fr;gap:18px;padding:22px 0;border-top:1px solid #CFC5B5;background:{"transparent" if i % 2 else "rgba(239,230,214,.6)"}"><div style="{CG}font-size:26px;font-weight:600;padding-left:8px">{E(a)}</div><div style="font-size:22px;line-height:1.35">{E(b)}</div><div style="font-size:22px;line-height:1.35">{E(c)}</div></div>' for i, (a, b, c) in enumerate(rows))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Dla Polaków")}{H("Wigilia czy <i style=\'color:"+RED+"\'>Nochebuena?</i>", 84)}'
             f'<div style="font-size:22px;color:{MUT};margin-top:12px">Jak świętuje Polska, a jak Hiszpania – porównanie w jednym miejscu</div>{rule()}{head}{rr}</div>')
    return frame(n, N, 'Dla Polaków', inner)

def P_slodycze(n, N):
    items = [('x_turron.jpg', 'Turrón', 'Nugat z migdałów i miodu. Twardy (z Alicante) albo miękki (z Jijony) – oba znajdziesz w każdym supermarkecie.', 'Fot. Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0'),
             ('x_rosc.jpg', 'Roscón de Reyes', 'Drożdżowy wieniec z kandyzowanymi owocami, jedzony 6.01. W środku figurka i fasolka.', 'Fot. Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0')]
    cards = ''.join(f'<div>{""}<img src="file://{PH}{a}" style="width:100%;height:300px;object-fit:cover"><div style="font-size:12px;color:{MUT};margin-top:4px">{E(d)}</div>{hdr(b, 38, RED)}<div style="font-size:20px;line-height:1.45">{E(c)}</div></div>' for a, b, c, d in items)
    more = ''.join(f'<div style="border-top:1px solid #CFC5B5;padding:12px 0;display:grid;grid-template-columns:230px 1fr;gap:16px"><div style="{CG}font-size:28px;font-weight:600;color:{GRN}">{a}</div><div style="font-size:19px;line-height:1.4">{b}</div></div>' for a, b in [
        ('Polvorones', 'Kruche ciasteczka z migdałami, które rozsypują się w ustach. Najsłynniejsze pochodzą z Estepy pod Sewillą.'),
        ('Mantecados', 'Krewni polvorones – na smalcu, często cynamonowe lub cytrynowe.'),
        ('Pestiños', 'Andaluzyjskie smażone ciasteczka w miodzie, z nutą anyżu.'),
        ('Mazapán', 'Marcepan – najbardziej znany jest ten z Toledo.')])
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Na słodko")}{H("Co Hiszpanie <i style=\'color:"+RED+"\'>jedzą na święta</i>", 78)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:30px">{cards}</div><div style="margin-top:18px">{more}</div></div>')
    return frame(n, N, 'Na słodko', inner)

def P_ciekawostki(n, N):
    facts = [('Żywe szopki', 'Belén viviente to szopka z aktorami i zwierzętami – w wielu andaluzyjskich miasteczkach to całe przedstawienie.'),
             ('Zambomba', 'Spotkania z kolędami w rytmie flamenco. Nazwa pochodzi od bębna z trzciną, który „buczy” przy pocieraniu.'),
             ('Paga extra', 'W grudniu wielu pracowników dostaje dodatkową pensję – stąd świąteczne zakupy na dużą skalę.'),
             ('Kosz od szefa', 'Cesta de Navidad – kosz z szynką, winem i słodyczami, który firmy dają pracownikom.'),
             ('Listy do Króli', 'Dzieci piszą listy do Trzech Króli i wręczają je ich „paziom” w centrach handlowych.'),
             ('Węgiel dla niegrzecznych', 'Kto był niegrzeczny, dostaje od Króli węgiel – ale z cukru.'),
             ('Fasolka w cieście', 'Kto w rosconie trafi na fasolkę, zwyczajowo płaci za ciasto w przyszłym roku.'),
             ('Winogrona w puszce', 'Przed Sylwestrem sklepy sprzedają 12 obranych winogron w puszce – łatwiej zdążyć.'),
             ('Czerwona bielizna', 'W Sylwestra wiele osób zakłada czerwoną bieliznę – ma przynieść szczęście w nowym roku.'),
             ('Zegar z Puerta del Sol', 'Północ cała Hiszpania odlicza z telewizją, która pokazuje zegar na Puerta del Sol w Madrycie.'),
             ('Śpiewane numery', 'W El Gordo dzieci ze szkoły San Ildefonso śpiewają wylosowane numery.'),
             ('Prima aprilis w grudniu', '28.12 to Día de los Inocentes – dzień żartów, także w mediach.')]
    cc = ''.join(f'<div style="display:flex;gap:16px;padding:12px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:46px;font-weight:600;color:{[RED, GRN, GOLD][i % 3]};line-height:.9;min-width:52px">{i+1}</div><div><div style="font-size:21px;font-weight:700">{E(a)}</div><div style="font-size:18px;line-height:1.4;color:#4A443D;margin-top:3px">{E(b)}</div></div></div>' for i, (a, b) in enumerate(facts))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Ciekawostki")}{H("12 rzeczy, które <i style=\'color:"+RED+"\'>zaskakują Polaków</i>", 74)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 36px">{cc}</div></div>')
    return frame(n, N, 'Ciekawostki', inner)

def P_sylwester(n, N):
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Sylwester · Trzech Króli")}{H("Winogrona, cava <i style=\'color:"+RED+"\'>i trzech króli</i>", 78)}{rule()}</div>'
             + photo('xmas_uvas.jpg', 64, 290, 455, 330, '50% 80%', 'Fot. Zarateman / Wikimedia Commons, CC0')
             + photo('x_rosc.jpg', 561, 290, 455, 330, '50% 45%', 'Fot. Juan Emilio Prades Bel / Wikimedia Commons, CC BY 4.0')
             + f'<div style="position:absolute;left:64px;top:670px;width:455px">{hdr("31.12 – Nochevieja", 38, RED)}'
             + p('O północy Hiszpanie zjadają <b>12 winogron</b> – po jednym przy każdym uderzeniu zegara. Każde to szczęście na jeden miesiąc.', 20)
             + p('W Maladze wspólne odliczanie odbywa się na <b>Plaza de la Constitución</b>. Potem toast cavą – hiszpańskim winem musującym.', 20)
             + box('Wskazówka', 'Wybierz małe winogrona bez pestek – na 12 uderzeń zegara jest tylko kilkanaście sekund.', GRN) + '</div>'
             + f'<div style="position:absolute;left:561px;top:670px;width:455px">{hdr("5–6.01 – Reyes", 38, GRN)}'
             + p('Wieczorem 5.01 przez miasta przechodzą <b>Cabalgatas de Reyes</b> – barwne pochody, z wozów leci w tłum deszcz cukierków.', 20)
             + p('Rano 6.01 dzieci znajdują prezenty, a na stół trafia <b>roscón de Reyes</b>. To dzień wolny.', 20)
             + box('Dla rodziców', 'Na cabalgatę weź torbę lub odwrócony parasol – dzieci łapią do niego cukierki.', RED) + '</div>')
    return frame(n, N, 'Tradycje', inner)

def P_slowniczek(n, N):
    w = [('¡Feliz Navidad!', 'Wesołych Świąt!'), ('¡Próspero Año Nuevo!', 'Szczęśliwego Nowego Roku!'), ('Nochebuena', 'Wigilia'), ('Nochevieja', 'Sylwester'),
         ('los Reyes Magos', 'Trzej Królowie'), ('el belén', 'szopka'), ('el villancico', 'kolęda'), ('el árbol de Navidad', 'choinka'),
         ('el regalo', 'prezent'), ('las uvas de la suerte', 'winogrona szczęścia'), ('las campanadas', 'uderzenia zegara o północy'), ('el décimo', 'los loterii (1/10)'),
         ('la cabalgata', 'pochód (Trzech Króli)'), ('el turrón', 'nugat'), ('la Misa del Gallo', 'pasterka'), ('el alumbrado', 'iluminacja świąteczna')]
    cc = ''.join(f'<div style="padding:13px 0;border-top:1px solid #CFC5B5"><div style="{CG}font-size:31px;font-weight:600;color:{[RED, GRN][i % 2]}">{E(a)}</div><div style="font-size:20px;color:#4A443D;margin-top:2px">{E(b)}</div></div>' for i, (a, b) in enumerate(w))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Po hiszpańsku")}{H("Świąteczny <i style=\'color:"+RED+"\'>słowniczek</i>", 86)}{rule()}'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 40px">{cc}</div>'
             f'<div style="margin-top:20px">{box("Złota fraza", "<b>¡Felices fiestas!</b> – „Wesołych świąt!”, uniwersalnie: pasuje i do sąsiada, i do klienta.", GRN)}</div></div>')
    return frame(n, N, 'Po hiszpańsku', inner)

def P_quiz(n, N):
    q = [('Ile winogron je się o północy w Sylwestra?', 'a) 7   b) 12   c) 24'),
         ('Kto w Hiszpanii przynosi główne prezenty?', 'a) Mikołaj   b) Aniołek   c) Trzej Królowie'),
         ('Jak nazywa się główna nagroda świątecznej loterii?', 'a) El Gordo   b) El Grande   c) El Rey'),
         ('Co znajdziesz w rosconie de Reyes?', 'a) monetę   b) figurkę i fasolkę   c) migdał'),
         ('Kiedy Hiszpanie robią sobie żarty jak u nas 1 kwietnia?', 'a) 28.12   b) 31.12   c) 6.01'),
         ('Co oznacza „villancico”?', 'a) wioska   b) kolęda   c) szopka')]
    qq = ''.join(f'<div style="padding:16px 0;border-top:1px solid #CFC5B5;display:flex;gap:20px"><div style="{CG}font-size:52px;font-weight:600;color:{[RED, GRN, GOLD][i % 3]};line-height:.9;min-width:46px">{i+1}</div><div><div style="font-size:24px;font-weight:700;line-height:1.3">{E(a)}</div><div style="font-size:21px;color:#4A443D;margin-top:6px;white-space:pre">{E(b)}</div></div></div>' for i, (a, b) in enumerate(q))
    inner = (f'<div style="position:absolute;left:64px;right:64px;top:56px">{kick("Sprawdź się")}{H("Świąteczny <i style=\'color:"+RED+"\'>quiz</i>", 88)}<div style="font-size:22px;color:{MUT};margin-top:10px">Ile wiesz o hiszpańskich świętach? Napisz swój wynik w komentarzu 👇</div>{rule()}{qq}'
             f'<div style="margin-top:22px;background:{SAND};padding:16px 22px;font-size:19px;transform:rotate(180deg);text-align:center">Odpowiedzi: 1b · 2c · 3a · 4b · 5a · 6b</div></div>')
    return frame(n, N, 'Quiz', inner)

def P_koniec(n, N):
    inner = (photo('x_tree_palm.jpg', 0, 10, 1080, 1340, '50% 40%') +
             f'<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,24,17,.25) 0%,rgba(8,24,17,.6) 45%,rgba(8,24,17,.94) 70%)"></div>'
             f'<div style="position:absolute;left:64px;right:64px;top:690px;color:#FAF7F2;text-align:center">'
             f'<div style="{CG}font-style:italic;font-size:46px;color:#F2C14E">¡Feliz Navidad!</div>'
             f'<div style="{CG}font-size:120px;font-weight:600;line-height:1">Wesołych Świąt</div>'
             f'<div style="font-size:26px;line-height:1.5;margin-top:20px">życzy redakcja Sol y Sól</div>'
             f'<div style="font-size:23px;line-height:1.5;margin-top:26px;color:#E9E1D2">Daty z Marbelli i kolejnych miejscowości dopiszemy, gdy ratusze je ogłoszą.<br>Codziennie o <b>8:00</b> i <b>19:00</b> – wydania z wybrzeża.</div>'
             f'<div style="display:flex;justify-content:center;gap:16px;margin-top:34px;font-size:19px;font-weight:800;letter-spacing:.16em"><span style="background:{RED};padding:15px 20px">🔔 OBSERWUJ @SOLYSOL.PL</span><span style="border:2px solid #FAF7F2;padding:13px 20px">ZAPISZ · UDOSTĘPNIJ</span></div></div>'
             f'<div style="position:absolute;right:30px;top:24px;font-size:13px;color:rgba(255,255,255,.85)">Fot. Bogdan Migulski / Wikimedia Commons, CC BY 2.0</div>')
    return page(GARL + inner, '#08180F', '#FAF7F2')

PAGES = [P_cover, P_liczby, P_kalendarz, P_malaga, P_marbella, P_fue_est, P_gordo, P_mit, P_pl_es, P_slodycze, P_sylwester, P_ciekawostki, P_slowniczek, P_quiz, P_koniec]
