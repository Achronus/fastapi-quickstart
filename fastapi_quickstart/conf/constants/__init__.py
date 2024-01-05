import os
import sys

from ..helper import dirname_check
from ...config import STATIC_FILES_DIR, VENV_NAME, DATABASE_URL


# Change venv activation depending on OS
VENV_LOCATION = os.path.join(os.getcwd(), VENV_NAME)

if sys.platform.startswith("win"):
    VENV = f"{VENV_LOCATION}\\Scripts"
else:
    VENV = f"source {VENV_LOCATION}/bin/"

# Define core PIP packages
CORE_PIP_PACKAGES = [
    "fastapi", 
    "uvicorn[standard]", 
    "sqlalchemy",
    "jinja2", 
    "python-dotenv",
    "poetry"
]

# Define core .env file parameters
CORE_ENV_PARAMS = [
    f'DATABASE_URL={DATABASE_URL}'
]

# Define core NPM packages to install
NPM_PACKAGES = [
    "tailwindcss", 
    "flowbite", 
    "alpinejs"
]

# Custom print emoji's
PASS = '[green]\u2713[/green]'
FAIL = '[red]\u274c[/red]'
PARTY = ':party_popper:'

# Set default static directory name
VALID_STATIC_DIR_NAMES =  ['static', 'public', 'assets']

STATIC_DIR_NAME = dirname_check(
    VALID_STATIC_DIR_NAMES, 
    STATIC_FILES_DIR,
    err_msg_start="[blue]STATIC_FILES_DIR[/blue] in [yellow]config.py[/yellow]"
)

# Define Poetry script commands
TW_CMD = f'tailwindcss -i ./{STATIC_DIR_NAME}/css/input.css -o ./{STATIC_DIR_NAME}/css/output.css'

START_SERVER_CMD = "uvicorn main:app --reload"
WATCH_TW_CMD = f"{TW_CMD} --watch --minify"


# Define Poetry script content
# Specific to setup/venv.py -> init_project()
SCRIPT_INSERT_LOC = 'readme = "README.md"'
SCRIPT_CONTENT = '\n'.join([
    "[tool.poetry.scripts]",
    f'run-server = "{START_SERVER_CMD} && {WATCH_TW_CMD}"'
])
