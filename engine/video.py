"""Vidéo TikTok MathSquads : scènes fixes + voix off Kokoro + sous-titres incrustés."""
import json, sys, os, subprocess, re
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from render import render, W, H, P, I, INK, WHITE, CORAL, wrap, ASSETS, tl, tx
import soundfile as sf, numpy as np
from kokoro_onnx import Kokoro

K = Kokoro(ASSETS + "/voices/kokoro-v1.0.onnx", ASSETS + "/voices/voices-v1.0.bin")
SR = 24000
ENC = ["-c:v", "libx264", "-crf", "20", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", "30"]


def tts(text, speed=1.08):
    s, sr = K.create(text, voice="ff_siwis", speed=speed, lang="fr-fr")
    assert sr == SR
    return s


def chunks(text, maxw=4):
    words = text.split(); out = []; cur = []
    for w in words:
        cur.append(w)
        if len(cur) >= maxw or re.search(r"[.?!:,]$", w):
            out.append(" ".join(cur)); cur = []
    if cur: out.append(" ".join(cur))
    return out


def caption(img, text, y=1430):
    d = ImageDraw.Draw(img); f = P(700, 62)
    lines = wrap(d, text, f, 860); lh = int(f.size * 1.25)
    h = lh * len(lines) + 50
    wmax = max(tl(d, l, f) for l in lines)
    d.rounded_rectangle(((W - wmax) / 2 - 40, y, (W + wmax) / 2 + 40, y + h), 28, fill=INK)
    yy = y + 22
    for l in lines:
        tx(d, ((W - tl(d, l, f)) / 2, yy), l, f, WHITE); yy += lh


def still(png, dur, out):
    tmp = out[:-4] + ".part.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", "30", "-i", png, "-vf",
                    f"format=yuv420p,loop=-1:1,trim=duration={dur:.3f}", *ENC, tmp], check=True)
    os.rename(tmp, out)


def build(spec_path, outdir):
    spec = json.load(open(spec_path)); os.makedirs(outdir, exist_ok=True)
    slides = spec["slides"]; clips = []; audio = []; n = 0
    for si, sc in enumerate(spec["scenes"]):
        base = f"{outdir}/base{si}.png"
        render(slides[sc["slide"]], sc["slide"], len(slides), base)
        if "countdown" in sc:
            for c in range(sc["countdown"], 0, -1):
                im = Image.open(base).convert("RGB"); d = ImageDraw.Draw(im)
                d.ellipse((W/2 - 130, 1380, W/2 + 130, 1640), fill=CORAL)
                f = P(800, 170); t = str(c); b = d.textbbox((0, 0), t, font=f)
                d.text((W/2 - (b[2]-b[0])/2 - b[0], 1510 - (b[3]-b[1])/2 - b[1]), t, font=f, fill=WHITE)
                fr = f"{outdir}/f{n}.png"; im.save(fr); clip = f"{outdir}/c{n}.mp4"; still(fr, 1.0, clip)
                clips.append(clip); n += 1
            audio.append(np.zeros(SR * sc["countdown"], dtype=np.float32))
            continue
        voice = tts(sc["say"]); pad = np.zeros(int(SR * 0.25), dtype=np.float32)
        seg = np.concatenate([voice, pad]); audio.append(seg)
        total = len(seg) / SR; parts = chunks(sc.get("sub", sc["say"]))
        weights = [len(p) for p in parts]; acc = 0.0
        for k, p in enumerate(parts):
            dur = total * weights[k] / sum(weights)
            # aligne sur la grille de 30 i/s pour éviter la dérive audio/vidéo
            start = round(acc * 30) / 30; acc += dur; end = round(acc * 30) / 30
            im = Image.open(base).convert("RGB"); caption(im, p)
            fr = f"{outdir}/f{n}.png"; im.save(fr); clip = f"{outdir}/c{n}.mp4"
            still(fr, end - start, clip); clips.append(clip); n += 1
    wav = f"{outdir}/voice.wav"; sf.write(wav, np.concatenate(audio), SR)
    lst = f"{outdir}/list.txt"; open(lst, "w").write("".join(f"file '{os.path.abspath(c)}'\n" for c in clips))
    silent = f"{outdir}/silent.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent], check=True)
    final = f"{outdir}/{spec['name']}.mp4"; tmp = final[:-4] + ".part.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-i", wav, "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-shortest", tmp], check=True)
    os.rename(tmp, final); print(final)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
