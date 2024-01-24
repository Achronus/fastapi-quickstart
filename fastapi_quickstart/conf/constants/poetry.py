from . import STATIC_DIR_NAME
from ..helper import set_tw_standalone_filename
from .filepaths import get_project_name, AssetFilenames


# Define Poetry script commands
class PoetryCommands:
    def __init__(self) -> None:
        self.project_name = get_project_name()
        
        self.TW_CMD = 'tailwindcss -i {INPUT_PATH} -o {OUTPUT_PATH}'
        self.WATCH_TW_CMD = f"{self.TW_CMD} --watch --minify"

        self.INIT_CMD = f"{self.project_name}.{AssetFilenames.BUILD.split('.')[0]}"
        self.START_SERVER_CMD = f"{self.INIT_CMD}:start"
        self.WATCH_POETRY_CMD = f"{self.INIT_CMD}:tw_build"

# Define Poetry script content
# Specific to setup/venv.py -> init_project()
class PoetryContent:
    def __init__(self) -> None:
        self.tw_type = set_tw_standalone_filename()
        self.project_name = get_project_name()
        self.commands = PoetryCommands()

        self.SCRIPT_INSERT_LOC = 'readme = "README.md"'
        self.SCRIPT_CONTENT = '\n'.join([
            "exclude = [",
            f'\t"{self.project_name}/tailwind.config.js",',
            f'\t"{self.project_name}/tailwindcss.exe"',
            "]\n",
            "[tool.poetry.scripts]",
            f'run = "{self.commands.START_SERVER_CMD}"',
            f'watch = "{self.commands.WATCH_POETRY_CMD}"'
        ])

        self.start_desc = '"""Start the server."""'
        self.build_desc = '"""Build TailwindCSS."""'
        self.BUILD_FILE_CONTENT = f"""
        import os
        import subprocess
        from pathlib import Path
        from dotenv import load_dotenv

        import uvicorn

        ROOT_PATH = Path(__file__).resolve().parent.parent
        ROOT_ENV = os.path.join(ROOT_PATH, '.env')

        load_dotenv(ROOT_ENV)

        PROJECT_DIR = os.path.basename(ROOT_PATH)
        CSS_DIR = os.path.join('frontend', '{STATIC_DIR_NAME}', 'css')
        INPUT_PATH = os.path.join(CSS_DIR, 'input.css')
        OUTPUT_PATH = os.path.join(CSS_DIR, 'styles.min.css')

        def start() -> None:
            {self.start_desc}
            reload_check = True if os.getenv('ENV_TYPE') == 'dev' else False

            uvicorn.run(
                f"{{os.getenv('PROJECT_NAME')}}.backend.main:app", 
                host=os.getenv('HOST'), 
                port=int(os.getenv('PORT')), 
                reload=reload_check 
        )


        def tw_build() -> None:
            {self.build_desc}
            cmd = f"{'npx ' if self.tw_type == 'unsupported' else ''}{self.commands.WATCH_TW_CMD}"
            os.chdir(os.path.join(os.getcwd(), '{self.project_name}'))
            subprocess.run(cmd.split(' '), check=True)
        """
