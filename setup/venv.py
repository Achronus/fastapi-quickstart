import os
import subprocess

from conf.constants import VENV, PASS, CORE_PIP_PACKAGES
from config import ADDITIONAL_PIP_PACKAGES
from utils.helper import task_desc_formatter

from rich.console import Console
from rich.progress import Progress


console = Console()


class VEnv:
    """A controller for creating a Python virtual environment."""
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

    @classmethod
    def run(cls, progress: Progress) -> None:
        """Runs controller sub-tasks."""
        sub_tasks = [
            (cls.create, task_desc_formatter("Building venv")),
            (cls.update_pip, task_desc_formatter("Updating PIP")),
            (cls.install, task_desc_formatter("Installing PIP packages")),
            (cls.requirements, task_desc_formatter("Creating [magenta]requirements.txt[/magenta]"))
        ]

        for task, desc in sub_tasks:
            task_id = progress.add_task(description=desc, total=None)
            task()
            progress.update(task_id, completed=1, description=f"{desc} {PASS}")
