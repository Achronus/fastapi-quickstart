import os

from . import STATIC_DIR_NAME
from ..helper import set_tw_standalone_filename


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
    MAIN = 'main.py'
    BUILD = 'build.py'


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


def set_project_name(name: str) -> str:
    os.environ['PROJECT_NAME'] = name


def get_project_name() -> str:
    return os.environ.get('PROJECT_NAME')


# Project directory and filename filepaths
class ProjectPaths:
    def __init__(self) -> None:
        self.PROJECT_NAME = get_project_name()

        self.ROOT = os.path.join(os.path.dirname(os.getcwd()), self.PROJECT_NAME)
        self.PROJECT = os.path.join(self.ROOT, self.PROJECT_NAME)

        self.INIT_POETRY_CONF = os.path.join(self.PROJECT, AssetFilenames.POETRY_CONF)
        self.INIT_README = os.path.join(self.PROJECT, AssetFilenames.README)
        
        self.POETRY_CONF = os.path.join(self.ROOT, AssetFilenames.POETRY_CONF)
        self.PROJECT_MAIN = os.path.join(self.PROJECT, AssetFilenames.MAIN)
        self.PROJECT_BUILD = os.path.join(self.PROJECT, AssetFilenames.BUILD)

        self.STATIC = os.path.join(self.PROJECT, STATIC_DIR_NAME)
        self.CSS = os.path.join(self.STATIC, SetupAssetsDirNames.CSS)
        self.JS = os.path.join(self.STATIC, SetupAssetsDirNames.JS)
        self.IMGS = os.path.join(self.STATIC, SetupAssetsDirNames.IMGS)
