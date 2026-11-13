"""
Module : SerialiseurXSPF.py

Description :
    Ce module définit la classe SerialiseurXSPF, qui permet de transformer
    une playlist audio (objet PlaylistAudioXSPF) en fichier XML au format
    XSPF (XML Shareable Playlist Format), conformément à la spécification
    disponible à l'adresse https://xspf.org/.

    Le sérialiseur construit un arbre XML respectant le namespace officiel
    du format XSPF et écrit le résultat sur le disque en encodage UTF-8.

    Les informations suivantes sont sérialisées pour chaque piste :
        - la localisation du fichier audio (URI file:///...)
        - le titre, l'artiste (creator), l'album
        - la durée en millisecondes (exigence du format XSPF)

Historique des versions :
    - 1.0 : Création de la classe SerialiseurXSPF permettant de générer
            un fichier XSPF valide à partir d'une PlaylistAudioXSPF.

Auteur : Nassim BERRANDOU
Version : 1.0
"""

# Importation des modules
import xml.etree.ElementTree as ET
from pathlib import Path

from library.donnees.PisteAudio import PisteAudio
from library.donnees.PlaylistAudioXSPF import PlaylistAudioXSPF


class SerialiseurXSPF:
    """
    Sérialise une playlist audio au format XSPF.

    La classe transforme un objet PlaylistAudioXSPF en un fichier XML
    respectant le namespace officiel du format XSPF. Elle gère la
    conversion des chemins d'accès en URI et la conversion des durées
    en millisecondes.

    :pre: La playlist doit contenir au moins une piste pour être valide
          au sens du validateur en ligne https://validator.xspf.org/.
    """

    # Namespace officiel du format XSPF
    NAMESPACE: str = "http://xspf.org/ns/0/"

    def __init__(self) -> None:
        """
        Initialise le sérialiseur XSPF.

        :return: Aucun retour.
        """
        # Enregistrement du namespace par défaut pour éviter le préfixe ns0:
        ET.register_namespace("", self.NAMESPACE)

    def serialiser(
        self, playlist: PlaylistAudioXSPF, chemin_fichier: str | Path
    ) -> None:
        """
        Sérialise une playlist audio dans un fichier XSPF.

        Construit l'arbre XML correspondant à la playlist, puis l'écrit
        sur le disque au chemin spécifié, en encodage UTF-8.

        :param playlist: Playlist audio à sérialiser.
        :param chemin_fichier: Chemin de destination du fichier XSPF
                               (str ou Path).
        :return: None. Aucune valeur n'est retournée.
        :raises ValueError: Si la playlist est vide.
        :raises OSError: Si l'écriture du fichier échoue (permission,
                         disque plein, chemin invalide, etc.).
        """
        # Vérification que la playlist contient au moins une piste
        if playlist.nombre_pistes == 0:
            raise ValueError("La playlist est vide et ne peut pas être sérialisée.")

        # Construction arbre XML
        arbre: ET.ElementTree = self._construire_arbre(playlist)

        # Ecriture du fichier
        self._ecrire_fichier(arbre, Path(chemin_fichier))

    def _construire_arbre(self, playlist: PlaylistAudioXSPF) -> ET.ElementTree:
        """
        Construit l'arbre XML correspondant à la playlist audio.

        :param playlist: Playlist audio à transformer en arbre XML.
        :return: Arbre XML (ElementTree) représentant la playlist.
        """
        # Création de l'élément racine <playlist> avec le namespace
        racine = ET.Element(f"{{{self.NAMESPACE}}}playlist", attrib={"version": "1"})

        # Ajout du titre de la playlist
        titre = ET.SubElement(racine, f"{{{self.NAMESPACE}}}title")
        titre.text = playlist.nom

        # Création de la liste des pistes
        liste_pistes = ET.SubElement(racine, f"{{{self.NAMESPACE}}}trackList")

        # Ajout de chaque piste
        for piste in playlist.pistes:
            self._ajouter_piste(liste_pistes, piste)

        # Retourne l'arbre complet
        return ET.ElementTree(racine)

    def _ajouter_piste(self, parent: ET.Element, piste: PisteAudio) -> None:
        """
        Ajoute une piste audio à l'arbre XML.

        L'élément créé contient les métadonnées principales de la piste :
        localisation, titre, artiste (creator), album et durée.

        :param parent: Élément parent <trackList> auquel ajouter la piste.
        :param piste: Piste audio à sérialiser.
        :return: None. Aucune valeur n'est retournée.
        """

        # Création de l'élément <track> pour la piste
        track: ET.Element = ET.SubElement(parent, f"{{{self.NAMESPACE}}}track")

        # Localisation du fichier audio (URI)
        location: ET.Element = ET.SubElement(track, f"{{{self.NAMESPACE}}}location")
        location.text = self._chemin_uri(piste.chemin_fichier)

        # Titre de la piste
        titre: ET.Element = ET.SubElement(track, f"{{{self.NAMESPACE}}}title")
        titre.text = piste.metadonnees.titre

        # Artiste (creator en XSPF)
        creator: ET.Element = ET.SubElement(track, f"{{{self.NAMESPACE}}}creator")
        creator.text = piste.metadonnees.artiste

        # Album de la piste
        album: ET.Element = ET.SubElement(track, f"{{{self.NAMESPACE}}}album")
        album.text = piste.metadonnees.album

        # Durée en millisecondes (exigence XSPF)
        duree: ET.Element = ET.SubElement(track, f"{{{self.NAMESPACE}}}duration")
        duree.text = str(int(piste.metadonnees.duree * 1000))  # Conversion en ms

    def _chemin_uri(self, chemin: str) -> str:
        """
        Convertit un chemin d'accès en URI conforme au format XSPF.

        Le format XSPF impose que la localisation d'une piste soit une URI absolue.
        Cette méthode convertit un chemin local (ex : C:\\Musique\\chanson.mp3) en URI (ex : file:///C:/Musique/chanson.mp3).

        :param chemin: Chemin d'accès local du fichier audio.
        :return: URI correspondante au chemin d'accès.
        """
        return Path(chemin).resolve().as_uri()

    def _ecrire_fichier(self, arbre: ET.ElementTree, chemin: Path) -> None:
        """
        Écrit l'arbre XML sur le disque au chemin spécifié.

        Le fichier est écrit en encodage UTF-8 avec une indentation
        de deux espaces pour améliorer la lisibilité. La déclaration
        XML est ajoutée automatiquement.

        :param arbre: Arbre XML à écrire.
        :param chemin: Chemin de destination du fichier.
        :return: None. Aucune valeur n'est retournée.
        :raises OSError: Si l'écriture du fichier échoue.
        """
        # Indentation de l'arbre pour lisibilité
        ET.indent(arbre, space="  ")

        # Création des dossiers parents si nécessaire
        chemin.parent.mkdir(parents=True, exist_ok=True)

        # Écriture du fichier XML en UTF-8
        arbre.write(chemin, encoding="utf-8", xml_declaration=True)
