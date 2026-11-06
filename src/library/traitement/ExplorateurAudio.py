"""
Module : ExplorateurAudio.py

Description : Ce module définit la classe ExplorateurFichiersAudio permettant
              d'explorer récursivement un dossier et ses sous-dossiers afin
              de rechercher les fichiers audio possédant une extension
              autorisée.

              Les chemins des fichiers audio trouvés sont retournés sous
              forme de chaînes de caractères.

Historique des versions :
    - 1.0 : Création de la classe permettant d'explorer un dossier à
            la recherche de fichiers audio.
    - 1.1 : Amélioration de l'exploration récursive avec exclusion des
            liens symboliques et vérification des extensions autorisées.

Auteurs : Menaouer Ammari
Version : 1.1
"""

# Importation des modules
from pathlib import Path
from config import EXTENSIONS_AUTORISES

class ExplorateurAudio:
    """
    Explore récursivement un dossier à la recherche de fichiers audio.

    La classe parcourt le dossier fourni ainsi que ses sous-dossiers.
    Elle identifie les fichiers possédant une extension autorisée et
    ignore les liens symboliques.
    """

    def __init__(self, dossier: Path):
        """
        Initialise l'explorateur avec le dossier à parcourir.

        Vérifie que le chemin fourni correspond à un dossier existant.

        :param dossier: Chemin du dossier à explorer.
        :raises NotADirectoryError: Si le chemin ne correspond pas à un dossier.
        """
        self._dossier: Path = dossier

    def extraire_fichiers_musique(self) -> list[str]:
        """
        Récupère les chemins des fichiers audio présents dans le dossier.

        Lance l'exploration récursive du dossier initial et de ses
        sous-dossiers afin de constituer la liste des fichiers audio trouvés.

        :return: Liste des chemins des fichiers audio sous forme de chaînes.
        """

        # Récupération des fichiers musicaux
        return self._parcourir_dossier(self._dossier, fichiers_audio=[])

    def _parcourir_dossier(self, dossier: Path, fichiers_audio: list[str]) -> list[str]:
        """
        Parcourt récursivement un dossier à la recherche de fichiers audio.

        Explore les sous-dossiers, ignore les liens symboliques et ajoute
        à la liste les fichiers possédant une extension autorisée.

        :param dossier: Chemin du dossier actuellement exploré.
        :param fichiers_audio: Liste des fichiers audio déjà identifiés.
        :return: Liste actualisée des chemins des fichiers audio trouvés.
        """

        # Parcours du dossier
        for fichier in dossier.iterdir():

            # Vérification si c'est un lien symbolique
            if fichier.is_symlink():
                continue

            # Exploration du sous-dossier
            if fichier.is_dir():
                self._parcourir_dossier(fichier, fichiers_audio)
            # Vérification du fichier
            else:
                # Récupération de l'extension du fichier
                extension: str = fichier.suffix.lower()

                # Vérification de l'extension
                if extension in EXTENSIONS_AUTORISES:
                    fichiers_audio.append(str(fichier))

        return fichiers_audio
