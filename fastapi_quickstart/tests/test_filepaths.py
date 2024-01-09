import os
import pytest

from conf.constants.filepaths import ProjectPaths, SetupDirPaths


def __directory_splitter(dir_path: str) -> list[str]:
    """Helper function for splitting a path into a list of directories."""
    _, path_to_split = os.path.splitdrive(dir_path)
    directories = []

    while path_to_split:
        path_to_split, directory = os.path.split(path_to_split)
        
        if directory:
            directories.insert(0, directory)

    return directories


def test_project_name_valid() -> None:
    pass


class TestProjectPaths:
    def test_root_valid() -> None:
        pass

    def test_project_valid() -> None:
        pass

    def test_init_poetry_conf_valid() -> None:
        pass

    def test_init_readme_valid() -> None:
        pass

    def test_poetry_conf_valid() -> None:
        pass

    def test_project_main_valid() -> None:
        pass

    def test_project_build_valid() -> None:
        pass

    def test_static_valid() -> None:
        pass

    def test_static_css_valid() -> None:
        pass

    def test_static_js_valid() -> None:
        pass

    def test_static_imgs_valid() -> None:
        pass


class TestSetupDirPaths:
    def test_root_valid() -> None:
        pass

    def test_setup_root_valid() -> None:
        pass

    def test_assets_valid() -> None:
        pass

    def test_project_name_valid() -> None:
        pass
