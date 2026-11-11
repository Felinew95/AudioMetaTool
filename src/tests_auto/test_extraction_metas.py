"""
Module : test_extraction_metas.py

Description : Ce module permet de tester le fonctionnement de l'extraction
              des métadonnées et des pochettes des fichiers audio, ainsi que
              la création d'une playlist XSPF à partir des fichiers trouvés
              dans un dossier et ses sous-dossiers.

              Il vérifie le bon fonctionnement de PlaylistAudioXSPFBuilder
              en construisant une playlist et en affichant son contenu.

Historique des versions :
    - 1.0 : Création du module de test.
    - 1.1 : Utilisation de trouver_dossier_musique() pour cibler un dossier
            audio dédié au lieu d'explorer tout le projet

Auteurs : Alexandre BURIN, Nassim BERRANDOU
Version : 1.1
"""

# Importation des modules
from src.config import trouver_dossier_musique
from src.library.traitement import PlaylistAudioXSPFBuilder

def test_extraction_metas() -> None:
    """
    Teste le fonctionnement de l'extraction des métadonnées et des pochettes
    des fichiers audio, ainsi que la création d'une playlist XSPF à partir
    des fichiers trouvés dans un dossier et ses sous-dossiers.

    Cette fonction vérifie le bon fonctionnement de PlaylistAudioXSPFBuilder
    en construisant une playlist et en affichant son contenu.
    """
    try:
        # Résolution du dossier de musique
        dossier = trouver_dossier_musique()

        # Création de la playlist
        playlist_builder = PlaylistAudioXSPFBuilder(
            dossier, "Ma playlist", "./maplaylist.xspf"
        )
        playlist = playlist_builder.construire()

        # Affichage de la playlist
        print(playlist)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    test_extraction_metas()
