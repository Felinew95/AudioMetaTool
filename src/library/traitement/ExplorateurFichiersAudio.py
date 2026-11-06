from pathlib import Path

"""!
@brief Classe permettant d'explorer récursivement les fichiers audio
d'un dossier et de ses sous-dossiers
@version 2.1
@date 05/11/2026
@author Menaouer Ammari
"""

class ExplorateurFichiersAudio:

    def __init__(self, dossier: str):
        self._dossier = Path(dossier)
        self._extensions = {".mp3", ".flac"}

    """!
    @brief Recherche récursivement les fichiers audio dans un dossier et ses sous-dossiers
    @return Liste des chemins des fichiers audio trouvés.
    @throws NotADirectoryError Si le dossier est introuvable.
    """
    def rechercher_fichiers(self) -> list[str]:

        if not self._dossier.is_dir():
            raise NotADirectoryError("Le dossier est introuvable")

        fichiers_audio = []
        self.parcourir(self._dossier, fichiers_audio)

        return fichiers_audio

    """!
    @brief Parcourt récursivement un dossier et ses sous-dossiers.
    @details Identifie les fichiers audio selon leur extension et ignore les liens symboliques.
    @param dossier Chemin du dossier à explorer.
    @param fichiers_audio Liste dans laquelle sont ajoutés les fichiers audio trouvés.
    """
    def parcourir(self, dossier: Path, fichiers_audio: list[str]) -> None:
        for element in dossier.iterdir():
            if element.is_symlink():
                continue

            # Explorer les sous-dossiers
            if element.is_dir():
                self.parcourir(element, fichiers_audio)
            # Vérifier les fichiers
            elif element.is_file():
                extension = element.suffix.lower()

                if extension in self._extensions:
                    fichiers_audio.append(str(element))
