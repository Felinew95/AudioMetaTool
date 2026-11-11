"""
Module : test_demo_avancement.py

Description :
    Test de démonstration pour le point d'avancement du 13/11.

    Vérifie la chaîne complète du projet AudioMetaTool :
        1. Exploration d'un dossier (recherche MP3/FLAC)
        2. Extraction des métadonnées d'un fichier
        3. Construction d'une playlist
        4. Sérialisation au format XSPF

    Affiche un rapport synthétique avec le nombre de tests réussis.

Historique des versions :
    - 1.0 : Création du test de démonstration.
    - 1.1 : Utilisation de trouver_dossier_musique() du module config
            pour centraliser la résolution des chemins et supprimer la
            fonction locale _trouver_dossier() dupliquée

Auteur : Nassim BERRANDOU
Version : 1.1
"""

from pathlib import Path

from src.config import NOM_PLAYLIST_TEST_AVANCEMENT
from src.library.traitement import (
    ExplorateurAudio,
    PisteAudioBuilder,
    PlaylistAudioXSPFBuilder,
    SerialiseurXSPF,
)
from src.config import trouver_dossier_musique


def test_exploration() -> None:
    """Vérifie que l'exploration trouve des fichiers audio."""
    dossier = trouver_dossier_musique()
    explorateur = ExplorateurAudio(dossier)
    fichiers = explorateur.extraire_fichiers_musique()

    assert len(fichiers) > 0, "Aucun fichier audio trouvé"
    assert all(
        f.lower().endswith((".mp3", ".flac")) for f in fichiers
    ), "Extensions non conformes"
    print(f"  → {len(fichiers)} fichiers audio trouvés dans {dossier}/")


def test_extraction() -> None:
    """Vérifie l'extraction des métadonnées d'un fichier."""
    dossier = trouver_dossier_musique()
    fichiers = ExplorateurAudio(dossier).extraire_fichiers_musique()

    builder = PisteAudioBuilder()
    builder.fichier = Path(fichiers[0])
    piste = builder.construire()

    assert piste.metadonnees.titre, "Titre vide"
    assert piste.metadonnees.duree > 0, "Durée nulle"
    assert piste.chemin_fichier, "Chemin vide"
    print(
        f"  → Métadonnées extraites : {piste.metadonnees.titre} "
        f"({piste.metadonnees.duree:.1f} sec)"
    )


def test_playlist() -> None:
    """Vérifie la construction d'une playlist."""
    dossier = trouver_dossier_musique()
    builder = PlaylistAudioXSPFBuilder(dossier, "Test", "test.xspf")
    playlist = builder.construire()

    assert playlist.nombre_pistes > 0, "Playlist vide"
    assert playlist.duree_totale > 0, "Durée totale nulle"
    print(
        f"  → Playlist construite : {playlist.nombre_pistes} pistes, "
        f"{playlist.duree_totale:.1f} sec"
    )


def test_serialisation() -> None:
    """Vérifie la sérialisation XSPF et sa structure."""
    dossier = trouver_dossier_musique()
    builder = PlaylistAudioXSPFBuilder(dossier, "Test", NOM_PLAYLIST_TEST_AVANCEMENT)
    playlist = builder.construire()

    chemin = Path("playlist/test_demo.xspf")
    SerialiseurXSPF().serialiser(playlist, chemin)

    assert chemin.is_file(), "Fichier XSPF non créé"
    contenu = chemin.read_text(encoding="utf-8")
    assert 'xmlns="http://xspf.org/ns/0/"' in contenu, "Namespace manquant"
    assert "<trackList>" in contenu, "trackList manquant"
    assert (
        contenu.count("<track>") == playlist.nombre_pistes
    ), "Nombre de tracks incorrect"
    print(f"  → XSPF valide : {chemin}")


def run_demo() -> None:
    """Lance les 4 tests et affiche un rapport synthétique."""
    tests = [
        ("Exploration", test_exploration),
        ("Extraction métadonnées", test_extraction),
        ("Construction playlist", test_playlist),
        ("Sérialisation XSPF", test_serialisation),
    ]

    print("=" * 55)
    print("DÉMONSTRATION - AudioMetaTool (point d'avancement)")
    print("=" * 55)

    reussis = 0
    for nom, test in tests:
        print(f"\n[{nom}]")
        try:
            test()
            print(f"OK")
            reussis += 1
        except AssertionError as e:
            print(f"ÉCHEC : {e}")
        except Exception as e:
            print(f"ERREUR : {type(e).__name__} - {e}")

    print("\n" + "=" * 55)
    print(f"RÉSULTAT : {reussis}/{len(tests)} tests réussis")
    print("=" * 55)


# Lancement du programme
if __name__ == "__main__":
    run_demo()
