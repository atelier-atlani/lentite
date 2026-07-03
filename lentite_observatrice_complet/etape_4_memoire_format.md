# Étape 4 — Format de mémoire structurée
## Entité IA d'observation critique du réel

---

## PRINCIPE

La mémoire ne stocke pas de l'information — elle stocke
du jugement amélioré.

Cinq registres distincts. Chacun sert un usage précis.
Ils ne se remplacent pas — ils se complètent.

---

## REGISTRE 1 — ANALYSES ARCHIVÉES

Une entrée par dossier analysé. Sert à détecter les dossiers
similaires et à comparer les trajectoires dans le temps.

```
ANALYSE [ID auto-incrémenté]

Date :
Dossier :
Type d'objet :
  [ ] Décision politique formelle
  [ ] Conflit militaire / crise
  [ ] Politique économique
  [ ] Politique sociale
  [ ] Processus participatif
  [ ] Autre :

Registre dominant du discours officiel :
  [ ] Économique  [ ] Moral  [ ] Souverain
  [ ] Technique  [ ] Hybride

Question §0 "À qui profite le crime ?" — réponse préliminaire :

Fragment observé :
Poste d'observation :
Type d'output déclaré : [ ] Analyse du réel  [ ] Carte des discours

Hypothèse principale retenue :
Degré de confiance global : Faible / Modéré / Fort
Ce qui ferait changer l'analyse :

Agents ayant travaillé ce dossier :
  [ ] Contradicteur  [ ] Économiste  [ ] Juriste
  [ ] Sociologue  [ ] Analyste discours

Objections valides reçues : [nombre]
Révisions produites : [liste courte]

Statut : [ ] Fermé  [ ] Ouvert (dossier en cours)
```

---

## REGISTRE 2 — ERREURS ET CORRECTIONS

Une entrée par correction valide reçue. Sert à ne pas
reproduire les mêmes erreurs sur les mêmes types d'objets.

```
ERREUR [ID]

Date :
Dossier source :
Agent correcteur : Contradicteur / Économiste / Juriste /
                   Sociologue / Analyste discours / Humain

Type d'erreur :
  O1 Degré surestimé        O2 Marqueur incorrect
  O2bis Preuve fantôme      O3 Causalité sans preuve
  O4 Bénéficiaire = cause   O5 Alternative manquante
  O6 Omission non traitée   O7 Hypothèse irréfutable
  O7bis Requalification     O8 Pondération erronée
  O9 Auto-validation        EO[n] Économique
  JO[n] Juridique           SO[n] Sociologique
  DO[n] Discursif

Affirmation originale :
Affirmation corrigée :
Raison de la correction :

Condition déclenchante :
[Sur quel type d'objet cette erreur se produit-elle ?]

Règle apprise :
[Quelle instruction du protocole cette erreur a-t-elle
 produite ou devrait-elle produire ?]

Correction intégrée au protocole : [ ] Oui  [ ] Non  [ ] En attente
Fichier modifié :
```

---

## REGISTRE 3 — HYPOTHÈSES OUVERTES

Pour les dossiers en cours ou les questions transversales
qui ne sont pas tranchées. Une hypothèse reste ouverte
jusqu'à ce qu'elle soit confirmée, affaiblie ou fermée.

```
HYPOTHÈSE [ID]

Date d'ouverture :
Dossier(s) concerné(s) :
Formulation :

Indices pour (avec marqueur et date) :
  [date] [marqueur] :
  [date] [marqueur] :

Indices contre (avec marqueur et date) :
  [date] [marqueur] :

Degré de confiance actuel : Faible / Modéré / Fort
Évolution : Stable / En hausse / En baisse

Statut :
  [ ] Ouverte — insuffisamment tranchée
  [ ] Renforcée — nouveaux indices positifs
  [ ] Affaiblie — nouveaux indices négatifs
  [ ] Fermée confirmée — preuve suffisante
  [ ] Fermée invalidée — réfutée
  [ ] Suspendue — manque de données

Ce qui la ferait progresser :
[Quelle information permettrait de trancher ?]
```

---

## REGISTRE 4 — CALIBRATION DES MÉTHODES

Matrice croissante. S'enrichit à chaque dossier traité.
Sert à choisir la méthode avant de commencer l'analyse.

```
ENTRÉE MÉTHODE [ID]

Date :
Dossier :
Type d'objet :
Méthode appliquée :

Ce que cette méthode a révélé :
  -
  -

Ce que cette méthode a manqué :
  -
  -

Méthode complémentaire qui aurait manqué moins :

Leçon pour les dossiers futurs de ce type :
[Si objet = [type], alors appliquer [méthode] en priorité
 et ne pas oublier [angle manquant]]
```

**Matrice synthétique (mise à jour après chaque entrée) :**

| Type d'objet | Méthode principale | Méthodes complémentaires | Angle souvent manqué |
|---|---|---|---|
| Décision politique formelle | Chaîne décisionnelle | Alternatives écartées, discours | Effets sectoriels |
| Conflit actif | Carte des discours | Aucune analyse du réel possible | Niveau de contamination info |
| Politique sociale | Sociologique + Économique | Territorial | Distribution par groupe |
| Processus participatif | Discours + Chaîne | Économique (qui bénéficie) | Registre de légitimation |

---

## REGISTRE 5 — PATTERNS RÉCURRENTS

Observations transversales qui dépassent un dossier unique.
Se constitue progressivement à mesure que les dossiers s'accumulent.

### 5A — Patterns discursifs

```
PATTERN DISCURSIF [ID]

Observation :
[Registre utilisé systématiquement pour quel type de décision]

Dossiers où observé :
  -

Fonction produite :
[Ce que ce registre produit systématiquement]

Vulnérabilité systématique :
[Comment ce registre peut être retourné]

Intérêts que ce registre rend systématiquement invisibles :
```

### 5B — Patterns sectoriels ("à qui profite")

```
PATTERN SECTORIEL [ID]

Observation :
[Quel secteur bénéficie systématiquement de quel type de contrainte]

Dossiers où observé :
  -

Mécanisme économique :
[Pourquoi ce secteur bénéficie de cette contrainte]

Hypothèse transversale :
[Ce que ce pattern suggère sur la structure des décisions]

Degré de confiance : Faible / Modéré / Fort
```

### 5C — Patterns d'erreurs systématiques de l'entité

```
PATTERN D'ERREUR [ID]

Erreur récurrente :
[Type + Condition déclenchante]

Dossiers où produite :
  -

Instruction manquante ou insuffisante dans le protocole :

Correction à apporter :
```

---

## RÈGLE DE NON-ACCUMULATION

La mémoire n'est pas un archive — c'est un filtre.

Seul ce qui améliore le jugement est mémorisé.
Un fait documenté qui n'améliore pas la méthode
ou n'ouvre pas une hypothèse transversale
ne va pas dans la mémoire — il reste dans le dossier source.

Révision annuelle : supprimer les entrées qui n'ont pas
été consultées depuis 12 mois. Si une entrée n'est pas utile,
elle encombre.
