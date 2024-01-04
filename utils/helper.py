import os


def strip_whitespace_and_dashes(name: str) -> str:
    """Replaces whitespace and dashes with '_' for a given `name` and returns the updated version."""
    name_split = []

    if '-' in name:
        name_split = name.split('-')
    elif ' ' in name:
        name_split = name.split(' ')

    if len(name_split) != 0:
        name = '_'.join(name_split)
    
    return name.strip()


def tw_executable_exists(project_path: str) -> bool:
    """Checks if the `tailwindcss` executable exists in the project root directory."""
    windows_tw = os.path.join(project_path, 'tailwindcss.exe')
    other_tw = os.path.join(project_path, 'tailwindcss')

    # If executable exists, return True
    if os.path.exists(other_tw) or os.path.exists(windows_tw):
        return True
    return False
