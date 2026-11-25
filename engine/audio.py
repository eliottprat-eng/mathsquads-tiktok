"""Audio des vidéos : voix off (Kokoro), 3 musiques d'ambiance originales générées par code
(donc libres de droits), bruitages légers, et mixage avec ducking sous la voix."""
import os, re
import numpy as np
from scipy.signal import butter, sosfilt

SR = 24000
ASSETS = os.environ.get("MSQ_ASSETS", os.path.expanduser("~/msq-assets"))
_K = None

# Prononciations forcées (IPA) : la marque se dit « math - squads (anglais) - point - com ».
BRAND_IPA = [(re.compile(r"math ?squads", re.I), "mat skwˈɑdz")]


def _kokoro():
    global _K
    if _K is None:
        from kokoro_onnx import Kokoro
        _K = Kokoro(ASSETS + "/voices/kokoro-v1.0.onnx", ASSETS + "/voices/voices-v1.0.bin")
    return _K


def tts(text, speed=1.08):
    """Lit `text` en français ; les mots de BRAND_IPA sont remplacés par leur phonétique."""
    k = _kokoro()
    parts, pos = [], 0
    spans = sorted((m.start(), m.end(), ipa) for rx, ipa in BRAND_IPA for m in rx.finditer(text))
    for s, e, ipa in spans:
        if s > pos: parts.append(k.tokenizer.phonemize(text[pos:s], "fr-fr"))
        parts.append(ipa); pos = e
    if pos < len(text): parts.append(k.tokenizer.phonemize(text[pos:], "fr-fr"))
    ph = " ".join(p.strip() for p in parts if p.strip())
    ph = re.sub(r"\s+([.,?!:;])", r"\1", ph)
    s, sr = k.create(ph, voice="ff_siwis", speed=speed, lang="fr-fr", is_phonemes=True)
    assert sr == SR
    return s.astype(np.float32)


# ---------------------------------------------------------------- musique
def _f(m): return 440.0 * 2 ** ((m - 69) / 12)


def _env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / d)


def _ep(m, dur, vel=0.5):
    """Piano électrique doux : quelques partiels qui s'éteignent."""
    n = int(dur * SR); t = np.arange(n) / SR; f = _f(m)
    w = (np.sin(2*np.pi*f*t) + 0.35*np.sin(2*np.pi*2*f*t)*np.exp(-t/0.25) + 0.12*np.sin(2*np.pi*3*f*t)*np.exp(-t/0.12))
    w *= (1 + 0.08*np.sin(2*np.pi*4.5*t))
    return vel * w * _env(n, 0.006, 0.9)


def _pad(ms, dur, vel=0.12):
    n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros(n)
    for m in ms:
        f = _f(m)
        for det in (-0.12, 0.12):
            out += np.sin(2*np.pi*f*(1 + det/100)*t)
    a = np.minimum(1, t / 0.4) * np.minimum(1, (dur - t) / 0.4).clip(0)
    return vel * out / len(ms) * a


def _bass(m, dur, vel=0.45):
    n = int(dur * SR); t = np.arange(n) / SR
    return vel * np.sin(2*np.pi*_f(m)*t) * _env(n, 0.01, 0.6)


def _kick(vel=0.5):
    n = int(0.25 * SR); t = np.arange(n) / SR
    f = 50 + 70*np.exp(-t/0.03)
    return vel * np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t/0.09)


def _hat(rng, vel=0.06):
    n = int(0.05 * SR); x = rng.standard_normal(n)
    x = sosfilt(butter(2, 6000, "hp", fs=SR, output="sos"), x)
    return vel * x * np.exp(-np.arange(n)/SR/0.012)


TRACKS = [  # (bpm, accords, basses, motif d'arpège sur 8 croches ; -1 = silence)
    (84, [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 64]], [36, 33, 41, 43], [0, 2, 3, 2, 1, -1, 2, 3]),
    (76, [[62, 65, 69, 72], [55, 59, 62, 65], [60, 64, 67, 71], [57, 62, 64, 67]], [38, 43, 36, 45], [3, -1, 2, 1, -1, 2, 0, -1]),
    (92, [[65, 69, 72, 76], [64, 67, 71, 74], [62, 65, 69, 72], [60, 64, 67, 71]], [41, 40, 38, 36], [0, 1, 2, 3, 2, 1, -1, 2]),
]


def music(idx, seconds):
    """Boucle lo-fi originale n° idx (0, 1, 2), de durée ≥ seconds."""
    cache = f"{ASSETS}/music/track{idx}.npy"
    if os.path.exists(cache):
        loop = np.load(cache)
    else:
        bpm, chords, basses, arp = TRACKS[idx]
        rng = np.random.default_rng(idx + 7)
        beat = 60 / bpm; bar = 4 * beat; bars = 16
        loop = np.zeros(int(bars * bar * SR) + SR)
        def add(sig, at):
            i = int(at * SR); loop[i:i + len(sig)] += sig[:len(loop) - i]
        for b in range(bars):
            ch = chords[b % 4]; t0 = b * bar
            add(_pad(ch, bar), t0)
            add(_bass(basses[b % 4], 2 * beat), t0); add(_bass(basses[b % 4], 2 * beat, 0.3), t0 + 2 * beat)
            for k, a in enumerate(arp):
                if a >= 0 and not (b % 8 == 7 and k > 4):
                    add(_ep(ch[a] + 12, beat * 1.5, 0.16 + 0.04 * rng.random()), t0 + k * beat / 2)
            for q in range(4):
                if q in (0, 2): add(_kick(0.35), t0 + q * beat)
                if b >= 2:
                    add(_hat(rng, 0.05), t0 + q * beat + beat / 2)
                    if q in (1, 3): add(_hat(rng, 0.03), t0 + q * beat)
        loop += 0.004 * sosfilt(butter(1, 2500, "lp", fs=SR, output="sos"), rng.standard_normal(len(loop)))  # souffle vinyle
        loop = sosfilt(butter(2, 5000, "lp", fs=SR, output="sos"), loop)
        loop = loop[: int(bars * bar * SR)]
        loop = (loop / np.sqrt(np.mean(loop ** 2)) * 0.1).astype(np.float32)  # RMS fixe
        os.makedirs(os.path.dirname(cache), exist_ok=True); np.save(cache, loop)
    reps = int(np.ceil(seconds * SR / len(loop))) + 1
    return np.tile(loop, reps)[: int(seconds * SR)]


# ---------------------------------------------------------------- bruitages
def sfx(name):
    rng = np.random.default_rng(len(name))
    if name == "whoosh":
        n = int(0.42 * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
        lo = sosfilt(butter(2, [300, 2500], "bp", fs=SR, output="sos"), x)
        hi = sosfilt(butter(2, [1500, 7000], "bp", fs=SR, output="sos"), x)
        mixk = np.clip(t / 0.42, 0, 1)
        e = np.sin(np.pi * np.clip(t / 0.42, 0, 1)) ** 2
        return (0.22 * e * ((1 - mixk) * lo + mixk * hi)).astype(np.float32)
    if name == "tick":
        n = int(0.06 * SR); t = np.arange(n) / SR
        return (0.25 * np.sin(2*np.pi*1800*t) * np.exp(-t/0.008)).astype(np.float32)
    if name == "ding":
        n = int(1.0 * SR); t = np.arange(n) / SR
        w = np.sin(2*np.pi*1318.5*t) + 0.5*np.sin(2*np.pi*1975.5*t)*np.exp(-t/0.25) + 0.25*np.sin(2*np.pi*2637*t)*np.exp(-t/0.12)
        return (0.16 * w * _env(n, 0.003, 0.35)).astype(np.float32)
    if name == "pop":
        n = int(0.09 * SR); t = np.arange(n) / SR
        f = 900 - 500 * t / 0.09
        return (0.14 * np.sin(2*np.pi*np.cumsum(f)/SR) * np.exp(-t/0.025)).astype(np.float32)
    if name == "chime":
        out = np.zeros(int(1.2 * SR))
        for k, m in enumerate([76, 79, 84]):
            s = _ep(m, 1.0, 0.12); i = int(k * 0.09 * SR); out[i:i + len(s)] += s[: len(out) - i]
        return out.astype(np.float32)
    raise KeyError(name)


def mix(voice, events, music_idx, total):
    """voice : piste voix complète ; events : [(t, nom_sfx)] ; renvoie le mix final."""
    n = int(total * SR)
    v = np.zeros(n, np.float32); v[: min(n, len(voice))] = voice[:n]
    fx = np.zeros(n, np.float32)
    for t, name in events:
        s = sfx(name); i = int(t * SR)
        if i < n: fx[i:i + len(s)] += s[: n - i]
    m = music(music_idx, total)
    # ducking : la musique baisse quand la voix parle
    env = np.convolve(np.abs(v), np.ones(int(0.12 * SR)) / int(0.12 * SR), mode="same")
    duck = 1 - 0.55 * np.clip(env / 0.04, 0, 1)
    fade = np.minimum(1, np.arange(n) / (0.8 * SR)) * np.minimum(1, (n - np.arange(n)) / (1.2 * SR))
    out = v + fx + 0.35 * m * duck * fade
    peak = np.max(np.abs(out))
    return (out / peak * 0.95 if peak > 0.95 else out).astype(np.float32)
