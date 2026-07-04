# L'Entité — Document maître

*Document dérivé (communication/pilotage). La doctrine (couche A, `doctrine/V2.1/`) et les décisions structurantes (`.claude/decisions/`) font foi en cas de divergence. Toute révision doctrinale déclenche la resynchronisation de ce document, jamais l'inverse.*

*Version 1.1 — 4 juillet 2026. Licence CC BY 4.0. (v1.1 : identité à deux étages noyau/instance ; axe postes d'observation multiples.)*

---

## 1. Identité — deux étages

### Le noyau (la méthode)

**L'Entité est une méthode outillée par IA pour établir, à partir de traces, ce qui s'est passé et pourquoi — dans les domaines où l'expérience contrôlée est impossible et où les acteurs ont des intentions.**

Son territoire épistémologique est identifié : le *paradigme indiciaire* (Ginzburg) — le mode de connaissance du juge, de l'historien, de l'enquêteur, qui remonte du singulier vers ses causes par les traces, là où le paradigme expérimental généralise par la reproduction. Ce paradigme n'a jamais eu ses instruments ; L'Entité le mécanise et le discipline. Le noyau est agnostique au domaine : quadripartition dit/fait/produit/voulu, omission formelle, réfutabilité mécanique, clôture de corpus, calibration, bitemporalité, séparation des étages.

### L'instance n°1 (le terrain de preuve)

**L'observatoire du réel politique : documenter les écarts entre ce que les acteurs publics disent, font, produisent et veulent — et livrer des hypothèses causales auditables, chacune portant ses sources, son degré de confiance et ses conditions de réfutation.**

Une instance = le noyau + trois paramètres : une ontologie de domaine, une politique de corpus, un régime de responsabilité. Changer les paramètres change l'instance (contentieux, conformité déclarative, archéologie décisionnelle…) ; le noyau ne bouge pas.

### En trois phrases

L'Entité n'est ni un chatbot, ni un média, ni un fact-checker : c'est un pipeline qui transforme un corpus de traces (discours, votes, budgets, silences documentables) en dossiers d'enquête formels où chaque affirmation est un objet attaquable — datée, sourcée, munie de conditions d'invalidation, révisable avec trace. Sa figure n'est pas l'oracle qui répond mais l'enquêteur forensique qui remet un dossier ; sa singularité tient à trois choix que personne ne combine : l'omission comme objet formel de première classe, la réfutabilité comme contrainte de schéma non contournable, et l'auditabilité publique du chemin complet. Sa phrase-cœur : **la vérité est dans la qualité du chemin, pas dans la conclusion.**

### Ce que c'est / ce que ce n'est pas

| C'est | Ce n'est pas |
|---|---|
| Une infrastructure épistémique (méthode + pipeline + graphe) | Une application ou un chatbot |
| Un producteur de dossiers d'enquête auditables | Un producteur de réponses ou de vérités |
| Un système qui hypothétise sous contrainte de réfutabilité | Un système qui « détermine les causes réelles » |
| Un instrument qui déclare son poste d'observation | Un observateur neutre |
| Une discipline maintenue par des validateurs mécaniques | Une charte de bonnes intentions |

## 2. L'ADN — cinq invariants

1. **L'objet** : le réel *produit* par les actions humaines, en deux dimensions reliées — les actes effectifs et les récits qui structurent l'arène — les chaînes causales étant des objets d'enquête, jamais des présupposés.
2. **La quadripartition** : dit / fait / produit / voulu, chacun avec son propre régime de preuve. Tout le reste en découle.
3. **Le poste d'observation déclaré, non neutralisé** : déclarer le biais ne le corrige pas, il le rend attaquable. Ce qui distingue le projet d'un fact-checker.
4. **La révisabilité constitutive** : toute inférence porte au minimum deux defeaters (conditions d'invalidation) ; toute révision est tracée. Une conclusion sans condition d'invalidation n'est pas une conclusion, c'est un récit.
5. **La séparation des pouvoirs techniques** : le LLM extrait et propose, le validateur juge la forme, le graphe mémorise, l'humain arbitre — jamais de fusion des rôles. Le cœur du système n'est pas le modèle de langage : c'est la boucle.

## 3. Architecture

### Couches doctrinales (le versionné)

| Couche | Contenu | Emplacement |
|---|---|---|
| A — Charte | ADN, modes, engagements, ferme/négociable | `doctrine/V2.1/lentite_charte_v2_1.md` |
| B — Gabarit | Grammaire des méthodes : schémas, contraintes, degrés de confiance, politique de corpus, calibration | `doctrine/V2.1/` + `pipeline/schemas*.py` |
| C — Méthodes | M01 (analyse rhétorique individuelle), M03 (comparatif multi-acteurs) | `doctrine/V2.1/` |
| Exécution | Pipeline Python : validation, graphe, orchestration | `pipeline/` |

### Étages techniques (le principe)

1. **LLM — extracteur et générateur, jamais juge.** Ingestion des sources, extraction des candidats dit/fait/produit/voulu, reconstruction charitable des arguments, génération d'hypothèses et de defeaters. Tout ce qu'il produit est candidat.
2. **Validation — la doctrine rendue mécanique.** Schémas Pydantic : une hypothèse sans defeaters, une omission sans clôture de corpus sont *rejetées par le validateur*, pas déconseillées. Tests négatifs versionnés prouvant que les contraintes mordent.
3. **Graphe — mémoire dérivée, jamais source.** Les YAML validés dans git sont l'unique source de vérité ; le graphe (NetworkX, puis PostgreSQL+AGE sur seuils) est une vue reconstructible par rejeu. Aucune écriture directe, par personne.

Traçabilité transversale : journal méthodologique markdown append-only (git), artefacts de log JSON par appel d'agent, un commit par opération logique.

### Axe d'évolution : postes d'observation multiples (post-dossier zéro)

Le poste d'observation, aujourd'hui déclaré au niveau du projet (P3), a vocation à devenir un **paramètre instrumenté** : la même chaîne causale exécutée depuis plusieurs postes disciplinaires déclarés (juridique, financier, sociologique…), dont on compare les pondérations. La convergence inter-postes fonde les degrés de confiance les plus robustes ; la divergence devient une donnée déclarée du dossier (« le poids de cette omission dépend du poste : lourd en droit, marginal en finance »). Deux axes orthogonaux et combinables : les agents fonctionnels (Charité, Vulnérabilités, Chaînes causales, Synthèse) sont des *étapes* ; les postes disciplinaires sont des *perspectives* — le matériau existe déjà (`pipeline/agents/`, prompts analystes hérités du prototype de mai). Évolution de couches B/C sous moratoire : candidate structurée pour l'après-dossier-zéro ; sa mise en œuvre (boucle parallèle sur postes) est un déclencheur identifié de la bascule d'orchestration (décision 001 §7).

## 4. Modes d'utilisation

### Les quatre modes

| Mode | Fonction | Public | Statut |
|---|---|---|---|
| **0 — Atelier** | Auto-discipline : journal, cas-jouets, calibration, rejeux | Le projet lui-même | **Actif** — seul mode opérationnel, produit la valeur cumulative |
| **1 — Éclairage** | Dossiers d'enquête publics (M01/M03) | Journalistes, chercheurs, analystes | Cible après dossier zéro + verrou juridique |
| **2 — Conseil** | Scénarisation, cartographie des rapports de force, sans prescription | Décideurs, sous contrat | Cible économique, après jalon 2 |
| **3 — Chat public** | Auto-pédagogie de la distinction | Grand public | Reporté doctrinalement |

### Les quatre variables (grille de décision par mode)

Toute extension d'usage s'arbitre sur : **fonction** (documenter / scénariser / diffuser / se discipliner), **symétrie d'accès** (ouvert vs contractuel), **degré d'automatisation** (où l'humain reste en boucle), **régime de responsabilité** (qui signe, qui répond — verrou juridique requis avant tout Mode 1 public).

## 5. État réel — 4 juillet 2026

**Acquis.**
- Doctrine v2.1.1 stable, sous moratoire jusqu'au dossier zéro.
- Corpus validé : 7 analyses M01 réelles (Fabius, Lecornu, Panot, Vallaud + cas Ciotti en jouet), 2 applications M03 (séquence retraites octobre 2025), 3 cas-jouets étalons, 6 tests négatifs.
- Cinq décisions structurantes prises et documentées (§6).
- Repo privé `atelier-atlani/lentite`, assaini, licencié (SPDX), test d'onboarding à froid réussi.
- Gabarit durci : bloc omission à quatre champs contraints, bitemporalité, politique de corpus v1, grille de calibration, sentinelles NON_RENSEIGNE / NON_DOCUMENTE.
- `validate.py` (M01) et `validate_m03.py` opérationnels.

**En cours (plan_action_002, séquence 2).** `graph_builder.py` (graphe NetworkX dérivé), audits comme parcours de graphe, orchestrateur quatre agents (Charité, Vulnérabilités, Chaînes causales, Synthèse) avec logs JSON, test de bout en bout étalonné contre une analyse manuelle.

**Premier rendement empirique.** La revalidation du corpus sous gabarit durci a produit une donnée méthodologique inattendue : sur 57 champs de datation, 21 dates réelles contre 36 NON_DOCUMENTE — asymétrie systématique entre faits ponctuels médiatisés (toujours datés) et processus diffus (jamais datés au jour près). Le flux médiatique date les événements, pas les processus. Le gabarit a révélé une structure de la médiatisation avant même le premier dossier : démonstration en miniature de ce que le système est censé faire.

## 6. Les cinq décisions structurantes (3 juillet 2026)

| # | Décision | Choix | Mécanisme clé |
|---|---|---|---|
| 001 | Orchestration | Custom Python minimal, pipeline linéaire 4 agents | Logs JSON par appel ; bascule langgraph sur critères (topologie non linéaire) |
| 002 | Persistance graphe | Fichiers-source-de-vérité, graphe NetworkX dérivé | Rejeu intégral ; bascule PostgreSQL+AGE sur seuils (~50 analyses, multi-utilisateurs) |
| 003 | Persistance journal | Git + markdown append-only + front matter YAML | Aucune écriture agentique ; index dérivé si besoin |
| 004 | Licence | Tri-partition | Apache 2.0/CC BY (spec, standard) + AGPL-3.0 copyright unique (moteur, double licence Mode 2) + CC BY-SA (analyses) |
| 005 | Distribution | Duale à trois jalons | J1 privé (fait) → J2 public (dossier zéro + verrou juridique) → J3 commercial Mode 2 |

Verrou transversal : **CLA obligatoire** avant toute contribution externe sur le périmètre AGPL — condition du droit de double licence.

## 7. Trajectoire

```
Phase 0 (en cours) ── plan_action_002
  Séq. 0 Hygiène ✓ · Séq. 1 Gabarit durci ✓ · Séq. 2 Prototype pipeline (en cours)
        │
Phase 1 ── plan_action_003 : DOSSIER ZÉRO rétrospectif
  Cas clos (candidat : loi Climat-Résilience 2021), 20-50 sources,
  M01 + M03 + omissions + hypothèses, confrontation aux effets connus.
  Produit : chiffrage boucle humaine, calibration inter-annotateurs,
  test adversarial minimal. Critère : plus vérifiable, proportionné
  et attaquable proprement qu'un bon article de synthèse (charte §21.3).
        │
Jalon 2 ── Passage public du cœur
  Conditions conjointes : dossier zéro relu par 2 lecteurs externes
  + relecture juridique responsabilité éditoriale.
        │
Jalon 3 ── Ouverture commerciale Mode 2 (jamais avant le jalon 2 :
  l'auditabilité précède la monétisation).
```

Règles de conduite : moratoire doctrinal jusqu'au dossier zéro ; une session = un livrable ; toute friction au journal ; l'Implementer ne prend aucune décision structurante.

## 8. Débouchés — le scope et au-delà

La pile de discipline (quadripartition, omission formelle, réfutabilité mécanique, clôture de corpus, calibration, séparation des étages, bitemporalité) est agnostique au domaine. Critère de transposition : écarts dit/fait à enjeu + traces documentaires datées + tension naïveté/paranoïa non outillée + payeur ou obligation réglementaire.

**Trois familles, sept domaines qualifiés :**
- *Audit de sincérité* — conformité déclarative ESG/greenwashing (pression réglementaire CSRD, le plus mûr commercialement) ; commande publique ; audit épistémique des systèmes d'IA (model cards vs comportement réel) ; intégrité scientifique (claims vs evidence).
- *Dossier probatoire* — contentieux et pré-contentieux (arbitrage, construction, post-M&A) : l'e-discovery trouve les documents, L'Entité construit l'argumentation avec ses points faibles.
- *Mémoire disciplinée* — archéologie décisionnelle des organisations (post-mortems bitemporels : juger sur l'information disponible à la date de la décision).

**Le méta-débouché : le standard.** Le gabarit publié comme spécification ouverte de *claim défaisable* (assertion portant source, confiance, defeaters, clôture de corpus) avec validateurs de référence — positionner L'Entité comme l'origine d'une grammaire plutôt que comme un outil parmi d'autres. Coût marginal faible (le gabarit existe), autorisé en publication anticipée par la décision 005.

**Séquence impérative** : aucune transposition avant le dossier zéro — il est l'actif de crédibilité commun à tous les débouchés.

## 9. Gouvernance et risques

| Risque | Traitement |
|---|---|
| Responsabilité éditoriale (diffamation, RGPD) | Verrou du jalon 2 : consultation juridique avant toute publication ; signature humaine des dossiers |
| Capture propriétaire du moteur | AGPL + copyright unique + CLA (décision 004) |
| Dérive oracle (le LLM qui « répond ») | Validateurs mécaniques + séparation des étages + moratoire |
| Injection via sources hostiles | Test adversarial minimal au dossier zéro ; isolation contenu/instruction au pipeline |
| Homme seul | Onboarding co-dirigeant (CLA préalable) ; comité de lecture à trois profils adverses au jalon 2 |
| Perte de discipline sous pression | La singularité EST la liste des éléments fermes de la charte — tout relâchement reclasse le projet en chatbot d'analyse parmi cent |

## 10. Glossaire minimal

**Defeater** — condition explicite d'invalidation d'une inférence ; minimum deux par lien causal, exigé par le validateur. **Omission** — inaction formalisée : pouvoir d'agir documenté + opportunité datée + absence dans un corpus clos déclaré + explications innocentes examinées. **Clôture de corpus** — déclaration du périmètre de sources dans lequel une absence est constatée (monde clos local, assumé et daté). **NON_DOCUMENTE / NON_RENSEIGNE** — l'information n'existe pas dans les sources vs le champ n'a pas été rempli. **Bitemporalité** — date du fait vs date de sa connaissance ; permet de juger une décision sur l'information disponible à l'époque. **M01 / M03** — méthode d'analyse individuelle / comparative multi-acteurs. **Dossier zéro** — premier dossier rétrospectif complet sur cas clos, juge de paix de la méthode.

---

*Document maître v1.1 — 4 juillet 2026. Emplacement cible : `communication/00_document_maitre.md`. Documents frères : 01_positionnement_usages, 02_stack_technique, 03_communication_marketing, 04_exploitation_actifs.*
