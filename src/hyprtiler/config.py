import os
from datetime import datetime
from rich.console import Console
import sys

# hyprtiler version
VERSION = "0.1.2"

# Define the console
cl = Console()


def printAsciiArt() -> None:
    ascii_art = r"""
 _                      _   _ _           
| |__  _   _ _ __  _ __| |_(_) | ___ _ __ 
| '_ \| | | | '_ \| '__| __| | |/ _ \ '__|
| | | | |_| | |_) | |  | |_| | |  __/ |   
|_| |_|\__, | .__/|_|   \__|_|_|\___|_|   
       |___/|_|
    """
    cl.print(ascii_art)


def writeConfigFile(rule: str, window_class: str) -> None:
    homeDir = os.path.expanduser("~")
    configDir = os.path.join(homeDir, ".config", "hypr")

    configFilePath = os.path.join(configDir, "hyprland.conf")

    try:
        with open(configFilePath, "a") as configFile:
            configFile.write(f"\n# Rule written by hyprtiler\n")
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
