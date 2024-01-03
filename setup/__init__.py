from .venv import VEnv
from .static import StaticAssets
from .libraries import install_libraries
from .clean import tidy_project
from .fastapi import create_fastapi_files
from conf.constants import PASS

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn


TASKS = [
    (VEnv.run, "Creating virtual environment..."),
    (StaticAssets.run, "Creating static assets..."),
    (install_libraries, "Installing libraries..."),
    (tidy_project, "Cleaning project..."),
    (create_fastapi_files, "Creating FastAPI assets...")
]

console = Console()


def run_tasks() -> None:
    """The task handler for performing each operation in the CLI."""
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        for idx, (task, desc) in enumerate(TASKS, 1):
            new_desc = f"{idx}. {desc}"
            task_id = progress.add_task(description=new_desc, total=None)
            task(progress)
            progress.update(task_id, completed=1, description=f"{new_desc} {PASS}")
            typer.Exit()
