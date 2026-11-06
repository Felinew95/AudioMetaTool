"""
Module : PisteAudioBuilder.py

Description : Ce module définit la classe PisteAudioBuilder permettant de
              construire un objet PisteAudio à partir d'un fichier audio.
              Elle centralise la vérification du fichier, l'extraction des
              métadonnées et la récupération de la pochette intégrée.

              Les formats audio pris en charge sont le MP3 et le FLAC.

Historique des versions :
    - 1.0 : Regroupement des classes d'extraction des métadonnées et des
            pochettes audio au sein d'une classe unique PisteAudioBuilder.
            Ajout de la construction centralisée des objets PisteAudio.
    - 1.1 : Modification du constructeur pour permettre l'initialisation
            sans fichier audio.
            Ajout d'un getter et d'un setter pour modifier le fichier utilisé.
            Centralisation des vérifications et du chargement du fichier
            dans une méthode interne.

Auteurs : Menaouer Ammari, Alexandre Burin
Version : 1.1
"""

# Importation des modules
from pathlib import Path

from typing import Any

from mutagen import File
from mutagen.flac import FLAC
from mutagen.mp3 import MP3

from config import EXTENSIONS_AUTORISES

from library import PisteAudio
from library import MetadonneesAudio
from library import PochettePiste

class PisteAudioBuilder:
    """
    Construit un objet PisteAudio à partir d'un fichier audio.

    Cette classe applique le patron de conception Builder afin de
    centraliser la vérification et l'extraction des informations
    nécessaires à la création d'une piste audio.

    Formats pris en charge :
        - MP3
        - FLAC
    """

    def __init__(self) -> None:
        """
        Initialise le constructeur
        """
        self._fichier = None
        self._extension = None
        self._audio = None

    def _get_fichier(self) -> Path:
        """
        Retourne le chemin du fichier audio actuellement utilisé.

        :return: Chemin du fichier audio.
        """
        return self._fichier


    def _set_fichier(self, fichier: Path) -> None:
        """
        Modifie le fichier audio utilisé par le Builder.

        :param fichier: Nouveau chemin du fichier audio.
        :raises FileNotFoundError: Si le fichier n'existe pas.
        :raises ValueError: Si son extension n'est pas autorisée.
        """
        self._charger_fichier(fichier)

    def _charger_fichier(self, fichier: Path):
        """
        Vérifie et charge un fichier audio dans le Builder.

        :param fichier: Chemin du fichier audio à charger.
        :raises FileNotFoundError: Si le fichier n'existe pas.
        :raises ValueError: Si l'extension ou le format audio n'est pas reconnu.
        """
        # Vérification de l'existence du fichier
        if not fichier.is_file():
            raise FileNotFoundError(f"Le fichier {fichier} n'existe pas")

        # Récupération de l'extension
        extension: str = fichier.suffix.lower()

        # Vérification de l'extension
        if extension not in EXTENSIONS_AUTORISES:
            raise ValueError(f"Extensions acceptées : {', '.join(EXTENSIONS_AUTORISES)}")

        # Chargement du nouveau fichier audio
        audio = File(str(fichier), easy=True)
        if audio is None:
            raise ValueError(f"Format audio non reconnu : {fichier}")

        # Mise à jour
        self._fichier: Path = fichier
        self._extension: str = extension
        self._audio = audio

    def _extraire_metadonnees(self) -> MetadonneesAudio:
        """
        Extrait les métadonnées textuelles du fichier audio.

        Récupère le titre, l'artiste, l'album, le genre, l'année,
        le numéro de piste, la durée, l'artiste de l'album et le compositeur.
        Utilise des valeurs par défaut lorsque certaines informations
        sont absentes ou invalides.

        :return: Objet contenant les métadonnées extraites.
        """
        # Récupération des métadonnées
        tags: dict = self._audio.tags or {}

        titre: str = self._lire_tag(tags, "title", self._fichier.stem)
        artiste: str = self._lire_tag(tags, "artist", "Inconnu")
        album: str = self._lire_tag(tags, "album", "Inconnu")
        genre: str = self._lire_tag(tags, "genre", "Inconnu")
        date: str = self._lire_tag(tags, "date", "0")
        numero: str = self._lire_tag(tags, "tracknumber", "1")
        artiste_album: str = self._lire_tag(tags, "albumartist", artiste)
        compositeur: str = self._lire_tag(tags, "composer", "Inconnu")

        # Convertion de l'année
        try:
            annee: int = int(date[:4])
        except ValueError:
            annee: int = 0

        # Convertion du numéro de piste
        try:
            num_piste: int = int(numero.split("/")[0])
            num_piste = max(1, num_piste)
        except ValueError:
            num_piste: int = 1

        # Récupération la durée
        duree: float|int = self._audio.info.length

        # Construire l'objet métadonnées
        metadonnees: MetadonneesAudio = MetadonneesAudio(
            titre=titre,
            artiste=artiste,
            album=album,
            genre=genre,
            annee=annee,
            num_piste=num_piste,
            duree=duree,
            artiste_album=artiste_album,
            compositeur=compositeur
        )

        return metadonnees

    def _extraire_pochette(self) -> PochettePiste | None:
        """
        Extrait la pochette intégrée au fichier audio.

        Prend en charge les images APIC des fichiers MP3 et les images
        intégrées des fichiers FLAC.

        :return: Objet PochettePiste ou None si aucune image exploitable
                     n'est disponible.
        """

        # Extraction des données en fonction de l'extension
        images: list = []
        match self._extension:
            case ".mp3":
                audio: MP3 = MP3(str(self._fichier))
                images = audio.tags.getall("APIC") if audio.tags else []
            case ".flac":
                audio: FLAC = FLAC(str(self._fichier))
                images = audio.pictures

        # Vérifier si le fichier possède au moins une image
        if not images:
            return None

        # Récupérer la première image
        image = images[0]
        if not image.data or not image.mime:
            return None
        if image.mime == "-->":
            return None

        # Créer l'objet pochette
        return PochettePiste(donnees=image.data,format_pochette=image.mime)

    def construire(self) -> PisteAudio:
        """
        Construit un objet PisteAudio à partir du fichier audio.

        Regroupe les métadonnées extraites, la pochette et la taille
        du fichier afin de créer une nouvelle instance de PisteAudio.

        :return: Objet PisteAudio contenant les informations du fichier.
        """
        # Récupération des métadonnées
        metadonnees: MetadonneesAudio = self._extraire_metadonnees()

        # Récupération de la pochette
        pochette: PochettePiste|None = self._extraire_pochette()
        if pochette is None:
            pochette: PochettePiste = PochettePiste(donnees=b"", format_pochette="Inconnu")

        # Extraction de la taille en Mo du fichier
        taille: float|int = self._fichier.stat().st_size / 1_000_000

        # Création de la piste musicale
        return PisteAudio(str(self._fichier), taille, metadonnees, pochette)

    @staticmethod
    def _lire_tag(tags: dict, cle: str, val_defaut: str) -> str:
        """
        Récupère la valeur d'une métadonnée à partir de sa clé.

        Retourne la première valeur associée à la clé lorsque celle-ci
        existe, ou la valeur par défaut dans le cas contraire.

        :param tags: Dictionnaire contenant les métadonnées audio.
        :param cle: Clé de la métadonnée recherchée.
        :param val_defaut: Valeur retournée si la clé est absente.
        :return: Valeur de la métadonnée sous forme de chaîne de caractères.
        """

        # Récupère les données liées à la clé
        valeurs: Any = tags.get(cle)

        # Récupération de la première valeur
        return str(valeurs[0]) if valeurs else val_defaut

    # Définition des propriétés
    fichier: property = property(_get_fichier, _set_fichier)