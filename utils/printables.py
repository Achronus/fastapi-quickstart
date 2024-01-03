import os

from conf.constants import PASS, FAIL

from rich.table import Table


def project_table(name: str, path: str) -> Table:
    """Creates a printable project table showing whether it exists based on a `name` and `path`."""
    colour, icon = ('green', PASS) if os.path.exists(path) else ('red', FAIL)
        
    table = Table()
    table.add_column("Project", style="cyan", justify="center")
    table.add_column("Exists", style=colour, justify="center")
    table.add_row(name, icon)
    return table
