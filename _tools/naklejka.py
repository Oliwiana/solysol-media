# Naklejka-wycinanka do kolaży Sol y Sól (od 22.11.2026).
# Wycina obiekt ze zdjęcia (rembg), robi wersję cz-b z rastrem (halftone) albo kolorową, dodaje gruby biały obrys i cień.
# Użycie: python3 naklejka.py WEJ.jpg WYJ.png [bw|color|halftone] [szer_px]
import sys, numpy as np, cv2
from PIL import Image, ImageOps, ImageEnhance, ImageFilter
from rembg import remove, new_session
_S = None
def cut(src, mode='bw', width=700, outline=14, shadow=True):
    global _S
    if _S is None: _S = new_session('isnet-general-use')
    im = Image.open(src).convert('RGB'); im.thumbnail((1400, 1400))
    rgba = remove(im, session=_S, post_process_mask=True)
    a = np.array(rgba.split()[-1]); a = (a > 128).astype(np.uint8) * 255
    n, lab, st, _ = cv2.connectedComponentsWithStats(a)           # zostaw największy obiekt
    if n > 1:
        k = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA])); a = np.where(lab == k, 255, 0).astype(np.uint8)
    a = cv2.morphologyEx(a, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    rgb = rgba.convert('RGB')
    if mode in ('bw', 'halftone'):
        g = ImageOps.autocontrast(rgb.convert('L'), cutoff=2); g = ImageEnhance.Contrast(g).enhance(1.35)
        if mode == 'halftone':
            arr = np.array(g, dtype=np.float32) / 255; h, w = arr.shape; cell = max(5, w // 110)
            out = np.full((h, w), 255, np.uint8)
            for y in range(0, h, cell):
                for x in range(0, w, cell):
                    v = arr[y:y + cell, x:x + cell].mean(); r = (1 - v) * cell * .72
                    if r > .6: cv2.circle(out, (x + cell // 2, y + cell // 2), int(round(r)), 0, -1, cv2.LINE_AA)
            g = Image.fromarray(out)
        rgb = g.convert('RGB')
    else:
        rgb = ImageEnhance.Color(rgb).enhance(1.25); rgb = ImageEnhance.Contrast(rgb).enhance(1.1)
    ys, xs = np.where(a > 0); x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    rgb = rgb.crop((x0, y0, x1 + 1, y1 + 1)); a = a[y0:y1 + 1, x0:x1 + 1]
    sc = width / rgb.width; rgb = rgb.resize((width, max(1, int(rgb.height * sc))), Image.LANCZOS)
    a = cv2.resize(a, rgb.size, interpolation=cv2.INTER_LINEAR)
    P = outline * 2 + 30; W, H = rgb.width + 2 * P, rgb.height + 2 * P
    am = np.zeros((H, W), np.uint8); am[P:P + rgb.height, P:P + rgb.width] = a
    ring = cv2.dilate(am, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (outline * 2 + 1, outline * 2 + 1)))
    ring = cv2.GaussianBlur(ring, (3, 3), 0)
    canvas = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    if shadow:
        sh = cv2.GaussianBlur(ring, (0, 0), 9); sh = (sh * .45).astype(np.uint8)
        shimg = Image.new('RGBA', (W, H), (0, 0, 0, 0)); shimg.putalpha(Image.fromarray(np.roll(np.roll(sh, 12, 0), 8, 1)))
        canvas = Image.alpha_composite(canvas, shimg)
    white = Image.new('RGBA', (W, H), (255, 255, 255, 0)); white.putalpha(Image.fromarray(ring)); canvas = Image.alpha_composite(canvas, white)
    obj = Image.new('RGBA', (W, H), (0, 0, 0, 0)); obj.paste(rgb, (P, P)); obj.putalpha(Image.fromarray(am))
    return Image.alpha_composite(canvas, obj)
if __name__ == '__main__':
    m = sys.argv[3] if len(sys.argv) > 3 else 'bw'; w = int(sys.argv[4]) if len(sys.argv) > 4 else 700
    cut(sys.argv[1], m, w).save(sys.argv[2])
