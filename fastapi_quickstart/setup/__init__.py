from .venv import VEnvController
from .static import StaticAssetsController
from .libraries import LibraryController
from .fastapi import FastAPIFileController
from .docker import DockerFileController
from .clean import CleanupController
from ..conf.constants import PASS

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn


TASKS = [
    (VEnvController, "Creating virtual environment..."),
    (StaticAssetsController, "Creating static assets..."),
    (LibraryController, "Installing libraries..."),
    (FastAPIFileController, "Checking FastAPI assets..."),
    (DockerFileController, "Creating Dockerfiles..."),
    (CleanupController, "Cleaning project...")
]

console = Console()


def run_tasks() -> None:
    """The task handler for performing each operation in the CLI."""
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        for idx, (task, desc) in enumerate(TASKS, 1):
            new_desc = f"{idx}. {desc}"
            task_id = progress.add_task(description=new_desc, total=None)
            task().run(progress)
            progress.update(task_id, completed=1, description=f"{new_desc} {PASS}")
