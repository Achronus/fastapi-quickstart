import textwrap

from .base import ControllerBase
from ..conf.constants.fastapi import FastAPIDirPaths, FastAPIContent
from ..conf.constants.poetry import PoetryCommands, PoetryContent
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

        self.poetry_commands = PoetryCommands()
        self.poetry_content = PoetryContent()

        self.dir_paths = FastAPIDirPaths()

    def check_db(self) -> None:
        """Checks that the correct database config is setup."""
        sqlite_db = DATABASE_URL.split(':')[0] == 'sqlite'

        if sqlite_db:
            insert_into_file(
                FastAPIContent.SQLITE_DB_POSITION, 
                FastAPIContent.SQLITE_DB_CONTENT, 
                self.dir_paths.DATABASE_INIT_FILE
            )

    def check_start_cmd(self) -> None:
        """Updates start server command."""
        replace_content(
            self.poetry_content.START_CMD_OLD, 
            self.poetry_content.START_CMD_NEW, 
            self.project_paths.PROJECT_MAIN
        )

    def create_build(self) -> None:
        """Creates a build file in the root directory for watching TailwindCSS."""
        content = textwrap.dedent(self.poetry_content.BUILD_FILE_CONTENT)

        with open(self.project_paths.PROJECT_BUILD, 'w') as file:
            file.write(content)
