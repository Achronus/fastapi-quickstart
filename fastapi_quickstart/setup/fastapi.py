from .base import ControllerBase
from ..conf.constants.fastapi import FastAPIDirPaths, FastAPIContent
from ..conf.constants.filepaths import ProjectPaths
from ..conf.constants.poetry import START_CMD_OLD, START_CMD_NEW, BUILD_FILE_CONTENT
from ..conf.file_handler import insert_into_file, replace_content
from ..config import DATABASE_URL


class FastAPIFileController(ControllerBase):
    """A FastAPI file creation controller."""
    def __init__(self) -> None:
        tasks = [
            (self.check_db, "Checking [red]database[/red] files"),
            (self.check_start_cmd, "Checking [green]run[/green] command"),
            (self.create_build, "Creating [yellow]build[/yellow] file")
        ]

        super().__init__(tasks)

    @staticmethod
    def check_db() -> None:
        """Checks that the correct database config is setup."""
        sqlite_db = DATABASE_URL.split(':')[0] == 'sqlite'

        if sqlite_db:
            insert_into_file(
                FastAPIContent.SQLITE_DB_POSITION, 
                FastAPIContent.SQLITE_DB_CONTENT, 
                FastAPIDirPaths.DATABASE_INIT_FILE
            )

    @staticmethod
    def check_start_cmd() -> None:
        """Updates start server command."""
        replace_content(START_CMD_OLD, START_CMD_NEW, ProjectPaths.PROJECT_MAIN)

    @staticmethod
    def create_build() -> None:
        """Creates a build file in the root directory for watching TailwindCSS."""
        with open(ProjectPaths.PROJECT_BUILD, 'w') as file:
            file.write(BUILD_FILE_CONTENT)
