from hyprtiler.click import cli
import os


def isHyprland() -> bool:
    """
    Checks if Hyprland is the current window manager.

    Returns:
        bool: True if Hyprland is running, False otherwise.
    """
    # Hyprland typically sets the XDG_CURRENT_DESKTOP environment variable to "Hyprland"
    xdg_current_desktop = os.environ.get("XDG_CURRENT_DESKTOP")
    if xdg_current_desktop and "hyprland" in xdg_current_desktop.lower():
        return True

    # Another variable that Hyprland might set
    hyprland_instance_signature = os.environ.get("HYPRLAND_INSTANCE_SIGNATURE")
    if hyprland_instance_signature:
        return True

    # Check if the "Hyprland" process is running (more generic approach, might require 'psutil')
    # This part is optional and can be more complex to implement robustly without external libraries.
    # For simplicity, we'll focus on environment variables, which are more direct.

    return False


def main() -> None:
    if isHyprland():
        cli(prog_name="hyprtiler")
    else:
        print("This app is intended to be run from Hyprland. Sorry!")
