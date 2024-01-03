import time

from .venv import create_venv
from .static import create_static_assets
from .libraries import install_libraries
from .clean import tidy_project
from .fastapi import create_fastapi_files
from conf.constants import PASS

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

TASKS = [
    (create_venv, "Creating virtual environment..."),
    (create_static_assets, "Creating static assets..."),
    (install_libraries, "Installing libraries..."),
    (tidy_project, "Cleaning project..."),
    (create_fastapi_files, "Creating FastAPI assets...")
]

console = Console()


def run_tasks() -> None:
    """The task handler for performing each operation in the CLI."""
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        for task, desc in TASKS:
            task_id = progress.add_task(description=desc, total=None)
            # progress.console.print('test')
            time.sleep(1)
            progress.update(task_id, completed=1, description=f"{desc} {PASS}")
            # task()
