"""
Module : PlaylistAudioXSPF.py

Description :
    Ce module définit la classe PlaylistAudioXSPF, qui permet de représenter
    une playlist audio au format XSPF et de gérer les pistes qu'elle contient.

    Les informations de la playlist sont encapsulées dans des attributs
    préfixés par un underscore et accessibles à travers des propriétés
    correspondantes.

    Ces propriétés permettent de consulter et de modifier le nom, le chemin
    de la playlist, le nombre de pistes et sa durée totale. La classe permet
    également d'ajouter des pistes audio et d'accéder à la liste des pistes
    contenues dans la playlist.

Versions :
    - 1.0 : Version initiale de la classe PlaylistAudioXSPF.
    - 1.1 : Ajout des assertions dans le constructeur pour vérifier
      la validité des informations de la playlist.

Auteur : Alexandre BURIN
Version : 1.1
"""

# Importation des modules
from library.donnees import PisteAudio

class PlaylistAudioXSPF:
    """
    Représente une playlist audio au format XSPF.

    La classe stocke le nom, le chemin, le nombre de pistes et la durée
    totale de la playlist. Elle permet également de gérer les pistes
    audio qu'elle contient et d'accéder à ses informations à travers
    des propriétés.
    """

    def __init__(self, nom: str, chemin_playlist: str) -> None:
        """
        Initialise les informations de la playlist audio.

        :param nom: Nom de la playlist.
        :param chemin_playlist: Chemin d'accès au fichier de playlist.

        :return: None. Aucune valeur n'est retournée.

        :raises AssertionError: Si le nom ou le chemin est vide, ou si
            le nombre de pistes ou la durée totale est négatif.
        """
        assert nom, "Le nom de la playlist ne peut pas être vide"
        assert chemin_playlist, "Le chemin de la playlist ne peut pas être vide"

        self._nom: str = nom
        self._chemin_playlist: str = chemin_playlist
        self._nombre_pistes: int = 0
        self._duree_totale: float|int = 0
        self._pistes: list[PisteAudio] = []

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de la playlist et de ses pistes.

        :return: Chaîne contenant les informations de la playlist
                 et la description de chacune de ses pistes.
        """
        # Informations de la playlist
        aff: str = "==== " + self._nom + " ====\n\n"
        aff += "Chemin : " + self._chemin_playlist + "\n"
        aff += "Nombre de pistes : " + str(self._nombre_pistes) + "\n"
        aff += "Durée totale : " + str(self._duree_totale) + " sec\n\n"

        # Affichage des pistes
        for i in range(self._nombre_pistes):
            aff += f"== Piste {i+1} ==\n" + str(self._pistes[i]) + "\n"

        return aff

    def _get_nom(self) -> str:
        """
        Retourne le nom de la playlist.

        :return: Nom de la playlist.
        """
        return self._nom

    def _set_nom(self, nom: str) -> None:
        """
        Modifie le nom de la playlist.

        :param nom: Nouveau nom de la playlist.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si le nom fourni est vide.
        """
        if not nom:
            raise ValueError("Le nom de la playlist ne peut pas être vide")
        self._nom = nom

    def _get_chemin_playlist(self) -> str:
        """
        Retourne le chemin d'accès à la playlist.

        :return: Chemin du fichier de playlist.
        """
        return self._chemin_playlist

    def _set_chemin_playlist(self, chemin_playlist: str) -> None:
        """
        Modifie le chemin d'accès à la playlist.

        :param chemin_playlist: Nouveau chemin du fichier de playlist.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si le chemin fourni est vide.
        """
        if not chemin_playlist:
            raise ValueError("Le chemin de la playlist ne peut pas être vide")
        self._chemin_playlist = chemin_playlist

    def _get_nombre_pistes(self) -> int:
        """
        Retourne le nombre de pistes de la playlist.

        :return: Nombre de pistes.
        """
        return self._nombre_pistes

    def _set_nombre_pistes(self, nombre_pistes: int) -> None:
        """
        Modifie le nombre de pistes de la playlist.

        :param nombre_pistes: Nouveau nombre de pistes.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si le nombre de pistes est négatif.
        """
        if nombre_pistes < 0:
            raise ValueError("Le nombre de pistes ne peut pas être négatif")
        self._nombre_pistes = nombre_pistes

    def _get_duree_totale(self) -> float | int:
        """
        Retourne la durée totale de la playlist.

        :return: Durée totale de la playlist.
        """
        return self._duree_totale

    def _set_duree_totale(self, duree_totale: float | int) -> None:
        """
        Modifie la durée totale de la playlist.

        :param duree_totale: Nouvelle durée totale de la playlist.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si la durée totale est négative.
        """
        if duree_totale < 0:
            raise ValueError("La durée totale ne peut pas être négative")
        self._duree_totale = duree_totale

    def _get_pistes(self) -> list:
        """
        Retourne la liste des pistes audio de la playlist.

        :return: Liste des objets PisteAudio contenus dans la playlist.
        """
        return self._pistes

    def ajouter_piste(self, piste: PisteAudio) -> None:
        """
        Ajoute une piste audio à la playlist.

        Le nombre de pistes et la durée totale sont mis à jour lors
        de l'ajout.

        :param piste: Piste audio à ajouter.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si la piste est déjà présente dans la playlist.
        """
        if piste in self._pistes:
            raise ValueError("La piste est déjà dans la playlist")

        self._nombre_pistes += 1
        self._duree_totale += piste.metadonnees.duree

        self._pistes.append(piste)

    # Définition des propriétés
    nom: property = property(_get_nom, _set_nom)
    chemin_playlist: property = property(_get_chemin_playlist, _set_chemin_playlist)
    nombre_pistes: property = property(_get_nombre_pistes, _set_nombre_pistes)
    duree_totale: property = property(_get_duree_totale, _set_duree_totale)
    pistes: property = property(_get_pistes)