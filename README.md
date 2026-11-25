# MathSquads × TikTok

Le contenu TikTok de **@mathsquads.fr** est généré et programmé automatiquement : 1 vidéo par jour, avec voix off, sous-titres et une promo de mathsquads.com à la fin.

## Comment ça marche

1. `posts/AAAA-MM.py` : les 30 scripts du mois (texte lu, sous-titres, écrans, vérifications mathématiques).
2. `engine/build.py` vérifie chaque calcul avec sympy, puis génère les vidéos : écrans avec `render.py`, voix Kokoro et montage ffmpeg avec `video.py`.
3. `media/AAAA-MM/` : les vidéos finales. GitHub les sert à un lien public, que Metricool télécharge.
4. Les posts sont programmés dans Metricool (marque « Mathsquads », réseau TikTok) à 18 h 30, heure de Paris.
5. Une tâche programmée Claude refait tout ça le 25 de chaque mois pour le mois suivant (voir `RUNBOOK.md`).

## Générer à la main

```bash
bash engine/setup.sh                       # polices, voix, paquets (une seule fois)
cd engine
python3 build.py ../posts/2026-12.py OUT   # vérifie les maths + écrit les specs
python3 build.py ../posts/2026-12.py OUT --render   # + génère les vidéos
```

## Supprimer ou modifier un post

Dans Metricool → Planification, supprime le post concerné. Les autres ne bougent pas.

Polices : Poppins et Inter (SIL OFL, via Fontsource). Repli DejaVu Sans (licence libre, dans `engine/fonts`). Voix : Kokoro (Apache 2.0).
