"""
Package donnees : classes de représentation des données audio.

Expose les classes principales du modèle objet :
- MetadonneesAudio : métadonnées textuelles d'un fichier audio
- PochettePiste   : pochette (image) associée à une piste
- PisteAudio      : fichier audio (chemin, taille, métadonnées, pochette)
- PlaylistAudioXSPF : playlist au format XSPF

Auteur : Nassim Berrandou
Version : 1.0
"""

# Importation des modules
from .MetadonneesAudio import MetadonneesAudio
from .PisteAudio import PisteAudio
from .PlaylistAudioXSPF import PlaylistAudioXSPF
from .PochettePiste import PochettePiste
from .LecteurAudio import LecteurAudio