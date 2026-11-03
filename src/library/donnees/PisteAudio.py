"""
Module : PisteAudio.py

Description :
    Ce module définit la classe PisteAudio, qui permet de représenter
    un fichier audio en regroupant son chemin, sa taille, ses métadonnées
    textuelles et sa pochette.

    Les informations du fichier audio sont encapsulées dans des attributs
    préfixés par un underscore et accessibles à travers des propriétés
    correspondantes.

    Ces propriétés permettent de consulter et de modifier le chemin du
    fichier, sa taille, ses métadonnées et sa pochette. Elles permettent
    également de contrôler les valeurs attribuées à ces informations.

Versions :
    - 1.0 : Version initiale de la classe PisteAudio.
    - 1.1 : Ajout des assertions dans le constructeur pour vérifier
      la présence du chemin du fichier et la validité de sa taille.

Auteur : Alexandre BURIN
Version : 1.1
"""

from src.library.donnees.MetadonneesAudio import MetadonneesAudio
from src.library.donnees.PochettePiste import PochettePiste


class PisteAudio:
    """
    Représente un fichier audio et regroupe ses principales informations.
    
    La classe stocke le chemin d'accès, la taille, les métadonnées
    textuelles et la pochette du fichier audio. Les propriétés permettent
    d'accéder aux attributs internes et de les modifier de manière contrôlée.
    
    Auteur : Alexandre BURIN
    Version : 1.1
    """

    def __init__(self, chemin_fichier: str, taille: float|int,
                 metadonnees: MetadonneesAudio, pochette: PochettePiste) -> None:
        """
        Initialise les informations du fichier audio.

        :param chemin_fichier: Chemin d'accès au fichier audio.
        :param taille: Taille du fichier audio.
        :param metadonnees: Métadonnées textuelles du fichier audio.
        :param pochette: Pochette associée au fichier audio.
        :return: None. Aucune valeur n'est retournée.
        """
        assert chemin_fichier, "Le chemin du fichier ne peut pas être vide"
        assert taille >= 0, "La taille du fichier ne peut pas être négatif"

        self._chemin_fichier = chemin_fichier
        self._taille = taille
        self._metadonnees = metadonnees
        self._pochette = pochette

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle du fichier audio.

        :return: Chaîne contenant le chemin, la taille, les métadonnées
                 et la pochette du fichier audio.
        """
        aff = "\nChemin du fichier : " + self._chemin_fichier
        aff += "\nTaille : " + str(self._taille) + " ko\n"
        aff += ("\n-- Méta-données -- \n" + str(self._metadonnees)
            + "\n" + 18*"-" + "\n")
        aff += ("\n-- Pochette -- \n" + str(self._pochette)
                + "\n" + 14 * "-" + "\n")
        return aff

    def __eq__(self, valeur: object) -> bool:
        """
        Compare deux fichiers audio.

        Deux fichiers audio sont considérés comme égaux si leur chemin,
        leur taille, leurs métadonnées et leur pochette sont identiques.

        :param valeur: Objet à comparer avec le fichier audio.
        :return: True si les deux fichiers audio sont égaux, False sinon.
        """
        # Vérifie si l'objet est une instance de PochettePiste
        if not(isinstance(valeur, PisteAudio)):
            return False

        # Compare les métadonnées des deux objets
        return (
            self._chemin_fichier == valeur._chemin_fichier and
            self._taille == valeur._taille and
            self._metadonnees == valeur._metadonnees and
            self._pochette == valeur._pochette
        )

    def _get_chemin_fichier(self) -> str:
        """
        Retourne le chemin d'accès au fichier audio.

        :return: Chemin du fichier audio.
        """
        return self._chemin_fichier

    def _set_chemin_fichier(self, chemin_fichier: str) -> None:
        """
        Modifie le chemin d'accès au fichier audio.

        :param chemin_fichier: Nouveau chemin du fichier audio.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si le chemin fourni est vide.
        """
        if not chemin_fichier:
            raise ValueError("Le chemin du fichier ne peut pas être vide.")
        self._chemin_fichier = chemin_fichier

    def _get_taille(self) -> float | int:
        """
        Retourne la taille du fichier audio.

        :return: Taille du fichier audio.
        """
        return self._taille

    def _set_taille(self, taille: float | int) -> None:
        """
        Modifie la taille du fichier audio.

        :param taille: Nouvelle taille du fichier audio.
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si la taille fournie est négative.
        """
        if taille < 0:
            raise ValueError("La taille du fichier ne peut pas être négative.")
        self._taille = taille

    def _get_metadonnees(self) -> MetadonneesAudio:
        """
        Retourne les métadonnées textuelles du fichier audio.

        :return: Objet contenant les métadonnées du fichier audio.
        """
        return self._metadonnees

    def _set_metadonnees(self, metadonnees: MetadonneesAudio) -> None:
        """
        Modifie les métadonnées textuelles du fichier audio.

        :param metadonnees: Nouvelles métadonnées du fichier audio.
        :return: None. Aucune valeur n'est retournée.
        """
        self._metadonnees = metadonnees

    def _get_pochette(self) -> PochettePiste:
        """
        Retourne la pochette associée au fichier audio.

        :return: Objet représentant la pochette du fichier audio.
        """
        return self._pochette

    def _set_pochette(self, pochette: PochettePiste) -> None:
        """
        Modifie la pochette associée au fichier audio.

        :param pochette: Nouvelle pochette du fichier audio.
        :return: None. Aucune valeur n'est retournée.
        """
        self._pochette = pochette

    # Définition des propriétés
    chemin_fichier = property(_get_chemin_fichier, _set_chemin_fichier)
    taille = property(_get_taille, _set_taille)
    metadonnees = property(_get_metadonnees, _set_metadonnees)
    pochette = property(_get_pochette, _set_pochette)
