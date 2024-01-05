import os

from .filepaths import ProjectPaths


# FastAPI directory and filenames names
class FastAPIDirnames:
    DATABASE = 'database'


class FastAPIFilenames:
    BASE = '__init__.py'


# FastAPI directory filepaths
class FastAPIDirPaths:
    DATABASE_DIR = os.path.join(ProjectPaths.PROJECT, FastAPIDirnames.DATABASE)
    DATABASE_INIT_FILE = os.path.join(DATABASE_DIR, FastAPIFilenames.BASE)


# Define extra content
class FastAPIContent:
    SQLITE_DB_POSITION = "os.getenv('DATABASE_URL')"
    SQLITE_DB_CONTENT = ', connect_args={"check_same_thread": False}'
