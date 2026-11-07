"""
Module : test_serialisation_xspf.py

Description :
    Ce module permet de tester le fonctionnement de la classe SerialiseurXSPF
    en générant un fichier XSPF à partir des données de test contenues dans
    le fichier CSV tests_classes.csv.

    Le fichier généré peut ensuite être validé sur le site officiel
    https://validator.xspf.org/ pour vérifier sa conformité.

Historique des versions :
    - 1.0 : Création du module de test pour la sérialisation XSPF.

Auteur : Nassim BERRANDOU
Version : 1.0
"""

# Importation des modules
from pathlib import Path

from src.library.traitement import SerialiseurXSPF
from src.tests_auto.tests_classes import creer_playlist_csv


def test_serialisation_xspf() -> None:
    """
    Teste la sérialisation d'une playlist au format XSPF.

    Charge une playlist de test à partir du fichier CSV, la sérialise
    dans un fichier XSPF, puis affiche le contenu généré pour permettre
    sa validation manuelle sur https://validator.xspf.org/.

    :return: None. Aucune valeur n'est retournée.
    """
    # Création de la playlist de test à partir du CSV
    playlist = creer_playlist_csv("src/tests_auto/tests_classes.csv")

    # Sérialisation vers un fichier XSPF
    chemin_sortie = Path("src/tests_auto/test_playlist.xspf")
    serialiseur = SerialiseurXSPF()
    serialiseur.serialiser(playlist, chemin_sortie)

    # Affichage du résultat
    print(f"\nPlaylist générée : {chemin_sortie}")
    print(f"Nombre de pistes : {playlist.nombre_pistes}")
    print(f"Durée totale    : {playlist.duree_totale:.1f} sec\n")

    # Affichage du contenu du fichier
    print("=== Contenu du fichier XSPF ===")
    print(chemin_sortie.read_text(encoding="utf-8"))


# Lancement du programme
if __name__ == "__main__":
    test_serialisation_xspf()
