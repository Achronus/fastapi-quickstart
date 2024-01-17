import os
import shutil
import subprocess

from ..conf.helper import tw_executable_exists
from ..conf.constants import VENV_NAME
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
    
    def node_modules(self) -> None:
        """Removes the `node_modules` folder if `tailwindcss` does not exist."""
        # If exists, remove node_modules
        if tw_executable_exists(self.project_paths.ROOT):
            shutil.rmtree(os.path.join(self.project_paths.ROOT, 'node_modules'))

    def poetry_install(self) -> None:
        """Finalise the application with a poetry install."""
        subprocess.run(["poetry", "shell"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["poetry", "install"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def delete_venv(self) -> None:
        """Deletes the virtual environment folder and assets."""
        shutil.rmtree(os.path.join(os.path.dirname(self.project_paths.ROOT), VENV_NAME))

    def remove_files(self) -> None:
        """Removes redundant files."""
        os.remove(os.path.join(self.project_paths.ROOT, '__init__.py'))
        os.remove(os.path.join(self.project_paths.ROOT, 'package.json'))
        os.remove(os.path.join(self.project_paths.ROOT, 'package-lock.json'))

