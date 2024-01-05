from .base import ControllerBase
from ..conf.constants.fastapi import FastAPIDirPaths, FastAPIContent
from ..conf.file_handler import insert_into_file
from ..config import DATABASE_URL


class FastAPIFileController(ControllerBase):
    """A FastAPI file creation controller."""
    def __init__(self) -> None:
        tasks = [
            (self.check_db, "Checking [red]database[/red] files")
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
