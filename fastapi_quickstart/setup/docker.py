import os

from .base import ControllerBase
from ..conf.constants.docker import DockerFileMapper
from ..conf.constants.filepaths import DockerPaths
from ..conf.file_handler import write_to_file


class DockerFileController(ControllerBase):
    """A FastAPI file creation controller."""
    def __init__(self) -> None:
        tasks = [
            (self.create_dockerfiles, "Generating [bright_blue]Docker[/bright_blue] files"),
            (self.create_compose_files, "Generating [bright_blue]Compose[/bright_blue] files")
        ]

        super().__init__(tasks)

        self.mapper = DockerFileMapper()
        self.paths = DockerPaths()

    def __create_files(self, path_content_pair: list[tuple[str, str]]) -> None:
        """Helper function for creating files."""
        for (path, content) in path_content_pair:
            write_to_file(content, path)

    def create_dockerfiles(self) -> None:
        """Creates the required Dockerfiles in the appropriate folder."""
        os.makedirs(self.paths.ROOT_DIR, exist_ok=True)
        self.__create_files(self.mapper.dockerfiles())

    def create_compose_files(self) -> None:
        """Creates the required docker-compose files in the root directory."""
        open(self.paths.IGNORE, 'w')

        self.__create_files(self.mapper.compose_files())
