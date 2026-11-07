"""
Module : LecteurAudio.py

Description :
    Ce module définit la classe LecteurAudio permettant de gérer
    la lecture de fichiers audio à l'aide de la bibliothèque Pygame.

    Il permet de démarrer, mettre en pause, reprendre et arrêter
    la lecture d'un fichier audio.

Dépendance :
    - pygame

Historique des versions :
    - 1.0 : Création de la classe LecteurAudio.
    - 1.1 : Ajout de l'attribut fichier et du rafraîchissement
            de la boucle de lecture.
    - 1.2 : Ajout du threading pour permettre l'exécution
            de la lecture audio dans un thread séparé.

Auteurs : Menaouer Ammari, Alexandre Burin
Version : 1.2
"""

# Importation des modules
import pygame

from threading import Thread
from pygame.time import Clock
from src.config import FREQUENCE_RAFRAICHISSEMENT


class LecteurAudio(Thread):
    """
    Classe permettant de gérer la lecture de fichiers audio.

    Elle permet de charger et lire un fichier audio, de mettre en pause
    la lecture, de la reprendre et de l'arrêter à l'aide de la bibliothèque
    pygame.

    :pre: La bibliothèque pygame doit être installée.
    :pre: Le fichier audio doit être accessible et dans un format pris en charge.
    """

    def __init__(self, fichier: str) -> None:
        """
        Initialise le lecteur audio et configure le mixer de pygame.

        :param fichier (str): Chemin vers le fichier audio à lire.
        :return: Aucun retour.
        """
        super().__init__()
        self._fichier: str = fichier

        # Initialisation du mixer audio
        pygame.mixer.init()

    def run(self) -> None:
        """
        Démarre l'exécution du thread et lance la lecture audio.

        :return: Aucun retour.
        :rtype: None
        """
        self.lire()

    def lire(self) -> None:
        """
        Charge et démarre la lecture du fichier audio.

        La méthode maintient le programme en attente tant que la lecture
        est en cours, avec un rafraîchissement limité à 10 itérations
        par seconde.

        :return: Aucun retour.
        """
        # Initialisation de la lecture
        pygame.mixer.music.load(self._fichier)
        pygame.mixer.music.play()

        # Lecture du fichier
        horloge: Clock = Clock()
        while pygame.mixer.music.get_busy():
            # Rafraichissement de la lecture
            horloge.tick(FREQUENCE_RAFRAICHISSEMENT)

    def pause(self) -> None:
        """
        Met en pause la lecture du fichier audio.

        :return: Aucun retour.
        """
        pygame.mixer.music.pause()

    def reprendre(self) -> None:
        """
        Reprend la lecture du fichier audio après une mise en pause.

        :return: Aucun retour.
        """
        pygame.mixer.music.unpause()

    def arreter(self) -> None:
        """
        Arrête définitivement la lecture du fichier audio en cours.

        :return: Aucun retour.
        """
        pygame.mixer.music.stop()
