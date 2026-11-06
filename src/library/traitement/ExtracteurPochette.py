from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from src.library.donnees.PochettePiste import PochettePiste

"""!
@brief Extraction des pochettes des fichiers MP3 et FLAC.
@details Récupère la première image intégrée au fichier audio
à l'aide de la bibliothèque Mutagen
@version 2.1
@date 05/11/2026
@author Menaouer Ammari
"""
class ExtracteurPochetteAudio:
    """!
    @brief Extrait la pochette d'un fichier audio MP3 ou FLAC
    @param chemin_fichier Chemin du fichier audio
    @return Objet PochettePiste si une image est trouvée, sinon None
    @throws FileNotFoundError Si le fichier est introuvable
    """
    def extraire(self, chemin_fichier: str) -> PochettePiste | None:

        fichier = Path(chemin_fichier)
        if not fichier.is_file():
            raise FileNotFoundError("Fichier introuvable")
        extension = fichier.suffix.lower()
        # Cas d'un fichier mp3
        if extension == ".mp3":
            audio = MP3(str(fichier))
            if audio.tags is None:
                return None
            images = audio.tags.getall("APIC")
        # Cas d'un fichier flac

        elif extension == ".flac":
            audio = FLAC(str(fichier))
            images = audio.pictures
        else:
            return None

        # Vérifier si le fichier possède une image
        if len(images) == 0:
            return None
        # Récupérer la première image

        image = images[0]
        if not image.data or not image.mime:
            return None
        if image.mime == "-->":
            return None
        # Créer l'objet pochette
        pochette = PochettePiste(donnees=image.data,format_pochette=image.mime)
        return pochette

