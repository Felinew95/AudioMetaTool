# Répartition des rôles — AudioMetaTool

**Version :** 1.0
**Date :** 8 novembre 2026
**Groupe projet :** AudioMetaTool
**Membres :** Nassim BERRANDOU, Alexandre BURIN, Menaouer AMMARI

---

## 1. Vue d'ensemble

Ce document précise la répartition des tâches au sein du trinôme pour le projet
AudioMetaTool. Il est mis à jour au fur et à mesure de l'avancement et servira
de base pour personnaliser les questions lors de la soutenance.

---

## 2. Répartition par membre

### Nassim BERRANDOU

**Rôle principal :** Sérialisation XSPF et tests de bout en bout

**Contributions :**
- Conception et implémentation de la classe `SerialiseurXSPF`
  (`src/library/traitement/SerialiseurXSPF.py`) : génération de fichiers
  XSPF valides (namespace `http://xspf.org/ns/0/`, `<location>` en URI
  `file:///`, `<duration>` en millisecondes)
- Écriture des tests de sérialisation :
  - `test_serialisation_xspf.py` (avec données CSV)
  - `test_playlist_reelle.py` (avec de vrais fichiers audio, fallback
    automatique sur `src/tests_auto/` si `musique_test/` est absent)
  - `test_demo_avancement.py` (test unifié pour le point d'avancement)
- Correction des imports dans l'ensemble du projet
- Nettoyage des docstrings
- Validation des fichiers générés sur https://validator.xspf.org/
- Rédaction du document de répartition des rôles (`doc/rapport/repartition_roles.md`)
- Rédaction du README (`README.md`)

**Compétences mises en œuvre :**
- Manipulation de XML avec `xml.etree.ElementTree` (namespace, sous-éléments,
  indentation, écriture UTF-8 avec déclaration)
- Conversion de chemins locaux en URI (`pathlib.Path.as_uri()`)
- Conformité au standard XSPF (XML Shareable Playlist Format)
- Écriture de tests automatiques avec assertions (`assert`)
- Correction d'imports et résolution de problèmes
- Versionnage sémantique des docstrings (historique + bump de version)

---

### Alexandre BURIN

**Rôle principal :** Couche données et configuration

**Contributions :**
- Conception et implémentation des classes du modèle objet :
  - `MetadonneesAudio` (`src/library/donnees/MetadonneesAudio.py`)
  - `PisteAudio` (`src/library/donnees/PisteAudio.py`)
  - `PlaylistAudioXSPF` (`src/library/donnees/PlaylistAudioXSPF.py`)
  - `PochettePiste` (`src/library/donnees/PochettePiste.py`)
- Centralisation des constantes (`src/config/constantes.py`)
- Tests unitaires des classes (`tests_classes.py`)
- Tests d'extraction des métadonnées (`test_extraction_metas.py`)
- Tests du lecteur audio (`test_lecteur_audio.py`)

**Compétences mises en œuvre :**
- Programmation orientée objet (encapsulation, propriétés, assertions)
- Validation des données (getters/setters avec contrôles)
- Implémentation des méthodes spéciales (`__str__`, `__eq__`)
- Documentation complète (docstrings, historique de versions)

---

### Menaouer AMMARI

**Rôle principal :** Extraction des métadonnées, exploration et lecture audio

**Contributions :**
- Exploration récursive des dossiers (`src/library/traitement/ExplorateurAudio.py`)
- Extraction des métadonnées MP3/FLAC via `mutagen`
  (`src/library/traitement/PisteAudioBuilder.py`)
- Récupération des pochettes intégrées (APIC pour MP3, pictures pour FLAC)
- Construction des playlists (`src/library/traitement/PlaylistAudioXSPFBuilder.py`)
- Lecture audio via `pygame` avec threading
  (`src/library/traitement/LecteurAudio.py`)

**Compétences mises en œuvre :**
- Utilisation de la bibliothèque `mutagen` (formats MP3 et FLAC)
- Parcours récursif d'arborescences avec `pathlib`
- Patron de conception Builder (`PisteAudioBuilder`, `PlaylistAudioXSPFBuilder`)
- Programmation concurrente avec `threading`
- Lecture audio avec `pygame.mixer`

---

## 3. Répartition par module

| Module | Membres impliqués |
|---|---|
| `src/config/` | Alexandre BURIN |
| `src/library/donnees/` | Alexandre BURIN |
| `src/library/traitement/ExplorateurAudio.py` | Menaouer AMMARI |
| `src/library/traitement/PisteAudioBuilder.py` | Menaouer AMMARI, Alexandre BURIN |
| `src/library/traitement/PlaylistAudioXSPFBuilder.py` | Menaouer AMMARI, Alexandre BURIN |
| `src/library/traitement/SerialiseurXSPF.py` | Nassim BERRANDOU |
| `src/library/traitement/LecteurAudio.py` | Menaouer AMMARI, Alexandre BURIN |
| `src/tests_auto/` | Tous les membres |
| `src/cli/` | Alexandre BURIN (à venir) |
| `src/gui/` | Nassim BERRANDOU (à venir) |

---

## 4. État d'avancement au 13 novembre 2026

### ✅ Fonctionnalités terminées

- Modèle objet complet (métadonnées, pistes, playlist, pochette)
- Extraction des métadonnées MP3 et FLAC (via `mutagen`)
- Récupération des pochettes intégrées
- Exploration récursive d'un dossier avec filtre par extension
- Construction d'une playlist à partir d'un dossier
- Sérialisation au format XSPF (validée sur validator.xspf.org)
- Lecture audio (threading avec `pygame`)
- Tests automatiques de bout en bout

### ⏳ Fonctionnalités prévues pour le rendu final

- Interface en ligne de commande (CLI) avec `argparse`
- Interface graphique (GUI) avec `pyQt`
- Modification et sauvegarde des tags
- Recherche d'informations via API web
- Téléchargement automatique des pochettes manquantes

---

## 5. Organisation du travail

- **Réunions :** hebdomadaires
- **Communication :** groupe de messagerie dédié + dépôt Git partagé
- **Suivi :** diagramme de Gantt (déposé semaine 43)
- **Versionnage :** Git (dépôt GitHub partagé)

---

## 6. Répartition des tâches pour la période à venir

| Tâche | Responsable principal | Échéance |
|---|---|---|
| CLI (`src/cli/cli.py`) | À répartir | Semaine 47 |
| GUI (`src/gui/gui.py`) | Nassim BERRANDOU | Semaine 48 |
| Modification des tags | À répartir | Semaine 48 |
| Rapport de projet (5–10 pages) | Tous | Semaine 49 |
| Vidéo de démonstration | Tous | Semaine 49 |
| Diaporama de soutenance | Tous | Semaine 49–50 |

---

## 7. Historique des versions

- **1.0** (8 novembre 2026) : Version initiale du document pour le point
  d'avancement du 13 novembre 2026.