# Film z karuzeli ciekawostek LLN (gen_lln_fakty.py) – prawa kolumna siatki IG.
# Użycie: python3 mkreel_fakty.py katalog_ze_slajdami katalog_wyjściowy [sekundy_na_slajd]
# Bierze ig-01…ig-NN.jpg (1080×1350), obcina stopkę „Przesuń”, układa na granatowym tle 1080×1920,
# delikatny zoom + przenikanie → reel.mp4 (bez dźwięku – muzykę dodaje się w IG) i reel-cover.jpg (okładka w kadrze 3:4).
import sys, subprocess, glob
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
SRC = Path(sys.argv[1]); OUT = Path(sys.argv[2]).resolve(); OUT.mkdir(parents=True, exist_ok=True)
SEC = float(sys.argv[3]) if len(sys.argv) > 3 else 4.2
TMP = OUT / "fk_tmp"; TMP.mkdir(exist_ok=True)
NAVY = (15, 26, 51); ACC = (232, 160, 78); MUTED = (154, 166, 191)
FPS = 30; XF = 0.5
mono = "/home/claude/tools/node_modules/@fontsource/jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff"
slides = sorted(glob.glob(str(SRC / "ig-*.jpg")))
def frame(i, p):
    im = Image.open(p).convert("RGB")
    cut = 1130 if i == 0 else 1240          # 1. slajd: bez „@llnmarbella · Przesuń”, reszta: bez dolnej stopki
    im = im.crop((0, 0, 1080, cut))
    f = Image.new("RGB", (1080, 1920), NAVY)
    y = 240 + (1440 - cut) // 2            # środek kadru 3:4 (siatka profilu)
    f.paste(im, (0, y))
    d = ImageDraw.Draw(f)
    d.rectangle((0, y + cut, 1080, y + cut + 3), fill=ACC)
    try: fnt = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 26)
    except Exception: fnt = None
    t = "LLN MARBELLA  ·  COSTA DEL SOL"
    if fnt:
        w = d.textlength(t, font=fnt); d.text(((1080 - w) / 2, 1760), t, font=fnt, fill=MUTED)
    out = TMP / f"f{i:02d}.png"; f.save(out); return out
frames = [frame(i, p) for i, p in enumerate(slides)]
Image.open(frames[0]).convert("RGB").save(OUT / "reel-cover.jpg", quality=90)
parts = []
for i, fr in enumerate(frames):
    d = SEC + (0.6 if i == 0 else 0); n = int(d * FPS)
    z = f"'min(1+0.04*on/{n},1.04)'"
    o = TMP / f"p{i:02d}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-t", str(d), "-i", str(fr), "-vf",
                    f"scale=1188:2112,zoompan=z={z}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS},format=yuv420p",
                    "-t", str(d), "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(o)], check=True)
    parts.append((o, d))
ins = []; [ins.extend(["-i", str(p)]) for p, _ in parts]
fc = []; last = "[0:v]"; off = 0
for i in range(1, len(parts)):
    off += parts[i - 1][1] - XF; o = f"[x{i}]"
    fc.append(f"{last}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}{o}"); last = o
total = off + parts[-1][1]
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *ins, "-f", "lavfi", "-t", str(total), "-i", "anullsrc=r=44100:cl=stereo",
                "-filter_complex", ";".join(fc), "-map", last, "-map", f"{len(parts)}:a", "-shortest", "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "25", "-maxrate", "850k", "-bufsize", "1700k", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(OUT / "reel.mp4")], check=True)
print("ok", OUT / "reel.mp4", f"{total:.1f}s")
