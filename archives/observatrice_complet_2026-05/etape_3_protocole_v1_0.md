# Protocole d'interaction — Étape 3
## Entité + Contradicteur + Agents spécialisés
## Économiste et Juriste

---

## PRINCIPE

L'Étape 3 ajoute des agents spécialisés après le cycle Étape 2
(contradicteur général). Chaque agent apporte un angle disciplinaire
que le contradicteur général n'explore pas.

La différence fondamentale entre contradicteur et agents spécialisés :

| | Contradicteur | Agent spécialisé |
|---|---|---|
| Rôle | Attaquer | Attaquer + Ajouter |
| Angle | Épistémique général | Disciplinaire ciblé |
| Répète les objections précédentes ? | N/A | Non |
| Produit des additions ? | Non | Oui |

---

## AGENTS SPÉCIALISÉS DISPONIBLES

| Agent | Prompt | Angle central |
|-------|--------|--------------|
| Économiste | etape_3_prompt_economiste_v1_0 | Flux, coûts, incitations, contrefactuel |
| Juriste | etape_3_prompt_juriste_v1_0 | Contrainte réelle vs invoquée, outils non utilisés |
| Sociologue | etape_3_prompt_sociologue_v1_0 | Groupes, inégalités, logiques institutionnelles |
| Analyste du discours | etape_3_prompt_analyste_discours_v1_0 | Vocabulaire, sources, invisible, symétrie |

---

## SÉQUENCE COMPLÈTE ÉTAPES 2 + 3

```
T1 — Entité produit l'analyse (prompt v1.2)
T2 — Contradicteur attaque (prompt v1.1)
T3 — Entité répond et révise

T4 (parallèle) — Les 4 agents spécialisés travaillent
                 simultanément sur l'analyse révisée T3
                 Chaque agent reçoit aussi les outputs
                 des agents précédents pour éviter
                 les répétitions

T5 — Entité intègre les 4 lectures spécialisées
T6 — Synthèse finale consolidée
```

Option séquentielle (si les agents se nourrissent mutuellement) :
T3 → T4 Économiste → T5 Intégration →
T6 Juriste → T7 Intégration →
T8 Sociologue → T9 Intégration →
T10 Analyste discours → T11 Intégration →
T12 Synthèse finale

Règle de non-répétition : chaque agent reçoit
les objections déjà formulées par les agents précédents.
Il ne les répète pas. Il commence là où ils s'arrêtent.

---

## TEMPS 4 — AGENT ÉCONOMISTE

**Input :** Analyse révisée après T3 + dossier original
**Output :** Lecture économique + objections économiques
  + questions ouvertes économiques

**Instruction de non-répétition :**
L'économiste lit d'abord les objections du contradicteur (T2)
et l'auto-évaluation de l'entité. Il ne répète pas ce qui
a déjà été identifié. Il commence là où le contradicteur s'est arrêté.

**Ce que l'économiste cherche spécifiquement :**
- Flux budgétaires non tracés dans l'analyse
- Incitations ignorées (comportements d'adaptation prévisibles)
- Bénéficiaires identifiés sans magnitude
- Coûts sans distribution (qui paie vraiment ?)
- Contrefactuels absents
- Contraintes économiques invoquées mais non vérifiées

---

## TEMPS 5 — INTÉGRATION ÉCONOMISTE

**Format de réponse de l'entité :**

```
INTÉGRATION DE LA LECTURE ÉCONOMIQUE

Objections économiques acceptées :
  OE[n] — [Statut : Valide / Partiel / Non valide]
  Révision : [Ce qui change]

Points économiques ajoutés à l'analyse :
  Point [n] — [Accepté / Contesté / Noté comme limite]
  [Si contesté : pourquoi]

Questions économiques ouvertes intégrées comme limites :
  [Liste]

Impact sur les hypothèses :
  [Est-ce qu'un ajout économique renforce ou affaiblit
   une hypothèse existante ?]
```

---

## TEMPS 6 — AGENT JURISTE

**Input :** Analyse révisée après T5 + dossier original
**Output :** Lecture juridique + objections juridiques
  + questions ouvertes juridiques

**Instruction de non-répétition :**
Le juriste lit les objections du contradicteur (T2) et de
l'économiste (T4). Il ne répète pas ce qui a été identifié.
Il applique uniquement son angle disciplinaire.

**Ce que le juriste cherche spécifiquement :**
- Contraintes juridiques invoquées (sont-elles réelles ?)
- Outils juridiques disponibles non utilisés
- Dispositions sans mécanisme d'application effectif
- Statuts normatifs mal qualifiés (loi / décret / circulaire)
- Engagements préexistants non examinés
- Lacunes de base juridique

---

## TEMPS 7 — INTÉGRATION JURISTE

**Format identique à T5, adapté au droit :**

```
INTÉGRATION DE LA LECTURE JURIDIQUE

Objections juridiques acceptées :
  OJ[n] — [Statut]
  Révision : [Ce qui change]

Points juridiques ajoutés :
  [Accepté / Contesté / Limite]

Impact sur les hypothèses :
  [Un ajout juridique change-t-il le niveau de confiance
   d'une hypothèse ?]
```

---

## TEMPS 8 — SYNTHÈSE FINALE CONSOLIDÉE

L'entité produit la version finale de l'analyse intégrant :
- Les révisions du T3 (contradicteur)
- Les révisions du T5 (économiste)
- Les révisions du T7 (juriste)

Format de la synthèse finale :

```
ANALYSE CONSOLIDÉE — VERSION FINALE

Versions :
  T1 (analyse initiale) → T3 (post-contradicteur)
  → T5 (post-économiste) → T7 (post-juriste)

Delta total :
  Ce qui a changé entre T1 et la version finale

Ce qui tient après toutes les attaques :
  [Hypothèses et conclusions maintenues]

Ce qui a été révisé :
  [Liste des révisions avec motif]

Ce qui reste ouvert :
  [Questions non résolues après les 4 agents]

Confiance globale dans l'analyse :
  [Faible / Modérée / Forte — justifiée]
```

---

## GRILLE D'ÉVALUATION ÉTAPE 3

| Critère | Présent |
|---------|---------|
| Économiste ne répète pas le contradicteur | |
| Juriste ne répète pas économiste ni contradicteur | |
| Objections disciplinaires fondées sur mécanismes | |
| Additions disciplinaires sourcées ou marquées | |
| Entité révise sur objections valides | |
| Entité maintient sur objections non valides | |
| Impact sur hypothèses tracé explicitement | |
| Synthèse finale distingue ce qui tient et ce qui change | |

---

## ARCHIVAGE ÉTAPE 3

```
Dossier :
Date :

Agent contradicteur : objections valides [n] / total [n]
Agent économiste : objections [n], additions [n]
Agent juriste : objections [n], additions [n]

Révisions T3 (contradicteur) : [liste courte]
Révisions T5 (économiste) : [liste courte]
Révisions T7 (juriste) : [liste courte]

Hypothèses renforcées après Étape 3 : [liste]
Hypothèses affaiblies après Étape 3 : [liste]
Hypothèses maintenues : [liste]

Questions ouvertes non résolues : [liste]

Delta qualitatif T1 → Final : [en une phrase]

Agents à ajouter pour ce type de dossier :
  [Sociologue / Historien / Analyste du discours / Autre]
```

---

## QUAND AJOUTER D'AUTRES AGENTS

Les agents économiste et juriste couvrent les angles
matériels (flux, coûts, incitations) et normatifs (droit,
contraintes, outils). D'autres angles restent non couverts :

| Angle manquant | Agent à ajouter |
|----------------|----------------|
| Groupes sociaux, comportements collectifs | Sociologue |
| Trajectoires historiques comparées | Historien |
| Récits, vocabulaire, propagande | Analyste du discours |
| Signaux faibles, intentions stratégiques | Analyste stratégique |
| Information en temps de crise | Spécialiste désinformation |

Règle : ajouter un agent seulement si l'angle manquant
est central au dossier et ne peut pas être couvert
par les agents déjà disponibles.
