

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


def task_desc_formatter(desc: str) -> str:
    """Adds custom formatting to a task description."""
    return f"   {desc}..."
