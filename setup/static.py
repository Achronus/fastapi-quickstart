import os
import shutil

from conf.constants import PASS, STATIC_DIR_NAME, VALID_STATIC_DIR_NAMES, SetupDirPaths
from config import ENV_FILE_ADDITIONAL_PARAMS
from utils.helper import task_desc_formatter

from rich.console import Console
from rich.progress import Progress


console = Console()


class StaticAssets:
    """A controller for creating handling the static assets."""
    @staticmethod
    def create_dotenv() -> None:
        with open(".env", "a") as file:
            for item in ENV_FILE_ADDITIONAL_PARAMS:
                file.write(item)

    @staticmethod
    def move_setup_assets() -> None:
        static_exists = False
        correct_static_path = os.path.join(os.getcwd(), STATIC_DIR_NAME)

        # Move assets into root project dir
        shutil.copytree(SetupDirPaths.ASSETS, os.getcwd(), dirs_exist_ok=True)

        for dir_name in VALID_STATIC_DIR_NAMES:
            dir_path = os.path.join(os.getcwd(), dir_name)

            # Check if static folder exists and matches desired name
            if os.path.exists(dir_path) and os.path.isdir(dir_name):
                if dir_name != STATIC_DIR_NAME:
                    os.rename(dir_path, correct_static_path)
                static_exists = True
                break
        
        # If static folder doesn't exist, make one
        if not static_exists:
            os.mkdir(correct_static_path)

    @classmethod
    def run(cls, progress: Progress) -> None:
        """Runs controller sub-tasks."""
        sub_tasks = [
            (cls.create_dotenv, task_desc_formatter("Building [magenta].env[/magenta]")),
            (cls.move_setup_assets, task_desc_formatter("Creating static files and templates")),
        ]

        for task, desc in sub_tasks:
            task_id = progress.add_task(description=desc, total=None)
            task()
            progress.update(task_id, completed=1, description=f"{desc} {PASS}")
