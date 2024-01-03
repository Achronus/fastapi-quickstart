import os
import sys

from config import STATIC_FILES_DIR


# Change venv activation depending on OS
if sys.platform.startswith("win"):
    VENV = "venv\\Scripts"
else:
    VENV = "venv/bin/"

# Define core PIP packages
CORE_PIP_PACKAGES = [
    "fastapi", 
    "uvicorn[standard]", 
    "jinja2", 
    "python-dotenv"
]

# Custom print emoji's
PASS = '[green]\u2713[/green]'
FAIL = '[red]\u274c[/red]'
PARTY = ':party_popper:'

# Set default static directory name
VALID_STATIC_DIR_NAMES =  ['static', 'public', 'assets']

def static_dir_check(custom_name: str) -> str:
    if custom_name not in VALID_STATIC_DIR_NAMES:
        return ValueError(f"'STATIC_FILES_DIR' in 'config.py' must be one of: '{VALID_STATIC_DIR_NAMES}'!")

    return custom_name

STATIC_DIR_NAME = static_dir_check(STATIC_FILES_DIR)


# Setup assets directory names
class SetupAssetsDirNames:
    ROOT = 'setup_assets'
    CORE = 'core'
    PROJECT = 'project'


# Setup assets filepaths
class SetupDirPaths:
    ROOT = os.path.dirname(os.path.join(os.getcwd(), SetupAssetsDirNames.ROOT))
    ASSETS = os.path.join(ROOT, SetupAssetsDirNames.ROOT)
    CORE = os.path.join(ASSETS, SetupAssetsDirNames.CORE)
    PROJECT = os.path.join(ASSETS, SetupAssetsDirNames.PROJECT)


# Asset filenames
class AssetFilenames:
    _js_ext = '.min.js'
    _css_ext = '.min.css'

    ALPINE = 'alpine' + _js_ext
    HTMX = 'htmx' + _js_ext
    FLOWBITE_CSS = 'flowbite' + _css_ext
    FLOWBITE_JS = 'flowbite' + _js_ext


# Asset URLs
class AssetUrls:
    ALPINE = 'node_modules/alpinejs/dist/cdn.min.js'
    HTMX = f'https://unpkg.com/htmx.org/dist/{AssetFilenames.HTMX}'
    FLOWBITE_CSS = f'node_modules/flowbite/dist/{AssetFilenames.FLOWBITE_CSS}'
    FLOWBITE_JS = f'node_modules/flowbite/dist/{AssetFilenames.FLOWBITE_JS}'
