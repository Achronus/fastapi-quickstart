import os
import shutil
import subprocess

from ..conf.constants import (
    VENV, 
    CORE_PIP_PACKAGES, 
    PROJECT_NAME,
    START_SERVER_CMD,
    WATCH_TW_CMD,
    ProjectDirPaths
)
from ..conf.file_handler import insert_into_file
from ..config import ADDITIONAL_PIP_PACKAGES
from .base import ControllerBase


class VEnvController(ControllerBase):
    """A controller for creating a Python virtual environment."""
    def __init__(self) -> None:
        tasks = [
            (self.create, "Building [yellow]venv[/yellow]"),
            (self.update_pip, "Updating [yellow]PIP[/yellow]"),
            (self.install, "Installing [yellow]PIP[/yellow] packages"),
            (self.requirements, "Creating [magenta]requirements.txt[/magenta]"),
            (self.init_project, f"Initalising [cyan]{PROJECT_NAME}[/cyan] as [green]Poetry[/green] project")
        ]

        super().__init__(tasks)

    @staticmethod
    def create() -> None:
        """Creates a new virtual environment."""
        subprocess.run(["python", "-m", "venv", "venv"])

    @staticmethod
    def update_pip() -> None:
        """Updates `PIP` to the latest version."""
        subprocess.run([os.path.join(VENV, "pip"), "install", "--upgrade", "pip"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def install() -> None:
        """Installs a set of `PIP` packages."""
        subprocess.run([os.path.join(VENV, "pip"), "install", *CORE_PIP_PACKAGES, *ADDITIONAL_PIP_PACKAGES], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def requirements() -> None:
        """Creates a `requirements.txt` file."""
        with open("requirements.txt", "w") as file:
            subprocess.Popen([os.path.join(VENV, "pip"), "freeze"], stdout=file)

    @staticmethod
    def init_project() -> None:
        """Creates a poetry project."""
        subprocess.run(["poetry", "new", PROJECT_NAME], shell=True)

        # Organise new project directory
        shutil.rmtree(os.path.join(ProjectDirPaths.PROJECT, PROJECT_NAME))
        shutil.move(os.path.join(ProjectDirPaths.PROJECT, 'pyproject.toml'), ProjectDirPaths.ROOT)
        shutil.move(os.path.join(ProjectDirPaths.PROJECT, 'README.md'), ProjectDirPaths.ROOT)

        # Add scripts to pyproject.toml
        new_content = f'\n\n[tool.poetry.scripts]\nrun-server = "{START_SERVER_CMD} && {WATCH_TW_CMD}"'
        insert_into_file('readme = "README.md"', new_content, ProjectDirPaths.POETRY_CONF)

        # Move into project directory
        os.chdir(ProjectDirPaths.PROJECT)
