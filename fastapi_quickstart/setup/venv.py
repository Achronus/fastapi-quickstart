import os
import subprocess

from ..conf.constants import VENV, CORE_PIP_PACKAGES
from ..config import ADDITIONAL_PIP_PACKAGES
from .base import ControllerBase


class VEnvController(ControllerBase):
    """A controller for creating a Python virtual environment."""
    def __init__(self) -> None:
        tasks = [
            (self.create, "Building [yellow]venv[/yellow]"),
            (self.update_pip, "Updating [yellow]PIP[/yellow]"),
            (self.install, "Installing [yellow]PIP[/yellow] packages"),
            (self.requirements, "Creating [magenta]requirements.txt[/magenta]")
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
