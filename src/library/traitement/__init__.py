"""
Package traitement : modules de traitement des fichiers audio.

Expose les classes principales permettant d'explorer les fichiers audio,
d'extraire leurs métadonnées et leurs pochettes, ainsi que de centraliser
leur traitement.

Classes exportées :
    - ExplorateurFichiersAudio : exploration et recherche des fichiers audio.
    - ExtracteurMetadonnees : extraction des métadonnées audio.
    - ExtracteurPochetteAudio : extraction des pochettes associées aux pistes.
    - TraitementAudio : gestion du traitement des fichiers audio.

Auteur : Alexandre BURIN
Version : 1.0
"""

# Importation des modules
from .ExplorateurAudio import ExplorateurAudio
from .PisteAudioBuilder import PisteAudioBuilder
from .PlaylistAudioXSPFBuilder import PlaylistAudioXSPFBuilder
from .LecteurAudio import LecteurAudio