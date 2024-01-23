import os
import shutil

from ..conf.constants import STATIC_DIR_NAME, VALID_STATIC_DIR_NAMES, CORE_ENV_PARAMS
from ..conf.constants.docker import DockerContent
from ..conf.constants.filepaths import AssetFilenames, SetupDirPaths, SetupAssetsDirNames, ProjectPaths
from ..config import ENV_FILE_ADDITIONAL_PARAMS
from .base import ControllerBase


class StaticAssetsController(ControllerBase):
    """A controller for handling the static assets."""
    def __init__(self) -> None:
        tasks = [
            (self.move_setup_assets, "Creating [green]static files[/green] and [green]templates[/green]"),
            (self.create_dotenv, "Building [magenta].env[/magenta]")
        ]

        super().__init__(tasks)

        self.project_paths = ProjectPaths()

    def create_dotenv(self) -> None:
        """Creates a `.env` file in the root for docker specific config and another in the backend folder. Adds items to them both."""
        docker_content = DockerContent()
        docker_path = os.path.join(os.path.dirname(os.getcwd()), AssetFilenames.ENV)
        backend_path = os.path.join(self.project_paths.BACKEND, AssetFilenames.ENV)

        with open(docker_path, "w") as file:
            file.write(docker_content.env_config())

        with open(backend_path, "w") as file:
            for item in CORE_ENV_PARAMS + ENV_FILE_ADDITIONAL_PARAMS:
                file.write(item)

    def move_setup_assets(self) -> None:
        """Moves the items in the `setup_assets` folder into the project directory."""
        static_exists = False

        # Move assets into root project dir
        shutil.copytree(SetupDirPaths.ASSETS, os.getcwd(), dirs_exist_ok=True)

        for dir_name in VALID_STATIC_DIR_NAMES:
            dir_path = os.path.join(os.getcwd(), SetupAssetsDirNames.FRONTEND, dir_name)

            # Check if static folder exists and matches desired name
            if os.path.exists(dir_path):
                if dir_name != STATIC_DIR_NAME:
                    os.rename(dir_path, self.project_paths.STATIC)
                static_exists = True
                break

        # If static folder doesn't exist, make one
        if not static_exists:
            static_dirs = [
                self.project_paths.STATIC, 
                self.project_paths.CSS, 
                self.project_paths.JS, 
                self.project_paths.IMGS
            ]
            for item in static_dirs:
                os.mkdir(item)

        # Move .gitignore, if available
        gitignore_path = os.path.join(os.getcwd(), '.gitignore')
        if gitignore_path:
            shutil.copy(gitignore_path, os.path.dirname(os.getcwd()))
            os.remove(gitignore_path)
