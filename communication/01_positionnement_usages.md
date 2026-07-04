# L'Entité — Positionnement & usages

*Document dérivé (communication/pilotage). La doctrine (couche A) et les décisions `.claude/decisions/` font foi. Présuppose le document maître (00) lu — notamment l'identité à deux étages noyau/instance.*

*Version 1.0 — 4 juillet 2026. Licence CC BY 4.0.*

---

## 1. Le positionnement en une phrase

**L'Entité occupe le vide entre quatre mondes qui ne se parlent pas : elle apporte au journalisme la formalisation qu'il n'a pas, à l'académie la vitesse qu'elle n'a pas, au renseignement la transparence qu'il refuse, et à l'IA générative la discipline qu'elle ignore.**

Version courte, usage oral : *« Un enquêteur outillé par IA qui remet des dossiers vérifiables — jamais des réponses. »*

## 2. Le carré de positionnement

| Monde voisin | Ce qu'il a | Ce qui lui manque | Pourquoi il ne comblera pas le vide |
|---|---|---|---|
| Journalisme | L'objet (le réel politique), l'accès, l'audience | La formalisation, la traçabilité, la révisabilité outillée | Payé à la vitesse et au récit — les defeaters ralentissent et affaiblissent le titre |
| Académie | La méthode (process tracing, analyse d'hypothèses concurrentes) | La vitesse, l'outillage à l'échelle | Son système d'incitations la rend lente ; publier prime sur instrumenter |
| Renseignement / conseil | L'outillage (Palantir, SAT), les moyens | La transparence, la symétrie | Payé à la conclusion qui sert le client — exposer ses propres failles se vend mal |
| IA générative | L'échelle, la puissance | La discipline, l'auditabilité du chemin | Payée à l'engagement — l'oracle engage, l'enquêteur frustre |

**La douve n'est pas technique, elle est incitative** : chacun de ces mondes peut copier la stack en trois semaines ; aucun ne peut adopter la discipline sans contredire son modèle de revenus. La discipline de L'Entité est coûteuse *pour eux* structurellement. C'est pourquoi la singularité, bien que fragile en interne (elle ne tient qu'à la liste des éléments fermes de la charte), est défendable en externe.

**La preuve de discipline comme promesse de marque** : chaque dossier publié permet à un tiers de vérifier mécaniquement que la méthode a été tenue (defeaters présents, clôture de corpus déclarée, chemin rejouable, validateurs publics avec leurs tests négatifs). Phrase de marque : *« N'importe qui peut vérifier que nous avons tenu notre méthode. »* Aucun des quatre mondes ne peut la prononcer. Engagement effectif au jalon 2 : avant le passage public du cœur et le premier dossier Mode 1, cette phrase est une promesse documentée, pas encore une preuve publique.

## 3. Publics et usages, par mode

| Mode | Public | Ce qu'il reçoit | Ce qu'il en fait |
|---|---|---|---|
| 0 — Atelier (actif) | Le projet, le co-dirigeant, demain un comité de lecture | La méthode elle-même : gabarit, calibration, journal | Discipline cumulative ; onboarding par calibration |
| 1 — Éclairage (jalon 2) | Journalistes d'investigation, chercheurs, analystes, ONG | Dossiers d'enquête : chronologies reconstruites, écarts dit/fait, omissions, hypothèses hiérarchisées avec defeaters | Temps d'enquête compressé ; les defeaters comme programme de vérification |
| 2 — Conseil (jalon 3) | Décideurs publics et privés, sous contrat | Scénarisation, cartographie des rapports de force, conséquences non voulues — sans prescription | Décision informée ; la matrice postes × poids causaux comme lecture multi-perspectives |
| 3 — Chat public (reporté) | Grand public | Auto-pédagogie de la distinction | Hors scope jusqu'à décision doctrinale contraire |

Grille d'arbitrage pour tout nouvel usage (les quatre variables) : **fonction** (documenter / scénariser / diffuser / se discipliner) × **symétrie d'accès** (ouvert vs contractuel) × **automatisation** (où l'humain reste en boucle) × **responsabilité** (qui signe, qui répond). Aucun usage n'est validé sans réponse aux quatre.

## 4. Anti-positionnement — ce que L'Entité refuse d'être

Le projet étant difficilement communicable, la moitié du positionnement consiste à désamorcer les cases où l'interlocuteur voudra le ranger :

- **Pas un fact-checker** : le fact-checking vérifie des énoncés isolés contre des faits établis ; L'Entité documente des écarts et construit des hypothèses causales révisables. Le fact-checker dit vrai/faux ; L'Entité dit « voici le chemin, voici ce qui l'invaliderait ».
- **Pas un média** : elle ne produit pas de récit, elle produit des dossiers. Le récit est précisément ce qu'elle met à distance (dimension 2 de son objet).
- **Pas un oracle IA** : la valeur ne vient pas de la puissance du modèle mais de la contrainte qui lui est imposée. Le LLM propose, le validateur juge, l'humain arbitre.
- **Pas un Palantir** : l'asymétrie est son repoussoir constitutif — le cœur est public (jalon 2), le chemin auditable, le Mode 2 encadré par une charte qui lui interdit certains usages.
- **Pas un détecteur de mensonges ni un juge d'intentions** : le « voulu » est le niveau le plus incertain de la quadripartition et porte le régime de preuve le plus exigeant ; l'intentionnalité est hypothétisée sous defeaters, jamais assertée.
- **Pas une prétention à la vérité** : *la vérité est dans la qualité du chemin* — le projet livre des conclusions attaquables proprement, c'est sa définition du progrès épistémique.

## 5. Objections anticipées et réponses

**« C'est biaisé — qui décide du poste d'observation ? »** Tout observateur a un poste ; les autres le cachent, L'Entité le déclare, ce qui le rend attaquable — et son évolution (postes multiples instrumentés) fera de la divergence entre postes une donnée du dossier plutôt qu'un vice caché.

**« Un LLM hallucine — comment faire confiance ? »** On ne lui fait pas confiance : tout ce qu'il produit est candidat, rejeté mécaniquement s'il ne porte pas sources, defeaters et clôture de corpus. Les tests négatifs sont publics : on peut vérifier que les contraintes mordent.

**« Qui est responsable si un dossier se trompe ? »** Signature humaine des dossiers, procédure de contestation, et aucune publication avant le verrou juridique (jalon 2). Se tromper est prévu par construction : chaque dossier porte ses conditions de révision, et les révisions sont tracées.

**« Quel est le modèle économique ? »** Distribution duale jalonnée : cœur public (AGPL), service de conseil sous contrat (Mode 2) — l'auditabilité précède la monétisation, dans cet ordre, par décision documentée.

**« Pourquoi pas simplement demander à ChatGPT ? »** Réponse en une démonstration : poser la même question aux deux, et comparer ce qui est vérifiable dans les deux réponses. L'un rend une synthèse plausible ; l'autre rend un dossier dont chaque affirmation expose son chemin et ses failles.

**« Ça existe déjà (GDELT, Bellingcat, e-discovery…). »** Chaque brique existe ; l'assemblage n'existe pas. Personne ne combine l'omission comme objet formel, la réfutabilité comme contrainte de schéma et l'auditabilité publique du chemin. Et personne n'a intérêt à le faire (cf. §2, la douve incitative).

## 6. Messages par interlocuteur

- **Au journaliste / à l'analyste** : « Trois semaines de dépouillement compressées en un dossier structuré — et la liste de ce qui invaliderait chaque conclusion, avant que vos contradicteurs ne la trouvent. »
- **Au chercheur** : « Le paradigme indiciaire outillé : process tracing et analyse d'hypothèses concurrentes, exécutés à l'échelle, avec calibration mesurée et corpus clos déclarés. »
- **Au décideur (Mode 2)** : « Une lecture froide multi-perspectives : ce que le dossier établit, ce dont il doute, ce qui dépend du point de vue — et le programme de vérification pour trancher. »
- **Au financeur / à la fondation** : « Une infrastructure épistémique ouverte contre la double pathologie du débat public — la naïveté et le complotisme — avec une preuve de discipline vérifiable par quiconque. »
- **À l'associé technique** : « Un système où la valeur vient de la contrainte, pas de la puissance : validateurs, source de vérité en fichiers, graphe dérivé, orchestration auditable ligne à ligne. »
- **À l'étudiant** : « Une machine à apprendre la distinction : fait, inférence, hypothèse — et l'exercice le plus formateur qui soit : attaquer les defeaters. »

## 7. Discipline de communication

- Toujours présenter les **deux étages** dans cet ordre : l'instance prouve (l'observatoire politique), le noyau se transpose (la méthode). Inverser produit un manifeste abstrait ; fusionner produit un malentendu de média.
- Ne jamais promettre au-delà du dossier zéro tant qu'il n'existe pas : avant lui, le discours public est celui de la méthode en construction, documentée en marche.
- Vocabulaire à bannir : « vérité » (sauf dans la phrase-cœur), « détecter les mensonges », « IA objective », « neutre », « prédire ». Vocabulaire à employer : dossier, chemin, écart, hypothèse, defeater, poste d'observation, auditable, révisable.
- Toute communication d'analyse nommant des acteurs vivants attend le jalon 2 — sans exception, y compris pédagogique.

---

*Document 01 v1.0 — 4 juillet 2026. Emplacement cible : `communication/01_positionnement_usages.md`.*
