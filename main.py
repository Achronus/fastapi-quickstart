import os
import shutil

from conf.constants import PASS, PARTY
from setup import run_tasks
from utils.helper import strip_whitespace_and_dashes
from utils.printables import project_table

import typer
from typing_extensions import Annotated
from rich.console import Console


app = typer.Typer(rich_markup_mode="rich")

console = Console()
error_console = Console(stderr=True)


@app.command()
def main(name: Annotated[str, typer.Argument(help="The name of the project", show_default=False)]) -> None:
    """Create a FastAPI project with NAME."""
    name = strip_whitespace_and_dashes(name)
    path = os.path.join(os.path.dirname(os.getcwd()), name)

    name_print = f'[cyan]{name}[/cyan]'
    path_print = f'[dark_goldenrod]{path}[/dark_goldenrod]'

    if not os.path.isdir(path):
        raise FileExistsError(f"{path_print} is not a directory!")

    console.print(project_table(name, path))

    if os.path.exists(path):
        typer.confirm("Replace project?", abort=True)

        console.print(f"\nRemoving {name_print} and creating a new one...", end=' ')
        # shutil.rmtree(path)

        # os.makedirs(path)
        # os.chdir(path)
        console.print(PASS)

        # Run task handler
        run_tasks()

        # End of scriptparty
        console.print(f"\n{PARTY} Project created successfully! {PARTY}")
        console.print(f"Access {name_print} at {path_print}")
    else:
        raise FileNotFoundError(f"{path_print} doesn't exist!")

if __name__ == '__main__':
    app()
