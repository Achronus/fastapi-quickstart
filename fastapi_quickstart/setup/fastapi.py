from .base import ControllerBase
from ..conf.constants.fastapi import FastAPIDirPaths, FastAPIContent
from ..conf.constants.filepaths import ProjectPaths
from ..conf.constants.poetry import START_CMD_OLD, START_CMD_NEW
from ..conf.file_handler import insert_into_file, replace_content
from ..config import DATABASE_URL


class FastAPIFileController(ControllerBase):
    """A FastAPI file creation controller."""
    def __init__(self) -> None:
        tasks = [
            (self.check_db, "Checking [red]database[/red] files"),
            (self.check_start_cmd, "Checking [green]run[/green] command")
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
