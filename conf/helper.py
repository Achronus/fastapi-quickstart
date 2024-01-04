import os
import platform


def tw_executable_exists(project_path: str) -> bool:
    """Checks if the `tailwindcss` executable exists in the project root directory."""
    windows_tw = os.path.join(project_path, 'tailwindcss.exe')
    other_tw = os.path.join(project_path, 'tailwindcss')

    # If executable exists, return True
    if os.path.exists(other_tw) or os.path.exists(windows_tw):
        return True
    return False


def dirname_check(valid_names: list[str], dir_name: str, err_msg_start: str) -> str:
    """Checks if a directory name is within a valid list of names. If it is, we return it. Otherwise, we raise an error."""
    if dir_name not in valid_names:
        return ValueError(f"{err_msg_start} must be one of: '{valid_names}'!")

    return dir_name


def tw_standalone_filename_setter() -> str:
    """Checks the type of operating system the user is on and assigns the appropriate TailwindCSS Standalone CLI installation. Returns the filename. If Unsupported, returns `unsupported`."""
    # Determine os
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
        filename = 'unsupported'

    return filename
