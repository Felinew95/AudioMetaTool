"""
Module : test-lecteur-audio.py

Description :
    Ce module permet de tester la classe LecteurAudio en sélectionnant
    aléatoirement un fichier audio parmi plusieurs formats disponibles
    (FLAC et MP3), puis en démarrant sa lecture.

    La lecture est lancée à l'aide de la méthode start(), qui permet
    d'exécuter le lecteur audio dans un thread séparé.

Dépendances :
    - random : sélection aléatoire d'un fichier audio.
    - library : classe LecteurAudio.

Auteur : Alexandre BURIN
Version : 1.0
"""

# Importation des modules
from random import choice
from config import FICHIERS_AUDIO
from library import LecteurAudio

def test_lecteur_audio() -> None:
    """
    Teste la lecture d'un fichier audio à l'aide de la classe LecteurAudio.

    Sélectionne aléatoirement un fichier audio parmi ceux définis dans
    FICHIERS_AUDIO, puis démarre sa lecture dans un thread séparé.

    :return: None
    """
    # Choix du fichier audio
    fichier_test = choice(FICHIERS_AUDIO)

    # Lecture du fichier audio
    lecteur = LecteurAudio(fichier=fichier_test)
    lecteur.start()

# Lancement du programme
if __name__ == "__main__":
    test_lecteur_audio()