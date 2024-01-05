

def write_to_file(item: str, path: str) -> None:
    """Stores an item in a file."""
    with open(path, "w") as file:
        file.write(item)


def add_content_to_file(content: str, path: str) -> None:
    """Writes multiple lines (`content`) to a file at `path`."""
    with open(path, "w") as file:
        file.writelines(content)


def read_all_file_content(path: str) -> str:
    """Retrieves all content from a basic file."""
    with open(path, 'r') as file:
        content = file.read()
    
    return content


def insert_into_file(position: str, new_content: str, path: str) -> None:
    """Adds `new_content` to a file (`path`) at a specific `position`.
    
    Note: `new = (position + new_content).strip()`."""
    content = read_all_file_content(path)

    content = content.replace(
        position,
        (position + new_content).strip(),
        1
    )

    add_content_to_file(content, path)


def replace_content(old: str, new: str, path: str) -> None:
    """Replaces `old` content with `new` ones in a file at `path`."""
    content = read_all_file_content(path)

    content = content.replace(
        old,
        new.strip(),
        1
    )

    add_content_to_file(content, path)
