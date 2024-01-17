from . import STATIC_DIR_NAME
from ..helper import set_tw_standalone_filename
from .filepaths import get_project_name, AssetFilenames


# Define Poetry script commands
class PoetryCommands:
    def __init__(self) -> None:
        self.project_name = get_project_name()
        
        self.TW_CMD = 'tailwindcss -i {INPUT_PATH} -o {OUTPUT_PATH}'
        self.WATCH_TW_CMD = f"{self.TW_CMD} --watch --minify"

        self.START_SERVER_CMD = f"{self.project_name}.main:start"
        self.WATCH_POETRY_CMD = f"{self.project_name}.{AssetFilenames.BUILD.split('.')[0]}:tw_build"

# Define Poetry script content
# Specific to setup/venv.py -> init_project()
class PoetryContent:
    def __init__(self) -> None:
        self.tw_type = set_tw_standalone_filename()
        self.project_name = get_project_name()
        self.commands = PoetryCommands()

        self.SCRIPT_INSERT_LOC = 'readme = "README.md"'
        self.SCRIPT_CONTENT = '\n'.join([
            "[tool.poetry.scripts]",
            f'run = "{self.commands.START_SERVER_CMD}"',
            f'watch = "{self.commands.WATCH_POETRY_CMD}"'
        ])

        self.BUILD_FILE_CONTENT = f"""
        from pathlib import Path
        import os
        import subprocess

        PROJECT_DIR = os.path.basename(Path(__file__).resolve().parent)
        CSS_DIR = os.path.join('frontend', '{STATIC_DIR_NAME}', 'css')
        INPUT_PATH = os.path.join(CSS_DIR, 'input.css')
        OUTPUT_PATH = os.path.join(CSS_DIR, 'styles.min.css')
        
        def tw_build() -> None:
            cmd = f"{'npx ' if self.tw_type == 'unsupported' else ''}{self.commands.WATCH_TW_CMD}"
            os.chdir(os.path.join(os.getcwd(), '{self.project_name}'))
            subprocess.run(cmd.split(' '), check=True)
        """
