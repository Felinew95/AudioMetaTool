# AudioMetaTool

Application d'extraction et d'analyse des métadonnées audio aux formats
**MP3** et **FLAC**, et de gestion de playlists au format **XSPF**
(XML Shareable Playlist Format).

---

## Membres du projet

| Membre | Rôle principal |
|---|---|
| **Nassim BERRANDOU** | Sérialisation XSPF, tests de bout en bout |
| **Alexandre BURIN** | Couche données, configuration |
| **Menaouer AMMARI** | Extraction des métadonnées, exploration, lecture audio |

---

## Fonctionnalités

### ✅ Implémentées

- Extraction des métadonnées MP3 (ID3) et FLAC (Vorbis comments)
  via la bibliothèque `mutagen`
- Récupération des pochettes intégrées (APIC pour MP3, `pictures` pour FLAC)
- Exploration récursive d'un dossier avec filtrage des extensions autorisées
- Construction d'une playlist à partir d'un dossier exploré
- Sérialisation d'une playlist au format XSPF valide
  (validée sur https://validator.xspf.org/)
- Lecture audio via `pygame` (avec threading)
- Tests automatiques de bout en bout

### ⏳ Prévues pour le rendu final

- Interface en ligne de commande (CLI) avec `argparse`
- Interface graphique (GUI) avec `tkinter`
- Modification et sauvegarde des tags
- Recherche d'informations via API web (paroles, infos album)
- Téléchargement automatique des pochettes manquantes

---

## Prérequis

- **Python 3.11** ou supérieur
- Les dépendances suivantes (voir `requirements.txt`) :
  - `mutagen` (extraction des métadonnées MP3/FLAC)
  - `pygame` (lecture audio)
  - `pandas` (lecture des fichiers CSV de test)

Installation des dépendances :

```bash
pip install -r requirements.txt
```

---

## Structure du projet

    AudioMetaTool/
    ├── doc/
    │   ├── demonstration/      # Vidéo de démonstration (à venir)
    │   ├── diaporama/          # Diaporama de soutenance (à venir)
    │   ├── documentation/      # Documentation générée (Doxygen/Pydoc)
    │   └── rapport/            # Rapport de projet + document de rôles
    ├── musique_test/           # Morceaux de test locaux (non versionné)
    ├── src/
    │   ├── config/             # Constantes de configuration
    │   ├── library/
    │   │   ├── donnees/        # Modèle objet (métadonnées, pistes, playlist, pochette)
    │   │   └── traitement/     # Extraction, exploration, sérialisation, lecture
    │   ├── cli/                # Interface console (à venir)
    │   ├── gui/                # Interface graphique (à venir)
    │   └── tests_auto/         # Tests automatiques
    ├── .gitignore
    ├── README.md
    └── requirements.txt

## Utilisation

### Lancer la démonstration (point d'avancement)

    python -m src.tests_auto.test_demo_avancement

Vérifie la chaîne complète : exploration → extraction → playlist → XSPF.

### Générer une playlist XSPF à partir d'un dossier

    python -m src.tests_auto.test_playlist_reelle

Génère `default_playlist.xspf` à la racine du projet.

### Tester la sérialisation XSPF avec des données CSV

    python -m src.tests_auto.test_serialisation_xspf

### Tester la lecture audio

    python -m src.tests_auto.test_lecteur_audio

## Tests automatiques

Le projet inclut plusieurs tests dans `src/tests_auto/` :

| **Fichier**                  | **Description**                             |
|:-----------------------------|:--------------------------------------------|
| `tests_classes.py`           | Tests unitaires des classes de données      |
| `test_serialisation_xspf.py` | Test de sérialisation XSPF avec données CSV |
| `test_playlist_reelle.py`    | Test avec de vrais fichiers audio           |
| `test_extraction_metas.py`   | Test d'extraction des métadonnées           |
| `test_lecteur_audio.py`      | Test du lecteur audio                       |
| `test_demo_avancement.py`    | Test unifié pour le point d'avancement      |


## État d'avancement

Au 8 novembre 2026 (point d'avancement du 13 novembre) :

- Modèle objet complet
- Extraction MP3/FLAC avec `mutagen`
- Exploration récursive
- Construction de playlist
- Sérialisation XSPF valide
- Lecture audio
- Tests automatiques
- CLI et GUI en cours de développement

## Validation XSPF

Les fichiers XSPF générés sont conformes au standard officiel et ont été validés sur https://validator.xspf.org/.

Pour valider un fichier manuellement :

1. Ouvrir le fichier `.xspf` généré dans un éditeur de texte.
2. Copier son contenu.
3. Aller sur https://validator.xspf.org/.
4. Coller le contenu et cliquer sur « Validate ».

## Auteurs

Projet réalisé dans le cadre de la mineure « Python » de la L3 Informatique (2026–2027) par :

- **Nassim BERRANDOU**
- **Alexandre BURIN**
- **Menaouer AMMARI**

## Licence

Projet académique — Université, 2026–2027.



<img width="916" height="546" alt="logo_audiometatool" src="https://github.com/user-attachments/assets/8785fc71-e57a-495f-bcaf-9b6325e203c7" />

