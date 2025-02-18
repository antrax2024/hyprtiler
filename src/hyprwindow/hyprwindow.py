#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys


def printAsciiArt():
    ascii_art = r"""
     _                               _           _               
    | |__  _   _ _ __  _ ____      _(_)_ __   __| | _____      __
    | '_ \| | | | '_ \| '__\ \ /\ / / | '_ \ / _` |/ _ \ \ /\ / /
    | | | | |_| | |_) | |   \ V  V /| | | | | (_| | (_) \ V  V / 
    |_| |_|\__, | .__/|_|    \_/\_/ |_|_| |_|\__,_|\___/ \_/\_/  
           |___/|_|                                              
    """
    print(ascii_art)


def main():
    # Configuração do parser
    parser = argparse.ArgumentParser(
        description="An application to automatically configure windows on Hyprland",
        epilog="example: hyprwindow -r float -c 'alacritty'",
    )

    # Argumentos opcionais
    parser.add_argument(
        "-r",
        "--rule",
        choices=["float", "tile", "fullscreen"],
        default="float",
        help="rule that will be applied to the window. Default is float.",
    )

    parser.add_argument(
        "-c",
        "--window-class",
        type=str,
        help="Regular expression of the window class.",
    )

    parser.add_argument(
        "-t",
        "--title",
        help="Regular expression of the window title.",
    )

    # Processamento dos argumentos
    args = parser.parse_args()
    # Lógica do script usando os argumentos

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    print(f"Rule: {args.rule}")
    print(f"Window Class: {args.window_class}")
    print(f"Title: {args.title}")

    # ... seu código aqui ...


if __name__ == "__main__":
    printAsciiArt()
    main()
