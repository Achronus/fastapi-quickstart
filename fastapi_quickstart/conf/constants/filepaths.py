import os

from . import STATIC_DIR_NAME
from ..helper import set_tw_standalone_filename
from ..file_handler import read_all_file_content


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
