#!/usr/bin/env python3
"""Pobiera RSS źródeł Sol y Sól i zapisuje _feeds/latest.json (status + artykuły z 48 h)."""
import json, re, time, datetime as dt, urllib.request, email.utils, html
from xml.etree import ElementTree as ET
UA = {"User-Agent": "Mozilla/5.0 (SolySol feed monitor; +https://solysol.pl)"}
SOURCES = [
 ("The Spanish Eye", "https://www.thespanisheye.com/", ["https://www.thespanisheye.com/feed/", "https://www.thespanisheye.com/rss", "https://www.thespanisheye.com/feed"]),
 ("Diario Sur", "https://www.diariosur.es/", ["https://www.diariosur.es/rss/2.0/portada", "https://www.diariosur.es/rss/2.0/?section=malaga"]),
 ("La Opinión de Málaga", "https://www.laopiniondemalaga.es/", ["https://www.laopiniondemalaga.es/rss/", "https://www.laopiniondemalaga.es/rss/section/1"]),
 ("Málaga Hoy", "https://www.malagahoy.es/", ["https://www.malagahoy.es/rss/", "https://www.malagahoy.es/rss/malaga/"]),
 ("Marbella24horas", "https://www.marbella24horas.es/", ["https://www.marbella24horas.es/feed/", "https://www.marbella24horas.es/rss/"]),
 ("Área Costa del Sol", "https://www.areacostadelsol.com/", ["https://www.areacostadelsol.com/feed/"]),
 ("Sur in English", "https://www.surinenglish.com/", ["https://www.surinenglish.com/rss/2.0/portada"]),
 ("Euro Weekly News", "https://weeklynews.co.uk/", ["https://weeklynews.co.uk/feed/"]),
 ("Olive Press", "https://www.theolivepress.es/", ["https://www.theolivepress.es/feed/"]),
 ("101TV Málaga", "https://www.101tv.es/", ["https://www.101tv.es/rss/", "https://www.101tv.es/feed/"]),
 ("Europa Press Andalucía", "https://www.europapress.es/andalucia/", ["https://www.europapress.es/rss/rss.aspx?ch=00279"]),
]
def get(url, t=25):
    r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t)
    return r.status, r.read()
def discover(home):
    try:
        _, b = get(home)
        h = b.decode("utf-8", "ignore")
        return [html.unescape(m) if m.startswith("http") else home.rstrip("/") + "/" + m.lstrip("/")
                for m in re.findall(r'<link[^>]+type="application/(?:rss|atom)\+xml"[^>]+href="([^"]+)"', h)]
    except Exception:
        return []
def parse(b):
    root = ET.fromstring(b)
    out = []
    for it in root.iter():
        tag = it.tag.split("}")[-1]
        if tag not in ("item", "entry"): continue
        f = {c.tag.split("}")[-1]: (c.text or c.get("href") or "") for c in it}
        d = f.get("pubDate") or f.get("published") or f.get("updated") or f.get("date") or ""
        try: ts = email.utils.parsedate_to_datetime(d).timestamp()
        except Exception:
            try: ts = dt.datetime.fromisoformat(d.replace("Z", "+00:00")).timestamp()
            except Exception: ts = None
        out.append({"title": html.unescape(re.sub("<[^>]+>", "", f.get("title", ""))).strip(),
                    "link": f.get("link", "").strip(), "ts": ts,
                    "summary": html.unescape(re.sub("<[^>]+>", " ", f.get("description") or f.get("summary") or ""))[:300].strip()})
    return out
now = time.time(); res = {"checked": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "sources": [], "items": []}
for name, home, cands in SOURCES:
    st = {"name": name, "ok": False, "feed": None, "count": 0, "newest": None, "error": None}
    for u in cands + discover(home):
        try:
            code, b = get(u); items = parse(b)
            if not items: raise ValueError("pusty kanał")
            st.update(ok=True, feed=u, count=len(items), error=None)
            ts = [i["ts"] for i in items if i["ts"]]
            if ts: st["newest"] = dt.datetime.utcfromtimestamp(max(ts)).strftime("%Y-%m-%dT%H:%M:%SZ")
            for i in items:
                if i["ts"] is None or now - i["ts"] < 48 * 3600:
                    i["source"] = name
                    if i["ts"]: i["time"] = dt.datetime.utcfromtimestamp(i["ts"]).strftime("%Y-%m-%dT%H:%M:%SZ")
                    i.pop("ts", None); res["items"].append(i)
            break
        except Exception as e:
            st["error"] = f"{u}: {type(e).__name__} {str(e)[:80]}"
    res["sources"].append(st)
res["items"].sort(key=lambda i: i.get("time", ""), reverse=True)
json.dump(res, open("_feeds/latest.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps([(s["name"], s["ok"], s["count"], s["newest"]) for s in res["sources"]], ensure_ascii=False))
