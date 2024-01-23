import os
import sys

from ..helper import dirname_check
from fastapi_quickstart.config import DATABASE_URL


# Change venv activation depending on OS
VENV_NAME = 'env'
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
    "python-dotenv"
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

STATIC_FILES_DIR = 'public'
STATIC_DIR_NAME = dirname_check(
    VALID_STATIC_DIR_NAMES, 
    STATIC_FILES_DIR,
    err_msg_start="[blue]STATIC_FILES_DIR[/blue] in [yellow]config.py[/yellow]"
)
