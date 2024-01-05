import os
import shutil

from ..conf.constants import STATIC_DIR_NAME, VALID_STATIC_DIR_NAMES, CORE_ENV_PARAMS
from ..conf.constants.filepaths import AssetFilenames, ProjectDirPaths, SetupDirPaths
from ..config import ENV_FILE_ADDITIONAL_PARAMS
from .base import ControllerBase


class StaticAssetsController(ControllerBase):
    """A controller for handling the static assets."""
    def __init__(self) -> None:
        tasks = [
            (self.create_dotenv, "Building [magenta].env[/magenta]"),
            (self.move_setup_assets, "Creating [green]static files[/green] and [green]templates[/green]")
        ]

        super().__init__(tasks)

    @staticmethod
    def create_dotenv() -> None:
        """Creates a `.env` file and adds items to it."""
        with open(AssetFilenames.ENV, "a") as file:
            for item in CORE_ENV_PARAMS + ENV_FILE_ADDITIONAL_PARAMS:
                file.write(item)

    @staticmethod
    def move_setup_assets() -> None:
        """Moves the items in the `setup_assets` folder into the project directory."""
        static_exists = False

        # Move assets into root project dir
        shutil.copytree(SetupDirPaths.ASSETS, os.getcwd(), dirs_exist_ok=True)

        for dir_name in VALID_STATIC_DIR_NAMES:
            dir_path = os.path.join(os.getcwd(), dir_name)

            # Check if static folder exists and matches desired name
            if os.path.exists(dir_path) and os.path.isdir(dir_name):
                if dir_name != STATIC_DIR_NAME:
                    os.rename(dir_path, ProjectDirPaths.STATIC)
                static_exists = True
                break
        
        # If static folder doesn't exist, make one
        if not static_exists:
            static_dirs = [
                ProjectDirPaths.STATIC, 
                ProjectDirPaths.CSS, 
                ProjectDirPaths.JS, 
                ProjectDirPaths.IMGS
            ]
            for item in static_dirs:
                os.mkdir(item)
