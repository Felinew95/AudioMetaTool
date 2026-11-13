"""
Module : outils.py

Description : Ce module regroupe des fonctions utilitaires indépendantes
              de la logique métier de l'application AudioMetaTool.

              Il fournit notamment des outils de conversion et de formatage
              des durées exprimées en heures, minutes et secondes.

Historique des versions :
    - 1.0 : Création du module et ajout de la fonction de conversion
            d'une durée en heures, minutes et secondes.

Auteur : Alexandre BURIN
Version : 1.0
"""

def convertir_duree(duree: float | int) -> tuple[int, int, int]:
    """
    Convertit une durée exprimée en secondes en heures, minutes et secondes.

    :param duree: Durée à convertir, exprimée en secondes.
    :return: Tuple contenant les heures, les minutes et les secondes.
    """
    heures: int = int(duree) // 3600
    reste: int = int(duree) % 3600
    minutes: int = reste // 60
    secondes: int = reste % 60

    return heures, minutes, secondes