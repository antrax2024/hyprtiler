#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import sys
import os
from datetime import datetime


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


def writeConfigFile(rule: str, window_class: str, title: str):
    homeDir = os.path.expanduser("~")
    configDir = os.path.join(homeDir, ".config", "hypr")

    configFilePath = os.path.join(configDir, "hyprland.conf")

    try:
        with open(configFilePath, "a") as configFile:
            configFile.write(f"\n# Rule written by Hyprwindow\n")
            configFile.write(
                f"# datetime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            configFile.write(f"windowrulev2 = {rule}")
            if window_class:
                configFile.write(f",class: {window_class}")
            if title:
                configFile.write(f",title: {title}")

            configFile.write("\n")

        print(f"Config file written successfully at {configFilePath}")
    except Exception as e:
        print(f"Failed to write to config file: {e}")
        sys.exit(1)


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

    writeConfigFile(args.rule, args.window_class, args.title)


if __name__ == "__main__":
    printAsciiArt()
    main()
