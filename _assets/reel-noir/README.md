# Reel NOIR – wzór (reel o Bondzie, 53 s)

- wzor-bond.mp4 – gotowy wzór: hak 6 s (duży napis + pytanie lektora), potem historia na zdjęciach (Ken Burns, zmiana co 2–4 s), napisy słowo po słowie, podkład _assets/zagadki/noir-bed.mp3 (~0.3 pod lektorem), na końcu „Obserwuj @solysol.pl”.
- hook.html – plansza haka 1080×1920 (styl _tools/noir.py: czarno-białe zdjęcie, ziarno, Oswald z podkreśleniem, kursywa Cormorant, etykiety niebieska #5b7cff i żółta #f2e35b).
- index9.html + rend9.js – animacja HTML renderowana klatka po klatce (puppeteer-core) – dostosuj teksty, zdjęcia i czasy do transkrypcji lektora.
- cover.html – okładka reela (= hak).
- Czcionki @fontsource: zawsze subsety latin + latin-ext (inaczej psuje się „ś”).
- Lektor: ElevenLabs creative_generate_speech, eleven_v4, voice mGixAdrjHFNdj6tN93zP, generations_count 1, flow K4uEgqHMS67vXeFy9jZA; pobieranie przez workflow fetch.yml; transkrypcja creative_transcribe_audio na znaczniki czasu. Marka czytana „Sol i Sól”.
- Gotowy reel musi mieć < 4 MB (automat publikacji czyta z aplikacji maks. 4 MB): ffmpeg -c:v libx264 -crf 28 -preset veryfast, ewentualnie 720×1280, audio aac 128k.
