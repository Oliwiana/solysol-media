# Sol y Sól Studio – szablony produkcji (wzorce z 25.11.2026)

Aplikacja: https://claude.ai/artifact/GFW2TBPk7b5CaULMvkPXjz (slug 7b7f6146-c581-46e0-8e3b-ab7fa0ace4b5), kolekcja `plan`.

- `karuzela-okladka/` – LEWA kolumna: karuzela 1080×1350 w stylu okładki magazynu (pasek DZIŚ·data·SOLYSOL.PL, winieta SOL Y SÓL, ramka z żółtym akcentem, żółta taśma, okrągła plakietka „ODCINEK n / PRZESUŃ →”, nadtytuł żółty, tytuł Cormorant z kursywą, 3 kolumny na dole, kropki postępu). gen.py → p*.html, shot.js → post-N.jpg. Kolor tła dopasuj do tematu (fiolet 25N, granat domyślnie).
- `bond-reel/` – PRAWA kolumna (kryminał/afera): tablica śledcza – kartki z pinezkami, czerwone nitki, pieczątki z błyskiem i drżeniem, licznik roku, oś czasu, ziarno, napisy słowo po słowie, intro 3 haseł. build.py cfg.json → pro.html; rend4.js renderuje (puppeteer 30 fps). Cfg: seg[] = starty segmentów lektora (silencedetect), caps[], c{} = momenty pieczątek.
- `mapa-reel/` – ŚRODEK (przyziemne/dane): animowana mapa wybrzeża, liczniki, rozdziały 01/09, napisy bez belki, wipe, plansza końcowa z logo. Ten sam schemat cfg.
- `okladka-zolta/` – okładka Zagadek (żółta, halftone, naklejki).

Dźwięk: lektor ElevenLabs Dariusz (voice mGixAdrjHFNdj6tN93zP, model eleven_v4), przyspieszenie atempo 1.2; muzyka ElevenLabs music (eleven_music_v2_5) – noir do kryminałów, newsowa do przyziemnych; ducking sidechaincompress, „boom” na pieczątkach, „whoosh” przy zmianie sceny. Na początku reela 1,6 s okładki. NIE pisać w treściach, że użyto ElevenLabs.
Wymagania: fonty @fontsource (inter, cormorant-garamond, special-elite, anton) w /home/claude/tools/node_modules; puppeteer-core; /usr/bin/google-chrome; ffmpeg.
