# Protocole d'interaction v1.1
## Entité principale + Agent contradicteur
### Mis à jour après deux sessions de test

---

## CHANGELOG v1.0 → v1.1

- Ajout : déclaration du type d'output avant le Temps 2
- Ajout : critère d'une objection nulle (signal que l'analyse tient)
- Mise à jour : archivage avec champ "patterns détectés"
- Mise à jour : critères de passage Étape 3
- Clarification : "moins réfutée" ≠ "meilleure explication"

---

## PRINCIPE

L'entité produit. Le contradicteur attaque. L'entité répond.
Le résultat est une analyse révisée — ou une analyse maintenue
avec les objections réfutées. Les deux sont valides.

Une entité qui accepte toutes les objections est aussi défaillante
qu'une entité qui n'en accepte aucune.

---

## TEMPS 1 — ANALYSE PRINCIPALE

**Qui :** L'entité (prompt système v1.2)
**Input :** Le dossier brut — faits, sources disponibles, sources absentes
**Output :** Protocole v1.2 complet, incluant le TYPE D'OUTPUT DÉCLARÉ

Le type d'output déclaré conditionne l'attaque du contradicteur :
- Analyse du réel → le contradicteur attaque sur tous les types O1-O9
- Carte des discours → le contradicteur vérifie que la limitation
  est bien nommée comme limite (O7bis) et que la carte produite
  est effectivement plus précise que ce que d'autres ont produit

---

## TEMPS 2 — ATTAQUE DU CONTRADICTEUR

**Qui :** Le contradicteur (prompt v1.1)
**Input :** L'analyse complète du Temps 1
**Séquence obligatoire :**

1. Effectuer les trois vérifications préliminaires (V1, V2, V3)
2. Identifier 3 à 5 objections ciblées
3. Produire chaque objection au format prescrit
4. Produire le bilan

**Si aucune objection solide n'est trouvée :**
Le dire explicitement. Ce n'est pas un échec du contradicteur —
c'est un signal que l'analyse tient sur ce dossier avec ces sources.
Une analyse irréprochable sur un dossier pauvre n'est pas
un résultat moins valide qu'une analyse attaquable sur un dossier riche.

---

## TEMPS 3 — RÉPONSE DE L'ENTITÉ

**Input :** Analyse T1 + objections T2
**Format pour chaque objection :**

```
RÉPONSE À L'OBJECTION [numéro]

Statut : [ ] Valide  [ ] Partiellement valide  [ ] Non valide

Si valide :
Révision :
[Formulation corrigée, degré abaissé, marqueur corrigé, ou limite reconnue]

Si partiellement valide :
Ce qui est juste :
Ce qui ne l'est pas :
Révision partielle :

Si non valide :
Réfutation :
[Argument et preuve qui maintiennent l'affirmation]
```

**Puis : ANALYSE RÉVISÉE**
Sections impactées par les objections valides ou partiellement valides.
Les objections non valides sont enregistrées comme réfutées, pas intégrées.

---

## GRILLE D'ÉVALUATION DU TEMPS 3

| Critère | Présent | Absent |
|---------|---------|--------|
| Chaque objection reçoit une réponse | | |
| Le statut (valide/partiel/non) est explicité | | |
| Les révisions sont précises, pas vagues | | |
| Les objections non valides sont réfutées avec preuve | | |
| L'analyse révisée intègre les corrections | | |
| L'entité ne cède pas à des objections injustifiées | | |
| Les degrés de confiance révisés sont cohérents | | |
| La synthèse dit "moins réfutée" pas "meilleure explication" | | |

---

## CE QU'ON MESURE

**Avant l'attaque :** qualité formelle (grille auto-évaluation)
**Après l'attaque :** qualité épistémique (cohérence, consistance, honnêteté)
**Le delta :** ce que le contradicteur apporte réellement

Si le delta est nul sur deux dossiers consécutifs, le contradicteur
est trop faible — renforcer le prompt, pas conclure que l'entité est parfaite.

---

## ARCHIVAGE — FORMAT COMPLET

```
Dossier :
Date :
Type d'objet du dossier :
Type d'output déclaré par l'entité :
Contradicteur : Claude / Humain (préciser)
Prompt version : v1.0 / v1.1 / ...

Objections produites : [nombre]
  Valides : [nombre]
  Partiellement valides : [nombre]
  Non valides : [nombre]

Sections révisées : [liste]

Patterns détectés :
  [ ] Degré de confiance surestimé (O1)
  [ ] Marqueur épistémique incorrect (O2)
  [ ] Preuve fantôme dans l'analyse (O2bis)
  [ ] Preuve fantôme dans la fiche (O2bis renforcé)
  [ ] Causalité sans preuve (O3)
  [ ] Bénéficiaire présenté comme cause (O4)
  [ ] Alternative non examinée (O5)
  [ ] Omission non traitée (O6)
  [ ] Hypothèse irréfutable (O7)
  [ ] Requalification de limite en méthode (O7bis)
  [ ] Pondération abstraite (O8)
  [ ] Auto-validation méthodologique (O9)

Patterns non détectés par le contradicteur :
  [Angles morts du prompt contradicteur identifiés]

Delta qualitatif principal :
  [En une phrase]

Instructions à ajouter au prompt contradicteur :
  [Si applicable]

Critère de passage Étape 3 : Atteint / Non atteint
```

---

## CRITÈRES DE PASSAGE ÉTAPE 3

L'Étape 3 (agents spécialisés multiples) est déclenchée quand :

1. Le protocole en 3 temps a fonctionné sur au moins **2 dossiers
   de types différents** (ex. : politique domestique + conflit actif)
2. Sur chaque dossier, le contradicteur a trouvé des objections valides
3. L'entité a révisé correctement sur les objections valides
4. L'entité a maintenu correctement sur les objections non valides
5. Le delta qualitatif entre Temps 1 et Temps 3 est documenté
   et positif sur les deux dossiers

**Critère atteint après les sessions Loi Climat + Guerre Iran.**

---

## STRUCTURE DE L'ÉTAPE 3

L'Étape 3 ajoute des agents spécialisés selon le type de dossier.
Chaque agent spécialisé a un angle disciplinaire unique.

Agents disponibles selon le dossier :

| Dossier politique / social | Dossier militaire / géopolitique |
|---------------------------|----------------------------------|
| Sociologue | Analyste stratégique |
| Juriste | Juriste droit international |
| Économiste | Économiste (énergie, sanctions) |
| Historien | Historien régional |
| Analyste du discours | Analyste de la propagande |
| Red team général | Red team désinformation |

Protocole Étape 3 :
1. Entité produit l'analyse (T1, prompt v1.2)
2. Contradicteur général attaque (T2, prompt v1.1)
3. Entité révise (T3)
4. Agent spécialisé attaque depuis son angle disciplinaire (T4)
5. Entité révise à nouveau (T5)
6. Synthèse finale

L'Étape 3 sera formalisée après la validation sur un troisième
dossier avec le protocole en 3 temps.
