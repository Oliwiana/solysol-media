#!/usr/bin/env python3
"""Pobiera zdjęcia z Wikimedia Commons (wolne licencje) do _photos/commons/<slug>/ z plikiem credits.json.
Użycie: python3 _tools/commons.py "zapytanie" [liczba]
Kilka zapytań w jednym przebiegu: "zapytanie 1 || zapytanie 2 || zapytanie 3" (każde do osobnego folderu)."""
import sys, os, re, json, urllib.request, urllib.parse
UA = {"User-Agent": "SolySolBot/1.0 (https://solysol.pl; redakcja@solysol.pl)"}

def fetch(q, n):
    slug = re.sub(r"[^a-z0-9]+", "-", q.lower()).strip("-")[:50]
    out = f"_photos/commons/{slug}"; os.makedirs(out, exist_ok=True)
    api = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode({
      "action": "query", "format": "json", "generator": "search", "gsrsearch": f"filetype:bitmap {q}",
      "gsrnamespace": 6, "gsrlimit": 40, "prop": "imageinfo", "iiprop": "url|size|extmetadata|mime", "iiurlwidth": 1800})
    d = json.load(urllib.request.urlopen(urllib.request.Request(api, headers=UA), timeout=40))
    pages = sorted(d.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    cred = []; i = 0
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
        if ii.get("mime") not in ("image/jpeg", "image/png") or ii.get("width", 0) < 1200: continue
        lic = m.get("LicenseShortName", {}).get("value", "")
        if not re.search(r"CC0|Public domain|CC BY", lic, re.I): continue
        i += 1; fn = f"{out}/{i:02d}.jpg"
        open(fn, "wb").write(urllib.request.urlopen(urllib.request.Request(ii.get("thumburl") or ii["url"], headers=UA), timeout=60).read())
        author = re.sub("<[^>]+>", "", m.get("Artist", {}).get("value", "")).strip()
        cred.append({"file": f"{i:02d}.jpg", "title": p["title"], "author": author, "license": lic, "source": ii.get("descriptionurl")})
        if i >= n: break
    json.dump(cred, open(f"{out}/credits.json", "w"), ensure_ascii=False, indent=1)
    print(out, len(cred))

n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
for q in [x.strip() for x in sys.argv[1].split("||") if x.strip()]:
    try: fetch(q, n)
    except Exception as e: print("ERR", q, e)
