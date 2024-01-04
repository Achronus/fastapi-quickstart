import os
import sys


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

# Setup assets directory name and child directory names
SETUP_ROOT_ASSETS_NAME = 'setup_assets'
SETUP_ROOT_ASSETS_ROOT_FOLDER = 'core'
SETUP_ROOT_ASSETS_STATIC_FOLDER = 'static'
SETUP_ROOT_ASSETS_TEMPLATE_FOLDER = 'templates'


# Setup assets filepaths
class SetupDirPaths:
    ROOT = os.path.dirname(os.path.join(os.getcwd(), SETUP_ROOT_ASSETS_NAME))
    ASSETS = os.path.join(ROOT, SETUP_ROOT_ASSETS_NAME)
    CORE = os.path.join(ASSETS, SETUP_ROOT_ASSETS_ROOT_FOLDER)
    STATIC = os.path.join(ASSETS, SETUP_ROOT_ASSETS_STATIC_FOLDER)
    TEMPLATE = os.path.join(ASSETS, SETUP_ROOT_ASSETS_TEMPLATE_FOLDER)


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
