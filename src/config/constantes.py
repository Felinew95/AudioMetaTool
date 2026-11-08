"""
Module : constantes.py

Description : Ce module centralise les constantes utilisées dans le projet
              AudioMetaTool, notamment les extensions des fichiers audio
              pris en charge et les dossiers utilisés pour les tests.

              Il fournit également une fonction utilitaire permettant de
              localiser le dossier de musique de test, avec un fallback
              automatique sur les fichiers versionnés.

Historique des versions :
    - 1.0 : Création du module et définition des constantes initiales.
    - 1.1 : Ajout des constantes de dossiers de musique et de la fonction
            trouver_dossier_musique() pour centraliser la résolution des
            chemins
    - 1.2 : Suppression de la constante FICHIERS_AUDIO (devenue inutile suite à
        la sélection dynamique des fichiers dans test_lecteur_audio) et
        ajout des constantes NOM_PLAYLIST_DEFAUT et TIMEOUT_ARRET_AUDIO

Auteurs : Alexandre BURIN, Nassim BERRANDOU
Version : 1.2
"""

from pathlib import Path

# Formats audio disponibles
EXTENSIONS_AUTORISES = (".mp3", ".flac")

# Dossier de musique de test (à la racine, non versionné)
DOSSIER_MUSIQUE_TEST = Path("musique_test")

# Dossier de fallback (fichiers audio versionnés)
DOSSIER_MUSIQUE_FALLBACK = Path("src/tests_auto")

# Fréquence de rafraichissement du lecteur audio en Hz
FREQUENCE_RAFRAICHISSEMENT = 10

# Nom par défaut de la playlist générée (imposé par le sujet)
NOM_PLAYLIST_DEFAUT = "default_playlist.xspf"

# Timeout (en secondes) pour l'arrêt du thread audio
TIMEOUT_ARRET_AUDIO = 2


def trouver_dossier_musique() -> Path:
    """
    Trouve le dossier contenant les fichiers audio à utiliser.

    Priorité :
        1. musique_test/ (vrais morceaux, non versionnés)
        2. src/tests_auto/ (fichiers de test versionnés)

    :return: Chemin du dossier à utiliser.
    """
    if DOSSIER_MUSIQUE_TEST.is_dir():
        return DOSSIER_MUSIQUE_TEST
    return DOSSIER_MUSIQUE_FALLBACK
