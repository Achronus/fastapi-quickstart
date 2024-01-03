from .venv import create_venv
from .static import create_static_assets
from .libraries import install_libraries
from .clean import tidy_project
from .fastapi import create_fastapi_files

from rich.console import Console

TASKS = [
    create_venv,
    create_static_assets,
    install_libraries,
    tidy_project,
    create_fastapi_files
]

console = Console()


def run_tasks() -> None:
    """The task handler for performing each operation in the CLI."""
    for task in TASKS:
        console.print('test')
        # task()
