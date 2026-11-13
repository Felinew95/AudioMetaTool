"""
Module : test_lecteur_audio.py

Description :
    Ce module permet de tester la classe LecteurAudio en sélectionnant
    aléatoirement un fichier audio parmi ceux trouvés dans le dossier
    de musique résolu (musique_test/ ou src/tests_auto/).

    La lecture est lancée dans un thread séparé via la méthode start(),
    afin de ne pas bloquer le programme principal. L'utilisateur peut
    appuyer sur Entrée pour arrêter la lecture à tout moment.

Historique des versions :
    - 1.0 : Création du module de test.
    - 1.1 : Utilisation de trouver_dossier_musique() pour résoudre le
            chemin des fichiers audio.
    - 1.2 : Sélection dynamique d'un fichier audio présent dans le dossier
            résolu, au lieu d'utiliser une liste fixe de noms de fichiers.
    - 1.3 : Lancement de la lecture dans un thread séparé via start(),
            avec arrêt contrôlé par la touche Entrée.

Auteurs : Alexandre BURIN, Nassim BERRANDOU
Version : 1.4
"""

# Importation des modules
from pathlib import Path
from random import choice

from library.traitement.LecteurAudio import LecteurAudio

from src.config import (
    EXTENSIONS_AUTORISES,
    TIMEOUT_ARRET_AUDIO,
    trouver_dossier_musique,
)

def _lister_fichiers_audio(dossier: Path) -> list[Path]:
    """
    Liste les fichiers audio d'un dossier (non récursif).

    :param dossier: Dossier à parcourir.
    :return: Liste des chemins des fichiers audio trouvés.
    """
    return [
        f
        for f in dossier.iterdir()
        if f.is_file() and f.suffix.lower() in EXTENSIONS_AUTORISES
    ]


def test_lecteur_audio() -> None:
    """
    Teste la lecture d'un fichier audio à l'aide de la classe LecteurAudio.

    Sélectionne aléatoirement un fichier audio présent dans le dossier
    résolu, lance sa lecture dans un thread séparé, puis attend que
    l'utilisateur appuie sur Entrée pour arrêter la lecture.

    :return: None
    """
    # Résolution du dossier de musique
    dossier_audio = trouver_dossier_musique()

    # Liste des fichiers audio disponibles
    fichiers = _lister_fichiers_audio(dossier_audio)

    if not fichiers:
        print(f"Aucun fichier audio trouvé dans {dossier_audio}/")
        return

    # Choix aléatoire d'un fichier audio
    fichier_test = choice(fichiers)
    print(f"Fichier lu : {fichier_test}")

    # Lecture du fichier audio dans un thread séparé
    lecteur = LecteurAudio(fichier=str(fichier_test))
    lecteur.start()

    # Attente de l'utilisateur pour arrêter la lecture
    input("Appuyez sur Entrée pour arrêter la lecture...\n")

    # Arrêt de la lecture
    lecteur.arreter()
    lecteur.join(timeout=TIMEOUT_ARRET_AUDIO)

    print("Lecture arrêtée.")

# Lancement du programme
if __name__ == "__main__":
    test_lecteur_audio()
