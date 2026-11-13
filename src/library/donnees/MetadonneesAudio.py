"""
Module : MetadonneesAudio.py

Description :
    Ce module définit la classe MetadonneesAudio, qui permet de représenter
    les métadonnées textuelles d'un fichier audio.

    Les données gérées par la classe sont le titre, le nom de l'artiste principal,
    le titre de l'album, le genre musical, l'année de publication, le numéro de piste,
    la durée du fichier audio, le nom de l'artiste de l'album et celui du compositeur.

    Chaque donnée textuelle est encapsulée dans un attribut préfixé par
    un underscore et accessible à travers une propriété correspondante.

    Les propriétés permettent de consulter et de modifier les métadonnées
    de manière contrôlée, notamment en vérifiant la validité des valeurs
    lors de leur modification.

Versions :
    - 1.0 : Version initiale de la classe MetadonneesAudio.
    - 1.1 : Corrige la comparaison des attributs dans la méthode __eq__
      et améliore les messages d'erreur des propriétés.
    - 1.2 : Ajout des assertions dans le constructeur pour vérifier
      la validité des métadonnées lors de l'initialisation.

Auteur : Alexandre BURIN
Version : 1.2
"""

# Importation des modules
from library.utilitaires.outils import convertir_date

class MetadonneesAudio:
    """
    Représente les métadonnées textuelles d'un fichier audio.

    La classe regroupe les principales informations descriptives d'un
    fichier audio. Chaque attribut interne possède une propriété qui
    permet d'y accéder et de le modifier indirectement.

    Auteur : Alexandre BURIN
    Version : 1.2
    """
    def __init__(
            self,
            titre: str,
            artiste: str,
            album: str,
            genre: str,
            annee: int,
            num_piste: int,
            duree: float|int,
            artiste_album: str,
            compositeur: str
    ) -> None:
        """
        Initialise les métadonnées textuelles d'un fichier audio.

        :param titre: Titre du fichier audio.
        :param artiste: Nom de l'artiste principal.
        :param album: Titre de l'album.
        :param genre: Genre musical.
        :param annee: Année de publication.
        :param num_piste: Numéro de la piste.
        :param duree: Durée du fichier audio.
        :param artiste_album: Nom de l'artiste de l'album.
        :param compositeur: Nom du compositeur.

        :return: None. Aucune valeur n'est retournée.
        """
        assert titre, "Le titre ne peut pas être vide."
        assert artiste, "L'artiste ne peut pas être vide."
        assert album, "L'album ne peut pas être vide."
        assert genre, "Le genre ne peut pas être vide."
        assert annee >= 0, "L'année ne peut pas être négative."
        assert num_piste >= 1, "Le numéro de piste doit être supérieur ou égal à 1."
        assert duree >= 0, "La durée ne peut pas être négative."
        assert artiste_album, "L'artiste de l'album ne peut pas être vide."
        assert compositeur, "Le compositeur ne peut pas être vide."

        self._titre: str = titre
        self._artiste: str = artiste
        self._album: str = album
        self._genre: str = genre
        self._annee: int = annee
        self._num_piste: int = num_piste
        self._duree: float|int = duree
        self._artiste_album: str = artiste_album
        self._compositeur: str = compositeur

    def __str__(self) -> str:
        """
        Retourne les métadonnées du fichier audio sous forme de texte.

        :return: Métadonnées du fichier audio formatées sur plusieurs lignes.
        """
        heures, minutes, secondes = convertir_date(duree=self._duree)

        aff = "Titre : " + self._titre
        aff += "\nArtiste : " + self._artiste
        aff += "\nAlbum : " + self._album
        aff += "\nGenre : " + self._genre
        aff += "\nAnnée : " + str(self._annee)
        aff += "\nNuméro de Piste : " + str(self._num_piste)
        aff += f"\nDurée : {int(heures)}h {int(minutes)}min {int(secondes)}s"
        aff += "\nArtiste de l'album : " + self._artiste_album
        aff += "\nCompositeur : " + self._compositeur
        return aff

    def __eq__(self, valeur: object) -> bool:
        """
        Compare les métadonnées de deux fichiers audio afin de déterminer
        si elles sont identiques.

        :param valeur: Objet à comparer avec les métadonnées courantes.
        :return: True si les références sont identiques ou si les deux
             objets possèdent les mêmes métadonnées, False sinon.
        """
        # Vérifie si l'objet est une instance de MetadonneesAudio
        if not isinstance(valeur, MetadonneesAudio):
            return False

        # Compare les métadonnées des deux objets
        return (
            self._titre == valeur._titre and
            self._artiste == valeur._artiste and
            self._album == valeur._album and
            self._genre == valeur._genre and
            self._annee == valeur._annee and
            self._num_piste == valeur._num_piste and
            abs(self._duree - valeur._duree) < 1e9 and
            self._artiste_album == valeur._artiste_album and
            self._compositeur == valeur._compositeur
        )

    def _get_titre(self) -> str:
        """
        Retourne le titre du fichier audio.

        :return: Titre du fichier audio.
        """
        return self._titre

    def _set_titre(self, titre: str) -> None:
        """
        Modifie le titre du fichier audio après validation.

        :param titre: Nouveau titre du fichier audio.
        :return: None

        :raise ValueError: Si le titre est vide.
        """
        if not titre:
            raise ValueError("Le titre ne peut pas être vide.")
        self._titre = titre

    def _get_artiste(self) -> str:
        """
        Retourne le nom de l'artiste principal.

        :return: Nom de l'artiste principal.
        """
        return self._artiste

    def _set_artiste(self, artiste: str) -> None:
        """
        Modifie le nom de l'artiste après validation.

        :param artiste: Nouveau nom de l'artiste.
        :return: None

        :raise ValueError: Si le nom de l'artiste est vide.
        """
        if not artiste:
            raise ValueError("Le nom de l'artiste ne peut pas être vide.")
        self._artiste = artiste

    def _get_album(self) -> str:
        """
        Retourne le titre de l'album.

        :return: Titre de l'album.
        """
        return self._album

    def _set_album(self, album: str) -> None:
        """
        Modifie le titre de l'album après validation.

        :param album: Nouveau titre de l'album.
        :return: None

        :raise ValueError: Si le titre de l'album est vide.
        """
        if not album:
            raise ValueError("Le titre de l'album ne peut pas être vide.")
        self._album = album

    def _get_genre(self) -> str:
        """
        Retourne le genre musical.

        :return: Genre musical du fichier audio.
        """
        return self._genre

    def _set_genre(self, genre: str) -> None:
        """
        Modifie le genre musical après validation.

        :param genre: Nouveau genre musical.
        :return: None
        :raise ValueError: Si le genre musical est vide.
        """
        if not genre:
            raise ValueError("Le genre musical ne peut pas être vide.")
        self._genre = genre

    def _get_annee(self) -> int:
        """
        Retourne l'année de publication.

        :return: Année de publication.
        """
        return self._annee

    def _set_annee(self, annee: int) -> None:
        """
        Modifie l'année de publication après validation.

        :param annee: Nouvelle année de publication.
        :return: None
        :raise ValueError: Si l'année est négative.
        """
        if annee < 0:
            raise ValueError("L'année de publication ne peut pas être négative.")
        self._annee = annee

    def _get_num_piste(self) -> int:
        """
        Retourne le numéro de la piste.

        :return: Numéro de la piste.
        """
        return self._num_piste

    def _set_num_piste(self, num_piste: int) -> None:
        """
        Modifie le numéro de la piste après validation.

        :param num_piste: Nouveau numéro de la piste.
        :return: None

        :raise ValueError: Si le numéro de piste est inférieur ou égal à zéro.
        """
        if num_piste < 1:
            raise ValueError("Le numéro de piste doit être supérieur ou égal à 1.")
        self._num_piste = num_piste

    def _get_duree(self) -> float|int:
        """
        Retourne la durée du fichier audio.

        :return: Durée du fichier audio.
        """
        return self._duree

    def _set_duree(self, duree: float|int) -> None:
        """
        Modifie la durée du fichier audio après validation.

        :param duree: Nouvelle durée du fichier audio.
        :return: None

        :raise ValueError: Si la durée est inférieure ou égale à zéro.
        """
        if duree < 0:
            raise ValueError("La durée ne peut pas être négative.")
        self._duree = duree

    def _get_artiste_album(self) -> str:
        """
        Retourne le nom de l'artiste de l'album.

        :return: Nom de l'artiste de l'album.
        """
        return self._artiste_album

    def _set_artiste_album(self, artiste_album: str) -> None:
        """
        Modifie le nom de l'artiste de l'album après validation.

        :param artiste_album: Nouveau nom de l'artiste de l'album.
        :return: None

        :raise ValueError: Si le nom de l'artiste de l'album est vide.
        """
        if not artiste_album:
            raise ValueError("L'artiste de album est incorrect")
        self._artiste_album = artiste_album

    def _get_compositeur(self) -> str:
        """
        Retourne le nom du compositeur.

        :return: Nom du compositeur.
        """
        return self._compositeur

    def _set_compositeur(self, compositeur: str) -> None:
        """
        Modifie le nom du compositeur après validation.

        :param compositeur: Nouveau nom du compositeur.
        :return: None

        :raise ValueError: Si le nom du compositeur est vide.
        """
        if not compositeur:
            raise ValueError("Le compositeur est incorrect")
        self._compositeur = compositeur

    # Définition des propriétés
    titre: property = property(_get_titre, _set_titre)
    artiste: property = property(_get_artiste, _set_artiste)
    album: property = property(_get_album, _set_album)
    genre: property = property(_get_genre, _set_genre)
    annee: property = property(_get_annee, _set_annee)
    num_piste: property = property(_get_num_piste, _set_num_piste)
    duree: property = property(_get_duree, _set_duree)
    artiste_album: property = property(_get_artiste_album, _set_artiste_album)
    compositeur:property = property(_get_compositeur, _set_compositeur)