# Reele „Gwiazdy na Costa del Sol” (wzór Bond, polaroidy na tablicy)
- Dane reela: _reels/<id>/data.py (linie lektora, `*słowo` = żółte wyróżnienie, zdjęcia na każdą linię, `PH:` = plansza „ZDJĘCIE – DODA REDAKCJA”).
- `python3 gen.py data.py` → /home/claude/gw/<id>/index.html + timeline.json; `node rend.js <id>` → video.mp4; `./finish.sh <id>` → reel.mp4 (<4 MB).
- Wersja z 22.11.2026 jest BEZ LEKTORA (brak kredytów ElevenLabs). Po nagraniu lektora: transkrypcja → podmień czasy słów w timeline (wdur) i w finish.sh zmiksuj lektor + podkład 0.3.
