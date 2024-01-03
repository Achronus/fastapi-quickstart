from rich.console import Console

TASKS = [
    'test',
    'test'
]

console = Console()


def run_tasks() -> None:
    """The task handler for performing each operation in the CLI."""
    for task in TASKS:
        console.print('test')

