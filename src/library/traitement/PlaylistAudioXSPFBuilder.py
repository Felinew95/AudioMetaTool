
"""
Module : PlaylistAudioXSPFBuilder.py

Description : Ce module définit la classe PlaylistAudioXSPFBuilder permettant
              de construire une playlist XSPF à partir des fichiers audio
              présents dans un dossier et ses sous-dossiers.
              Elle utilise ExplorateurAudio pour rechercher les fichiers
              audio et PisteAudioBuilder pour extraire leurs métadonnées
              et leurs pochettes avant de les ajouter à la playlist.

Historique des versions :
    - 1.0 : Création d'une première classe permettant d'explorer un dossier
            et de créer une liste d'objets PisteAudio à partir des fichiers
            audio trouvés.
    - 1.1 : Amélioration de la classe avec l'utilisation du patron Builder.
            Ajout de la construction directe d'une playlist XSPF et de
            l'intégration des pistes audio au fur et à mesure de leur
            traitement.
    - 1.2 : Ajout de la modification du dossier source, du nom et du chemin
            de destination de la playlist.

Auteurs : Menaouer Ammari, Alexandre Burin
Version : 1.2
"""

# Importations des modules
from pathlib import Path
from mutagen import MutagenError

from src.library.traitement.ExplorateurAudio import ExplorateurAudio
from src.library.traitement.PisteAudioBuilder import PisteAudioBuilder
from src.library.donnees.PlaylistAudioXSPF import PlaylistAudioXSPF
from src.library.donnees.PisteAudio import PisteAudio

class PlaylistAudioXSPFBuilder:
    """
    Construit une playlist XSPF à partir des fichiers audio d'un dossier.

    Cette classe coordonne l'exploration des dossiers, l'extraction des
    métadonnées et des pochettes, ainsi que la création des objets PisteAudio.
    """

    def __init__(self, dossier: Path, nom: str, chemin_playlist: str) -> None:
        """
        Initialise le constructeur de playlist XSPF.

        Vérifie l'existence du dossier et initialise les objets nécessaires
        à l'exploration et à la construction de la playlist.

        :param dossier: Chemin du dossier contenant les fichiers audio.
        :param nom: Nom de la playlist à créer.
        :param chemin_playlist: Chemin de destination de la playlist XSPF.
        :return: None
        :raises NotADirectoryError: Si le chemin indiqué n'est pas un dossier.
        """
        # Initialisation du dossier
        self._dossier: Path = dossier

        # Vérification du dossier
        if not self._dossier.is_dir():
            raise NotADirectoryError("Le dossier est introuvable")

        # Initialisation de l'explorateur
        self._explorateur = ExplorateurAudio(dossier)

        # Initialisation du constructeur de pistes
        self._piste_builder = PisteAudioBuilder()

        # Initialisation de la playlist
        self._playlist = PlaylistAudioXSPF(nom, chemin_playlist)

    def _get_dossier(self) -> Path:
        """
        Retourne le chemin du dossier contenant les fichiers audio.

        :return: Chemin du dossier source.
        """
        return self._dossier

    def _set_dossier(self, dossier: Path) -> None:
        """
        Modifie le dossier contenant les fichiers audio.

        Vérifie que le nouveau chemin correspond à un dossier existant.

        :param dossier: Nouveau chemin du dossier source.
        :return: None
        :raises NotADirectoryError: Si le chemin indiqué n'est pas un dossier.
        """
        # Vérification du dossier
        if not dossier.is_dir():
            raise NotADirectoryError("Le dossier est introuvable")

        self._dossier = dossier
        self._explorateur = ExplorateurAudio(dossier)

    def _get_nom(self) -> str:
        """
        Retourne le nom de la playlist.

        :return: Nom de la playlist.
        """
        return self._playlist.nom

    def _set_nom(self, nom: str) -> None:
        """
        Modifie le nom de la playlist.

        :param nom: Nouveau nom de la playlist.
        :return: None
        """
        self._playlist.nom = nom

    def _get_chemin_playlist(self) -> str:
        """
        Retourne le chemin de destination de la playlist.

        :return: Chemin de destination de la playlist XSPF.
        """
        return self._playlist.chemin_playlist

    def _set_chemin_playlist(self, chemin_playlist: str) -> None:
        """
        Modifie le chemin de destination de la playlist.

        :param chemin_playlist: Nouveau chemin de destination de la playlist.
        :return: None
        """
        self._playlist.chemin_playlist = chemin_playlist

    def construire(self) -> PlaylistAudioXSPF:
        """
        Construit une playlist à partir des fichiers audio du dossier.

        Explore récursivement le dossier, construit les pistes audio
        correspondantes et les ajoute à la playlist.

        :return: Playlist XSPF contenant les pistes audio trouvées.
        """
        # Récupération des fichiers musicaux
        fichiers: list[str] = self._explorateur.extraire_fichiers_musique()

        # Création des pistes et ajout dans la playlist
        for fichier in fichiers:
            self._ajouter_piste(fichier)

        return self._playlist

    def _ajouter_piste(self, fichier: str) -> None:
        """
        Construit une piste audio et l'ajoute à la playlist.

        En cas d'erreur lors du chargement ou de l'extraction des informations,
        le fichier concerné est ignoré et un message d'erreur est affiché.

        :param fichier: Chemin du fichier audio à traiter.
        :return: None
        """
        try:
            # Mise à jour du fichier
            self._piste_builder.fichier = Path(fichier)

            # Création de la piste
            piste: PisteAudio = self._piste_builder.construire()

            # Ajout à la playlist
            self._playlist.ajouter_piste(piste)

        except (OSError, ValueError, MutagenError) as error:
            print(f"Erreur avec le fichier : {fichier} ({error})")

    # Définition des propriétés
    dossier: property = property(_get_dossier, _set_dossier)
    nom: property = property(_get_nom, _set_nom)
    chemin_playlist: property = property(_get_chemin_playlist, _set_chemin_playlist)
