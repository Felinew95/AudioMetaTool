"""
Module : cli.py

Description : Ce module définit la classe InterfaceCLI permettant
              d'utiliser AudioMetaTool en mode console.
              Elle permet d'extraire les métadonnées d'un fichier audio,
              d'explorer un dossier, de construire et sauvegarder une
              playlist XSPF et de lire les pistes audio.

Historique des versions :
    - 1.0 : Création de l'interface en ligne de commande.
    - 1.1 : Séparation des fonctionnalités en méthodes et ajout
            de la documentation.
    - 1.2 : Centralisation de la vérification des extensions des fichiers
            et amélioration de la gestion des arguments et des commandes.

Auteurs : Burin Alexandre, Ammari Menaouer
Version : 1.2
"""

# Importation des modules
import sys
from pathlib import Path

from argparse import ArgumentParser, Namespace, RawDescriptionHelpFormatter

from config.constantes import NOM_PLAYLIST_DEFAUT, CHEMIN_PLAYLIST_DEFAUT, DOSSIER_PLAYLIST_DEFAUT, \
    EXTENSIONS_AUTORISES, FICHIER_EXEMPLE_GUI, FICHIER_DESCRIPTION_CLI, TIMEOUT_LECTURE_AUDIO
from library.utilitaires.outils import lire_fichier
from src.library.donnees.PisteAudio import PisteAudio
from src.library.donnees.PlaylistAudioXSPF import PlaylistAudioXSPF
from src.library.traitement.LecteurAudio import LecteurAudio
from src.library.traitement.SerialiseurXSPF import SerialiseurXSPF
from src.library.traitement.PisteAudioBuilder import PisteAudioBuilder
from src.library.traitement.PlaylistAudioXSPFBuilder import PlaylistAudioXSPFBuilder

class InterfaceCLI:
    """
    Gère l'interface utilisateur en ligne de commandes.

    Cette classe permet d'analyser des fichiers audio, d'explorer des
    dossiers, de lire des fichiers audio et de modifier leurs tags
    à partir d'arguments fournis dans le terminal.
    """

    def __init__(self) -> None:
        """
        Initialise l'interface en ligne de commandes.

        Configure le parseur d'arguments, initialise les builders
        nécessaires à l'analyse audio et à la création de playlists,
        puis définit les arguments disponibles.

        :return: None
        """
        # Initialisation du parseur
        self._parser: ArgumentParser = ArgumentParser(
            description=lire_fichier(str(FICHIER_DESCRIPTION_CLI)),
            formatter_class=RawDescriptionHelpFormatter,
            epilog = lire_fichier(str(FICHIER_EXEMPLE_GUI))
        )

        # Initialisation des builders
        self._builderPisteAudio: PisteAudioBuilder = PisteAudioBuilder()
        self._builderPlaylist: PlaylistAudioXSPFBuilder = PlaylistAudioXSPFBuilder(
            nom=NOM_PLAYLIST_DEFAUT,
            chemin_playlist=CHEMIN_PLAYLIST_DEFAUT,
            dossier=DOSSIER_PLAYLIST_DEFAUT
        )

        # Initialisation du lecteur
        self._lecteur: LecteurAudio

        # Initialise les arguments disponibles
        self._set_arguments()

    def _set_arguments(self) -> None:
        """
        Définit les arguments disponibles dans l'interface CLI.

        Configure les arguments permettant d'analyser un fichier audio,
        d'explorer un dossier, de lire un fichier ou de créer une playlist XSPF
        Les arguments principaux sont mutuellement exclusifs.

        :return: None
        """
        # Création d'un groupe d'arguments
        groupe = self._parser.add_mutually_exclusive_group(required=True)

        # Argument pour analyser un fichier audio
        groupe.add_argument("-f", "--file", type=Path,
                            help="Analyse un fichier audio de type MP3 ou FLAC")

        # Argument pour explorer un dossier et afficher les métadonnées des fichiers audio
        groupe.add_argument("-d", "--directory", type=Path,
                            help="Explorer un dossier et analyse les fichiers audios MP3 ou FLAC")

        # Argument pour la lecture d'un fichier audio ou d'une playlist
        groupe.add_argument("-p", "--play", type=Path,
                            help="Lire un fichier audio")

        # Argument pour créer une playlist au format XSPF
        self._parser.add_argument("-o", "--output", type=Path,
                                  help="Fichier de playlist XSPF de sortie")

    def _analyser(self, fichier: Path) -> None:
        """
        Affiche les métadonnées d'une piste audio.

        Utilise PisteAudioBuilder pour construire une piste audio à partir
        du fichier indiqué, puis affiche ses métadonnées.

        :param fichier: Chemin du fichier audio à analyser.
        :return: None
        """
        # Attribution du fichier en cours
        self._builderPisteAudio.fichier = fichier

        # Création de la piste audio avec les métadonnées
        piste: PisteAudio = self._builderPisteAudio.construire()

        # Affichage des métadonnées
        print(piste)

    def _explorer(self, dossier: Path, output: Path | None) -> None:
        """
        Explore un dossier et affiche les informations de la playlist créée.

        Utilise PlaylistAudioXSPFBuilder pour rechercher les fichiers audio
        et construire une playlist. Si un fichier de sortie est indiqué,
        on vérifie son extension puis enregistre la playlist au format XSPF
        si demandé.

        :param dossier: Chemin du dossier à explorer.
        :param output: Chemin du fichier XSPF de sortie, ou None si aucun
                       fichier ne doit être créé.
        :return: None
        :raises ValueError: Si le fichier de sortie ne possède pas
                            l'extension '.xspf'.
        """
        # Création de la playlist
        self._builderPlaylist.dossier = dossier

        # Vérification du fichier de sortie
        if output is not None:
            if output.suffix.lower() != ".xspf":
                raise ValueError("Extension .xspf obligatoire")
            self._builderPlaylist.nom = output.stem
            self._builderPlaylist.chemin_playlist = str(output)

        playlist: PlaylistAudioXSPF = self._builderPlaylist.construire()

        # Affichage de la playlist
        print(playlist)

        if output:
            # Enregistre la playlist
            SerialiseurXSPF().serialiser(playlist, output)
            print("Playlist enregistrée :", output.absolute())

    def _jouer(self, chemin: Path) -> None:
        """
        Lit un fichier audio.

        Initialise un lecteur audio à partir du chemin indiqué, démarre
        la lecture et attend sa fin. En cas d'interruption par l'utilisateur,
        arrête proprement la lecture et relance l'interruption.

        :param chemin: Chemin du fichier audio à lire.
        :return: None
        :raises KeyboardInterrupt: Si la lecture est interrompue par l'utilisateur.
        """
        # Affichage des métadonnées
        self._analyser(chemin)

        # Création du lecteur
        print("Lecture en cours...")
        self._lecteur = LecteurAudio(str(chemin))

        # Lancement de la lecture
        self._lecteur.start()

        try:
            # Joue la musique tant que le cœur est actif
            while self._lecteur.is_alive():
                # Attend au maximum 200 ms la fin du thread avant de vérifier son état.
                self._lecteur.join(TIMEOUT_LECTURE_AUDIO)
        except KeyboardInterrupt:
            self._lecteur.arreter()
            self._lecteur.join()
            raise

    def _verifier_extension_fichier(self, chemin: Path) -> None:
        """
        Vérifie que le chemin est bien un fichier et
        possède une extension audio autorisée.

        :param chemin: Chemin à vérifier.
        :return: None
        """
        if not chemin.exists():
            raise ValueError("Le chemin n'existe pas")
        if not chemin.is_file():
            raise ValueError("Le chemin indiqué n'est pas un fichier")

        extension_fichier = chemin.suffix.lower()
        if extension_fichier not in EXTENSIONS_AUTORISES:
            self._parser.error(f"Extension {extension_fichier} non valide (.mp3 et .flac sont valides)")

    def executer(self, arguments: list[str]|None = None) -> int:
        """
        Exécute la commande demandée à partir des arguments fournis.

        Analyse les arguments, vérifie leur validité puis appelle la méthode
        correspondant à l'opération demandée. Gère également les interruptions
        et les erreurs rencontrées pendant l'exécution.

        :param arguments: Liste des arguments à traiter. Si None, utilise
                          les arguments transmis au programme.
        :return: Code de retour de l'exécution (0 si succès, 1 si erreur,
                 130 si interruption).
        """

        # Arguments par défaut
        if arguments is None:
            arguments = sys.argv[1:]

        # Vérification d'au moins un argument
        if not arguments:
            self._parser.error(
                "Paramètres invalides. Utilisez -h pour afficher "
                "les aides du programme"
            )

        # Liste des arguments
        args: Namespace = self._parser.parse_args(arguments)

        try:
            if args.file:
                self._verifier_extension_fichier(args.file)
                self._analyser(args.file)
            elif args.directory:
                self._explorer(args.directory, args.output)
            else:
                self._verifier_extension_fichier(args.play)
                self._jouer(args.play)
            return 0
        except KeyboardInterrupt:
            print("\nProgramme interrompu")
            return 130

        except Exception as e:
            print("Erreur :", e)
            return 1

def main() -> int:
    """
    Initialise et lance l'interface en ligne de commandes.

    :return: Code de retour de l'exécution du programme.
    """
    cli: InterfaceCLI = InterfaceCLI()
    return cli.executer()

# Lancement du programme
if __name__ == "__main__":
    sys.exit(main())