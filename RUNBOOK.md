# Procédure mensuelle (lue par la tâche programmée Claude, le 25 de chaque mois)

Objectif : produire et programmer **1 vidéo TikTok par jour pour tout le mois suivant**, sans intervention humaine.

## 1. Préparer

- Cloner `eliottprat-eng/mathsquads-tiktok` (accès en écriture), puis `bash engine/setup.sh`.
- Lire `posts/HISTORY.md` et les fichiers `posts/*.py` existants. **Aucun sujet déjà traité ne doit revenir** (même notion, mêmes nombres).
- Vérifier avec `getBrandSettings` que la marque Metricool « Mathsquads » est là, avec TikTok connecté. Sinon, s'arrêter et prévenir l'utilisateur.

## 2. Écrire `posts/AAAA-MM.py`

Copier la structure de `posts/2026-12.py` : mêmes helpers, une entrée par jour, `date` = chaque jour du mois.

Règles de contenu :
- **Mélange sur le mois** : environ 40 % de défis (avec `CD`, le compte à rebours), 25 % d'erreurs classiques, 20 % de méthodes ou astuces, 15 % de « vrai ou faux » ou « le savais-tu ».
- **Niveaux** : environ 40 % collège, 45 % lycée, 15 % terminale ou prépa. Indiquer le niveau dans la pastille du premier écran.
- **Coller au calendrier** : brevet blanc et bac blanc en décembre-janvier, conseils de révisions pendant les vacances, bac et brevet en mai-juin, rentrée en septembre.
- **Accroche** dans la 1re phrase, en moins de 3 secondes. Vidéo de 20 à 35 secondes, CTA compris.
- `say` : tout écrit en toutes lettres pour la voix (« moins trois au carré », « math squads point com »). `sub` : la version avec symboles.
- **Aucun emoji** dans les écrans ni dans `sub` (la police ne les a pas). Les emojis vont seulement dans `caption`.
- `checks` : au moins une expression sympy vraie par post qui contient un calcul. `build.py` refuse le fichier si une vérification échoue.
- `cta` : alterner A, B et C.
- **Seules affirmations autorisées sur MathSquads** : 1re heure offerte, remboursé si pas satisfait, cours dès 20 €/h, profs issus des meilleures grandes écoles, collège, lycée et prépa. **Jamais** de chiffres (nombre de cours, % de satisfaction, notes), de promesses de résultats ou de comparaison avec des concurrents.

## 3. Générer et contrôler

```bash
cd engine
python3 build.py ../posts/AAAA-MM.py /tmp/out                 # maths vérifiées ?
python3 build.py ../posts/AAAA-MM.py /tmp/out --render        # environ 30 s par vidéo
```

- Regarder une planche d'écrans de 5 posts au hasard (lisibilité, débordements, symboles).
- Vérifier avec ffprobe que chaque mp4 dure entre 15 et 45 s et contient de l'audio.
- Copier les mp4 dans `media/AAAA-MM/`, ajouter les sujets à `posts/HISTORY.md`, commit puis push sur `main`.
- Tester un lien `https://raw.githubusercontent.com/eliottprat-eng/mathsquads-tiktok/main/media/AAAA-MM/<fichier>.mp4` : il doit renvoyer HTTP 200.

## 4. Programmer dans Metricool

Pour chaque post, appeler `createScheduledPost` avec :
- `blogId` = l'id de la marque Mathsquads (via `getBrandSettings`) ;
- `date` = jour J à 18:30 Europe/Paris ;
- `info` : `autoPublish: true`, `providers: [{"network":"tiktok"}]`, `text` = caption, `media` = [lien raw],
  `publicationDate: {"dateTime":"AAAA-MM-JJT18:30:00","timezone":"Europe/Paris"}`,
  `tiktokData: {"privacyOption":"PUBLIC_TO_EVERYONE","isAigc":true,"title":"","disableComment":false,"disableDuet":false,"disableStitch":false,"commercialContentOwnBrand":false,"commercialContentThirdParty":false,"autoAddMusic":false}`.

Ensuite, `getScheduledPosts` sur le mois doit renvoyer exactement un post TikTok par jour. Corriger les manques ou les doublons.

## 5. Prévenir

Envoyer à l'utilisateur un récapitulatif court : nombre de posts programmés, liste « date : sujet », et tout problème rencontré. Rappeler qu'il peut supprimer un post dans Metricool → Planification.
