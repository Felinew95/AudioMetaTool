"""
Module : test_playlist_reelle.py

Description :
    Génère une playlist XSPF à partir de vrais fichiers audio.
    Utilise le dossier musique_test/ s'il existe (démo locale),
    sinon utilise src/tests_auto/ (fichiers de test versionnés).

Auteur : Nassim BERRANDOU
Version : 1.2
"""

from pathlib import Path

from src.library.traitement import PlaylistAudioXSPFBuilder, SerialiseurXSPF


def _trouver_dossier_musique() -> Path:
    """
    Trouve le dossier contenant les fichiers audio à utiliser.

    Priorité :
        1. musique_test/ (démo locale avec vrais morceaux)
        2. src/tests_auto/ (fichiers de test versionnés)

    :return: Chemin du dossier à explorer.
    """
    if Path("musique_test").is_dir():
        return Path("musique_test")
    return Path("src/tests_auto")


def test_playlist_reelle() -> None:
    """Génère une playlist XSPF à partir des fichiers audio disponibles."""
    dossier = _trouver_dossier_musique()

    print(f"Dossier utilisé : {dossier}")

    if not dossier.is_dir():
        print(f"Le dossier {dossier} n'existe pas.")
        return

    builder = PlaylistAudioXSPFBuilder(
        dossier, "Ma playlist réelle", "default_playlist.xspf"
    )
    playlist = builder.construire()

    if playlist.nombre_pistes == 0:
        print(f"Aucun fichier audio trouvé dans {dossier}/")
        return

    chemin_sortie = Path("default_playlist.xspf")
    SerialiseurXSPF().serialiser(playlist, chemin_sortie)

    print(f"\nPlaylist générée : {chemin_sortie}")
    print(f"Nombre de pistes : {playlist.nombre_pistes}")
    print(f"Durée totale    : {playlist.duree_totale:.1f} sec\n")
    print("=== Contenu ===")
    print(chemin_sortie.read_text(encoding="utf-8"))


if __name__ == "__main__":
    test_playlist_reelle()
