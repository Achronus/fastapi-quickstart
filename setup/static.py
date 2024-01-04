import os
import shutil

from conf.constants import STATIC_DIR_NAME, VALID_STATIC_DIR_NAMES, SetupDirPaths
from config import ENV_FILE_ADDITIONAL_PARAMS
from setup.base import ControllerBase


class StaticAssetsController(ControllerBase):
    """A controller for handling the static assets."""
    def __init__(self) -> None:
        sub_tasks = [
            (self.create_dotenv, "Building [magenta].env[/magenta]"),
            (self.move_setup_assets, "Creating static files and templates")
        ]

        super().__init__(sub_tasks)

    @staticmethod
    def create_dotenv() -> None:
        """Creates a `.env` file and adds items to it."""
        with open(".env", "a") as file:
            for item in ENV_FILE_ADDITIONAL_PARAMS:
                file.write(item)

    @staticmethod
    def move_setup_assets() -> None:
        """Moves the items in the `setup_assets` folder into the project directory."""
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
