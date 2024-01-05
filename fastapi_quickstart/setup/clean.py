import os
import shutil
import subprocess

from ..conf.helper import tw_executable_exists
from ..conf.constants.filepaths import ProjectDirPaths
from .base import ControllerBase


class CleanupController(ControllerBase):
    """A controller for handling project cleanup."""
    def __init__(self) -> None:
        tasks = [
            (self.node_modules, "Removing [magenta]node_modules[/magenta]"),
            (self.delete_venv, "Removing [yellow]venv[/yellow]"),
            (self.remove_files, "Removing redundant files"),
            (self.poetry_install, "Finalising project")
        ]

        super().__init__(tasks)
    
    @staticmethod
    def node_modules() -> None:
        """Removes the `node_modules` folder if `tailwindcss` does not exist."""
        # If exists, remove node_modules
        if tw_executable_exists(ProjectDirPaths.PROJECT):
            shutil.rmtree(os.path.join(ProjectDirPaths.PROJECT, 'node_modules'))

    @staticmethod
    def poetry_install() -> None:
        """Finalise the application with a poetry install."""
        subprocess.run(["poetry", "shell"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["poetry", "install"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @staticmethod
    def delete_venv() -> None:
        """Deletes the virtual environment folder and assets."""
        shutil.rmtree(os.path.join(ProjectDirPaths.ROOT, 'env'))

    @staticmethod
    def remove_files() -> None:
        """Removes redundant files."""
        os.remove(os.path.join(ProjectDirPaths.PROJECT, '__init__.py'))

