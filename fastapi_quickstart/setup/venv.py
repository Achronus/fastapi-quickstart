import os
import shutil
import subprocess

from ..conf.constants import VENV, VENV_NAME, CORE_PIP_PACKAGES
from ..conf.constants.filepaths import get_project_name
from ..conf.constants.poetry import PoetryContent
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
            (self.init_project, f"Initalising [cyan]{get_project_name()}[/cyan] as [green]Poetry[/green] project"),
            (self.add_dependencies, "Adding [yellow]PIP[/yellow] packages to [green]Poetry[/green]")
        ]

        super().__init__(tasks)

        self.poetry_content = PoetryContent()

    @staticmethod
    def create() -> None:
        """Creates a new virtual environment."""
        subprocess.run(["python", "-m", "venv", VENV_NAME], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def update_pip() -> None:
        """Updates `PIP` to the latest version."""
        subprocess.run([os.path.join(VENV, "pip"), "install", "--upgrade", "pip"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def install() -> None:
        """Installs a set of `PIP` packages."""
        subprocess.run([os.path.join(VENV, "pip"), "install", *CORE_PIP_PACKAGES, *ADDITIONAL_PIP_PACKAGES], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def init_project(self) -> None:
        """Creates a poetry project."""
        # Create Poetry project
        subprocess.run(["poetry", "new", self.project_paths.PROJECT_NAME], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Organise new project directory
        shutil.rmtree(os.path.join(self.project_paths.PROJECT, self.project_paths.PROJECT_NAME))
        shutil.move(self.project_paths.INIT_POETRY_CONF, self.project_paths.ROOT)
        shutil.move(self.project_paths.INIT_README, self.project_paths.ROOT)

        # Add scripts to pyproject.toml
        insert_into_file(
            self.poetry_content.SCRIPT_INSERT_LOC, 
            f'\n\n{self.poetry_content.SCRIPT_CONTENT}', 
            self.project_paths.POETRY_CONF
        )

    def add_dependencies(self) -> None:
        """Adds PIP packages to the poetry project."""
        subprocess.run(["poetry", "shell"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        subprocess.run(["poetry", "add", *CORE_PIP_PACKAGES, *ADDITIONAL_PIP_PACKAGES], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Move into project directory
        os.chdir(self.project_paths.PROJECT)
