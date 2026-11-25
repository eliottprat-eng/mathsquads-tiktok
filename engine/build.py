"""Transforme un fichier de posts (liste de dicts courts) en specs vidéo + vérifie les maths.

Usage : python3 build.py ../posts/2026-12.py OUTDIR [--only N] [--render]
Chaque post : {"date","name","caption","checks":[expr python vraie],"cta":"A|B|C","scenes":[...]}
Une scène : {"slide":[éléments] | "same", "say":texte lu, "sub":sous-titre (défaut = say)}
            ou {"countdown":3} (réutilise la dernière slide).
"""
import sys, os, json, runpy
import sympy as sp

CORAL, SAGE, INK = "#E1613E", "#4F7A5E", "#1B2A44"

CTA = {
    "A": ({"dark": True, "top": 470, "els": [
            {"k": "h", "t": "Besoin d'aide en maths ?", "s": 92, "after": 60},
            {"k": "card", "t": "1re heure offerte", "s": 80, "c": CORAL, "after": 40},
            {"k": "p", "t": "mathsquads.com", "w": 600, "s": 58}]},
          "Abonne-toi pour d'autres astuces. Et ta première heure de cours est offerte, sur math squads point com.",
          "Abonne-toi pour d'autres astuces. Et ta 1re heure de cours est offerte, sur mathsquads.com"),
    "B": ({"dark": True, "top": 430, "els": [
            {"k": "h", "t": "Des profs issus des meilleures grandes écoles", "s": 80, "after": 60},
            {"k": "card", "t": "Dès 20 € / heure", "s": 80, "c": CORAL, "after": 40},
            {"k": "p", "t": "Collège · Lycée · Prépa", "s": 50, "after": 30},
            {"k": "p", "t": "mathsquads.com", "w": 600, "s": 58}]},
          "Tu veux un prof qui explique vraiment ? Cours particuliers dès vingt euros de l'heure, sur math squads point com.",
          "Tu veux un prof qui explique vraiment ? Cours particuliers dès 20 €/h, sur mathsquads.com"),
    "C": ({"dark": True, "top": 470, "els": [
            {"k": "h", "t": "Pas satisfait ? Remboursé.", "s": 92, "after": 60},
            {"k": "card", "t": "1re heure offerte", "s": 80, "c": CORAL, "after": 40},
            {"k": "p", "t": "mathsquads.com", "w": 600, "s": 58}]},
          "Chez math squads, ta première heure est offerte. Et si tu n'es pas satisfait, on te rembourse. Rendez-vous sur math squads point com.",
          "Chez MathSquads, ta 1re heure est offerte. Pas satisfait ? On te rembourse. mathsquads.com"),
}


def check(post):
    x, y, n, a, b = sp.symbols("x y n a b")
    env = {"sp": sp, "x": x, "y": y, "n": n, "a": a, "b": b, "S": sp.S, "R": sp.Rational}
    for c in post.get("checks", []):
        ok = eval(c, env)
        if ok is not True and not (hasattr(ok, "__bool__") and bool(ok)):
            raise AssertionError(f"{post['name']}: vérification fausse -> {c}")


def to_spec(post):
    slides, scenes = [], []
    for sc in post["scenes"]:
        if "countdown" in sc:
            scenes.append({"slide": len(slides) - 1, "countdown": sc["countdown"]}); continue
        if sc.get("slide") != "same":
            s = sc["slide"]
            slides.append(s if isinstance(s, dict) else {"top": sc.get("top", 470), "els": s})
        scenes.append({"slide": len(slides) - 1, "say": sc["say"], "sub": sc.get("sub", sc["say"])})
    cta_slide, say, sub = CTA[post.get("cta", "A")]
    slides.append(cta_slide); scenes.append({"slide": len(slides) - 1, "say": say, "sub": sub})
    return {"name": post["name"], "caption": post["caption"], "slides": slides, "scenes": scenes}


if __name__ == "__main__":
    posts = runpy.run_path(sys.argv[1])["POSTS"]; out = sys.argv[2]
    only = int(sys.argv[sys.argv.index("--only") + 1]) if "--only" in sys.argv else None
    os.makedirs(out, exist_ok=True)
    names = set()
    for i, p in enumerate(posts):
        assert p["name"] not in names, p["name"]; names.add(p["name"])
        check(p)
        if only is not None and i != only: continue
        spec = to_spec(p); path = f"{out}/{p['date']}_{p['name']}.json"
        json.dump(spec, open(path, "w"), ensure_ascii=False, indent=1)
        if "--render" in sys.argv:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from video import build
            build(path, f"{out}/work/{p['name']}")
            os.replace(f"{out}/work/{p['name']}/{p['name']}.mp4", f"{out}/{p['date']}_{p['name']}.mp4")
    print(f"{len(posts)} posts vérifiés")
