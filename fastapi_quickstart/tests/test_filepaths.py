import os
import pytest

from conf.constants.filepaths import (
    ProjectPaths, 
    SetupDirPaths, 
    get_project_name,
    set_project_name,
    AssetFilenames,
    SetupAssetsDirNames
)
from conf.constants import STATIC_DIR_NAME

PROJECT_NAME = 'test_project'

set_project_name(PROJECT_NAME)
CUSTOM_PROJECT_PARENT = get_project_name()
CUSTOM_PROJECT_ROOT = os.path.join(CUSTOM_PROJECT_PARENT, get_project_name())
CUSTOM_PROJECT_STATIC = os.path.join(CUSTOM_PROJECT_ROOT, STATIC_DIR_NAME)

SETUP_ROOT = 'fastapi-quickstart'
SETUP_PROJECT_ROOT = os.path.join(SETUP_ROOT, 'fastapi_quickstart')
STATIC = os.path.join(SETUP_PROJECT_ROOT, STATIC_DIR_NAME)


@pytest.fixture
def project_paths() -> None:
    set_project_name(PROJECT_NAME)
    return ProjectPaths()


def test_project_name_valid(project_paths: ProjectPaths) -> None:
    set_project_name(ProjectPaths().PROJECT_NAME)
    assert get_project_name() is not None
    assert get_project_name() != ''
    assert get_project_name != project_paths.PROJECT_NAME


class TestProjectPaths:
    @pytest.fixture(autouse=True)
    def initialize_project_paths(self) -> None:
        set_project_name(PROJECT_NAME)
        self.project_paths = ProjectPaths()

    def __validate_path(self, directory_path: str, ending: str) -> None:
        assert directory_path.endswith(ending)

    def test_root_valid(self) -> None:
        self.__validate_path(
            self.project_paths.ROOT, 
            CUSTOM_PROJECT_PARENT
        )

    def test_project_valid(self) -> None:
        self.__validate_path(
            self.project_paths.PROJECT, 
            CUSTOM_PROJECT_ROOT
        )

    def test_init_poetry_conf_valid(self) -> None:
        self.__validate_path(
            self.project_paths.INIT_POETRY_CONF, 
            os.path.join(CUSTOM_PROJECT_ROOT, AssetFilenames.POETRY_CONF)
        )

    def test_init_readme_valid(self) -> None:
        self.__validate_path(
            self.project_paths.INIT_README, 
            os.path.join(CUSTOM_PROJECT_ROOT, AssetFilenames.README)
        )

    def test_poetry_conf_valid(self) -> None:
        self.__validate_path(
            self.project_paths.POETRY_CONF, 
            os.path.join(CUSTOM_PROJECT_PARENT, AssetFilenames.POETRY_CONF)
        )

    def test_project_main_valid(self) -> None:
        self.__validate_path(
            self.project_paths.PROJECT_MAIN, 
            os.path.join(CUSTOM_PROJECT_ROOT, AssetFilenames.MAIN)
        )

    def test_project_build_valid(self) -> None:
        self.__validate_path(
            self.project_paths.PROJECT_BUILD, 
            os.path.join(CUSTOM_PROJECT_ROOT, AssetFilenames.BUILD)
        )

    def test_static_valid(self) -> None:
        self.__validate_path(
            self.project_paths.STATIC,
            CUSTOM_PROJECT_STATIC 
        )

    def test_static_css_valid(self) -> None:
        self.__validate_path(
            self.project_paths.CSS, 
            os.path.join(CUSTOM_PROJECT_STATIC, SetupAssetsDirNames.CSS)
        )

    def test_static_js_valid(self) -> None:
        self.__validate_path(
            self.project_paths.JS, 
            os.path.join(CUSTOM_PROJECT_STATIC, SetupAssetsDirNames.JS)
        )

    def test_static_imgs_valid(self) -> None:
        self.__validate_path(
            self.project_paths.IMGS, 
            os.path.join(CUSTOM_PROJECT_STATIC, SetupAssetsDirNames.IMGS)
        )


class TestSetupDirPaths:
    def __validate_path(self, directory_path: str, ending: str) -> None:
        assert directory_path.endswith(ending)

    def test_root_valid(self) -> None:
        self.__validate_path(
            SetupDirPaths.ROOT, 
            SETUP_ROOT
        )

    def test_setup_root_valid(self) -> None:
        self.__validate_path(
            SetupDirPaths.SETUP_ROOT, 
            SETUP_PROJECT_ROOT
        )

    def test_assets_valid(self) -> None:
        self.__validate_path(
            SetupDirPaths.ASSETS, 
            os.path.join(SETUP_PROJECT_ROOT, SetupAssetsDirNames.ROOT)
        )

    def test_project_name_valid(self) -> None:
        self.__validate_path(
            SetupDirPaths.PROJECT_NAME, 
            os.path.join(SETUP_PROJECT_ROOT, 'conf', 'name')
        )
