from pathlib import Path
from mutagen import File
from src.library.donnees.MetadonneesAudio import MetadonneesAudio

"""!
@brief Classe permettant d'extraire les métadonnées des fichiers audio
@details Utilise la bibliothèque Mutagen pour récupérer les informations
des fichiers audio et les stocker dans un objet MetadonneesAudio
@version 2.1
@date 05/11/2026
@author Menaouer Ammari
"""
class ExtracteurMetadonnees:
    """!
    @brief Extrait les métadonnées d'un fichier audio
    @details Récupère le titre, l'artiste, l'album, le genre,
    l'année, le numéro de piste, la durée et les autres informations
    @param chemin_fichier Chemin du fichier audio à analyser
    @return Objet MetadonneesAudio contenant les informations extraites
    @throws FileNotFoundError Si le fichier est introuvable
    @throws ValueError Si le format audio n'est pas reconnu
    """
    def extracteur_metadonnees(self, chemin_fichier: str) -> MetadonneesAudio:

        fichier = Path(chemin_fichier)
        if not fichier.is_file():
            raise FileNotFoundError(f"Fichier {fichier} n'existe pas")

        # Ouvrir le fichier audio
        audio = File(str(fichier), easy=True)
        if audio is None:
            raise ValueError(f"Format audio non reconnu : {fichier}")

        # Récupérer les métadonnées
        tags = audio.tags or {}

        titre = self.lire_tag(tags, "title", fichier.stem)
        artiste = self.lire_tag(tags, "artist", "Inconnu")
        album = self.lire_tag(tags, "album", "Inconnu")
        genre = self.lire_tag(tags, "genre", "Inconnu")
        date = self.lire_tag(tags, "date", "0")
        numero = self.lire_tag(tags, "tracknumber", "1")
        artiste_album = self.lire_tag(tags, "albumartist", artiste)
        compositeur = self.lire_tag(tags, "composer", "Inconnu")

        # Convertir l'année
        try:
            annee = int(date[:4])
        except ValueError:
            annee = 0

        # Convertir le numéro de piste
        try:
            num_piste = int(numero.split("/")[0])
            num_piste = max(1, num_piste)
        except ValueError:
            num_piste = 1

        # Récupérer la durée
        duree = audio.info.length

        # Construire l'objet métadonnées
        metadonnees = MetadonneesAudio(
            titre=titre,
            artiste=artiste,
            album=album,
            genre=genre,
            annee=annee,
            num_piste=num_piste,
            duree=duree,
            artiste_album=artiste_album,
            compositeur=compositeur
        )

        return metadonnees

    """!
    @brief Récupère la valeur d'un tag audio
    @param tags Ensemble des métadonnées du fichier
    @param nom Nom du tag recherché
    @param defaut Valeur utilisée si le tag est absent
    @return Valeur du tag ou valeur par défaut
    """
    def lire_tag(self, tags, nom: str, defaut: str) -> str:

        valeurs = tags.get(nom)

        if valeurs:
            return str(valeurs[0])

        return defaut
