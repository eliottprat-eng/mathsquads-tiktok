"""Vidéo TikTok MathSquads : écrans + transitions + voix off + sous-titres + musique + bruitages.

Les images sont composées en Python image par image et envoyées directement à ffmpeg (pas de PNG
intermédiaires). Transitions : « push » horizontal entre écrans, fondu vers l'écran final (promo).
"""
import json, sys, os, subprocess, re
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import render, W, H, P, INK, WHITE, CORAL, wrap, tl, tx
import soundfile as sf
import audio

FPS = 30
TRANS = 0.4          # durée des transitions entre écrans (s)
CAP_Y = 1430         # position des sous-titres
OPS = {"=", "+", "−", "-", "×", "÷", "→", "<", ">", "≈", "±"}
ANSWER_PILLS = ("RÉPONSE", "VRAI", "RÉSULTAT", "À RETENIR", "ÉTAPE 3")


def chunks(text, maxw=4):
    words = text.split(); out, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        nxt = words[i + 1] if i + 1 < len(words) else None
        glued = w in OPS or (nxt in OPS) or bool(nxt and re.match(r"^[€%°)]", nxt))
        if (len(cur) >= maxw and not glued) or re.search(r"[.?!:,]$", w) or len(cur) >= maxw + 3:
            out.append(" ".join(cur)); cur = []
    if cur: out.append(" ".join(cur))
    return out


def caption_img(text):
    f = P(700, 62); d = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    lines = wrap(d, text, f, 860); lh = int(f.size * 1.25)
    wmax = max(tl(d, l, f) for l in lines); bw, bh = int(wmax + 80), lh * len(lines) + 50
    im = Image.new("RGBA", (bw, bh), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, bw - 1, bh - 1), 28, fill=INK)
    y = 22
    for l in lines:
        tx(d, ((bw - tl(d, l, f)) / 2, y), l, f, WHITE); y += lh
    return im


def number_img(c):
    im = Image.new("RGBA", (260, 260), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((0, 0, 259, 259), fill=CORAL)
    f = P(800, 170); t = str(c); b = d.textbbox((0, 0), t, font=f)
    d.text((130 - (b[2] - b[0]) / 2 - b[0], 130 - (b[3] - b[1]) / 2 - b[1]), t, font=f, fill=WHITE)
    return im


def ease(p): return 1 - (1 - p) ** 3


def zoomed(img, age):
    """Zoom lent (2 % sur 8 s) pour donner du mouvement aux écrans fixes."""
    z = 1 + 0.02 * min(1, max(0, age) / 8)
    if z < 1.0005: return img.copy()
    bw, bh = int(W * z), int(H * z)
    return img.resize((bw, bh), Image.BILINEAR).crop(((bw - W) // 2, (bh - H) // 2, (bw - W) // 2 + W, (bh - H) // 2 + H))


def paste_scaled(frame, ov, cx, top, s, alpha=1.0):
    if s != 1.0:
        ov = ov.resize((max(1, int(ov.width * s)), max(1, int(ov.height * s))), Image.BILINEAR)
    if alpha < 1.0:
        a = ov.getchannel("A").point(lambda v: int(v * alpha)); ov = ov.copy(); ov.putalpha(a)
    frame.alpha_composite(ov, (int(cx - ov.width / 2), int(top + (1 - s) * ov.height / 2)))


def build(spec_path, outdir):
    spec = json.load(open(spec_path)); os.makedirs(outdir, exist_ok=True)
    slides = spec["slides"]; n_sl = len(slides)
    bases = []
    for i, s in enumerate(slides):
        p = f"{outdir}/slide{i}.png"; render(s, i, n_sl, p); bases.append(Image.open(p).convert("RGBA"))

    # ---- chronologie : segments (début, durée, écran, sous-titre | nombre) + voix + bruitages
    segs, voice, events, t = [], [], [], 0.0
    shown = set()
    for sc in spec["scenes"]:
        sl = sc["slide"]
        if sl not in shown:
            shown.add(sl)
            if t > 0: events.append((max(0, t - 0.12), "whoosh"))
            pill = next((e["t"] for e in slides[sl]["els"] if e["k"] == "pill"), "")
            if slides[sl].get("dark"): events.append((t + 0.25, "chime"))
            elif pill.startswith(ANSWER_PILLS): events.append((t + 0.3, "ding"))
        if "countdown" in sc:
            for c in range(sc["countdown"], 0, -1):
                segs.append((t, 1.0, sl, ("num", c))); events.append((t, "tick")); t += 1.0
            voice.append(np.zeros(int(audio.SR * sc["countdown"]), np.float32)); continue
        v = audio.tts(sc["say"]); pad = np.zeros(int(audio.SR * 0.25), np.float32)
        seg = np.concatenate([v, pad]); voice.append(seg); total = len(seg) / audio.SR
        parts = chunks(sc.get("sub", sc["say"])); wts = [len(x) for x in parts]; acc = 0.0
        for k, ptxt in enumerate(parts):
            d = total * wts[k] / sum(wts); segs.append((t + acc, d, sl, ("cap", ptxt))); acc += d
        t += total
    total = t + 0.6  # petite respiration finale
    voice = np.concatenate(voice)

    # premier instant où chaque écran apparaît (pour les transitions et le zoom lent)
    first = {}
    for st, d, sl, _ in segs: first.setdefault(sl, st)
    order = sorted(first, key=first.get)
    caps = {}

    # ---- rendu image par image vers ffmpeg
    silent = f"{outdir}/silent.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "20", "-preset", "veryfast",
                           "-pix_fmt", "yuv420p", silent], stdin=subprocess.PIPE)
    si = 0
    for fi in range(int(round(total * FPS))):
        tt = fi / FPS
        while si + 1 < len(segs) and segs[si + 1][0] <= tt: si += 1
        st, d, sl, item = segs[si]
        # zoom lent sur l'écran courant
        age = tt - first[sl]
        frame = zoomed(bases[sl], age)
        # transition depuis l'écran précédent
        k = order.index(sl)
        if k > 0 and age < TRANS:
            pv = order[k - 1]; prev = zoomed(bases[pv], first[sl] - first[pv]); p = ease(age / TRANS)
            if slides[sl].get("dark"):
                frame = Image.blend(prev, frame, p)
            else:
                o = int(p * W); fr = Image.new("RGBA", (W, H))
                fr.paste(prev.crop((o, 0, W, H)), (0, 0)); fr.paste(frame.crop((0, 0, o, H)), (W - o, 0)); frame = fr
        # sous-titre ou compte à rebours, avec petit effet « pop »
        local = tt - st; pp = min(1, local / 0.15); s = 0.9 + 0.1 * ease(pp)
        if item[0] == "cap":
            if item[1] not in caps: caps[item[1]] = caption_img(item[1])
            if not (k > 0 and age < TRANS * 0.7):
                paste_scaled(frame, caps[item[1]], W / 2, CAP_Y, s, pp)
        else:
            sn = 1.25 - 0.25 * ease(min(1, local / 0.2))
            paste_scaled(frame, number_img(item[1]), W / 2, 1380, sn)
        ff.stdin.write(frame.convert("RGB").tobytes())
    ff.stdin.close(); ff.wait()
    assert ff.returncode == 0

    # ---- audio + assemblage
    mixw = f"{outdir}/mix.wav"; sf.write(mixw, audio.mix(voice, events, spec.get("music", 0) % 3, total), audio.SR)
    final = f"{outdir}/{spec['name']}.mp4"; tmp = final[:-4] + ".part.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-i", mixw, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", tmp], check=True)
    os.rename(tmp, final); print(final)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
