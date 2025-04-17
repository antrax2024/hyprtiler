# hyprtiler
hyprtiler is a Python application designed to manage and automatize experience with windows in [Hyprland](https://hyprland.org/) Wayland Compositor. It provides advanced tiling, floating, and automation features to streamline your workflow with [Hyprland](https://hyprland.org/) writing rules directly in **hyprland.conf** file.

## Features
- Window rules for hyprland automation
- Lightweight and fast

## Requirements
- Python 3.12+
- Linux (tested on major distributions)
- Hyprland or compatible window manager running

## Installation

1. Create and activate a python Virtual Environment in any directory:
   ```bash
   cd any-dir/
   python -m venv .venv 
   source .venv/bin/activate.fish # if you use fish
   source .venv/bin/activate # if you use bash or zsh
   ```

2. Install application:
   ```bash
   pip install hyprtiler
   ```

## Usage
Run the application with:
```bash
hyprtiler
```

## Command-line Arguments

The `hyprtiler` application provides the following command-line arguments:

- `-h`, `--help` (optional):
  - Type: string
  - Description: Show the help.

- `-r`, `--rule` (optional):
  - Type: string
  - Description: Rule that will be applied to the window. Default is `float`.

- `-c`, `--window-class` (required):
  - Type: string
  - Description: Regular expression of the window class.

- `-v`, `--version`:
  - Action: Shows the version number and exits.

### Example Usage

```sh
hyprtiler -r float -c 'alacritty'
```

This command applies the `float` rule to windows matching the class `alacritty`.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
