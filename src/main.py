import time
from enum import Enum

import typer
from rich import print
from rich.panel import Panel
from rich.progress import Progress
from rich.table import Table
from typing_extensions import Annotated


# Custom types
class Color(str, Enum):
    red = "red"
    blue = "blue"
    green = "green"


# Typer application CLI
app = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]},
    rich_markup_mode="markdown",
    epilog="Author: Li Productions :sunglasses:",
)


@app.command(help=":wave: **Shows** hello world.")
def hello_world(
    name: Annotated[str, typer.Option(help="name")] = "World",
    formal: Annotated[bool, typer.Option(help="formalism")] = True,
    color: Annotated[Color, typer.Option(help="color to use")] = Color.blue,
):
    """Prints hello to the user.

    Args:
        name (Annotated[str, typer.Option, optional): The name to use. Defaults to "name")]=userid.
        formal (Annotated[bool, typer.Option, optional): Formalism of speaker. Defaults to "formalism")]=True.
        color (Annotated[Color, typer.Option, optional): The color to use. Defaults to "color to use")]=Color.blue.
    """

    # Generate a
    if formal:
        output = f"[{color}]Hello {name}!"
    else:
        output = f"[{color}]Good morning {name}!"

    print(Panel(output))


@app.command(help=":fire: **Shows** a progress bar.")
def progress_bar(
    steps: Annotated[int, typer.Option(help="number of steps in progress bar")] = 10,
):
    """Shows a progress bar animation for long running tasks.

    Args:
        steps (Annotated[int, typer.Option, optional): The number of steps to iterate through. Defaults to "number of steps in progress bar")]=10.
    """
    counter = 0

    with Progress() as progress:
        task = progress.add_task("Running...", total=steps)

        while counter < steps:
            counter += 1
            progress.update(task, completed=counter)
            time.sleep(0.1)


@app.command(help=":white_heavy_check_mark: **Shows** a table.")
def table():
    """Display a basic table."""

    # Show a basic table
    table = Table(
        "Col 1",
        "Col 2",
        title="Basic Table",
    )
    table.add_row(*["val1", "val2"])
    print(table)


if __name__ == "__main__":
    app()
