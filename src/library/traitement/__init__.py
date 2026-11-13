"""
Package traitement : modules de traitement des fichiers audio.

Expose les classes principales permettant d'explorer les fichiers audio,
d'extraire leurs métadonnées et leurs pochettes, ainsi que de centraliser
leur traitement.

Classes exportées :
    - ExplorateurAudio       : exploration et recherche des fichiers audio.
    - PisteAudioBuilder      : construction des objets PisteAudio.
    - PlaylistAudioXSPFBuilder : construction des playlists XSPF.
    - LecteurAudio           : lecture des fichiers audio.
    - SerialiseurXSPF        : sérialisation au format XSPF.

Historique des versions :
    - 1.0 : Création du package et exportation des classes principales.
    - 1.1 : Ajout de l'exportation de LecteurAudio.
    - 1.2 : Ajout de l'exportation de SerialiseurXSPF (sérialisation
            des playlists au format XSPF).

Auteurs : Alexandre BURIN, Nassim BERRANDOU
Version : 1.2
"""