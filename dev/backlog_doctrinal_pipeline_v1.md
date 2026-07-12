# L'Entité — Backlog doctrinal pour le pipeline

*Document de liaison entre la couche doctrinale et la couche de développement. Produit en Mode Architecte après exploration d'un corpus épistémologique (abduction, non-monotonie, défaisabilité, raisonnement temporel, causalité, argumentation) et examen d'un champ exploratoire externe.*

*Vocation — dire au dev ce qui, de cette exploration, se traduit en code, quand, et surtout ce qui ne doit PAS s'y traduire. La partie la plus utile de ce document est la section 4 (refus motivés) : elle protège les Phases 0-1 de la dispersion.*

*Destinataires — Mode Architecte (plans), Mode Implementer (exécution), Mode Reviewer (contrôle de non-dérive).*

---

## 0. Principe de tri

L'exploration doctrinale a produit une *fondation épistémologique* (section candidate de la charte) qui est **strictement descriptive**. Elle nomme les filiations du raisonnement déjà pratiqué — elle n'invente rien et n'exige rien.

**Conséquence directe pour le dev : la fondation, en elle-même, ne demande aucun code.** Si elle était classée sans suite, le pipeline serait inchangé et valide.

Ce backlog isole le sous-ensemble étroit qui a une valeur d'implémentation réelle. Il est volontairement maigre. Un backlog qui gonflerait après une session d'exploration théorique serait le signal que la théorie a pris le dessus sur la production — le failure pattern que le projet surveille.

---

## 1. Immédiat — révision mineure v2.1.2 (deux champs)

Deux amendements de schéma. Légers, optionnels, rétrocompatibles. **Aucun YAML existant n'est invalidé.** Exécutables par un Implementer en une session courte.

### 1.1 Typage des defeaters

**Problème constaté.** Le gabarit exige au moins deux defeaters par conséquence plausible (chaîne causale aval). Cette contrainte est satisfaisable par deux objections *de même nature*, ce qui laisse la conclusion non testée sous l'autre angle. Le corpus montre une domination écrasante d'un seul type — les attaques qui fragilisent le lien causal — et une rareté des attaques frontales sur la conclusion elle-même.

**Amendement.** Ajouter au modèle `Defeater` (ou à la structure de defeater dans `downstream_causal_chains`) un champ :

```python
class DefeaterType(str, Enum):
    REBUTTING = "rebutting"      # raison de croire la conclusion contraire
    UNDERCUTTING = "undercutting" # raison de croire que le lien prémisse→conclusion ne tient pas
```

Champ `defeater_type: DefeaterType | None = None` — **optionnel** en v2.1.2.

**Définitions opérationnelles pour l'analyste (à documenter dans le gabarit).**

- *Rebutant* — j'ai une raison de penser que c'est l'inverse qui se produira. Il annonce généralement une hypothèse concurrente.
- *Sapant* — je ne dis pas que l'inverse se produira ; je dis que le lien invoqué ne suffit pas. Il fragilise sans renverser.

**Validation.** Aucune contrainte bloquante en v2.1.2 (champ optionnel). Un test négatif peut être ajouté plus tard si l'on décide d'exiger au moins un rebutant par chaîne.

**Audit associé (à brancher sur l'infrastructure d'audit existante).** `defeater_balance_audit` — distribution rebutants/sapants sur fenêtre roulante. Une écrasante majorité de sapants signale une contradiction systématiquement timide : la méthode fragilise les liens mais n'ose pas envisager l'issue inverse.

### 1.2 Qualification des conditions de révision

**Problème constaté.** Les conditions de révision inscrites en fin d'analyse ne distinguent pas deux situations qui n'ont pas les mêmes conséquences.

**Amendement.** Ajouter au modèle des conditions de révision :

```python
class ChangeType(str, Enum):
    REVISION = "revision"  # le monde n'a pas changé — la croyance était fausse/incomplète
    UPDATE = "update"      # le monde a changé — l'analyse n'était pas fausse, sa fenêtre se clôt
```

Champ `change_type: ChangeType | None = None` — **optionnel** en v2.1.2.

**Pourquoi ça compte analytiquement.** Une *révision* atteint rétroactivement la solidité de l'analyse (on s'était trompé). Une *mise-à-jour* ne l'atteint pas (le monde a bougé). Les confondre produit deux erreurs symétriques : croire qu'on a échoué quand le monde a simplement évolué, ou croire que le monde a évolué quand on s'était trompé.

**Cas de référence disponibles dans le corpus** pour tester le champ : le désaveu d'un chiffrage par une institution mandatée (révision — la situation n'avait pas bougé, l'estimation était fausse) ; une censure parlementaire (mise-à-jour — l'analyse antérieure restait juste, son objet a changé).

### 1.3 Livrables attendus de la session

- `schemas.py` — deux enums + deux champs optionnels.
- Gabarit — deux paragraphes de définition opérationnelle (section correspondante).
- Tests — un test positif par champ (YAML valide avec le champ renseigné), un test de rétrocompatibilité (YAML sans le champ → toujours valide).
- Aucune modification des YAML existants (rétrocompatibilité stricte).

**Estimation** — session courte. Modèle recommandé : Sonnet.

---

## 2. Phase 3 (persistance) — structure cible : le graphe abductif

**À ne pas engager avant que la persistance soit décidée et la Phase 1-2 livrée.** Cette section est une *spécification d'intention*, pas une tâche.

### 2.1 Motif

Les registres actuels (JSON plats) stockent les hypothèses ouvertes, les erreurs, les patterns. Ils ne permettent pas de *requêter les relations* entre eux. Or les audits inscrits à la doctrine sont, dans leur forme, des requêtes sur relations — quelle hypothèse a été défaite par quoi, quels defeaters ont porté, quelle distribution d'écarts sur quelle fenêtre.

Tant que ces audits se font par comptage manuel, ils seront faits tard ou pas du tout.

### 2.2 Structure

Un graphe distinct du graphe discursif (acteurs/propositions/objets), dédié au raisonnement lui-même.

**Nœuds** — `Fact` (fait établi), `Inference` (inférence, avec confidence et premise), `Hypothesis` (hypothèse concurrente, avec confidence et type intentionnel/non-intentionnel), `Observation` (effet observé, pattern temporel).

**Arêtes typées** —
- `supports` (fait → inférence, inférence → hypothèse)
- `rebuts` (defeater rebutant → conclusion attaquée)
- `undercuts` (defeater sapant → lien attaqué)
- `revises` (observation → inférence antérieure, avec `change_type`)
- `competes_with` (hypothèse ↔ hypothèse)

**Propriété.** L'acceptabilité est *graduelle*, pas binaire — les confidences ne sont pas des probabilités mais des degrés de survie d'un argument après attaque. Toute agrégation doit préserver cette gradualité.

### 2.3 Audits reformulés en requêtes

- `intentionality_bias_audit` → distribution des confidences par `type` d'hypothèse, sur fenêtre roulante.
- `hypothesis_gap_audit` → distribution des écarts entre les deux hypothèses dominantes.
- `defeater_balance_audit` → ratio `rebuts` / `undercuts`.
- `typology_audit` → fréquence d'apparition des types de patterns et d'effets, détection des candidats hors typologie.

### 2.4 Note d'implémentation

Représentation en mémoire (par run, reconstruite) et persistance ne sont **pas concurrentes** : la première sert au calcul d'une analyse, la seconde à l'accumulation inter-analyses. Le choix du support de persistance relève des décisions structurantes de Phase 0 et n'est pas préempté ici.

---

## 3. Notes de vigilance (à verser dans les plans concernés)

### 3.1 Phase 2 — piège de l'agrégation multi-agents

Quand plusieurs agents produisent des analyses partiellement divergentes, l'orchestrateur devra les agréger. **L'agrégation naïve (moyenne, vote majoritaire) viole des propriétés de rationalité connues** — notamment le fait que le résultat fusionné devrait rester cohérent avec chaque contribution individuelle, propriété qu'aucun opérateur simple ne garantit.

Ce n'est pas un chantier à ouvrir. C'est un piège à connaître *au moment où l'orchestrateur agrégera*. Recommandation minimale : ne pas moyenner les confidences ; conserver les divergences comme divergences et les remonter à l'humain plutôt que de les lisser.

### 3.2 Toutes phases — asymétrie OWA/CWA à maintenir consciemment

**L'analyse opère en monde ouvert** — ce qui n'est pas observé n'est pas faux. **Le pipeline valide en monde clos** — ce qui n'est pas prévu par le schéma est rejeté.

Cette asymétrie est saine et doit être *maintenue*. Deux dérives symétriques à surveiller :

- Un schéma qui s'assouplirait pour « accepter les cas particuliers » **cesserait de mordre** — c'est ce qui rend les tests négatifs indispensables.
- Une analyse qui traiterait l'absence de donnée comme une donnée d'absence **cesserait d'enquêter** — c'est ce que garde la distinction entre fenêtre ouverte et fenêtre close.

Le Reviewer doit vérifier périodiquement que ni l'une ni l'autre n'a glissé.

### 3.3 Frictions de typologie — procédure déjà établie, à ne pas contourner

Quand le pipeline rencontre un cas qui ne rentre pas dans une typologie (effet observable, relation d'arène, pattern), la discipline est : **requalifier dans le type existant le plus proche, inscrire la friction pour examen ultérieur, ne jamais étendre la typologie à chaud.** L'extension n'est justifiée qu'après plusieurs cas externes documentables.

Deux candidats sont actuellement en attente d'examen. Ils ne doivent pas être intégrés au schéma tant que le seuil de cas n'est pas atteint.

---

## 4. Refus motivés — ce qu'il ne faut PAS coder

*Section la plus importante de ce document. Elle protège les Phases 0-1 de la dispersion. Toute proposition de réintroduction de ces items doit passer par une décision structurante documentée, pas par une session de code.*

### 4.1 Ontologie OWL/SHACL parallèle — REFUSÉ

**Proposition écartée.** Formaliser une TBox (ontologie de description) avec concepts et rôles, en parallèle des schémas Pydantic.

**Motif du refus.** Doublon fonctionnel. Les schémas Pydantic *sont déjà* la spécification normative des sorties. Maintenir deux langages de schéma en parallèle garantit leur divergence à moyen terme, et double le coût de toute évolution doctrinale.

**Ce qui est retenu à la place.** Si une spécification publique lisible hors code est nécessaire (distribution, onboarding, standard ouvert), elle sera **générée depuis les schémas Pydantic**, jamais maintenue à côté d'eux. Source unique de vérité.

### 4.2 Moteur de révision non-monotone — REPORTÉ (pas refusé)

**Proposition écartée pour maintenant.** Implémenter un moteur de révision de croyances (règles non-monotones, propagation automatique des défaites).

**Motif.** Le pipeline actuel *valide* des analyses produites par des humains. Il n'en *produit* pas encore. Construire un moteur de révision avant d'avoir un pipeline de production est un engagement prématuré caractérisé.

**Condition de réexamen.** Après livraison de la Phase 2 (agents produisant des analyses) et de la Phase 3 (persistance). Pas avant.

### 4.3 Tableaux sémantiques / solveur logique — REFUSÉ en l'état

**Proposition écartée.** Intégrer un solveur (tableaux sémantiques, SAT, ASP) pour la génération ou la sélection d'explications.

**Motif.** Aucun besoin réel identifié. Le nombre d'hypothèses concurrentes par analyse est petit (typiquement 4-5). Elles sont formulées par jugement, pas engendrées combinatoirement. Un solveur résoudrait un problème que le projet n'a pas.

**Condition de réexamen.** Si un jour le nombre d'hypothèses candidates devient trop grand pour être traité par jugement — situation qui ne s'est jamais présentée.

### 4.4 Connecteurs de corpus externes — REPORTÉ (Phase 4+)

**Proposition écartée pour maintenant.** Brancher des bases d'événements ouvertes pour alimenter faits et defeaters.

**Motif.** Utile, mais suppose un pipeline de production fonctionnel en amont. Sans lui, on alimenterait un moteur qui n'existe pas.

**Condition de réexamen.** Phase 4, en même temps que les interfaces du premier mode opérationnel.

### 4.5 Gouvernance multi-contributeurs — REPORTÉ (pas de contributeurs)

**Proposition écartée pour maintenant.** Modèle noyau/cercles/sandbox, flux de promotion des contributions, accord de contribution.

**Motif.** Le projet a un porteur unique. Construire une gouvernance multi-contributeurs avant d'avoir des contributeurs est de l'architecture spéculative.

**Condition de réexamen.** Quand un premier contributeur externe se présente. Le modèle est déjà esquissé et sera repris à ce moment-là.

### 4.6 Vocabulaire logique dans les sorties — REFUSÉ

**Précision importante.** La fondation épistémologique nomme des filiations (abduction, non-monotonie, défaisabilité, etc.). **Ce vocabulaire ne doit apparaître ni dans les sorties humaines, ni dans les sorties publiques.**

Une sortie destinée à un lecteur informé non-analyste qui parlerait de « defeater sapant » ou de « clôture du monde » aurait échoué. Les concepts structurent le travail ; ils ne s'exhibent pas dans le produit.

Seuls les champs de la sortie machine peuvent porter les termes techniques — c'est leur fonction.

---

## 5. Synthèse pour le plan de dev

| Item | Horizon | Effort | Statut |
|---|---|---|---|
| Typage des defeaters (`rebutting`/`undercutting`) | Immédiat (v2.1.2) | Session courte | **À planifier** |
| Qualification révision/mise-à-jour | Immédiat (v2.1.2) | Session courte | **À planifier** |
| `defeater_balance_audit` | Avec 1.1 | Trivial (compteur) | À planifier |
| Graphe abductif | Phase 3 | Substantiel | Spec posée, non engagé |
| Audits reformulés en requêtes | Phase 3 | Modéré | Dépend du graphe |
| Note agrégation multi-agents | Phase 2 | — | À verser au plan Phase 2 |
| Vigilance OWA/CWA | Toutes | — | À verser au rôle Reviewer |
| Ontologie OWL/SHACL | — | — | **Refusé** |
| Moteur de révision | Après Phase 3 | — | Reporté |
| Solveur logique | — | — | **Refusé en l'état** |
| Connecteurs externes | Phase 4+ | — | Reporté |
| Gouvernance multi-contributeurs | Jalon 2 | — | Reporté |

**Le verrou du projet reste inchangé** : les décisions structurantes de Phase 0. Ce backlog ne le déplace pas et ne doit pas servir de prétexte à le contourner. Les deux items immédiats (1.1 et 1.2) sont assez petits pour être traités en parallèle de la délibération, sans la retarder ni s'y substituer.

---

*Backlog doctrinal v1.0 — produit en Mode Architecte. À réviser après livraison des items immédiats et après les décisions de Phase 0. Document de liaison, pas de doctrine : la doctrine est dans la charte, le plan est dans les plans.*
