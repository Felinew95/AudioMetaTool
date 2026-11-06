from pathlib import Path
from typing import List
from mutagen import MutagenError
from src.library.donnees.PisteAudio import PisteAudio
from src.library.application.ExplorateurFichiersAudio import ExplorateurFichiersAudio
from src.library.application.ExtracteurMetadonneesAudio import ExtracteurMetadonnees
from src.library.application.ExtracteurPochette import ExtracteurPochetteAudio

"""!
@brief Classe chargée du traitement des fichiers audio.
@details Récupère les fichiers audio, extrait leurs métadonnées
et leurs pochettes, puis crée les objets PisteAudio.
@version 1.1
@date 05/11/2026
@author Menaouer Ammari
"""
class TraitementAudio:

    def __init__(self, dossier: Path) -> None:
        self._explorateur = ExplorateurFichiersAudio(dossier)
        self._metadonnees = ExtracteurMetadonnees()
        self._pochettes = ExtracteurPochetteAudio()

    """!
    @brief Initialise les différents outils de traitement audio.
    @param dossier Chemin du dossier contenant les fichiers audio.
    """
    def traitements_audio(self) -> List[PisteAudio]:
        pistes = []
        fichiers_audio = self._explorateur.rechercher_fichiers()

        for fichier_audio in fichiers_audio:
            try:
                # Extraction des métadonnées
                metadonnees = self._metadonnees.extracteur_metadonnees(fichier_audio)

                # Extraction de la pochette
                pochette = self._pochettes.extraire(fichier_audio)
                # Création de la piste
                piste = PisteAudio(chemin_fichier=fichier_audio,metadonnees=metadonnees,pochette=pochette)
                pistes.append(piste)

            except (OSError, ValueError, MutagenError) as error:
                print("Erreur avec le fichier :", fichier_audio)
                print(error)

        return pistes
