from . import STATIC_DIR_NAME
from .filepaths import PROJECT_NAME, AssetFilenames


# Define Poetry script commands
TW_CMD = f'tailwindcss -i ./{STATIC_DIR_NAME}/css/input.css -o ./{STATIC_DIR_NAME}/css/output.css'
WATCH_TW_CMD = f"{TW_CMD} --watch --minify"

START_SERVER_CMD = f"{PROJECT_NAME}.main:start"
WATCH_POETRY_CMD = f"{PROJECT_NAME}.{AssetFilenames.BUILD.split('.')[0]}:tw_build"

# Define Poetry script content
# Specific to setup/venv.py -> init_project()
SCRIPT_INSERT_LOC = 'readme = "README.md"'
SCRIPT_CONTENT = '\n'.join([
    "[tool.poetry.scripts]",
    f'run = "{START_SERVER_CMD}"',
    f'watch = "{WATCH_POETRY_CMD}"'
])

START_CMD_OLD = 'uvicorn.run("main:app"'
START_CMD_NEW = f'uvicorn.run("{PROJECT_NAME}.main:app"'


BUILD_FILE_CONTENT = f"""
import os
import subprocess


def tw_build() -> None:
    cmd = "{WATCH_TW_CMD}"
    os.chdir(os.path.join(os.getcwd(), '{PROJECT_NAME}'))
    subprocess.run(cmd.split(' '), check=True)
"""
