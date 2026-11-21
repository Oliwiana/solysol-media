# Pobiera oferty rynku wtórnego z llnmarbella.com/rynek-wtorny (wyszukiwarka MLS) – uruchamiane w GitHub Actions (lln-oferty.yml).
# Użycie: python3 oferty.py '<json>' katalog_wyjściowy
# json: {"types":["Willa","Penthouse"], "areas":["Marbella","Estepona"], "min":0, "max":10000000, "beds":0, "baths":0,
#        "features":["Przy plaży","Widoki na morze"], "match":"all"|"any", "sort":"price_desc"|"price_asc"|"newest"|"oldest",
#        "keyword":"", "pages":3, "details":30, "photos":14}
# Wynik: oferty.json (lista ofert z danymi i adresami zdjęć), <ref>/NN.jpg (zdjęcia 1200 px), <ref>/sheet.jpg (podgląd ponumerowanych zdjęć),
#        opcje.json (wszystkie dostępne rodzaje, obszary i cechy z formularza).
import json, re, sys, os, html, time, io
import requests
from PIL import Image, ImageDraw

Q = json.loads(sys.argv[1] or "{}"); OUT = sys.argv[2]; os.makedirs(OUT, exist_ok=True)
BASE = "https://llnmarbella.com"
S = requests.Session(); S.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
U = lambda s: html.unescape(re.sub(r"<[^>]+>", " ", s)).strip()

page = S.get(BASE + "/rynek-wtorny/", timeout=60).text
form = page[page.find('id="search_form"'):]; form = form[:form.find("</form>")]
hidden = dict(re.findall(r'<input type="hidden" name="([^"]+)"[^>]*value="([^"]*)"', form))
def opts(select_id):
    i = form.find(f'id="{select_id}"'); blk = form[i:form.find("</select>", i)]
    return {U(t): v for v, t in re.findall(r'<option[^>]*value="([^"]*)"[^>]*>([^<]*)</option>', blk)}
types = opts("mls_search_type"); areas = {k: v for k, v in opts("mls_search_area").items()} if 'id="mls_search_area"' in form else {}
if not areas:
    i = form.find('name="mls_search_area[]"'); blk = form[i:form.find("</select>", i)]
    areas = {U(t): v for v, t in re.findall(r'<option value="([^"]*)"[^>]*>([^<]*)</option>', blk)}
feats = {}  # label -> (field, value)
for field, val, lab in re.findall(r"name='(mls_search_feature_[^']+)\[\]' value='([^']+)' >\s*<label[^>]*>([^<]+)</label>", form):
    feats.setdefault(U(lab), (field + "[]", val))
cats = re.findall(r"<h2 class='mls-af-accodian-title'>([^<]+)</h2>", form)
json.dump({"types": list(types), "areas": list(areas), "features": list(feats), "feature_groups": cats}, open(f"{OUT}/opcje.json", "w"), ensure_ascii=False, indent=1)

def norm(s): return re.sub(r"\s+", " ", s.lower().strip())
def pick(d, names, what):
    r = []
    for n in names:
        hit = [v for k, v in d.items() if norm(k) == norm(n)] or [v for k, v in d.items() if norm(n) in norm(k)]
        if hit: r.append(hit[0])
        else: print(f"UWAGA: nie znam {what}: {n}")
    return r

data = [(k, v) for k, v in hidden.items() if k not in ("p_sorttype",)]
data.append(("p_sorttype", {"price_asc": "0", "price_desc": "1", "location": "2", "newest": "3", "oldest": "4"}.get(Q.get("sort", "newest"), "3")))
data.append(("min_price", str(Q.get("min", 0)))); data.append(("max_price", str(Q.get("max", 10000000))))
data.append(("mls_search_beds", str(Q.get("beds", "") or ""))); data.append(("mls_search_baths", str(Q.get("baths", "") or "")))
data.append(("mls_search_keyword", Q.get("keyword", "")))
for v in pick(types, Q.get("types", []), "rodzaju"): data.append(("mls_search_type[]", v))
for v in pick(areas, Q.get("areas", []), "obszaru"): data.append(("mls_search_area[]", v))
for lab in Q.get("features", []):
    hit = [fv for k, fv in feats.items() if norm(k) == norm(lab)] or [fv for k, fv in feats.items() if norm(lab) in norm(k)]
    if hit: data.append(hit[0])
    else: print(f"UWAGA: nie znam cechy: {lab}")
data.append(("mls_search_features_search_type", "2" if Q.get("match", "all") == "all" else "1"))
data.append(("mls_search_submit", "Wyszukaj"))
r = S.post(BASE + "/wp-admin/admin-post.php", data=data, timeout=90, allow_redirects=True)
qid = re.search(r"query_id=([0-9a-f-]{20,})", r.url) or re.search(r"query_id=([0-9a-f-]{20,})", r.text)
SORT = dict(data)["p_sorttype"]
RES = lambda p: f"{BASE}/rynek-wtorny/?mls_search_performed=1&query_id={qid.group(1)}&page_num={p}&p_sorttype={SORT}"
res = S.get(RES(1), timeout=60).text if qid else r.text
print("wyniki:", RES(1) if qid else r.url)

def cards(h):
    out = []
    for blk in h.split('class="mls-property-box')[1:]:
        m = re.search(r'<h2>\s*<a href="([^"]+)"[^>]*>(.*?)</a>', blk, re.S)
        if not m: continue
        url = html.unescape(m.group(1)).replace("&#038;", "&")
        price = re.search(r"<h3>([^<]*)</h3>", blk)
        ref = re.search(r"Ref:\s*(R?\d+)", blk)
        f = {alt: U(v) for alt, v in re.findall(r'alt="([^"]+)"\s*/?>\s*<span>(.*?)</span>', blk, re.S)}
        out.append({"url": url, "title": U(m.group(2)), "price": U(price.group(1)) if price else "", "ref": ref.group(1) if ref else "",
                    "beds": f.get("Bedrooms", ""), "baths": f.get("Bathrooms", ""), "built": f.get("Built Area", "").replace(" 2", "²"),
                    "terrace": f.get("Terrace", "").replace(" 2", "²"), "plot": f.get("Plot", f.get("Plot Size", "")).replace(" 2", "²")})
    return out

L = cards(res)
for p in range(2, int(Q.get("pages", 3)) + 1):
    if not qid: break
    L += cards(S.get(RES(p), timeout=60).text); time.sleep(1)
seen = set(); L = [x for x in L if not (x["url"] in seen or seen.add(x["url"]))]
print("ofert na liście:", len(L))

def detail(o):
    h = S.get(re.sub(r"[?&]lang=\d+", "", o["url"]).replace("?type=81709&", "?type=81709"), timeout=60).text  # wersja EN – stałe etykiety
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    lines = [l.strip() for l in html.unescape(re.sub(r"<[^>]+>", "\n", t)).split("\n") if l.strip()]
    def after(lbl):
        try: return lines[lines.index(lbl) + 1]
        except ValueError: return ""
    o["location"] = after("Location"); o["type"] = after("Property type")
    feat = {}
    if "Features" in lines:
        i = lines.index("Features") + 1
        while i < len(lines) - 1 and lines[i] not in ("Description", "Amenities"):
            feat[lines[i]] = lines[i + 1]; i += 2
    o["features"] = feat
    if "Description" in lines:
        i = lines.index("Description") + 1; d = []
        while i < len(lines) and lines[i] not in ("Amenities", "Property Location (Approximate)", "Book a Viewing"): d.append(lines[i]); i += 1
        o["description"] = "\n".join(d)
    o["photos"] = list(dict.fromkeys(re.findall(r"https://cdn\.resales-online\.com/[^\"' ]+/w1200/[^\"' ]+\.jpg[^\"' ]*", h)))
    o["photos"].sort(key=lambda u: int(re.search(r"/w1200/(\d+)-", u).group(1)) if re.search(r"/w1200/(\d+)-", u) else 999)
    return o

N = int(Q.get("details", 30)); NP = int(Q.get("photos", 14))
for o in L[:N]:
    try: detail(o)
    except Exception as e: o["error"] = str(e)
    if NP and o.get("photos"):
        d = f"{OUT}/{o['ref'] or 'x'}"; os.makedirs(d, exist_ok=True); th = []
        for k, u in enumerate(o["photos"][:NP], 1):
            try:
                im = Image.open(io.BytesIO(S.get(u, timeout=60).content)).convert("RGB")
                im.save(f"{d}/{k:02d}.jpg", quality=88); th.append(im)
            except Exception: pass
        if th:
            cols = 4; w, hh = 300, 200; rows = (len(th) + cols - 1) // cols
            sh = Image.new("RGB", (cols * w, rows * hh), "black"); dr = ImageDraw.Draw(sh)
            for k, im in enumerate(th):
                x, y = k % cols * w, k // cols * hh; t2 = im.copy(); t2.thumbnail((w - 4, hh - 4)); sh.paste(t2, (x + 2, y + 2))
                dr.rectangle([x + 4, y + 4, x + 40, y + 30], fill="black"); dr.text((x + 10, y + 9), f"{k+1:02d}", fill="white")
            sh.save(f"{d}/sheet.jpg", quality=80)
    time.sleep(0.5)
json.dump({"query": Q, "url": r.url, "count": len(L), "offers": L}, open(f"{OUT}/oferty.json", "w"), ensure_ascii=False, indent=1)
print("gotowe:", len(L), "ofert,", sum(1 for o in L if o.get("photos")), "ze szczegółami")
