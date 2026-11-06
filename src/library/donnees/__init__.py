"""
Package donnees : classes de représentation des données audio.

Expose les classes principales du modèle objet :
    - MetadonneesAudio    : métadonnées textuelles d'un fichier audio.
    - PochettePiste       : pochette (image) associée à une piste.
    - PisteAudio          : fichier audio (chemin, taille, métadonnées, pochette).
    - PlaylistAudioXSPF   : playlist au format XSPF.
    - LecteurAudio        : gestion de la lecture des fichiers audio.

Historique des versions :
    - 1.0 : Création du package et exportation des classes principales.
    - 1.1 : Ajout de l'importation de la classe LecteurAudio.

Auteurs : Nassim Berrandou, Alexandre Burin
Version : 1.1
"""

# Importation des modules
from .MetadonneesAudio import MetadonneesAudio
from .PisteAudio import PisteAudio
from .PlaylistAudioXSPF import PlaylistAudioXSPF
from .PochettePiste import PochettePiste
from .LecteurAudio import LecteurAudio