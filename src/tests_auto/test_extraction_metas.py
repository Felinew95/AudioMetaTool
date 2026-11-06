"""
Module : test_extraction_metas.py

Description : Ce module permet de tester le fonctionnement de l'extraction
              des métadonnées et des pochettes des fichiers audio, ainsi que
              la création d'une playlist XSPF à partir des fichiers trouvés
              dans un dossier et ses sous-dossiers.

              Il vérifie le bon fonctionnement de PlaylistAudioXSPFBuilder
              en construisant une playlist et en affichant son contenu.

Historique des versions :
    - 1.0 : Création du module de test permettant de vérifier l'extraction
            des métadonnées, la récupération des pochettes et la création
            d'une playlist XSPF.

Auteur : Alexandre BURIN
Version : 1.0
"""

# Importation des modules
from pathlib import Path
from library import PlaylistAudioXSPFBuilder

try:
    # Création de la playlist
    playlist_builder = PlaylistAudioXSPFBuilder(Path("."), "Ma playlist", "./maplaylist.xspf")
    playlist = playlist_builder.construire()

    # Affichage de la playlist
    print(playlist)
except Exception as e:
    print(e)