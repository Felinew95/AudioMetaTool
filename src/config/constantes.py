"""
Module : constantes.py

Description : Ce module centralise les constantes utilisées dans le projet
              AudioMetaTool, notamment les extensions des fichiers audio
              pris en charge et les fichiers utilisés pour les tests.

Historique des versions :
    - 1.0 : Création du module et définition des constantes initiales.

Auteur : Alexandre BURIN
Version : 1.0
"""

# Formats audio disponibles
EXTENSIONS_AUTORISES = (".mp3", ".flac")

# Fichiers disponibles pour le test du lecteur
FICHIERS_AUDIO = ["test_audio_2.flac", "test_audio.mp3"]

# Fréquence de rafraichissement du lecteur audio en Hz
FREQUENCE_RAFRAICHISSEMENT = 10