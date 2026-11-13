"""
Module : test_playlist_reelle.py

Description :
    Génère une playlist XSPF à partir de vrais fichiers audio.
    Utilise le dossier musique_test/ s'il existe (démo locale),
    sinon utilise src/tests_auto/ (fichiers de test versionnés).

    Le chemin du dossier est résolu via la fonction
    trouver_dossier_musique() du module config.

Historique des versions :
    - 1.0 : Création du module avec fallback local.
    - 1.1 : Ajout de la fonction _trouver_dossier_musique() locale.
    - 1.2 : Utilisation de trouver_dossier_musique() du module config
            pour centraliser la résolution des chemins

Auteur : Nassim BERRANDOU
Version : 1.2
"""

from pathlib import Path

from library.traitement.PlaylistAudioXSPFBuilder import PlaylistAudioXSPFBuilder
from library.traitement.SerialiseurXSPF import SerialiseurXSPF

from config import NOM_PLAYLIST_DEFAUT
from config import trouver_dossier_musique



def test_playlist_reelle() -> None:
    """Génère une playlist XSPF à partir des fichiers audio disponibles."""
    dossier = trouver_dossier_musique()

    print(f"Dossier utilisé : {dossier}")

    if not dossier.is_dir():
        print(f"Le dossier {dossier} n'existe pas.")
        return

    builder = PlaylistAudioXSPFBuilder(
        dossier, "Ma playlist réelle", NOM_PLAYLIST_DEFAUT
    )
    playlist = builder.construire()

    if playlist.nombre_pistes == 0:
        print(f"Aucun fichier audio trouvé dans {dossier}/")
        return

    chemin_sortie = Path(NOM_PLAYLIST_DEFAUT)
    SerialiseurXSPF().serialiser(playlist, chemin_sortie)

    print(f"\nPlaylist générée : {chemin_sortie}")
    print(f"Nombre de pistes : {playlist.nombre_pistes}")
    print(f"Durée totale    : {playlist.duree_totale:.1f} sec\n")
    print("=== Contenu ===")
    print(chemin_sortie.read_text(encoding="utf-8"))


if __name__ == "__main__":
    test_playlist_reelle()
