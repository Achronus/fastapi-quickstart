import argparse
import os
import platform
import shutil
import subprocess
import sys
from functools import wraps
import urllib.request

from setup_assets.constants import (
    VENV,
    CORE_PIP_PACKAGES,
    SetupDirPaths,
    AssetFilenames,
    AssetUrls
)
from config import (
    ADDITIONAL_PIP_PACKAGES,
    STATIC_FILES_DIR,
    TEMPLATE_FILES_DIR,
    ENV_FILE_ADDITIONAL_PARAMS,
)

project_name = ''  # Modified by user input
KEEP_NODE_MODULES = False


# Helper functions
def __handle_project_name(project_name: str) -> str:
    """Helper function for replacing whitespace and dashes in the project name."""
    name_split = []

    if '-' in project_name:
        name_split = project_name.split('-')
    elif ' ' in project_name:
        name_split = project_name.split(' ')

    if len(name_split) != 0:
        project_name = '_'.join(name_split)
    
    return project_name.strip()


# Decorators
def readwrite_lines(path: str):
    """Decorator for using 'file.readlines()' and updating content to it."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(path, "r") as file:
                content = file.readlines()

            for i, line in enumerate(content):
                content = func(content, i, line, *args, **kwargs)

            with open(path, "w") as file:
                file.writelines(content)

        return wrapper
    return decorator


def readwrite_file(path: str):
    """Decorator for using 'file.read()' and writing replacement content to it."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(path, "r") as file:
                content = file.read()

            content = func(content, *args, **kwargs)

            with open(path, "w") as file:
                file.writelines(content)

        return wrapper
    return decorator


# Setup functions
def create_root_directory(name: str, outside_flag: bool, force_flag: bool) -> None:
    """Creates the root project directory."""
    name = __handle_project_name(name)
    print(f"Project name set to: '{name}'.\n")

    if outside_flag:
        path = os.path.join(os.path.dirname(os.getcwd()), name)
    else:
        path = os.path.join(os.getcwd(), name)
    
    qs_dir = os.path.basename(os.getcwd())
    parent_sq_dir = f"'{os.path.basename(os.path.dirname(path))}'"
    outside_folder_text = f"outside '{qs_dir}' -> into {parent_sq_dir}"
    inside_folder_text = f"inside '{qs_dir}'"
    creation_str = f"{outside_folder_text if outside_flag else inside_folder_text}..."
    print(f"Attempting project creation {creation_str}", end=' ')

    if os.path.exists(path):
        print('Failed.\n')
        print(f"Project with name '{name}' already exists!")
        if force_flag:
            print("Attempting force deletion...", end=' ')
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print('Success!')
                    print(f"Project successfully removed. Creating new one {creation_str} Success!")
                else:
                    print('Failed!')
                    print(f"The path '{path}' is not a directory.")
                    sys.exit()
            except Exception as e:
                print('Failed!')
                print(e)
                sys.exit()
        else:
            print(f"A project already exists with that name ('{name}')! Use the '--force' flag to delete it and create a new one.")
            sys.exit()
    else:
        print('Success!')

    os.makedirs(path)
    print(f"Project '{name}' created at '{path}'.\n")
    os.chdir(path)


def create_virtual_environment() -> None:
    subprocess.run(["python", "-m", "venv", "venv"])


def install_packages() -> None:
    subprocess.run([os.path.join(VENV, "pip"), "install", "--upgrade", "pip"])
    subprocess.run([os.path.join(VENV, "pip"), "install", *CORE_PIP_PACKAGES, *ADDITIONAL_PIP_PACKAGES])


def create_requirements_txt() -> None:
    with open("requirements.txt", "w") as file:
        subprocess.Popen([os.path.join(VENV, "pip"), "freeze"], stdout=file)


def make_static_dirs() -> None:
    os.makedirs(os.path.join(STATIC_FILES_DIR, "css"))
    os.makedirs(os.path.join(STATIC_FILES_DIR, "js"))
    os.makedirs(os.path.join(STATIC_FILES_DIR, "imgs"))
    os.makedirs(os.path.join(STATIC_FILES_DIR, "tailwindcss"))


def move_setup_assets_to_project() -> None:
    """Duplicates the items in the `setup_assets` folder into the respective locations in the project directory."""
    try:
        # Move core folder assets into root project dir
        shutil.copytree(SetupDirPaths.CORE, os.getcwd(), dirs_exist_ok=True)

        # Move static into static dir
        shutil.copytree(SetupDirPaths.STATIC, STATIC_FILES_DIR, dirs_exist_ok=True)

        # Move templates into templates dir
        shutil.copytree(SetupDirPaths.TEMPLATE, TEMPLATE_FILES_DIR, dirs_exist_ok=True)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"{e}\nDoes a 'setup_assets' folder exist in: '{os.getcwd()}' and contain the required folder?")


def generate_env_file() -> None:
    # Add additional custom config settings
    with open(".env", "a") as file:
        for item in ENV_FILE_ADDITIONAL_PARAMS:
            file.write(item)


def configure_npm_assets() -> None:
    subprocess.run(["npm", "install", "-D", "tailwindcss"], shell=True)
    subprocess.run(["npm", "install", "flowbite", "alpinejs"], shell=True)
    
    subprocess.run(["npx", "tailwindcss", "-i", f"./{STATIC_FILES_DIR}/css/input.css", "-o", f"./{STATIC_FILES_DIR}/css/output.css"], shell=True)


def install_tailwind_standalone() -> None:
    release_url = 'https://github.com/tailwindlabs/tailwindcss/releases/latest/download/'

    # Determine the platform
    system_platform = platform.system().lower()
    machine = platform.machine()

    # Define the filename based on the platform
    if system_platform == 'darwin' and machine == 'arm64':
        filename = 'tailwindcss-macos-arm64'
    elif system_platform == 'darwin' and machine == 'x86_64':
        filename = 'tailwindcss-macos-x64'
    elif system_platform == 'linux' and machine == 'arm64':
        filename = 'tailwindcss-linux-arm64'
    elif system_platform == 'linux' and machine == 'armv7l':
        filename = 'tailwindcss-linux-armv7'
    elif system_platform == 'linux' and machine == 'x86_64':
        filename = 'tailwindcss-linux-x64'
    elif system_platform == 'windows' and machine == 'AMD64':
        filename = 'tailwindcss-windows-x64.exe'
    elif system_platform == 'windows' and machine == 'arm64':
        filename = 'tailwindcss-windows-arm64.exe'
    else:
        print("OS not supported for standalone TailwindCSS. Keeping `node_modules`.")
        KEEP_NODE_MODULES = True

    # Download the file
    try:
        with urllib.request.urlopen(release_url + filename) as response, open(filename, 'wb') as file:
            file.write(response.read())

        # Make executable if not windows exe
        if not filename.endswith('.exe'):
            os.chmod(filename, 0o755)

        _, extension = os.path.splitext(filename)
        os.rename(filename, f'tailwindcss{extension}')

    except Exception as e:
        print(f"Error: {e}")


def download_js_libraries_to_static() -> None:
    # Copy Flowbite from node_modules
    shutil.copy(AssetUrls.FLOWBITE_CSS, os.path.join(STATIC_FILES_DIR, 'css', AssetFilenames.FLOWBITE_CSS))
    shutil.copy(AssetUrls.FLOWBITE_JS, os.path.join(STATIC_FILES_DIR, 'js', AssetFilenames.FLOWBITE_JS))

    # Retrieve HTMX from official downloads page
    with urllib.request.urlopen(AssetUrls.HTMX) as response:
        htmx_content = response.read().decode('utf-8')
    
    with open(os.path.join(STATIC_FILES_DIR, 'js', AssetFilenames.HTMX), 'w') as file:
        file.write(htmx_content)

    # Retrieve AlpineJS from node_modules
    shutil.copy(AssetUrls.ALPINE, os.path.join(STATIC_FILES_DIR, 'js', AssetFilenames.ALPINE))


def remove_node_modules() -> None:
    if not KEEP_NODE_MODULES:
        shutil.rmtree(os.path.join(os.getcwd(), 'node_modules'))


def create_fastapi_files() -> None:
    pass


def run_setup() -> None:
    # Step 2: Create a virtual environment
    print('Creating virtual environment...')
    create_virtual_environment()

    # Step 3: Access virtual environment, update pip, and install packages
    install_packages()

    # Step 4: Create requirements.txt
    create_requirements_txt()

    # Step 5: Moving root, static, and template setup assets to project
    print('Creating static files and templates...', end='')
    move_setup_assets_to_project()

    # Step 6: Generate .env file
    generate_env_file()
    print("Complete.")

    # Step 7: Add Tailwind CSS and Flowbite
    print("Installing Tailwind CSS...")
    configure_npm_assets()
    install_tailwind_standalone()

    # Step 8: Add HTMX, AlpineJS, and Flowbite to static folder
    print("Downloading HTMX, AlpineJS, and Flowbite...", end='')
    download_js_libraries_to_static()
    print("Complete.")

    # Step 9: Clean-up folder
    print("Tidying project folder...", end='')
    remove_node_modules()
    print("Complete.")

    # Step 10: Create FastAPI files
    print('Creating FastAPI files...', end='')
    create_fastapi_files()
    print('Complete.')

    # Warn users if required
    if KEEP_NODE_MODULES:
        print(f"Note: Standalone TailwindCSS failed to install due to incompatible OS. Please run Tailwind through 'npx' ->\n\t'npx tailwindcss -i ./{STATIC_FILES_DIR}/assets/input.css -o ./{STATIC_FILES_DIR}/assets/output.css --watch --minify'")

    # End of script
    print("Setup completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple way to create a new Django, TailwindCSS, HTMX, and AlpineJS project, fast.")
    parser.add_argument("name", help="Name of the project directory. Note: automatically converts 'whitespace' and '-' to '_'.", type=str)
    parser.add_argument("--outside", action="store_true", help="Create the directory outside the setup folder.")
    parser.add_argument("--force", action="store_true", help="Forcefully remove an existing directory with the same name.")

    args = parser.parse_args()

    # Step 1: Create a root project directory
    create_root_directory(args.name, args.outside, args.force)

    # Run setup
    run_setup()
