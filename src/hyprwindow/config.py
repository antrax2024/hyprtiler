import os
from datetime import datetime
from rich.console import Console
import sys

# Hyprwindow version
VERSION = "0.1.3"

# Define the console
cl = Console()


def printAsciiArt() -> None:
    ascii_art = r"""
     _                               _           _               
    | |__  _   _ _ __  _ ____      _(_)_ __   __| | _____      __
    | '_ \| | | | '_ \| '__\ \ /\ / / | '_ \ / _` |/ _ \ \ /\ / /
    | | | | |_| | |_) | |   \ V  V /| | | | | (_| | (_) \ V  V / 
    |_| |_|\__, | .__/|_|    \_/\_/ |_|_| |_|\__,_|\___/ \_/\_/  
           |___/|_|                                              
    """
    cl.print(ascii_art)


def writeConfigFile(rule: str, window_class: str) -> None:
    homeDir = os.path.expanduser("~")
    configDir = os.path.join(homeDir, ".config", "hypr")

    configFilePath = os.path.join(configDir, "hyprland.conf")

    try:
        with open(configFilePath, "a") as configFile:
            configFile.write(f"\n# Rule written by Hyprwindow\n")
            configFile.write(
                f"# datetime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            )
            configFile.write(f"windowrulev2 = {rule},class:{window_class}\n")

        cl.print(f"Config file written successfully at {configFilePath}")
    except Exception as e:
        cl.print(f"Failed to write to config file: {e}")
        sys.exit(1)


if __name__ == "__main__":
    pass
