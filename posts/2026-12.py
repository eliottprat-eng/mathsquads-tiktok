# Posts TikTok MathSquads — décembre 2026 (1 par jour, du 1er au 30).
# "say" = texte lu par la voix off (tout en mots), "sub" = sous-titre affiché.
# "checks" = expressions Python/sympy qui doivent être vraies (vérifiées avant rendu).

CORAL, SAGE, INK = "#E1613E", "#4F7A5E", "#1B2A44"
def pill(t, bg=CORAL): return {"k": "pill", "t": t, "bg": bg}
def h(t, s=90, after=40): return {"k": "h", "t": t, "s": s, "after": after}
def big(t, s=300, after=40): return {"k": "big", "t": t, "s": s, "after": after}
def card(t, s=96, c=INK, o=None, after=50): return {"k": "card", "t": t, "s": s, "c": c, "o": o, "after": after}
def good(t, s=96): return card(t, s, c=SAGE, o=SAGE)
def bad(t, s=96): return card(t, s, c=CORAL, o=CORAL)
def p(t, s=50): return {"k": "p", "t": t, "s": s}
TAGS = "#maths #mathstok #brevet #bac #college #lycee #astucemaths #revisions"
TAGS_SUP = "#maths #mathstok #prepa #bac #terminale #astucemaths #etudiant"
CD = {"countdown": 3}

POSTS = [
 # 1 — défi -3²
 {"date": "2026-12-01", "name": "moins3carre", "title": "Combien fait −3² ?", "cta": "A", "checks": ["-3**2 == -9", "(-3)**2 == 9"],
  "caption": "Moins trois au carré… t'es sûr de toi ? 😏 Ta réponse en commentaire 👇 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI MATHS · 4e à 2nde"), h("Combien fait…", 100, 10), big("−3²", 340)], "top": 520,
    "say": "Combien fait moins trois au carré ? Attention, beaucoup d'élèves se trompent sur celui-là.",
    "sub": "Combien fait −3² ? Attention, beaucoup d'élèves se trompent sur celui-là."},
   {"slide": "same", "say": "Tu as trois secondes.", "sub": "Tu as 3 secondes."}, CD,
   {"slide": [pill("LA RÈGLE"), h("La puissance passe AVANT le signe moins", 84, 70), card("−3² = −(3²)")],
    "say": "La règle : la puissance passe avant le signe moins. Le carré s'applique seulement au trois.",
    "sub": "La règle : la puissance passe avant le signe moins. Le carré s'applique seulement au 3."},
   {"slide": [pill("RÉPONSE"), bad("−3² = −9", 120), card("(−3)² = 9", 100)], "top": 400,
    "say": "Donc moins trois au carré, ça fait moins neuf. Et si tu veux le carré de moins trois, il faut des parenthèses. Là, ça fait neuf.",
    "sub": "Donc −3², ça fait −9. Et pour le carré de −3, il faut des parenthèses : (−3)² = 9."}]},

 # 2 — erreur (a+b)²
 {"date": "2026-12-02", "name": "identite-remarquable", "title": "(x + 3)² = x² + 9 ? Non !", "cta": "B", "checks": ["sp.expand((x+3)**2) == x**2+6*x+9"],
  "caption": "L'erreur n°1 en calcul littéral 😬 Tu la faisais ? " + TAGS,
  "scenes": [
   {"slide": [pill("ERREUR CLASSIQUE · 3e à 1re"), h("Arrête d'écrire ça :", 96, 60), bad("(x + 3)² = x² + 9", 90)], "top": 500,
    "say": "Arrête tout de suite d'écrire que x plus trois, le tout au carré, ça fait x carré plus neuf. C'est faux, et ça te coûte des points à chaque contrôle.",
    "sub": "Arrête d'écrire (x + 3)² = x² + 9. C'est faux, et ça te coûte des points à chaque contrôle."},
   {"slide": [pill("LA BONNE FORMULE", SAGE), card("(a + b)² = a² + 2ab + b²", 80), p("Il ne faut pas oublier le double produit : 2 × a × b.")],
    "say": "La bonne formule : a plus b, le tout au carré, égale a carré, plus deux a b, plus b carré. Le piège, c'est d'oublier le double produit.",
    "sub": "La bonne formule : (a + b)² = a² + 2ab + b². Le piège : oublier le double produit 2ab."},
   {"slide": [pill("RÉPONSE", SAGE), good("(x + 3)² = x² + 6x + 9", 84), p("2 × x × 3 = 6x")],
    "say": "Donc x plus trois, le tout au carré, égale x carré plus six x plus neuf. Le six x, c'est deux fois x fois trois.",
    "sub": "Donc (x + 3)² = x² + 6x + 9. Le 6x, c'est 2 × x × 3."}]},

 # 3 — fractions 1/2 + 1/3
 {"date": "2026-12-03", "name": "fractions-addition", "title": "1/2 + 1/3 = 2/5 ?", "cta": "A", "checks": ["R(1,2)+R(1,3) == R(5,6)", "R(1,2)+R(1,3) != R(2,5)"],
  "caption": "1/2 + 1/3 = 2/5 ? 🤔 Réponds avant la fin " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI MATHS · 6e à 4e"), h("Vrai ou faux ?", 100, 40), big("1/2 + 1/3 = 2/5", 160)], "top": 540,
    "say": "Vrai ou faux : un demi plus un tiers, ça fait deux cinquièmes ?",
    "sub": "Vrai ou faux : 1/2 + 1/3 = 2/5 ?"},
   {"slide": "same", "say": "Réfléchis trois secondes.", "sub": "Réfléchis 3 secondes."}, CD,
   {"slide": [pill("FAUX !"), h("On n'additionne JAMAIS les dénominateurs", 80, 60), card("1/2 = 3/6     1/3 = 2/6", 76)],
    "say": "Faux ! On n'additionne jamais les dénominateurs. On met d'abord les deux fractions sur le même dénominateur : un demi, c'est trois sixièmes, et un tiers, c'est deux sixièmes.",
    "sub": "Faux ! On n'additionne jamais les dénominateurs. Même dénominateur d'abord : 1/2 = 3/6 et 1/3 = 2/6."},
   {"slide": [pill("RÉPONSE", SAGE), good("3/6 + 2/6 = 5/6", 100)],
    "say": "Trois sixièmes plus deux sixièmes, ça fait cinq sixièmes. La bonne réponse, c'est cinq sixièmes.",
    "sub": "3/6 + 2/6 = 5/6. La bonne réponse : 5/6."}]},

 # 4 — +20% puis -20%
 {"date": "2026-12-04", "name": "pourcentages-piege", "title": "+20 % puis −20 % : le piège", "cta": "C", "checks": ["100*R(12,10)*R(8,10) == 96"],
  "caption": "+20 % puis −20 %… tu reviens au prix de départ ? 💸 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 3e à Terminale"), h("Un pull à 100 €", 96, 30), p("augmente de 20 %, puis baisse de 20 %."), h("Il coûte combien ?", 90)], "top": 520,
    "say": "Un pull coûte cent euros. Son prix augmente de vingt pour cent, puis baisse de vingt pour cent. Combien il coûte maintenant ?",
    "sub": "Un pull à 100 €. +20 %, puis −20 %. Combien il coûte maintenant ?"},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("LE CALCUL"), card("100 × 1,2 = 120 €", 84), card("120 × 0,8 = 96 €", 84)],
    "say": "Plus vingt pour cent, c'est multiplier par un virgule deux : cent vingt euros. Moins vingt pour cent, c'est multiplier par zéro virgule huit : quatre-vingt-seize euros.",
    "sub": "+20 % = × 1,2 → 120 €. −20 % = × 0,8 → 96 €."},
   {"slide": [pill("RÉPONSE"), bad("96 €, pas 100 €", 100), p("La baisse s'applique sur 120 €, pas sur 100 €.")],
    "say": "Réponse : quatre-vingt-seize euros, pas cent. Parce que la baisse s'applique sur cent vingt euros, pas sur cent.",
    "sub": "Réponse : 96 €, pas 100 €. La baisse s'applique sur 120 €, pas sur 100 €."}]},

 # 5 — Pythagore ou Thalès
 {"date": "2026-12-05", "name": "pythagore-ou-thales", "title": "Pythagore ou Thalès ?", "cta": "B", "checks": [],
  "caption": "Pythagore ou Thalès ? Le test pour ne plus jamais hésiter 📐 Enregistre-le ! " + TAGS,
  "scenes": [
   {"slide": [pill("MÉTHODE · 4e-3e"), h("Pythagore ou Thalès ?", 100, 40), p("Le test en 2 questions pour ne plus jamais hésiter.")], "top": 560,
    "say": "Pythagore ou Thalès ? Voici le test en deux questions pour ne plus jamais hésiter au brevet.",
    "sub": "Pythagore ou Thalès ? Le test en 2 questions pour ne plus jamais hésiter au brevet."},
   {"slide": [pill("QUESTION 1"), h("Un triangle rectangle ?", 90, 50), good("→ Pythagore", 90), p("Tu cherches une longueur avec 2 côtés connus.")],
    "say": "Question un : tu as un triangle rectangle, et tu connais deux côtés ? C'est Pythagore.",
    "sub": "Question 1 : un triangle rectangle et 2 côtés connus ? C'est Pythagore."},
   {"slide": [pill("QUESTION 2"), h("Deux droites parallèles ?", 90, 50), good("→ Thalès", 90), p("Deux triangles « emboîtés » qui partagent un sommet.")],
    "say": "Question deux : tu vois deux droites parallèles, avec deux triangles emboîtés ? C'est Thalès.",
    "sub": "Question 2 : deux droites parallèles et deux triangles emboîtés ? C'est Thalès."},
   {"slide": [pill("À RETENIR"), card("angle droit → Pythagore\nparallèles → Thalès", 70)],
    "say": "À retenir : angle droit, Pythagore. Parallèles, Thalès. Enregistre cette vidéo pour tes révisions.",
    "sub": "Angle droit → Pythagore. Parallèles → Thalès. Enregistre la vidéo pour tes révisions."}]},

 # 6 — racine d'une somme
 {"date": "2026-12-06", "name": "racine-somme", "title": "√(9 + 16) = 7 ?", "cta": "A", "checks": ["sp.sqrt(9+16) == 5", "sp.sqrt(9)+sp.sqrt(16) == 7"],
  "caption": "√(9 + 16) = 7 ? Le piège des racines 🌱 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 3e à 2nde"), h("Combien fait…", 100, 20), big("√(9 + 16)", 200)], "top": 540,
    "say": "Combien fait racine de neuf plus seize ?", "sub": "Combien fait √(9 + 16) ?"},
   {"slide": "same", "say": "Trois secondes, pas plus.", "sub": "3 secondes, pas plus."}, CD,
   {"slide": [pill("LE PIÈGE"), bad("√9 + √16 = 3 + 4 = 7", 80), p("La racine ne se « distribue » pas sur une somme.")],
    "say": "Le piège, c'est de répondre trois plus quatre, donc sept. Mais la racine ne se distribue pas sur une addition.",
    "sub": "Le piège : répondre 3 + 4 = 7. Mais la racine ne se distribue pas sur une addition."},
   {"slide": [pill("RÉPONSE", SAGE), good("√(9 + 16) = √25 = 5", 90), p("On calcule d'abord ce qu'il y a sous la racine.")],
    "say": "On calcule d'abord ce qu'il y a sous la racine : neuf plus seize, vingt-cinq. Et racine de vingt-cinq, c'est cinq.",
    "sub": "D'abord sous la racine : 9 + 16 = 25. Et √25 = 5."}]},

 # 7 — 0,999... = 1
 {"date": "2026-12-07", "name": "zero-virgule-neuf", "title": "0,999… = 1 ?", "cta": "B", "checks": ["3*R(1,3) == 1"],
  "caption": "0,999… = 1 ?! Le résultat qui choque tout le monde 🤯 " + TAGS,
  "scenes": [
   {"slide": [pill("VRAI OU FAUX · Lycée"), big("0,999… = 1", 170), p("(avec des 9 à l'infini)")], "top": 560,
    "say": "Vrai ou faux : zéro virgule neuf neuf neuf, avec des neuf à l'infini, c'est exactement égal à un ?",
    "sub": "Vrai ou faux : 0,999… (des 9 à l'infini) = 1 exactement ?"},
   {"slide": "same", "say": "À ton avis ?", "sub": "À ton avis ?"}, CD,
   {"slide": [pill("LA PREUVE"), card("1/3 = 0,333…", 84), card("× 3", 70), card("3/3 = 0,999…", 84)],
    "say": "Regarde : un tiers, c'est zéro virgule trois trois trois à l'infini. On multiplie par trois des deux côtés : trois tiers, c'est zéro virgule neuf neuf neuf à l'infini.",
    "sub": "1/3 = 0,333… On multiplie par 3 : 3/3 = 0,999…"},
   {"slide": [pill("VRAI !", SAGE), good("0,999… = 1", 110), p("Deux écritures différentes du même nombre.")],
    "say": "Or trois tiers, c'est un. Donc oui, c'est vrai : zéro virgule neuf neuf neuf à l'infini, c'est égal à un. Ce sont deux écritures du même nombre.",
    "sub": "Or 3/3 = 1. Donc c'est VRAI : 0,999… = 1. Deux écritures du même nombre."}]},

 # 8 — second degré
 {"date": "2026-12-08", "name": "second-degre-3-etapes", "title": "Le second degré en 3 étapes", "cta": "C",
  "checks": ["sp.solve(x**2-5*x+6, x) == [2, 3]", "(-5)**2-4*1*6 == 1"],
  "caption": "Le second degré en 3 étapes, sans stress 📈 Enregistre pour le bac blanc ! " + TAGS,
  "scenes": [
   {"slide": [pill("MÉTHODE · 1re"), h("Résoudre", 96, 10), big("x² − 5x + 6 = 0", 130)], "top": 560,
    "say": "Résoudre x carré moins cinq x plus six égale zéro, en trois étapes. C'est parti.",
    "sub": "Résoudre x² − 5x + 6 = 0 en 3 étapes. C'est parti."},
   {"slide": [pill("ÉTAPE 1"), h("Repère a, b et c", 86, 50), card("a = 1   b = −5   c = 6", 80)],
    "say": "Étape un : repère a, b et c. Ici, a égale un, b égale moins cinq, et c égale six.",
    "sub": "Étape 1 : repère a, b et c. a = 1, b = −5, c = 6."},
   {"slide": [pill("ÉTAPE 2"), h("Calcule le discriminant", 86, 50), card("Δ = b² − 4ac", 84), card("Δ = 25 − 24 = 1", 84)],
    "say": "Étape deux : calcule delta, égal à b carré moins quatre a c. Vingt-cinq moins vingt-quatre, ça fait un. Delta est positif, donc il y a deux solutions.",
    "sub": "Étape 2 : Δ = b² − 4ac = 25 − 24 = 1. Δ > 0, donc deux solutions."},
   {"slide": [pill("ÉTAPE 3", SAGE), card("x = (−b ± √Δ) / 2a", 76), good("x = 2  ou  x = 3", 90)],
    "say": "Étape trois : x égale moins b, plus ou moins racine de delta, sur deux a. Cinq moins un sur deux, ça fait deux. Cinq plus un sur deux, ça fait trois.",
    "sub": "Étape 3 : x = (−b ± √Δ) / 2a. (5 − 1)/2 = 2 et (5 + 1)/2 = 3."}]},

 # 9 — diviser par 0,5
 {"date": "2026-12-09", "name": "diviser-par-0-5", "title": "10 ÷ 0,5 = 5 ?", "cta": "A", "checks": ["10 / R(1,2) == 20"],
  "caption": "10 ÷ 0,5 = 5 ? Presque tout le monde tombe dans le piège 😅 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 6e à 3e"), h("Combien fait…", 100, 20), big("10 ÷ 0,5", 230)], "top": 540,
    "say": "Combien fait dix divisé par zéro virgule cinq ?", "sub": "Combien fait 10 ÷ 0,5 ?"},
   {"slide": "same", "say": "Attention au piège.", "sub": "Attention au piège."}, CD,
   {"slide": [pill("L'ASTUCE"), h("Diviser par 0,5, c'est se demander :", 76, 40), card("combien de moitiés\ndans 10 ?", 80)],
    "say": "L'astuce : diviser par zéro virgule cinq, c'est se demander combien de moitiés il y a dans dix.",
    "sub": "L'astuce : diviser par 0,5, c'est se demander combien de moitiés il y a dans 10."},
   {"slide": [pill("RÉPONSE", SAGE), good("10 ÷ 0,5 = 20", 110), p("Diviser par 0,5 = multiplier par 2.")],
    "say": "Il y a vingt moitiés dans dix. Donc la réponse, c'est vingt, pas cinq. Diviser par zéro virgule cinq, c'est multiplier par deux.",
    "sub": "Il y a 20 moitiés dans 10. Réponse : 20, pas 5. Diviser par 0,5 = multiplier par 2."}]},

 # 10 — puissances
 {"date": "2026-12-10", "name": "puissances-produit", "title": "2³ × 2⁴ = 2¹² ?", "cta": "B", "checks": ["2**3 * 2**4 == 2**7", "2**7 == 128"],
  "caption": "2³ × 2⁴ = 2¹² ? La règle des puissances en 20 secondes ⚡ " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 4e à 2nde"), h("Combien fait…", 100, 20), big("2³ × 2⁴", 240)], "top": 540,
    "say": "Combien fait deux puissance trois, fois deux puissance quatre ? Sous forme d'une seule puissance.",
    "sub": "Combien fait 2³ × 2⁴ ? Sous forme d'une seule puissance."},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("LE PIÈGE"), bad("2³ × 2⁴ = 2¹²", 100), p("On ne multiplie PAS les exposants.")],
    "say": "Beaucoup répondent deux puissance douze, en multipliant les exposants. C'est faux.",
    "sub": "Beaucoup répondent 2¹² en multipliant les exposants. C'est faux."},
   {"slide": [pill("RÉPONSE", SAGE), card("(2×2×2) × (2×2×2×2)", 70), good("= 2⁷ = 128", 100)],
    "say": "Deux puissance trois, c'est trois fois deux. Deux puissance quatre, quatre fois deux. Au total, sept fois deux : deux puissance sept, cent vingt-huit. On additionne les exposants.",
    "sub": "2³ = trois « 2 », 2⁴ = quatre « 2 ». En tout sept : 2⁷ = 128. On ADDITIONNE les exposants."}]},

 # 11 — dérivée de 1/x
 {"date": "2026-12-11", "name": "derivee-inverse", "title": "La dérivée de 1/x", "cta": "C", "checks": ["sp.diff(1/x, x) == -1/x**2"],
  "caption": "La dérivée de 1/x, c'est 1 ? 🚫 Le piège du bac " + TAGS_SUP,
  "scenes": [
   {"slide": [pill("DÉFI · 1re-Terminale"), h("Quelle est la dérivée de…", 84, 30), big("f(x) = 1/x", 190)], "top": 520,
    "say": "Quelle est la dérivée de f de x égale un sur x ?", "sub": "Quelle est la dérivée de f(x) = 1/x ?"},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("L'ASTUCE"), h("Écris-la comme une puissance", 80, 50), card("1/x = x⁻¹", 100), card("(xⁿ)' = n·xⁿ⁻¹", 84)],
    "say": "L'astuce : écris un sur x comme x puissance moins un. Et la dérivée de x puissance n, c'est n fois x puissance n moins un.",
    "sub": "L'astuce : 1/x = x⁻¹. Et la dérivée de xⁿ, c'est n·xⁿ⁻¹."},
   {"slide": [pill("RÉPONSE", SAGE), good("f'(x) = −1/x²", 110), p("−1 × x⁻² = −1/x²")],
    "say": "Donc la dérivée, c'est moins un fois x puissance moins deux. Autrement dit : moins un sur x carré. N'oublie surtout pas le signe moins.",
    "sub": "Donc f'(x) = −1 × x⁻² = −1/x². N'oublie surtout pas le signe moins."}]},

 # 12 — calcul mental 15 %
 {"date": "2026-12-12", "name": "calcul-mental-15-pourcent", "title": "15 % de tête en 3 secondes", "cta": "A", "checks": ["R(15,100)*80 == 12"],
  "caption": "Calculer 15 % de tête en 3 secondes 🧠 L'astuce des 10 % " + TAGS,
  "scenes": [
   {"slide": [pill("ASTUCE · 5e à Terminale"), h("15 % de 80 €", 110, 40), p("De tête, en 3 secondes. Voici comment.")], "top": 580,
    "say": "Calculer quinze pour cent de quatre-vingts euros, de tête, en trois secondes. Voici l'astuce.",
    "sub": "15 % de 80 €, de tête, en 3 secondes. Voici l'astuce."},
   {"slide": [pill("ÉTAPE 1"), h("10 % : on divise par 10", 84, 50), card("10 % de 80 = 8", 96)],
    "say": "Étape un : dix pour cent, c'est diviser par dix. Dix pour cent de quatre-vingts, c'est huit.",
    "sub": "Étape 1 : 10 %, c'est diviser par 10. 10 % de 80 = 8."},
   {"slide": [pill("ÉTAPE 2"), h("5 % : la moitié de 10 %", 84, 50), card("5 % de 80 = 4", 96)],
    "say": "Étape deux : cinq pour cent, c'est la moitié de dix pour cent. Donc quatre.",
    "sub": "Étape 2 : 5 %, c'est la moitié de 10 %. Donc 4."},
   {"slide": [pill("RÉSULTAT", SAGE), good("15 % de 80 = 8 + 4 = 12", 84)],
    "say": "Et quinze pour cent, c'est dix plus cinq : huit plus quatre, douze euros. Ça marche avec tous les pourcentages.",
    "sub": "15 % = 10 % + 5 % = 8 + 4 = 12 €. Ça marche avec tous les pourcentages."}]},

 # 13 — révisions vacances
 {"date": "2026-12-13", "name": "reviser-vacances-noel", "title": "Réviser les maths pendant les vacances", "cta": "C", "checks": [],
  "caption": "Vacances de Noël : comment réviser les maths sans y passer tes journées 🎄 " + TAGS,
  "scenes": [
   {"slide": [pill("MÉTHODE · Collège & Lycée"), h("Réviser les maths pendant les vacances", 88, 40), p("3 règles simples pour arriver serein au bac blanc ou au brevet blanc.")], "top": 520,
    "say": "Réviser les maths pendant les vacances de Noël, sans y passer tes journées. Trois règles simples.",
    "sub": "Réviser les maths pendant les vacances de Noël, sans y passer tes journées. 3 règles simples."},
   {"slide": [pill("RÈGLE 1"), h("30 minutes par jour", 96, 40), p("Mieux vaut un peu chaque jour qu'une journée entière la veille.")],
    "say": "Règle un : trente minutes par jour. C'est bien plus efficace qu'une journée entière la veille de la rentrée.",
    "sub": "Règle 1 : 30 minutes par jour. Bien plus efficace qu'une journée entière la veille."},
   {"slide": [pill("RÈGLE 2"), h("Des exercices, pas des fiches", 90, 40), p("Relire son cours ne suffit pas : refais les exercices sans regarder la correction.")],
    "say": "Règle deux : fais des exercices, pas juste des fiches. Refais les exercices du cours sans regarder la correction.",
    "sub": "Règle 2 : des exercices, pas juste des fiches. Refais-les sans regarder la correction."},
   {"slide": [pill("RÈGLE 3"), h("Commence par tes points faibles", 88, 40), p("Le chapitre que tu évites, c'est celui qui te fera gagner le plus de points.")],
    "say": "Règle trois : commence par le chapitre que tu évites. C'est celui qui te fera gagner le plus de points.",
    "sub": "Règle 3 : commence par le chapitre que tu évites. C'est lui qui te fera gagner le plus de points."}]},

 # 14 — probabilités deux pièces
 {"date": "2026-12-14", "name": "proba-deux-pieces", "title": "2 pièces : au moins un pile ?", "cta": "B", "checks": ["1 - R(1,2)**2 == R(3,4)"],
  "caption": "On lance 2 pièces : quelle chance d'avoir au moins un pile ? 🪙 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 3e à 1re"), h("On lance 2 pièces.", 96, 30), h("Probabilité d'avoir au moins un PILE ?", 80)], "top": 540,
    "say": "On lance deux pièces. Quelle est la probabilité d'obtenir au moins un pile ?",
    "sub": "On lance 2 pièces. Probabilité d'avoir au moins un PILE ?"},
   {"slide": "same", "say": "Un demi ? Deux tiers ? Trois quarts ? À toi.", "sub": "1/2 ? 2/3 ? 3/4 ? À toi."}, CD,
   {"slide": [pill("TOUS LES CAS"), card("PP   PF   FP   FF", 90), p("4 issues, toutes aussi probables.")],
    "say": "Liste tous les cas : pile pile, pile face, face pile, face face. Quatre issues, toutes aussi probables.",
    "sub": "Tous les cas : PP, PF, FP, FF. 4 issues, toutes aussi probables."},
   {"slide": [pill("RÉPONSE", SAGE), good("P = 3/4", 120), p("Seul FF n'a aucun pile : 1 − 1/4 = 3/4.")],
    "say": "Seul face face n'a aucun pile. Donc trois cas sur quatre : la probabilité est de trois quarts.",
    "sub": "Seul FF n'a aucun pile. Donc 3 cas sur 4 : P = 3/4."}]},

 # 15 — priorités 2 + 2 × 2
 {"date": "2026-12-15", "name": "priorites-operatoires", "title": "2 + 2 × 2 = 8 ?", "cta": "A", "checks": ["2 + 2*2 == 6"],
  "caption": "2 + 2 × 2 = 8 ? 🙃 Les priorités, c'est pas une option " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 6e à 4e"), h("Combien fait…", 100, 20), big("2 + 2 × 2", 220)], "top": 540,
    "say": "Combien fait deux plus deux fois deux ?", "sub": "Combien fait 2 + 2 × 2 ?"},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("LA RÈGLE"), h("× et ÷ passent AVANT + et −", 84, 50), card("2 × 2 = 4", 96)],
    "say": "La règle : la multiplication passe avant l'addition. On calcule d'abord deux fois deux, quatre.",
    "sub": "La règle : × passe avant +. On calcule d'abord 2 × 2 = 4."},
   {"slide": [pill("RÉPONSE", SAGE), good("2 + 4 = 6", 120), bad("et pas 8", 80)],
    "say": "Puis deux plus quatre : six. Et pas huit ! Pour obtenir huit, il aurait fallu des parenthèses.",
    "sub": "Puis 2 + 4 = 6. Et pas 8 ! Pour 8, il aurait fallu des parenthèses : (2 + 2) × 2."}]},

 # 16 — signe moins devant parenthèse
 {"date": "2026-12-16", "name": "moins-devant-parenthese", "title": "Le moins devant une parenthèse", "cta": "C", "checks": ["sp.expand(-(x-3)) == -x+3"],
  "caption": "Le signe moins devant une parenthèse : l'erreur qui coûte cher ⚠️ " + TAGS,
  "scenes": [
   {"slide": [pill("ERREUR CLASSIQUE · 4e à 2nde"), h("Développe :", 96, 30), big("−(x − 3)", 220)], "top": 540,
    "say": "Développe moins, parenthèse, x moins trois.", "sub": "Développe −(x − 3)."},
   {"slide": [pill("L'ERREUR"), bad("−(x − 3) = −x − 3", 90), p("On a oublié de changer le signe du 3.")],
    "say": "L'erreur classique : écrire moins x moins trois. On a oublié de changer le signe du trois.",
    "sub": "L'erreur classique : écrire −x − 3. On a oublié de changer le signe du 3."},
   {"slide": [pill("LA RÈGLE", SAGE), h("Un moins devant la parenthèse change TOUS les signes", 76, 50), good("−(x − 3) = −x + 3", 90)],
    "say": "La règle : un signe moins devant une parenthèse change tous les signes à l'intérieur. Donc moins x plus trois.",
    "sub": "La règle : un moins devant la parenthèse change TOUS les signes. Donc −x + 3."}]},

 # 17 — limite (1+1/n)^n
 {"date": "2026-12-17", "name": "limite-e", "title": "(1 + 1/n)ⁿ tend vers 1 ?", "cta": "B", "checks": ["sp.limit((1+1/n)**n, n, sp.oo) == sp.E"],
  "caption": "(1 + 1/n)ⁿ tend vers 1 ? Le piège préféré des profs de prépa 🎓 " + TAGS_SUP,
  "scenes": [
   {"slide": [pill("DÉFI · Terminale & Prépa"), h("Quand n → +∞…", 90, 30), big("(1 + 1/n)ⁿ", 200), h("tend vers ?", 84)], "top": 480,
    "say": "Quand n tend vers plus l'infini, vers quoi tend un plus un sur n, le tout puissance n ?",
    "sub": "Quand n → +∞, vers quoi tend (1 + 1/n)ⁿ ?"},
   {"slide": "same", "say": "Indice : ce n'est pas un.", "sub": "Indice : ce n'est pas 1."}, CD,
   {"slide": [pill("LE PIÈGE"), bad("1ⁿ = 1 donc → 1", 90), p("Forme indéterminée « 1 puissance ∞ » !")],
    "say": "Le piège : se dire que un plus un sur n tend vers un, et que un puissance n, ça fait un. Mais un puissance l'infini, c'est une forme indéterminée.",
    "sub": "Le piège : « 1 + 1/n → 1 et 1ⁿ = 1 ». Mais 1 puissance ∞ est une forme indéterminée !"},
   {"slide": [pill("RÉPONSE", SAGE), good("→ e ≈ 2,718", 110), card("(1 + 1/n)ⁿ = exp(n·ln(1 + 1/n))", 60)],
    "say": "On passe à l'exponentielle : n fois logarithme de un plus un sur n tend vers un. Donc la limite, c'est e, environ deux virgule sept un huit.",
    "sub": "On passe à l'exponentielle : n·ln(1 + 1/n) → 1. Donc la limite est e ≈ 2,718."}]},

 # 18 — moyenne coefficientée
 {"date": "2026-12-18", "name": "moyenne-coefficients", "title": "Ta moyenne avec coefficients", "cta": "A", "checks": ["(8*1 + 14*2) / R(3) == 12"],
  "caption": "Ta vraie moyenne avec les coefficients 📊 (ce n'est pas 11) " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 5e à Terminale"), card("8/20  coef 1", 84), card("14/20  coef 2", 84), h("Ta moyenne ?", 90)], "top": 480,
    "say": "Tu as huit sur vingt, coefficient un, et quatorze sur vingt, coefficient deux. Quelle est ta moyenne ?",
    "sub": "8/20 coef 1, et 14/20 coef 2. Quelle est ta moyenne ?"},
   {"slide": "same", "say": "Ce n'est pas onze.", "sub": "Ce n'est pas 11."}, CD,
   {"slide": [pill("LA MÉTHODE"), h("Chaque note × son coef, puis ÷ total des coefs", 72, 50), card("(8×1 + 14×2) ÷ 3", 84)],
    "say": "La méthode : on multiplie chaque note par son coefficient, on additionne, puis on divise par le total des coefficients.",
    "sub": "Chaque note × son coef, on additionne, puis ÷ le total des coefs : (8×1 + 14×2) ÷ 3."},
   {"slide": [pill("RÉPONSE", SAGE), good("36 ÷ 3 = 12/20", 110)],
    "say": "Huit plus vingt-huit, trente-six. Divisé par trois : douze sur vingt. Le quatorze compte double, donc il tire ta moyenne vers le haut.",
    "sub": "8 + 28 = 36, et 36 ÷ 3 = 12/20. Le 14 compte double, il tire la moyenne vers le haut."}]},

 # 19 — vitesse moyenne
 {"date": "2026-12-19", "name": "vitesse-moyenne", "title": "60 km/h puis 40 km/h : moyenne 50 ?", "cta": "C", "checks": ["R(2*60*40, 60+40) == 48"],
  "caption": "Aller à 60 km/h, retour à 40 km/h : moyenne 50 ? 🚗 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 4e à Terminale"), h("Aller : 60 km/h", 90, 20), h("Retour : 40 km/h", 90, 40), h("Vitesse moyenne ?", 84)], "top": 520,
    "say": "Tu fais un trajet aller à soixante kilomètres heure, et le retour à quarante. Quelle est ta vitesse moyenne ?",
    "sub": "Aller à 60 km/h, retour à 40 km/h. Quelle est ta vitesse moyenne ?"},
   {"slide": "same", "say": "Non, ce n'est pas cinquante.", "sub": "Non, ce n'est pas 50."}, CD,
   {"slide": [pill("EXEMPLE : 120 KM"), card("aller : 120 ÷ 60 = 2 h", 74), card("retour : 120 ÷ 40 = 3 h", 74)],
    "say": "Prends un trajet de cent vingt kilomètres. L'aller prend deux heures, le retour trois heures.",
    "sub": "Prenons 120 km. Aller : 2 h. Retour : 3 h."},
   {"slide": [pill("RÉPONSE", SAGE), good("240 km ÷ 5 h = 48 km/h", 80), p("On roule plus longtemps à 40 km/h.")],
    "say": "En tout, deux cent quarante kilomètres en cinq heures : quarante-huit kilomètres heure. Moins que cinquante, parce qu'on passe plus de temps à rouler lentement.",
    "sub": "240 km en 5 h = 48 km/h. Moins que 50, car on passe plus de temps à rouler lentement."}]},

 # 20 — équation 1er degré
 {"date": "2026-12-20", "name": "equation-premier-degre", "title": "Résoudre une équation en 2 étapes", "cta": "A", "checks": ["sp.solve(3*x+5-20, x) == [5]"],
  "caption": "Résoudre une équation en 2 étapes, même si t'es nul en maths ✌️ " + TAGS,
  "scenes": [
   {"slide": [pill("MÉTHODE · 5e à 3e"), h("Résoudre", 96, 10), big("3x + 5 = 20", 180)], "top": 560,
    "say": "Résoudre trois x plus cinq égale vingt, en deux étapes.", "sub": "Résoudre 3x + 5 = 20 en 2 étapes."},
   {"slide": [pill("ÉTAPE 1"), h("On enlève 5 des deux côtés", 84, 50), card("3x = 15", 110)],
    "say": "Étape un : on enlève cinq des deux côtés. Il reste trois x égale quinze.",
    "sub": "Étape 1 : on enlève 5 des deux côtés. 3x = 15."},
   {"slide": [pill("ÉTAPE 2", SAGE), h("On divise par 3 des deux côtés", 84, 50), good("x = 5", 130)],
    "say": "Étape deux : on divise par trois des deux côtés. x égale cinq. Et on vérifie : trois fois cinq plus cinq, ça fait bien vingt.",
    "sub": "Étape 2 : on divise par 3. x = 5. Vérif : 3 × 5 + 5 = 20"}]},

 # 21 — f(-2) avec x²
 {"date": "2026-12-21", "name": "image-fonction-carre", "title": "f(x) = x², f(−2) = ?", "cta": "B", "checks": ["(lambda v: v**2)(-2) == 4"],
  "caption": "f(x) = x², combien vaut f(−2) ? Le piège des parenthèses 🔁 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 3e à 2nde"), big("f(x) = x²", 200), h("Combien vaut f(−2) ?", 86)], "top": 520,
    "say": "f de x égale x au carré. Combien vaut f de moins deux ?", "sub": "f(x) = x². Combien vaut f(−2) ?"},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("LE RÉFLEXE"), h("On remplace x PAR (−2), avec les parenthèses", 74, 50), card("f(−2) = (−2)²", 100)],
    "say": "Le réflexe : on remplace x par moins deux, entre parenthèses. f de moins deux égale moins deux, entre parenthèses, au carré.",
    "sub": "Le réflexe : on remplace x par (−2), AVEC les parenthèses. f(−2) = (−2)²."},
   {"slide": [pill("RÉPONSE", SAGE), good("f(−2) = 4", 120), bad("et pas −4", 80)],
    "say": "Moins deux fois moins deux, ça fait quatre. Sans les parenthèses, tu aurais trouvé moins quatre, et c'est faux.",
    "sub": "(−2) × (−2) = 4. Sans les parenthèses, tu aurais trouvé −4 : faux !"}]},

 # 22 — 10^-3
 {"date": "2026-12-22", "name": "puissance-negative-10", "title": "10⁻³ est négatif ?", "cta": "C", "checks": ["R(10)**-3 == R(1,1000)"],
  "caption": "10⁻³, c'est un nombre négatif ? ❄️ " + TAGS,
  "scenes": [
   {"slide": [pill("VRAI OU FAUX · 4e-3e"), big("10⁻³ < 0", 220), p("10 puissance −3 est un nombre négatif ?")], "top": 540,
    "say": "Vrai ou faux : dix puissance moins trois, c'est un nombre négatif ?",
    "sub": "Vrai ou faux : 10⁻³ est un nombre négatif ?"},
   {"slide": "same", "say": "À toi.", "sub": "À toi."}, CD,
   {"slide": [pill("FAUX !"), h("Un exposant négatif = un INVERSE", 80, 50), card("10⁻³ = 1 / 10³", 96)],
    "say": "Faux ! Un exposant négatif ne rend pas le nombre négatif. Il veut dire : l'inverse. Dix puissance moins trois, c'est un sur dix puissance trois.",
    "sub": "Faux ! Un exposant négatif veut dire INVERSE : 10⁻³ = 1/10³."},
   {"slide": [pill("RÉPONSE", SAGE), good("10⁻³ = 0,001", 110), p("Un nombre positif, mais très petit.")],
    "say": "Donc un sur mille : zéro virgule zéro zéro un. Un nombre positif, juste très petit.",
    "sub": "Donc 1/1000 = 0,001. Positif, juste très petit."}]},

 # 23 — a^0 = 1
 {"date": "2026-12-23", "name": "puissance-zero", "title": "Pourquoi 2⁰ = 1 ?", "cta": "A", "checks": ["R(2**3, 2**3) == 2**0 == 1"],
  "caption": "Pourquoi n'importe quel nombre puissance 0 vaut 1 ? 🤔 La preuve en 20 s " + TAGS,
  "scenes": [
   {"slide": [pill("LE SAVAIS-TU ? · 4e à 2nde"), big("2⁰ = 1", 240), h("Mais pourquoi ?", 86)], "top": 520,
    "say": "Deux puissance zéro égale un. Mais pourquoi ? Pas zéro ? Voici la preuve en vingt secondes.",
    "sub": "2⁰ = 1. Mais pourquoi pas 0 ? La preuve en 20 secondes."},
   {"slide": [pill("LA PREUVE"), card("2³ ÷ 2³ = 8 ÷ 8 = 1", 84), p("Un nombre divisé par lui-même, ça fait 1.")],
    "say": "Prends deux puissance trois divisé par deux puissance trois. C'est huit divisé par huit, donc un.",
    "sub": "Prends 2³ ÷ 2³. C'est 8 ÷ 8 = 1."},
   {"slide": [pill("AVEC LES RÈGLES"), card("2³ ÷ 2³ = 2³⁻³ = 2⁰", 84), good("donc 2⁰ = 1", 100)],
    "say": "Mais avec les règles des puissances, deux puissance trois divisé par deux puissance trois, c'est deux puissance trois moins trois, donc deux puissance zéro. Conclusion : deux puissance zéro, c'est un.",
    "sub": "Avec les règles : 2³ ÷ 2³ = 2³⁻³ = 2⁰. Conclusion : 2⁰ = 1."}]},

 # 24 — simplification fraction
 {"date": "2026-12-24", "name": "simplifier-fraction-piege", "title": "(2 + x)/2 = x ? Non !", "cta": "B", "checks": ["R(2+6, 2) == 4"],
  "caption": "Simplifier (2 + x)/2 = x ? Non !! ✂️ " + TAGS,
  "scenes": [
   {"slide": [pill("ERREUR CLASSIQUE · 3e à 1re"), h("Peut-on simplifier ?", 90, 40), bad("(2 + x) / 2 = x", 100)], "top": 540,
    "say": "Peut-on simplifier deux plus x, sur deux, en barrant les deux ? Réponse : non, et voici pourquoi.",
    "sub": "Peut-on simplifier (2 + x)/2 en barrant les 2 ? Non, et voici pourquoi."},
   {"slide": [pill("TESTE AVEC x = 6"), card("(2 + 6) / 2 = 8 / 2 = 4", 80), bad("et pas 6", 80)],
    "say": "Teste avec x égale six : deux plus six, huit, divisé par deux, ça fait quatre. Pas six. Donc la simplification est fausse.",
    "sub": "Teste avec x = 6 : (2 + 6)/2 = 8/2 = 4. Pas 6. La simplification est fausse."},
   {"slide": [pill("LA RÈGLE", SAGE), h("On ne simplifie que des FACTEURS, jamais des termes", 74, 50), good("(2 + x)/2 = 1 + x/2", 86)],
    "say": "La règle : on ne simplifie que des facteurs, jamais des termes d'une somme. Ici, on peut juste écrire un plus x sur deux.",
    "sub": "La règle : on simplifie des FACTEURS, jamais des termes d'une somme. Ici : 1 + x/2."}]},

 # 25 — Gauss 1 à 100
 {"date": "2026-12-25", "name": "somme-gauss", "title": "1 + 2 + … + 100 en 10 secondes", "cta": "C", "checks": ["sum(range(1, 101)) == 5050", "50*101 == 5050"],
  "caption": "1 + 2 + 3 + … + 100 en 10 secondes, l'astuce de Gauss à 9 ans 🎁 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · Tous niveaux"), big("1 + 2 + … + 100", 140), h("En 10 secondes ?", 86)], "top": 540,
    "say": "Calcule un plus deux plus trois, jusqu'à cent, en dix secondes. Le mathématicien Gauss aurait trouvé l'astuce enfant.",
    "sub": "1 + 2 + 3 + … + 100 en 10 secondes ? Gauss aurait trouvé l'astuce enfant."},
   {"slide": [pill("L'ASTUCE"), card("1 + 100 = 101", 84), card("2 + 99 = 101", 84), card("3 + 98 = 101", 84)],
    "say": "L'astuce : on regroupe les nombres par paires. Un plus cent, cent un. Deux plus quatre-vingt-dix-neuf, cent un. Trois plus quatre-vingt-dix-huit, cent un.",
    "sub": "L'astuce : des paires ! 1 + 100 = 101, 2 + 99 = 101, 3 + 98 = 101…"},
   {"slide": [pill("RÉPONSE", SAGE), card("50 paires × 101", 90), good("= 5050", 120)],
    "say": "Il y a cinquante paires qui valent toutes cent un. Cinquante fois cent un : cinq mille cinquante. Joyeux Noël !",
    "sub": "50 paires × 101 = 5050. Joyeux Noël !"}]},

 # 26 — angles triangle
 {"date": "2026-12-26", "name": "angles-triangle", "title": "Le 3e angle du triangle", "cta": "A", "checks": ["180 - 50 - 60 == 70"],
  "caption": "Le 3e angle du triangle en 5 secondes 📐 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · 6e à 4e"), h("Un triangle a deux angles :", 84, 30), card("50°  et  60°", 110), h("Le troisième ?", 86)], "top": 500,
    "say": "Un triangle a deux angles de cinquante et soixante degrés. Combien mesure le troisième ?",
    "sub": "Un triangle a deux angles : 50° et 60°. Combien mesure le troisième ?"},
   {"slide": "same", "say": "Trois secondes.", "sub": "3 secondes."}, CD,
   {"slide": [pill("LA RÈGLE"), h("La somme des angles d'un triangle fait toujours", 76, 40), card("180°", 130)],
    "say": "La règle à connaître par cœur : dans un triangle, la somme des trois angles fait toujours cent quatre-vingts degrés.",
    "sub": "La règle : dans un triangle, la somme des 3 angles fait TOUJOURS 180°."},
   {"slide": [pill("RÉPONSE", SAGE), card("180 − 50 − 60", 90), good("= 70°", 130)],
    "say": "Donc cent quatre-vingts moins cinquante moins soixante : soixante-dix degrés.",
    "sub": "Donc 180 − 50 − 60 = 70°."}]},

 # 27 — racine de x²
 {"date": "2026-12-27", "name": "racine-de-x-carre", "title": "√(x²) = x ? Pas toujours", "cta": "B", "checks": ["sp.sqrt((-3)**2) == 3", "sp.sqrt(x**2) != x"],
  "caption": "√(x²) = x ? Pas toujours ! Le piège de la valeur absolue 🔍 " + TAGS_SUP,
  "scenes": [
   {"slide": [pill("VRAI OU FAUX · 2nde à Terminale"), big("√(x²) = x", 210), p("pour tout nombre réel x ?")], "top": 540,
    "say": "Vrai ou faux : racine de x au carré égale x, pour tout nombre réel x ?",
    "sub": "Vrai ou faux : √(x²) = x, pour tout réel x ?"},
   {"slide": "same", "say": "Teste dans ta tête.", "sub": "Teste dans ta tête."}, CD,
   {"slide": [pill("FAUX !"), h("Teste avec x = −3", 86, 40), card("√((−3)²) = √9 = 3", 84), bad("3, et pas −3", 80)],
    "say": "Faux ! Teste avec moins trois : moins trois au carré, neuf. Racine de neuf, trois. On trouve trois, pas moins trois.",
    "sub": "Faux ! Avec x = −3 : √((−3)²) = √9 = 3. On trouve 3, pas −3."},
   {"slide": [pill("LA BONNE FORMULE", SAGE), good("√(x²) = |x|", 120), p("La valeur absolue : la distance à zéro, toujours positive.")],
    "say": "La bonne formule : racine de x carré égale valeur absolue de x. Une racine carrée est toujours positive.",
    "sub": "La bonne formule : √(x²) = |x|. Une racine carrée est toujours positive."}]},

 # 28 — feuille pliée
 {"date": "2026-12-28", "name": "feuille-pliee-10-fois", "title": "Une feuille pliée 10 fois", "cta": "C", "checks": ["2**10 == 1024"],
  "caption": "Tu plies une feuille 10 fois : combien d'épaisseurs ? 📄 " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI · Tous niveaux"), h("Tu plies une feuille en deux…", 84, 30), big("10 fois", 220), h("Combien d'épaisseurs ?", 80)], "top": 480,
    "say": "Tu plies une feuille en deux, dix fois de suite. Combien d'épaisseurs de papier tu obtiens ?",
    "sub": "Tu plies une feuille en deux, 10 fois de suite. Combien d'épaisseurs ?"},
   {"slide": "same", "say": "Vingt ? Cent ? Plus ?", "sub": "20 ? 100 ? Plus ?"}, CD,
   {"slide": [pill("LE RAISONNEMENT"), card("1 pli : 2\n2 plis : 4\n3 plis : 8", 80), p("À chaque pli, on double.")],
    "say": "À chaque pli, le nombre d'épaisseurs double : deux, puis quatre, puis huit, et ainsi de suite.",
    "sub": "À chaque pli, on double : 2, puis 4, puis 8…"},
   {"slide": [pill("RÉPONSE", SAGE), good("2¹⁰ = 1024", 120), p("C'est la puissance des suites géométriques.")],
    "say": "Après dix plis, deux puissance dix : mille vingt-quatre épaisseurs ! C'est ça, la puissance d'une suite géométrique.",
    "sub": "Après 10 plis : 2¹⁰ = 1024 épaisseurs ! La puissance des suites géométriques."}]},

 # 29 — inéquation signe
 {"date": "2026-12-29", "name": "inequation-sens", "title": "−2x > 6 : le piège du signe", "cta": "A", "checks": ["sp.solveset(-2*x > 6, x, sp.S.Reals) == sp.Interval.open(-sp.oo, -3)"],
  "caption": "−2x > 6 donc x > −3 ? 🚨 La règle que tout le monde oublie " + TAGS,
  "scenes": [
   {"slide": [pill("ERREUR CLASSIQUE · 3e à 2nde"), h("Résous :", 96, 20), big("−2x > 6", 220)], "top": 540,
    "say": "Résous moins deux x strictement supérieur à six.", "sub": "Résous −2x > 6."},
   {"slide": [pill("L'ERREUR"), bad("x > −3", 120), p("On a divisé par −2 sans changer le sens.")],
    "say": "L'erreur classique : diviser par moins deux et écrire x supérieur à moins trois.",
    "sub": "L'erreur classique : diviser par −2 et écrire x > −3."},
   {"slide": [pill("LA RÈGLE", SAGE), h("Multiplier ou diviser par un NÉGATIF inverse le sens", 72, 50), good("x < −3", 130)],
    "say": "La règle : quand on multiplie ou divise par un nombre négatif, on inverse le sens de l'inégalité. Donc x strictement inférieur à moins trois.",
    "sub": "La règle : × ou ÷ par un NÉGATIF → on inverse le sens. Donc x < −3."}]},

 # 30 — 2027 premier
 {"date": "2026-12-30", "name": "2027-nombre-premier", "title": "2027 est-il premier ?", "cta": "B", "checks": ["sp.isprime(2027)", "sp.sqrt(2027) < 46"],
  "caption": "2027 est-il un nombre premier ? 🎆 Le défi de la nouvelle année " + TAGS,
  "scenes": [
   {"slide": [pill("DÉFI DE NOUVEL AN"), big("2027", 300), h("est-il un nombre premier ?", 80)], "top": 520,
    "say": "Défi de nouvel an : deux mille vingt-sept est-il un nombre premier ?",
    "sub": "Défi de nouvel an : 2027 est-il un nombre premier ?"},
   {"slide": "same", "say": "Ton pronostic en commentaire.", "sub": "Ton pronostic en commentaire."}, CD,
   {"slide": [pill("LA MÉTHODE"), h("On teste les diviseurs premiers jusqu'à √2027", 72, 40), card("√2027 ≈ 45", 90), p("2, 3, 5, 7, 11, 13 … 43 : aucun ne marche.")],
    "say": "La méthode : on teste les nombres premiers jusqu'à racine de deux mille vingt-sept, environ quarante-cinq. Deux, trois, cinq, sept, et ainsi de suite jusqu'à quarante-trois : aucun ne divise deux mille vingt-sept.",
    "sub": "On teste les nombres premiers jusqu'à √2027 ≈ 45 : 2, 3, 5, 7… 43. Aucun ne divise 2027."},
   {"slide": [pill("RÉPONSE", SAGE), good("2027 est premier !", 96), p("Bonne année 2027 de la part de MathSquads.")],
    "say": "Donc oui : deux mille vingt-sept est un nombre premier. Bonne année de la part de toute l'équipe math squads !",
    "sub": "Oui : 2027 est un nombre premier ! Bonne année de la part de toute l'équipe MathSquads"}]},
]
