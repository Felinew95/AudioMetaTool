"""
Module : cli.py

Description : Ce module définit la classe InterfaceCLI permettant
              d'utiliser AudioMetaTool en mode console.

              Elle permet d'extraire les métadonnées d'un fichier audio,
              d'explorer un dossier, de construire et sauvegarder une
              playlist XSPF, de lire les pistes et de modifier les tags.

Historique des versions :
    - 1.0 : Création de l'interface en ligne de commande.
    - 1.1 : Séparation des fonctionnalités en méthodes et ajout
            de la documentation.

Auteurs : Burin Alexandre, Ammari Menaouer
Version : 1.1
"""

import argparse
import sys
from pathlib import Path

from src.config import NOM_PLAYLIST_DEFAUT
from src.library.traitement.PisteAudioBuilder import PisteAudioBuilder
from src.library.traitement.PlaylistAudioXSPFBuilder import PlaylistAudioXSPFBuilder
from src.library.traitement.SerialiseurXSPF import SerialiseurXSPF
from src.library.traitement.DeserialiseurXSPF import DeserialiseurXSPF
from src.library.traitement.LecteurAudio import LecteurAudio
from src.library.traitement.EditeurTags import EditeurTags


class InterfaceCLI:
    """Gère les commandes du mode console."""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description="AudioMetaTool"
        )

        groupe = self.parser.add_mutually_exclusive_group(
            required=True
        )

        groupe.add_argument("-f", "--file", type=Path,
                            help="Analyser un fichier audio")

        groupe.add_argument("-d", "--directory", type=Path,
                            help="Explorer un dossier")

        groupe.add_argument("-p", "--play", type=Path,
                            help="Lire un morceau ou une playlist")

        groupe.add_argument("--tags", type=Path,
                            help="Modifier les tags")

        self.parser.add_argument("-o", "--output", type=Path,
                                 help="Fichier XSPF de sortie")

        self.parser.add_argument("--set", action="append",
                                 default=[], help="Tag : CHAMP=VALEUR")

    def analyser(self, fichier):
        """Affiche les métadonnées d'une piste audio."""

        builder = PisteAudioBuilder()
        builder.fichier = fichier

        piste = builder.construire()
        print(piste)

        return piste

    def explorer(self, dossier, output):
        """Explore un dossier et sauvegarde sa playlist."""

        if output is None:
            output = Path(NOM_PLAYLIST_DEFAUT)

        if output.suffix.lower() != ".xspf":
            raise ValueError("Extension .xspf obligatoire")

        builder = PlaylistAudioXSPFBuilder(
            dossier, output.stem, str(output)
        )

        playlist = builder.construire()

        for piste in playlist.pistes:
            print(piste)

        SerialiseurXSPF().serialiser(playlist, output)

        print("Nombre de pistes :", playlist.nombre_pistes)
        print("Playlist enregistrée :", output)

    def jouer(self, fichier):
        """Lit un morceau ou les morceaux d'une playlist."""

        fichiers = []

        if fichier.suffix.lower() == ".xspf":
            playlist = DeserialiseurXSPF().charger(fichier)

            for piste in playlist.pistes:
                fichiers.append(piste.chemin_fichier)

        else:
            fichiers.append(str(fichier))

        if not fichiers:
            raise ValueError("Playlist vide")

        for chemin in fichiers:
            print("Lecture :", chemin)

            lecteur = LecteurAudio(chemin)
            lecteur.start()

            try:
                while lecteur.is_alive():
                    lecteur.join(0.2)

            except KeyboardInterrupt:
                lecteur.arreter()
                lecteur.join()
                raise

            if lecteur.erreur:
                raise lecteur.erreur

    def modifier_tags(self, fichier, tags):
        """Modifie et sauvegarde les tags d'un fichier."""

        data = {}

        for tag in tags:
            champ, valeur = tag.split("=", 1)
            data[champ] = valeur

        if not data:
            raise ValueError("Indiquer au moins un tag avec --set")

        EditeurTags().sauvegarder(fichier, data)

        self.analyser(fichier)

    def executer(self, arguments=None):
        """Exécute la commande choisie."""

        if arguments is None:
            arguments = sys.argv[1:]

        if not arguments:
            self.parser.error(
                "Paramètres manquants. Utilisez -h."
            )

        args = self.parser.parse_args(arguments)

        if args.output and not args.directory:
            self.parser.error("-o doit être utilisé avec -d")

        if args.set and not args.tags:
            self.parser.error("--set doit être utilisé avec --tags")

        try:
            if args.file:
                self.analyser(args.file)

            elif args.directory:
                self.explorer(args.directory, args.output)

            elif args.play:
                self.jouer(args.play)

            elif args.tags:
                self.modifier_tags(args.tags, args.set)

            return 0

        except KeyboardInterrupt:
            print("\nProgramme interrompu")
            return 130

        except Exception as e:
            print("Erreur :", e, file=sys.stderr)
            return 1


def main():
    """Lance l'interface console."""

    cli = InterfaceCLI()
    return cli.executer()


if __name__ == "__main__":
    sys.exit(main())
