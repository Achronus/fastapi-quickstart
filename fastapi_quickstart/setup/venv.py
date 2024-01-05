import os
import shutil
import subprocess

from ..conf.constants import (
    VENV, 
    VENV_NAME,
    CORE_PIP_PACKAGES, 
    SCRIPT_INSERT_LOC,
    SCRIPT_CONTENT
)
from ..conf.constants.filepaths import PROJECT_NAME, ProjectDirPaths, AssetFilenames
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
        subprocess.run(["python", "-m", "venv", VENV_NAME])

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
        with open(AssetFilenames.REQUIREMENTS, "w") as file:
            subprocess.Popen([os.path.join(VENV, "pip"), "freeze"], stdout=file)

    @staticmethod
    def init_project() -> None:
        """Creates a poetry project."""
        subprocess.run(["poetry", "new", PROJECT_NAME], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Organise new project directory
        shutil.rmtree(os.path.join(ProjectDirPaths.PROJECT, PROJECT_NAME))
        shutil.move(ProjectDirPaths.INIT_POETRY_CONF, ProjectDirPaths.ROOT)
        shutil.move(ProjectDirPaths.INIT_README, ProjectDirPaths.ROOT)

        # Add scripts to pyproject.toml
        insert_into_file(SCRIPT_INSERT_LOC, f'\n\n{SCRIPT_CONTENT}', ProjectDirPaths.POETRY_CONF)

        # Move into project directory
        os.chdir(ProjectDirPaths.PROJECT)
