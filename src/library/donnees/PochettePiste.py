"""
Module : PochettePiste.py

Description :
    Ce module définit la classe PochettePiste, qui permet de représenter
    la pochette d'un fichier audio à partir de ses données binaires
    et de son format.

    Les données de la pochette et son format sont encapsulés dans des
    attributs préfixés par un underscore et accessibles à travers des
    propriétés correspondantes.

    Ces propriétés permettent de consulter et de modifier les données
    de la pochette de manière contrôlée, en vérifiant notamment que
    les valeurs fournies sont valides.

Versions :
    - 1.0 : Version initiale de la classe PochettePiste.
    - 1.1 : Ajout des assertions dans le constructeur pour vérifier
      la présence des données et du format de la pochette.

Auteur : Alexandre BURIN
Version : 1.1
"""

class PochettePiste:
    """
    Représente la pochette d'un fichier audio.

    La classe stocke les données binaires de l'image et son format.
    Les propriétés permettent d'accéder aux attributs internes et de
    les modifier de manière contrôlée.

    Auteur : Alexandre BURIN
    Version : 1.1
    """

    def __init__(self, donnees: bytes, format_pochette: str) -> None:
        """
        Initialise la pochette d'un fichier audio.

        :param donnees: Données binaires de l'image.
        :param format_pochette: Format de l'image de la pochette.

        :return: None. Aucune valeur n'est retournée.
        """
        assert format_pochette, "Le format de la pochette ne peut pas être vide"

        self._donnees: bytes = donnees
        self._format_pochette: str = format_pochette

    def __str__(self) -> str:
        """
        Retourne une représentation textuelle de la pochette.

        :return: Format de l'image de la pochette.
        """
        return "Format de la pochette : " + self._format_pochette

    def __eq__(self, valeur: object) -> bool:
        """
        Compare les pochettes de deux fichiers audio.

        :param valeur: Objet à comparer avec la pochette courante.
        :return: True si les références sont identiques ou si les deux
                 objets possèdent les mêmes données et le même format,
                 False sinon.
        """
        # Vérifie si l'objet est une instance de PochettePiste
        if not isinstance(valeur, PochettePiste):
            return False

        # Compare les métadonnées des deux objets
        return (
            self._donnees == valeur._donnees and
            self._format_pochette == valeur._format_pochette
        )

    def _get_donnees(self) -> bytes:
        """
        Retourne les données binaires de l'image.

        :return: Données binaires de la pochette.
        """
        return self._donnees

    def _set_donnees(self, donnees: bytes) -> None:
        """
        Modifie les données binaires de l'image après validation.

        :param donnees: Nouvelles données binaires de la pochette.
        :return: None. Aucune valeur n'est retournée.

        :raise ValueError: Si les données de l'image sont vides.
        """
        self._donnees = donnees

    def _get_format_pochette(self) -> str:
        """
        Retourne le format de l'image de la pochette.

        :return: Format de l'image.
        """
        return self._format_pochette

    def _set_format_pochette(self, format_pochette: str) -> None:
        """
        Modifie le format de l'image après validation.

        :param format_pochette: Nouveau format de la pochette.
        :return: None. Aucune valeur n'est retournée.

        :raise ValueError: Si le format de la pochette est vide.
        """
        if not format_pochette:
            raise ValueError("Le format de la pochette ne peut pas être vide.")
        self._format_pochette = format_pochette

    # Définition des propriétés
    donnees: property = property(_get_donnees, _set_donnees)
    format_pochette: property = property(_get_format_pochette, _set_format_pochette)