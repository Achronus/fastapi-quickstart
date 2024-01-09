from . import STATIC_DIR_NAME
from .filepaths import get_project_name, AssetFilenames


# Define Poetry script commands
class PoetryCommands:
    def __init__(self) -> None:
        self.project_name = get_project_name()
        
        self.TW_CMD = f'tailwindcss -i ./{STATIC_DIR_NAME}/css/input.css -o ./{STATIC_DIR_NAME}/css/output.css'
        self.WATCH_TW_CMD = f"{self.TW_CMD} --watch --minify"

        self.START_SERVER_CMD = f"{self.project_name}.main:start"
        self.WATCH_POETRY_CMD = f"{self.project_name}.{AssetFilenames.BUILD.split('.')[0]}:tw_build"

# Define Poetry script content
# Specific to setup/venv.py -> init_project()
class PoetryContent:
    def __init__(self) -> None:
        self.project_name = get_project_name()
        self.commands = PoetryCommands()

        self.SCRIPT_INSERT_LOC = 'readme = "README.md"'
        self.SCRIPT_CONTENT = '\n'.join([
            "[tool.poetry.scripts]",
            f'run = "{self.commands.START_SERVER_CMD}"',
            f'watch = "{self.commands.WATCH_POETRY_CMD}"'
        ])

        self.START_CMD_OLD = 'uvicorn.run("main:app"'
        self.START_CMD_NEW = f'uvicorn.run("{self.project_name}.main:app"'


        self.BUILD_FILE_CONTENT = f"""
        import os
        import subprocess


        def tw_build() -> None:
            cmd = "{self.commands.WATCH_TW_CMD}"
            os.chdir(os.path.join(os.getcwd(), '{self.project_name}'))
            subprocess.run(cmd.split(' '), check=True)
        """
