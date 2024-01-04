import os

from ..conf.constants import PASS, FAIL, PARTY

from rich.table import Table
from rich.panel import Panel


def project_table(name: str, path: str) -> Table:
    """Creates a printable project table showing whether it exists based on a `name` and `path`."""
    colour, icon = ('green', PASS) if os.path.exists(path) else ('red', FAIL)
        
    table = Table()
    table.add_column("Project", style="cyan", justify="center")
    table.add_column("Exists", style=colour, justify="center")
    table.add_row(name, icon)
    return table


def project_complete_panel() -> Panel:
    """Creates a printable project complete panel."""
    panel = Panel.fit(f"\n{PARTY} Project created successfully! {PARTY}", height=5, border_style="bright_green", style="bright_green")
    return panel
