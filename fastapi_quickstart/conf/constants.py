import os
import sys

from .helper import dirname_check, set_tw_standalone_filename
from .file_handler import read_all_file_content
from ..config import STATIC_FILES_DIR, VENV_NAME, DATABASE_URL


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


# Setup assets directory names
class SetupAssetsDirNames:
    ROOT = 'setup_assets'
    CSS = 'css'
    JS = 'js'
    IMGS = 'imgs'


# Asset filenames
class AssetFilenames:
    _js_ext = '.min.js'
    _css_ext = '.min.css'

    TW_STANDALONE = set_tw_standalone_filename()
    ALPINE = 'alpine' + _js_ext
    HTMX = 'htmx' + _js_ext
    FLOWBITE_CSS = 'flowbite' + _css_ext
    FLOWBITE_JS = 'flowbite' + _js_ext

    REQUIREMENTS = 'requirements.txt'
    POETRY_CONF = 'pyproject.toml'
    README = 'README.md'
    ENV = '.env'


# Asset URLs
class AssetUrls:
    TW_STANDALONE = 'https://github.com/tailwindlabs/tailwindcss/releases/latest/download/'
    ALPINE = 'node_modules/alpinejs/dist/cdn.min.js'
    HTMX = f'https://unpkg.com/htmx.org/dist/{AssetFilenames.HTMX}'
    FLOWBITE_CSS = f'node_modules/flowbite/dist/{AssetFilenames.FLOWBITE_CSS}'
    FLOWBITE_JS = f'node_modules/flowbite/dist/{AssetFilenames.FLOWBITE_JS}'


# Static folder directory names
class StaticDirNames:
    ROOT = os.path.join(os.getcwd(), STATIC_DIR_NAME)
    CSS = os.path.join(ROOT, SetupAssetsDirNames.CSS)
    JS = os.path.join(ROOT, SetupAssetsDirNames.JS)
    IMGS = os.path.join(ROOT, SetupAssetsDirNames.IMGS)


# Setup assets filepaths
class SetupDirPaths:
    ROOT = os.path.dirname(os.path.join(os.getcwd(), SetupAssetsDirNames.ROOT))
    SETUP_ROOT = os.path.join(ROOT, 'fastapi_quickstart')
    ASSETS = os.path.join(SETUP_ROOT, SetupAssetsDirNames.ROOT)
    PROJECT_NAME = os.path.join(SETUP_ROOT, 'conf', 'name')


# Store project name
PROJECT_NAME = read_all_file_content(SetupDirPaths.PROJECT_NAME)


# Project directory filepaths
class ProjectDirPaths:
    ROOT = os.path.join(os.path.dirname(os.getcwd()), PROJECT_NAME)
    PROJECT = os.path.join(ROOT, PROJECT_NAME)

    INIT_POETRY_CONF = os.path.join(PROJECT, AssetFilenames.POETRY_CONF)
    INIT_README = os.path.join(PROJECT, AssetFilenames.README)
    
    POETRY_CONF = os.path.join(ROOT, AssetFilenames.POETRY_CONF)

    STATIC = os.path.join(PROJECT, STATIC_DIR_NAME)
    CSS = os.path.join(STATIC, SetupAssetsDirNames.CSS)
    JS = os.path.join(STATIC, SetupAssetsDirNames.JS)
    IMGS = os.path.join(STATIC, SetupAssetsDirNames.IMGS)
