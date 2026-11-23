# Automatyczne naklejki-wycinanki na film (kolaż Sol y Sól, od 22.11.2026).
# python3 kolaz_auto.py WEJ.mp4 WYJ.mp4 "naklejka1,naklejka2,..." [unikaj "a-b,c-d"] [odstęp_s]
# Naklejki wskakują na cięciach (detekcja scen), rotują z listy, kolorowe koło pod spodem; omijają hak (3,5 s), końcówkę i okna `unikaj`.
import sys, json, subprocess, re, random
LIB = json.load(open('/tmp/sm/_assets/naklejki/lib.json'))
BLOB = ['#F2E35B', '#E8562A', '#5B7CFF', '#F2E35B', '#E8562A']
def cuts(v):
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', v, '-vf', "select='gt(scene,0.25)',showinfo", '-an', '-f', 'null', '-'], capture_output=True, text=True).stderr
    return [float(x) for x in re.findall(r'pts_time:([\d.]+)', out)]
def probe(v):
    j = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-show_entries', 'format=duration', '-of', 'json', v], capture_output=True, text=True).stdout)
    return j['streams'][0]['width'], j['streams'][0]['height'], float(j['format']['duration'])
def plan(v, names, avoid=(), gap=None, seed=1):
    W, H, D = probe(v); vert = H > W; gap = gap or (5.5 if D < 90 else 13)
    cs = [c for c in cuts(v) if 3.4 < c < D - 3.5]
    grid = [3.6 + i * gap for i in range(int((D - 7) / gap) + 1)]
    for g in grid:  # dopełnij tam, gdzie brak cięć
        if not any(abs(c - g) < gap * .6 for c in cs): cs.append(g)
    cs = sorted(c for c in cs if c < D - 3.5)
    rnd = random.Random(seed); S = []; last = -99; k = 0
    for i, c in enumerate(cs):
        if c - last < gap: continue
        nxt = next((x for x in cs[i + 1:] if x - c > 1.4), c + 2.6); t1 = min(c + 3.0, max(c + 1.6, nxt - .05), D - 3.2)
        if any(not (t1 < a or c > b) for a, b in avoid): continue
        n = names[k % len(names)]; k += 1; side = k % 2
        if vert:
            w = rnd.randint(300, 420); x = (1080 - w - rnd.randint(40, 90)) if side else rnd.randint(330, 420); y = rnd.randint(300, 430)
        else:
            w = rnd.randint(200, 250); x = rnd.randint(790, 840) - (w - 200) if side else rnd.randint(30, 60); y = rnd.randint(40, 70) if side else rnd.randint(70, 95)
        S.append(dict(src=LIB[n]['file'], t0=round(c, 3), t1=round(t1, 3), x=x, y=y, w=w, r=rnd.choice([-9, -6, -4, 4, 6, 9]),
                      blob=BLOB[k % len(BLOB)], bx=rnd.randint(-12, 8), by=rnd.randint(-18, -4), bs=rnd.randint(85, 110), name=n))
        last = c
    return S
if __name__ == '__main__':
    v, o, names = sys.argv[1], sys.argv[2], sys.argv[3].split(',')
    av = [tuple(map(float, p.split('-'))) for p in sys.argv[4].split(',')] if len(sys.argv) > 4 and sys.argv[4] else []
    gap = float(sys.argv[5]) if len(sys.argv) > 5 else None
    S = plan(v, names, av, gap); json.dump(S, open('/tmp/_spec.json', 'w'))
    print(len(S), 'naklejek:', ', '.join(f"{s['name']}@{s['t0']}" for s in S))
    subprocess.run(['node', '/tmp/sm/_tools/naklejki_reel.js', '/tmp/_spec.json', v, o], check=True)
    used = sorted({s['name'] for s in S}); json.dump(used, open(o + '.naklejki.json', 'w'))
