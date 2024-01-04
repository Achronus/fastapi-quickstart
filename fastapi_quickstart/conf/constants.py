import os
import sys

from .helper import dirname_check, set_tw_standalone_filename
from ..config import STATIC_FILES_DIR, VENV_NAME


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
    "jinja2", 
    "python-dotenv"
]

# Define CLI specific pip packages
CLI_PIP_PACKAGES = [
    "typer[all]",
    "poetry"
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
    err_msg_start="'STATIC_FILES_DIR' in 'config.py'"
)

# Setup assets directory names
class SetupAssetsDirNames:
    ROOT = 'setup_assets'


# Setup assets filepaths
class SetupDirPaths:
    ROOT = os.path.dirname(os.path.join(os.getcwd(), SetupAssetsDirNames.ROOT))
    ASSETS = os.path.join(ROOT, 'fastapi_quickstart', SetupAssetsDirNames.ROOT)


# Asset filenames
class AssetFilenames:
    _js_ext = '.min.js'
    _css_ext = '.min.css'

    TW_STANDALONE = set_tw_standalone_filename()
    ALPINE = 'alpine' + _js_ext
    HTMX = 'htmx' + _js_ext
    FLOWBITE_CSS = 'flowbite' + _css_ext
    FLOWBITE_JS = 'flowbite' + _js_ext


# Asset URLs
class AssetUrls:
    TW_STANDALONE = 'https://github.com/tailwindlabs/tailwindcss/releases/latest/download/'
    ALPINE = 'node_modules/alpinejs/dist/cdn.min.js'
    HTMX = f'https://unpkg.com/htmx.org/dist/{AssetFilenames.HTMX}'
    FLOWBITE_CSS = f'node_modules/flowbite/dist/{AssetFilenames.FLOWBITE_CSS}'
    FLOWBITE_JS = f'node_modules/flowbite/dist/{AssetFilenames.FLOWBITE_JS}'
