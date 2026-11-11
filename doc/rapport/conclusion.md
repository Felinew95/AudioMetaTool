# Conclusion — Point d'avancement 1

**Projet :** AudioMetaTool
**Groupe :** Groupe projet 02
**Date :** 13 novembre 2026
**Membres :** Nassim BERRANDOU, Alexandre BURIN, Menaouer AMMARI

---

## 1. Difficultés surmontées

- **Résolution des chemins** : mise en place d'une fonction centralisée
  `trouver_dossier_musique()` avec fallback automatique sur les fichiers
  versionnés (`src/tests_auto/`) si `musique_test/` est absent.
- **Lecture audio en thread** : gestion de `Ctrl+C` et arrêt contrôlé
  par la touche Entrée avec `pygame`.
- **Tests automatisés** : création d'un test unifié de bout en bout
  (`test_demo_avancement.py`) qui valide la chaîne complète
  exploration → extraction → playlist → sérialisation XSPF.

---

## 2. Items commencés (état actuel)

- **CLI** (`src/cli/cli.py`) : structure vide, à implémenter (semaine 47)
- **GUI** (`src/gui/gui.py`) : structure vide, à implémenter (semaine 48)
- **Documentation générée** (Pydoc/Doxygen) : docstrings complètes mais
  génération HTML à finaliser

---

## 3. Items restants (rendu final)

- Interface en ligne de commande (CLI) avec `argparse`
- Interface graphique (GUI) avec `pyQt`
- Modification et sauvegarde des tags
- Recherche d'informations via API web (paroles, infos album)
- Téléchargement automatique des pochettes manquantes
- Rapport de projet (5–10 pages)
- Vidéo de démonstration (5 min)
- Diaporama de soutenance

---

## 4. Bilan

Le projet est actuellement à **~55 % du cahier des charges**.
Le cœur métier (extraction, exploration, sérialisation, lecture) est
**entièrement fonctionnel** et **testé**. Les interfaces (CLI, GUI) et les
fonctionnalités complémentaires (API, tags, pochette fallback) restent à
implémenter pour le rendu final (semaine 49).