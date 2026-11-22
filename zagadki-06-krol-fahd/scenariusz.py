# Scenariusz Zagadki #6 – tekst dla lektora (liczby słownie). Rozdziały: (część, tytuł, akapity)
CH = [
(1,"Otwarcie",[
"Sierpień dwa tysiące drugiego roku. Lotnisko w Maladze. Na płytę kołują kolejne samoloty z Bliskiego Wschodu. Z jednego z nich zjeżdża wózek inwalidzki. Na nim siedzi starszy mężczyzna, który od lat jest jednym z najbogatszych ludzi na świecie.",
"Czekają limuzyny, policja, dziesiątki aut z bagażami. Kolumna rusza w stronę Marbelli. Sklepikarze, hotelarze i jubilerzy w całym mieście wiedzą już, co to oznacza. Przyleciał król.",
"Fahd, król Arabii Saudyjskiej. Człowiek, który w Marbelli postawił pałac podobny do Białego Domu. I którego letnie wizyty potrafiły zmienić rytm całego miasta.",
"To Sol i Sól i „Zagadki Costa del Sol”. Odcinek szósty. Król Fahd i saudyjska Marbella."]),
(1,"Biały Dom na Złotej Mili",[
"Zacznijmy od pałacu. Stoi przy Złotej Mili, między Marbellą a Puerto Banús. Nazywa się Mar-Mar. Kto widzi go pierwszy raz, przeciera oczy. Kolumny, biała fasada, portyk. Prasa na całym świecie pisze o nim jedno: to mała wersja Białego Domu z Waszyngtonu.",
"Pałac powstaje na początku lat osiemdziesiątych. Na działce stają kolejne budynki. Wille dla gości, pawilony dla służby, lądowisko dla helikopterów, a nawet prywatna klinika.",
"Zdaniem redakcji to nie jest letni dom. To małe miasteczko, zbudowane tak, żeby król mógł przenieść tu na kilka tygodni cały swój dwór."]),
(1,"Minaret nad Marbellą",[
"Obok pałacu wyrasta coś, czego na Costa del Sol wcześniej nie było. Biały minaret.",
"W tysiąc dziewięćset osiemdziesiątym pierwszym roku zostaje ukończony meczet Króla Abdulaziza, nazwany na cześć ojca Fahda, założyciela państwa saudyjskiego. Budowę finansuje rząd Arabii Saudyjskiej. Styl nawiązuje do architektury andaluzyjskiej.",
"Meczet działa do dziś. Dla wielu turystów to pierwszy znak, że ta część Marbelli od dekad ma bardzo bliskie związki z Zatoką Perską."]),
(2,"Lato, gdy przylatuje dwór",[
"Wróćmy do wizyt. Dwie zostały w pamięci miasta szczególnie mocno. Latem tysiąc dziewięćset dziewięćdziesiątego dziewiątego roku i latem dwa tysiące drugiego roku.",
"W dwa tysiące drugim roku król przylatuje z Genewy, gdzie spędził wcześniej kilka miesięcy. Ma już ponad osiemdziesiąt lat. Od udaru w tysiąc dziewięćset dziewięćdziesiątym piątym roku porusza się na wózku.",
"Razem z nim na lotnisku ląduje około czterystu osób. To dopiero początek. W kolejnych dniach dwór rośnie. Według różnych relacji w szczytowym momencie wokół króla w Marbelli jest nawet około trzech tysięcy ludzi. Rodzina, ministrowie, ochrona, lekarze, kucharze, kierowcy.",
"Wszyscy muszą gdzieś mieszkać. W hotelach na wybrzeżu rezerwowane są setki pokoi. Pod bramą pałacu ustawiają się kolejki miejscowych, którzy chcą dostać choć sezonową pracę."]),
(2,"Miliony dziennie",[
"A teraz pieniądze. I tu każde źródło podaje inne liczby. Jedni piszą o trzech milionach funtów dziennie. Inni o pięciu milionach dolarów dziennie. Wszyscy zgadzają się w jednym. Chodziło o miliony. Każdego dnia.",
"Kwiaciarnie, cukiernie, salony samochodowe, sklepy z zegarkami. Jubilerzy w Marbelli i w Puerto Banús uzupełniają witryny przed przylotem króla. Na wybrzeżu krąży opowieść o napiwku w wysokości dwustu trzydziestu pięciu tysięcy euro.",
"Zdaniem redakcji trudno dziś sprawdzić każdą z tych historii. Ale jedno jest pewne. Dla wielu firm z Marbelli tych kilka tygodni lata znaczyło więcej niż cały sezon turystyczny."]),
(3,"Pożegnanie króla",[
"Lato dwa tysiące drugiego roku okazuje się jednym z ostatnich takich spektakli. W sierpniu dwa tysiące piątego roku król Fahd umiera w Rijadzie.",
"Marbella nie zapomina. Jego imię nosi dziś w mieście ulica i ogród. Ale wielki dwór już nie przylatuje tak jak dawniej.",
"Według reportaży z ostatnich lat część zabudowań dawnego królewskiego kompleksu stoi opuszczona. Rozbite szyby, graffiti, puste baseny. Biały Dom na Złotej Mili zaczyna przypominać dekorację po zakończonym filmie."]),
(3,"Trzydzieści milionów euro",[
"Ale historia saudyjskiej Marbelli wcale się nie skończyła. Latem dwa tysiące dwudziestego szóstego roku rada miasta zatwierdza plan zagospodarowania gruntów należących do saudyjskiej rodziny królewskiej, na wzgórzach nad Złotą Milą.",
"Spółka właściciela ma zapłacić miastu około trzydziestu milionów euro. W zamian będzie mogła rozbudować kompleks o kolejne rezydencje, w tym nowe pałace.",
"Haczyk? Miasto też ma wobec właścicieli rozliczenia za grunty. Dlatego po wszystkich rachunkach do miejskiej kasy trafi tylko część tej kwoty."]),
(3,"Epilog",[
"Zdaniem redakcji to najlepiej pokazuje, czym była i jest saudyjska Marbella. Nie przygodą jednego lata, tylko trwającą ponad czterdzieści lat relacją. Miasto zarabiało na królu. A królewska rodzina do dziś zostawia tu ślad.",
"To były „Zagadki Costa del Sol”. Jeśli chcecie kolejną historię, zostawcie łapkę w górę i zasubskrybujcie kanał. W następnym odcinku, w niedzielę trzeciego stycznia, opowiemy o człowieku, który uczynił z Marbelli swoje królestwo. Jesús Gil.",
"Sol i Sól. Wszystko, co ważne na Costa del Sol. Do usłyszenia w niedzielę o osiemnastej."]),
]
def part(n): return "\n\n".join(p for c in CH if c[0]==n for p in c[2])
if __name__=="__main__":
    for n in (1,2,3): t=part(n); print(n, len(t), len(t.split()))
