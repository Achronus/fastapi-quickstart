import os
import shutil

from .conf.constants import STATIC_DIR_NAME
from .conf.helper import set_tw_standalone_filename
from .setup import run_tasks
from .utils.helper import strip_whitespace_and_dashes
from .utils.printables import project_table, project_complete_panel

import typer
from typing_extensions import Annotated
from rich.console import Console


app = typer.Typer(rich_markup_mode="rich")

console = Console()


@app.command()
def main(name: Annotated[str, typer.Argument(help="The name of the project", show_default=False)]) -> None:
    """Create a FastAPI project with NAME."""
    name = strip_whitespace_and_dashes(name)
    path = os.path.join(os.path.dirname(os.getcwd()), name)

    name_print = f'[cyan]{name}[/cyan]'
    path_print = f'[dark_goldenrod]{path}[/dark_goldenrod]'

    console.print(project_table(name, path))

    # Replace project if exists
    if os.path.exists(path):
        typer.confirm("Replace project?", abort=True)

        console.print(f"\nRemoving {name_print} and creating a new one...\n")
        shutil.rmtree(path)
    else:
        console.print(f"\nCreating project {name_print}...\n")

    # Create and move into directory
    os.makedirs(path)
    os.chdir(path)

    # Run task handler
    run_tasks()

    # End of script
    console.print(project_complete_panel())
    console.print(f"Access {name_print} at {path_print}")

    # Provide information for unsupported TailwindCSS standalone CLI
    if set_tw_standalone_filename() == 'unsupported':
        console.print('\nOS not supported for standalone TailwindCSS. [magenta]node_modules[/magenta] kept.')
        console.print('Please run Tailwind through [green]npx[/green] instead:')
        console.print(f'  [dark_goldenrod]npx tailwindcss -i ./{STATIC_DIR_NAME}/assets/input.css -o ./{STATIC_DIR_NAME}/assets/output.css --watch --minify[/dark_goldenrod]')


if __name__ == '__main__':
    app()
