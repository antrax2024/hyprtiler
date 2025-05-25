from rich.console import Console
from hyprpy import Hyprland
from rich.table import Table
from rich import box

cl = Console()


def printClients() -> None:
    """
    Prints the list of clients running on Hyprland
    """

    instance = Hyprland()
    windows = instance.get_windows()

    table = Table(
        title="Clients Running",
        box=box.ROUNDED,  # Outras opções: box.SIMPLE, box.MINIMAL, box.DOUBLE, box.HEAVY_EDGE, etc.
        title_style="bold magenta",
        border_style="bright_yellow",
        header_style="bold green",
        row_styles=["none", "dim"],
    )

    table.add_column("workspace", justify="center")
    table.add_column("address", justify="center")
    table.add_column("title")
    table.add_column("wm_class")
    table.add_column("size (wxh)")
    table.add_column("pid", justify="center")

    for window in windows:
        table.add_row(
            f"{window.workspace.id}",
            f"{window.address}",
            window.title[:20] if len(window.title) > 20 else window.title,
            window.wm_class,
            f"{window.width}x{window.height}",
            f"{window.pid}",
        )

    cl.print(table)
