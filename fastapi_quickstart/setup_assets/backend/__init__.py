import os
from pathlib import Path

from fastapi.templating import Jinja2Templates


ROOT_PATH = Path(__file__).resolve().parent.parent

PROJECT_DIR = os.path.basename(ROOT_PATH)
FRONTEND_DIR = os.path.join(PROJECT_DIR, 'frontend')

templates = Jinja2Templates(directory=os.path.join(FRONTEND_DIR, "templates"))
