"""Gabarit carrousel TikTok MathSquads (1080x1920)."""
from PIL import Image, ImageDraw, ImageFont
import sys, json, os
ASSETS = os.environ.get("MSQ_ASSETS", os.path.expanduser("~/msq-assets"))

W, H = 1080, 1920
CREAM, INK, CORAL, CORAL_LIGHT, GOLD, WHITE = "#FBF7F0", "#1B2A44", "#E1613E", "#FDF0EB", "#C99A3E", "#FFFFFF"
FD = ASSETS + "/fonts/package/files/poppins-latin-{}-normal.woff"
FI = ASSETS + "/fonts/inter/package/files/inter-latin-{}-normal.woff"


def P(w, s): return ImageFont.truetype(FD.format(w), s)
def I(w, s): return ImageFont.truetype(FI.format(w), s)


# --- Repli DejaVu pour les symboles absents de Poppins/Inter (√, ∞, ⁴, Δ, →…) ---
HERE = os.path.dirname(os.path.abspath(__file__))
_CMAPS, _FB = {}, {}
SUPS = set("⁰¹²³⁴⁵⁶⁷⁸⁹⁻ⁿ")


def _cmap(path):
    if path not in _CMAPS:
        from fontTools.ttLib import TTFont
        _CMAPS[path] = set(TTFont(path).getBestCmap())
    return _CMAPS[path]


def _fallback(font):
    bold = "poppins" in font.path or "-6" in font.path or "-7" in font.path or "-8" in font.path
    key = (bold, font.size)
    if key not in _FB:
        _FB[key] = ImageFont.truetype(f"{HERE}/fonts/DejaVuSans{'-Bold' if bold else ''}.ttf", int(font.size * 0.92))
    return _FB[key]


def runs(text, font):
    cm = _cmap(font.path)
    sup_fb = any(c in SUPS and ord(c) not in cm for c in text)  # exposants homogènes
    out = []
    for c in text:
        f = _fallback(font) if (ord(c) not in cm and c != " ") or (sup_fb and c in SUPS) else font
        if out and out[-1][1] is f: out[-1][0] += c
        else: out.append([c, f])
    return out


def tl(d, text, font):
    return sum(d.textlength(t, font=f) for t, f in runs(text, font))


def tx(d, xy, text, font, fill):
    x, y = xy; base = y + font.getmetrics()[0]
    for t, f in runs(text, font):
        d.text((x, base), t, font=f, fill=fill, anchor="ls"); x += d.textlength(t, font=f)


def wrap(d, text, font, maxw):
    lines = []
    for para in text.split("\n"):
        cur = ""
        for word in para.split(" "):
            t = (cur + " " + word).strip()
            if tl(d, t, font) <= maxw:
                cur = t
            else:
                lines.append(cur); cur = word
        lines.append(cur)
    return lines


def block(d, y, text, font, fill, maxw=880, gap=1.18, align="center"):
    for ln in wrap(d, text, font, maxw):
        w = tl(d, ln, font)
        x = (W - w) / 2 if align == "center" else 100
        tx(d, (x, y), ln, font, fill)
        y += int(font.size * gap)
    return y


def chrome(d, dark=False):
    fg = WHITE if dark else INK
    sq = WHITE if dark else CORAL
    d.rounded_rectangle((100, 110, 180, 190), 20, fill=sq)
    f = P(700, 38); t = "M²"
    b = d.textbbox((0, 0), t, font=f)
    d.text((140 - (b[2] - b[0]) / 2 - b[0], 150 - (b[3] - b[1]) / 2 - b[1]), t, font=f, fill=CORAL if dark else WHITE)
    d.text((200, 122), "MathSquads", font=P(700, 46), fill=fg)
    hf = I(600, 34); h = "@mathsquads.fr"
    d.text(((W - d.textlength(h, font=hf)) / 2, H - 150), h, font=hf, fill=fg)


def pill(d, y, text, bg=CORAL, fg=WHITE):
    f = P(600, 36); w = tl(d, text, f)
    d.rounded_rectangle(((W - w) / 2 - 36, y, (W + w) / 2 + 36, y + 76), 38, fill=bg)
    tx(d, ((W - w) / 2, y + 14), text, f, fg)
    return y + 76


def page_dots(d, i, n, dark=False):
    for k in range(n):
        x = W / 2 + (k - (n - 1) / 2) * 34
        c = (WHITE if dark else INK) if k == i else ("#F2A484" if dark else "#D9D2C5")
        d.ellipse((x - 8, H - 230, x + 8, H - 214), fill=c)


def render(slide, i, n, out):
    dark = slide.get("dark", False)
    im = Image.new("RGB", (W, H), CORAL if dark else CREAM)
    d = ImageDraw.Draw(im)
    chrome(d, dark)
    y = slide.get("top", 520)
    for el in slide["els"]:
        k = el["k"]
        if k == "pill":
            cols = [WHITE, CORAL] if dark else [el.get("bg", CORAL), WHITE]
            y = pill(d, y, el["t"], *cols) + el.get("after", 70)
        elif k == "h":
            y = block(d, y, el["t"], P(800, el.get("s", 96)), el.get("c", WHITE if dark else INK)) + el.get("after", 40)
        elif k == "big":
            s = el.get("s", 300)
            while tl(d, el["t"], P(800, s)) > 880 and s > 60:
                s -= 6
            y = block(d, y, el["t"], P(800, s), el.get("c", CORAL), gap=1.05) + el.get("after", 40)
        elif k == "p":
            y = block(d, y, el["t"], I(el.get("w", 400), el.get("s", 50)), el.get("c", WHITE if dark else INK), gap=1.4) + el.get("after", 40)
        elif k == "card":
            lines = el["t"].split("\n"); s = el.get("s", 80)
            while max(tl(d, l, P(700, s)) for l in lines) > 800 and s > 40:
                s -= 4
            f = P(700, s)
            hh = len(lines) * int(f.size * 1.35) + 90
            d.rounded_rectangle((100, y, W - 100, y + hh), 40, fill=el.get("bg", WHITE), outline=el.get("o"), width=6 if el.get("o") else 0)
            yy = y + 45
            for ln in lines:
                w = tl(d, ln, f); tx(d, ((W - w) / 2, yy), ln, f, el.get("c", INK)); yy += int(f.size * 1.35)
            y += hh + el.get("after", 50)
        elif k == "gap":
            y += el["v"]
    page_dots(d, i, n, dark)
    im.save(out)


if __name__ == "__main__":
    spec = json.load(open(sys.argv[1])); outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)
    for i, s in enumerate(spec["slides"]):
        render(s, i, len(spec["slides"]), f"{outdir}/{i+1:02d}.png")
