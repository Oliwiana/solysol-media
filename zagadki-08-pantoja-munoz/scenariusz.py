# Scenariusz Zagadki #8 – tekst dla lektora (liczby słownie). Rozdziały: (część, tytuł, akapity)
# Tylko fakty z wyroków i dokumentów sądowych (2 źródła na fakt), bez plotek.
CH = [
(1,"Otwarcie",[
"Szesnasty kwietnia dwa tysiące trzynastego roku. Sąd okręgowy w Maladze ogłasza wyrok w sprawie, o której mówi cała Hiszpania. Wśród skazanych są jedna z najbardziej znanych piosenkarek w kraju i były burmistrz Marbelli.",
"Sąd ogłasza wyrok. Ona: dwa lata więzienia za pranie pieniędzy. On: łącznie siedem lat więzienia.",
"To historia, w której miłość, władza i pieniądze z ratusza splotły się tak mocno, że rozplątał je dopiero sąd. Opowiadamy ją wyłącznie na podstawie wyroków i dokumentów.",
"To Sol i Sól i „Zagadki Costa del Sol”. Odcinek ósmy. Pantoja i Muñoz."]),
(1,"Człowiek Gila",[
"Julián Muñoz urodził się w tysiąc dziewięćset czterdziestym siódmym roku. W Marbelli robi karierę u boku Jesúsa Gila, w jego partii GIL. Przez lata jest radnym i zastępcą burmistrza.",
"W maju dwa tysiące drugiego roku sam zostaje burmistrzem Marbelli. Rządzi nieco ponad rok. W sierpniu dwa tysiące trzeciego roku radni z jego własnej partii przechodzą na drugą stronę i odwołują go w głosowaniu nad wotum nieufności.",
"Opowiadaliśmy o tym w odcinku o aferze Malaya. Dziś patrzymy na tę samą historię z innej strony."]),
(1,"Para z okładek",[
"W tym samym czasie, w dwa tysiące trzecim roku, Muñoz związuje się z Isabel Pantoją, jedną z najpopularniejszych piosenkarek w Hiszpanii.",
"Zdaniem redakcji to moment, w którym polityka Marbelli przenosi się z sesji rady miasta na okładki kolorowych magazynów. Ale nas interesuje nie romans, tylko to, co później ustalił sąd. Bo w aktach tej sprawy pojawią się konta, firmy i pieniądze z ratusza."]),
(2,"Malaya",[
"Dwa tysiące szósty rok. Rusza operacja Malaya, największe śledztwo korupcyjne w historii Marbelli. W tym samym roku zatrzymany zostaje także Julián Muñoz.",
"Śledczy przyglądają się majątkowi byłego burmistrza i temu, skąd pochodzą jego pieniądze.",
"Pytanie brzmi: gdzie te pieniądze trafiły? I tu w sprawie pojawia się nazwisko jego partnerki."]),
(2,"Sprawa prania pieniędzy",[
"Z wielkiego śledztwa zostaje wydzielona osobna sprawa. Dotyczy prania pieniędzy pochodzących z przestępstw Muñoza.",
"Proces toczy się przed sądem okręgowym w Maladze. Prokuratura żąda dla piosenkarki ponad trzech lat więzienia.",
"Szesnastego kwietnia dwa tysiące trzynastego roku zapada wyrok. Sąd uznaje, że przez firmy i konta Isabel Pantoi przechodziły pieniądze byłego burmistrza pochodzące z przestępstw. Kara: dwa lata więzienia i grzywna w wysokości ponad miliona stu tysięcy euro.",
"Julián Muñoz słyszy w tej samej sprawie wyroki za pranie pieniędzy i łapownictwo. Łącznie siedem lat więzienia."]),
(2,"Sąd Najwyższy",[
"Obie strony się odwołują. W czerwcu dwa tysiące czternastego roku Sąd Najwyższy utrzymuje karę dwóch lat dla piosenkarki.",
"Sąd w Maladze odmawia zawieszenia kary i nakazuje piosenkarce stawić się w więzieniu. Kolejne odwołania niczego nie zmieniają."]),
(3,"Alcalá de Guadaíra",[
"Dwudziesty pierwszy listopada dwa tysiące czternastego roku, wczesny ranek. Isabel Pantoja zgłasza się do więzienia dla kobiet w Alcalá de Guadaíra pod Sewillą.",
"Grzywnę spłaca w ratach. Na początku marca dwa tysiące szesnastego roku opuszcza je na stałe, na warunkowym zwolnieniu."]),
(3,"Wyroki burmistrza",[
"Dla Juliána Muñoza to nie koniec. Ma wyroki w kilku sprawach związanych z ratuszem w Marbelli, w tym w głównym procesie Malaya.",
"W maju dwa tysiące szesnastego roku przechodzi do systemu półotwartego. W dwa tysiące dwudziestym pierwszym roku dostaje warunkowe zwolnienie ze względu na ciężką chorobę.",
"Dwudziestego czwartego września dwa tysiące dwudziestego czwartego roku Julián Muñoz umiera w szpitalu w Marbelli. Miał siedemdziesiąt sześć lat."]),
(3,"Epilog",[
"Zdaniem redakcji ta historia pokazuje, jak długo trwa rozliczanie korupcji. Od pierwszych zatrzymań do wyjścia ostatnich skazanych z więzienia minęło kilkanaście lat.",
"I pokazuje coś jeszcze. Pieniądze z ratusza nie znikają. Trafiają na konta, do firm i do domów. A sąd potrafi je tam znaleźć, nawet jeśli ich właściciele są na pierwszych stronach gazet.",
"W następnym odcinku zostajemy przy brudnych pieniądzach. Operacja Ballena Blanca, czyli pralnia pieniędzy w Marbelli. Premiera w niedzielę, siedemnastego stycznia, o osiemnastej.",
"Jeśli lubicie takie historie, zostawcie łapkę w górę i zasubskrybujcie kanał.",
"Sol i Sól. Wszystko, co ważne na Costa del Sol."]),
]
def part(n): return "\n\n".join(p for c in CH if c[0]==n for p in c[2])
if __name__=="__main__":
    for n in (1,2,3): t=part(n); print(n, len(t), len(t.split()))
