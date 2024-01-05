from . import STATIC_DIR_NAME
from .filepaths import PROJECT_NAME


# Define Poetry script commands
TW_CMD = f'tailwindcss -i ./{STATIC_DIR_NAME}/css/input.css -o ./{STATIC_DIR_NAME}/css/output.css'

START_SERVER_CMD = f"uvicorn {PROJECT_NAME}.main:start"
WATCH_TW_CMD = f"{TW_CMD} --watch --minify"


# Define Poetry script content
# Specific to setup/venv.py -> init_project()
SCRIPT_INSERT_LOC = 'readme = "README.md"'
SCRIPT_CONTENT = '\n'.join([
    "[tool.poetry.scripts]",
    f'run-server = "{START_SERVER_CMD} && {WATCH_TW_CMD}"'
])
