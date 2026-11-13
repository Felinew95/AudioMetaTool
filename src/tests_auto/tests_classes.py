"""
Module : tests_classes.py

Description :
    Contient des fonctions permettant de créer des objets de test
    représentant des métadonnées audio, des pistes audio et des pochettes.

    Ces objets sont utilisés pour vérifier le fonctionnement des classes,
    notamment l'égalité et l'inégalité entre les objets.

Auteur : Alexandre BURIN
Version : 1.0
"""

# Importation des modules
import pandas as pd

from library.donnees.MetadonneesAudio import MetadonneesAudio
from library.donnees.PisteAudio import PisteAudio
from library.donnees.PlaylistAudioXSPF import PlaylistAudioXSPF
from library.donnees.PochettePiste import PochettePiste
from src.config import FICHIER_TEST_CLASSES

def creer_playlist_csv(fichier: str = FICHIER_TEST_CLASSES) -> PlaylistAudioXSPF:
    """
    Crée une playlist audio à partir des données d'un fichier CSV.

    Le fichier CSV est lu afin de créer les objets représentant les
    métadonnées, les pochettes et les pistes audio. Chaque piste créée
    est ensuite ajoutée à la playlist.

    Paramètres :
        :param fichier: Chemin du fichier CSV contenant les données
                        des pistes audio.
    Retour :
        :return PlaylistAudioXSPF : Playlist contenant les pistes créées à
                                    partir des données du fichier CSV.
    """
    # Création de la playlist
    p = PlaylistAudioXSPF(
        nom="Ma playlist",
        chemin_playlist="./ma_playlist.xspf",
    )

    # Lecture des données et création des objets
    df = pd.read_csv(fichier, sep=",")

    for index, row in df.iterrows():
        # Création des méta-données
        metas = MetadonneesAudio(
            titre=row["titre"],
            artiste=row["artiste"],
            album=row["album"],
            genre=row["genre"],
            annee=int(row["annee"]),
            num_piste=int(row["num_piste"]),
            duree=float(row["duree"]),
            artiste_album=row["artiste_album"],
            compositeur=row["compositeur"],
        )

        # Création de la pochette
        pochette = PochettePiste(
            donnees=bytes(row["donnees"], encoding="utf-8"),
            format_pochette=row["format_pochette"],
        )

        # Création de la piste audio
        piste = PisteAudio(
            chemin_fichier=row["chemin_fichier"],
            taille=float(row["taille"]),
            metadonnees=metas,
            pochette=pochette,
        )

        # Ajout dans la playlist
        p.ajouter_piste(piste=piste)

    return p


def creation_3_pistes() -> tuple[
    MetadonneesAudio,
    MetadonneesAudio,
    MetadonneesAudio,
    PisteAudio,
    PisteAudio,
    PisteAudio,
    PochettePiste,
    PochettePiste,
    PochettePiste,
]:
    """
    Crée trois pistes audio avec leurs métadonnées et leurs pochettes.

    La première piste correspond à un morceau de jazz. Les deux autres
    représentent le même morceau de blues, afin de disposer d'objets
    identiques pour tester l'égalité et l'inégalité entre les objets.

    Retour :
        :return tuple : Contient, dans l'ordre, les trois objets MetadonneesAudio,
                        les trois objets PisteAudio et les trois objets PochettePiste.
    """
    # Création de la piste 1
    pochette_1 = PochettePiste(
        donnees=b"\xff\xd8\xff\xe0\x00\x10JFIF", format_pochette="image/jpeg"
    )

    metadonnees_1 = MetadonneesAudio(
        titre="Take Five",
        artiste="Dave Brubeck",
        album="Time Out",
        genre="Jazz",
        annee=1959,
        num_piste=3,
        duree=324.0,
        artiste_album="Dave Brubeck Quartet",
        compositeur="Paul Desmond",
    )

    piste_1 = PisteAudio(
        chemin_fichier="/music/jazz/take_five.mp3",
        taille=8.45,
        metadonnees=metadonnees_1,
        pochette=pochette_1,
    )

    # Création de la piste 2
    pochette_2 = PochettePiste(
        donnees=b"\x89PNG\r\n\x1a\n", format_pochette="image/png"
    )

    metadonnees_2 = MetadonneesAudio(
        titre="The Thrill Is Gone",
        artiste="B.B. King",
        album="Completely Well",
        genre="Blues",
        annee=1969,
        num_piste=1,
        duree=324.5,
        artiste_album="B.B. King",
        compositeur="Roy Hawkins, Rick Darnell",
    )

    piste_2 = PisteAudio(
        chemin_fichier="/music/blues/thrill_is_gone.flac",
        taille=24.12,
        metadonnees=metadonnees_2,
        pochette=pochette_2,
    )

    # Création de la piste 3
    pochette_3 = PochettePiste(
        donnees=b"\x89PNG\r\n\x1a\n", format_pochette="image/png"
    )

    metadonnees_3 = MetadonneesAudio(
        titre="The Thrill Is Gone",
        artiste="B.B. King",
        album="Completely Well",
        genre="Blues",
        annee=1969,
        num_piste=1,
        duree=324.5,
        artiste_album="B.B. King",
        compositeur="Roy Hawkins, Rick Darnell",
    )

    piste_3 = PisteAudio(
        chemin_fichier="/music/blues/thrill_is_gone.flac",
        taille=24.12,
        metadonnees=metadonnees_3,
        pochette=pochette_3,
    )
    return (
        metadonnees_1,
        metadonnees_2,
        metadonnees_3,
        piste_1,
        piste_2,
        piste_3,
        pochette_1,
        pochette_2,
        pochette_3,
    )


def test_pistes() -> None:
    """
    Vérifie l'égalité et l'inégalité des objets représentant les pistes audio.

    Les tests comparent les pochettes, les métadonnées et les pistes audio
    afin de vérifier que des objets de contenus différents sont considérés
    comme différents et que des objets de contenus identiques sont considérés
    comme égaux.
    """
    (
        metadonnees_1,
        metadonnees_2,
        metadonnees_3,
        piste_1,
        piste_2,
        piste_3,
        pochette_1,
        pochette_2,
        pochette_3,
    ) = creation_3_pistes()

    assert pochette_1 != pochette_2, "Les pochettes devraient être différentes"
    assert metadonnees_1 != metadonnees_2, "Les métadonnées devraient être différentes"
    assert piste_1 != piste_2, "Les pistes devraient être différentes"

    assert pochette_2 == pochette_3, "Les pochettes devraient être égales"
    assert metadonnees_2 == metadonnees_3, "Les métadonnées devraient être égales"
    assert piste_2 == piste_3, "Les pistes devraient être égales"


def test_playlist(p: PlaylistAudioXSPF) -> None:
    """
    Vérifie la cohérence des informations de la playlist.

    Paramètres :
        :param p : Playlist à tester.

    Retour :
        :return : None. Rien à retourner
    """
    # Vérification du nombre de pistes
    assert p.nombre_pistes == len(p.pistes)

    # Vérification de la durée totale
    pistes = p.pistes
    duree = 0

    for piste in pistes:
        duree += piste.metadonnees.duree

    assert abs(p.duree_totale - duree) < 1e-9


# Lancement du programme
if __name__ == "__main__":
    # Création de la playlist
    playlist = creer_playlist_csv()

    # Affichage de la playlist
    print(playlist)

    try:
        # Tests sur les pistes
        test_pistes()

        # Tests sur les playlists
        test_playlist(playlist)
    except AssertionError as e:
        print(e)
