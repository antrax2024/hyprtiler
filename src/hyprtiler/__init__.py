from .config import *
import argparse
import sys


def main() -> None:
    printAsciiArt()
    # Configuração do parser
    parser = argparse.ArgumentParser(
        description=f"Application to write windows of windows on Hyprland. Version {VERSION}.",
        epilog="example: hyprtiler -r float -c 'alacritty'",
    )

    # Argumentos opcionais
    parser.add_argument(
        "-r",
        "--rule",
        type=str,
        default="float",
        help="rule that will be applied to the window. Default is float.",
    )

    parser.add_argument(
        "-c",
        "--window-class",
        type=str,
        required=True,
        help="Regular expression of the window class.",
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{VERSION}",
        help="show the version number and exit.",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Processamento dos argumentos
    args = parser.parse_args()

    # Lógica do script usando os argumentos
    writeConfigFile(args.rule, args.window_class)
