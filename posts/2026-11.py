# Posts TikTok MathSquads — lancement, du 25 au 30 novembre 2026 (1 par jour).
CORAL, SAGE, INK = "#E1613E", "#4F7A5E", "#1B2A44"
def pill(t, bg=CORAL): return {"k": "pill", "t": t, "bg": bg}
def h(t, s=90, after=40): return {"k": "h", "t": t, "s": s, "after": after}
def big(t, s=300, after=40): return {"k": "big", "t": t, "s": s, "after": after}
def card(t, s=96, c=INK, o=None, after=50): return {"k": "card", "t": t, "s": s, "c": c, "o": o, "after": after}
def good(t, s=96): return card(t, s, c=SAGE, o=SAGE)
def bad(t, s=96): return card(t, s, c=CORAL, o=CORAL)
def p(t, s=50): return {"k": "p", "t": t, "s": s}
TAGS = "#maths #mathstok #brevet #bac #college #lycee #astucemaths #revisions"
CD = {"countdown": 3}

POSTS = [
 {"date": "2026-11-25", "name": "multiplier-par-11", "title": "Multiplier par 11 en 2 secondes", "cta": "A",
  "checks": ["23*11 == 253", "45*11 == 495"],
  "caption": "Multiplier par 11 de tête en 2 secondes 🤯 Teste avec ton âge ! " + TAGS,
  "scenes": [
   {"slide": [pill("ASTUCE · Tous niveaux"), h("Multiplier par 11", 100, 30), h("en 2 secondes", 90, 40), big("23 × 11", 220)], "top": 480,
    "say": "Multiplier n'importe quel nombre à deux chiffres par onze, en deux secondes. Exemple : vingt-trois fois onze.",
    "sub": "Multiplier un nombre à 2 chiffres par 11, en 2 secondes. Exemple : 23 × 11."},
   {"slide": [pill("L'ASTUCE"), h("On écarte les deux chiffres…", 84, 40), card("2 _ 3", 120), p("…et on met leur somme au milieu : 2 + 3 = 5")],
    "say": "On écarte les deux chiffres, deux et trois, et on met leur somme au milieu. Deux plus trois, cinq.",
    "sub": "On écarte les deux chiffres, 2 et 3, et on met leur somme au milieu : 2 + 3 = 5."},
   {"slide": [pill("RÉSULTAT", SAGE), good("23 × 11 = 253", 110), card("45 × 11 = 495", 90)],
    "say": "Résultat : deux cent cinquante-trois. Ça marche aussi avec quarante-cinq : quatre, neuf, cinq. Quatre cent quatre-vingt-quinze.",
    "sub": "Résultat : 253. Ça marche aussi avec 45 : 4, 9, 5 → 495."}]},

 {"date": "2026-11-26", "name": "x-carre-egal-9", "title": "x² = 9 donc x = 3 ?", "cta": "B",
  "checks": ["set(sp.solve(x**2 - 9, x)) == {-3, 3}"],
  "caption": "x² = 9 donc x = 3 ? Il manque une solution 👀 " + TAGS,
  "scenes": [
   {"slide": [pill("ERREUR CLASSIQUE · 3e à 2nde"), h("Résous :", 96, 20), big("x² = 9", 260)], "top": 520,
    "say": "Résous x au carré égale neuf. Si tu réponds juste trois, tu perds la moitié des points.",
    "sub": "Résous x² = 9. Si tu réponds juste 3, tu perds la moitié des points."},
   {"slide": [pill("LE PIÈGE"), bad("x = 3", 120), p("Et (−3)² ? Ça fait aussi 9 !")],
    "say": "Le piège : oublier que moins trois au carré, ça fait aussi neuf.",
    "sub": "Le piège : oublier que (−3)², ça fait aussi 9."},
   {"slide": [pill("RÉPONSE", SAGE), good("x = 3  ou  x = −3", 96), p("Une équation x² = a (avec a > 0) a deux solutions : √a et −√a.")],
    "say": "Donc x égale trois, ou x égale moins trois. Une équation x carré égale un nombre positif a toujours deux solutions.",
    "sub": "Donc x = 3 ou x = −3. x² = un nombre positif → toujours deux solutions."}]},

 {"date": "2026-11-27", "name": "pourcentage-inverse", "title": "8 % de 50 de tête ?", "cta": "C",
  "checks": ["R(8,100)*50 == 4", "R(50,100)*8 == 4"],
  "caption": "8 % de 50 ? L'astuce que personne ne t'a apprise à l'école 🔄 " + TAGS,
  "scenes": [
   {"slide": [pill("ASTUCE · 5e à Terminale"), h("Calcule de tête :", 96, 30), big("8 % de 50", 200)], "top": 520,
    "say": "Calcule de tête huit pour cent de cinquante. Ça paraît dur ? Il y a une astuce.",
    "sub": "Calcule de tête 8 % de 50. Ça paraît dur ? Il y a une astuce."},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("L'ASTUCE"), h("On peut inverser les deux nombres !", 84, 50), card("8 % de 50 = 50 % de 8", 76)],
    "say": "L'astuce : on peut inverser les deux nombres. Huit pour cent de cinquante, c'est pareil que cinquante pour cent de huit.",
    "sub": "L'astuce : on peut inverser ! 8 % de 50 = 50 % de 8."},
   {"slide": [pill("RÉPONSE", SAGE), good("= 4", 140), p("50 %, c'est la moitié : la moitié de 8, c'est 4.")],
    "say": "Et cinquante pour cent, c'est la moitié. La moitié de huit : quatre. Teste avec d'autres nombres, ça marche à chaque fois.",
    "sub": "Et 50 %, c'est la moitié : la moitié de 8 = 4. Ça marche à chaque fois."}]},

 {"date": "2026-11-28", "name": "piece-cinq-piles", "title": "5 piles d'affilée… et après ?", "cta": "A",
  "checks": ["R(1,2) == R(1,2)"],
  "caption": "5 piles d'affilée : face a plus de chances au prochain lancer ? 🪙 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 3e à Terminale"), h("Une pièce tombe 5 fois sur PILE.", 84, 40), h("Au 6e lancer, FACE a plus de chances ?", 78)], "top": 520,
    "say": "Une pièce normale tombe cinq fois de suite sur pile. Au sixième lancer, est-ce que face a plus de chances de tomber ?",
    "sub": "Une pièce tombe 5 fois de suite sur PILE. Au 6e lancer, FACE a plus de chances ?"},
   {"slide": "same", "say": "Oui ou non ?", "sub": "Oui ou non ?"}, CD,
   {"slide": [pill("NON !"), h("La pièce n'a pas de mémoire", 88, 50), card("P(face) = 1/2", 100)],
    "say": "Non ! La pièce n'a pas de mémoire. À chaque lancer, la probabilité de face reste un demi.",
    "sub": "Non ! La pièce n'a pas de mémoire. À chaque lancer, P(face) = 1/2."},
   {"slide": [pill("À RETENIR", SAGE), h("Les lancers sont indépendants", 84, 40), p("Croire le contraire, c'est « l'erreur du joueur », celle qui fait perdre au casino.")],
    "say": "Les lancers sont indépendants. Croire le contraire, c'est ce qu'on appelle l'erreur du joueur.",
    "sub": "Les lancers sont indépendants. Croire le contraire, c'est « l'erreur du joueur »."}]},

 {"date": "2026-11-29", "name": "carre-finit-par-5", "title": "35² de tête en 3 secondes", "cta": "B",
  "checks": ["35**2 == 1225", "3*4 == 12", "65**2 == 4225"],
  "caption": "35² de tête en 3 secondes 😎 L'astuce des nombres qui finissent par 5 " + TAGS,
  "scenes": [
   {"slide": [pill("ASTUCE · 4e à Terminale"), h("Calcule de tête :", 96, 30), big("35²", 300)], "top": 520,
    "say": "Calcule trente-cinq au carré de tête, en trois secondes. Pour les nombres qui finissent par cinq, il y a une astuce.",
    "sub": "Calcule 35² de tête, en 3 secondes. Pour les nombres qui finissent par 5, il y a une astuce."},
   {"slide": [pill("ÉTAPE 1"), h("Le chiffre des dizaines × le suivant", 80, 50), card("3 × 4 = 12", 110)],
    "say": "Étape un : on prend le chiffre des dizaines, trois, et on le multiplie par le nombre suivant, quatre. Trois fois quatre, douze.",
    "sub": "Étape 1 : le chiffre des dizaines × le suivant : 3 × 4 = 12."},
   {"slide": [pill("ÉTAPE 2", SAGE), h("On colle 25 à la fin", 84, 50), good("35² = 1225", 110), card("65² : 6 × 7 = 42 → 4225", 70)],
    "say": "Étape deux : on colle vingt-cinq à la fin. Douze, vingt-cinq : mille deux cent vingt-cinq. Avec soixante-cinq : six fois sept, quarante-deux, donc quatre mille deux cent vingt-cinq.",
    "sub": "Étape 2 : on colle 25 à la fin → 1225. Avec 65 : 6 × 7 = 42 → 4225."}]},

 {"date": "2026-11-30", "name": "doubler-cote-carre", "title": "Côté doublé = aire doublée ?", "cta": "C",
  "checks": ["(2*a)**2 == 4*a**2", "3**2 == 9 and 6**2 == 36"],
  "caption": "Tu doubles le côté d'un carré : l'aire double ? 📏 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 6e à 3e"), h("Si tu doubles le côté d'un carré…", 84, 40), h("son aire double aussi ?", 84)], "top": 560,
    "say": "Si tu doubles le côté d'un carré, est-ce que son aire double aussi ?",
    "sub": "Si tu doubles le côté d'un carré, est-ce que son aire double aussi ?"},
   {"slide": "same", "say": "Trois secondes pour répondre.", "sub": "3 secondes pour répondre."}, CD,
   {"slide": [pill("EXEMPLE"), card("côté 3 cm → aire 9 cm²", 74), card("côté 6 cm → aire 36 cm²", 74)],
    "say": "Prends un carré de trois centimètres : aire, neuf centimètres carrés. Double le côté, six centimètres : aire, trente-six centimètres carrés.",
    "sub": "Côté 3 cm → aire 9 cm². Côté 6 cm → aire 36 cm²."},
   {"slide": [pill("RÉPONSE"), bad("L'aire est multipliée par 4 !", 76), p("Côté × 2 → aire × 2² = × 4")],
    "say": "Non, elle ne double pas : elle est multipliée par quatre ! Quand le côté est multiplié par deux, l'aire est multipliée par deux au carré.",
    "sub": "Non : l'aire est multipliée par 4 ! Côté × 2 → aire × 2² = × 4."}]},
]
