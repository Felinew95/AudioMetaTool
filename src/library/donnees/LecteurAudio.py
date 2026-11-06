import pygame
"""!
@brief Classe permettant de gérer la lecture des fichiers audio
Elle permet de lire, mettre en pause, reprendre et arrêter
la lecture d'un fichier audio à l'aide de pygame
@note Nécessite l'installation de la bibliothèque pygame
@version 2.1
@date 06/11/2026
@author Menaouer Ammari
"""
class LecteurAudio:

    def __init__(self):
        pygame.mixer.init()

    """!
    @brief Charge et lance la lecture d'un fichier audio.
    @param fichier_audio Chemin du fichier audio à lire.
    """
    def lire(self, fichier_audio: str):
        pygame.mixer.music.load(fichier_audio)
        pygame.mixer.music.play()

    """!
    @brief Arrête la lecture audio.
    """
    def pause(self):
        pygame.mixer.music.pause()

    """!
       @brief Arrête la lecture audio.
       """
    def reprendre(self):
        pygame.mixer.music.unpause()

    """!
    @brief Arrête la lecture audio.
    """
    def arreter(self):
        pygame.mixer.music.stop()