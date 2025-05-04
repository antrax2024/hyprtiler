from .constants import APP_NAME, APP_VERSION
from hyprtiler.config import writeConfigFile
import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


class CustomHelpCommand(click.Command):
    def format_help(self, ctx: click.Context, formatter: click.HelpFormatter) -> None:
        """Custom help formatter that includes app name and version."""
        formatter.write(f"{APP_NAME} v{APP_VERSION}\n\n")
        super().format_help(ctx=ctx, formatter=formatter)


@click.option(
    "-r",
    "--rule",
    "rule",
    type=click.STRING,
    default="float",
    help="Specifies the Rule for window. (default: float)",
)
@click.option(
    "-c",
    "--class",
    "window_class",
    type=click.STRING,
    # required=True,
    help="Windows Class",
)
@click.command(cls=CustomHelpCommand, context_settings=CONTEXT_SETTINGS)
@click.pass_context
def cli(ctx, rule, window_class) -> None:
    """A utility tool for managing windows in the Hyprland compositor environment."""
    click.echo(message=f"{APP_NAME} v{APP_VERSION}\n")

    if not window_class:
        click.echo("Error: --class is required.")

        ctx.exit(1)

    if rule:
        click.echo(f"Rule: {rule}")

    click.echo(f"Window Class: {window_class}")

    writeConfigFile(rule, window_class)
