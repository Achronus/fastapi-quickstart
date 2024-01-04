from ..conf.constants import PASS

from rich.progress import Progress


class ControllerBase:
    """A parent class for all controllers.
    
    :param tasks: (list[tuple]) - a list of tuples in the format of (task, desc), where `task` is a class method and `desc` is a descriptive string highlighting what the task does. For example:
    ```python
    sub_tasks = [
        (self.create, "Building venv"), 
        (self.update_pip, "Updating PIP")
    ]
    ```
    """
    def __init__(self, tasks: list[tuple]) -> None:
        self.tasks = tasks

    @staticmethod
    def update_desc(desc: str) -> str:
        """Updates task description format."""
        return f"   {desc}..."

    def format_tasks(self) -> None:
        """Formats controller tasks into a standardised format."""
        updated_tasks = []
        for task, desc in self.tasks:
            updated_tasks.append((task, self.update_desc(desc)))
        
        self.tasks = updated_tasks

    def run(self, progress: Progress) -> None:
        self.format_tasks()

        for task, desc in self.tasks:
            task_id = progress.add_task(description=desc, total=None)
            task()
            progress.update(task_id, completed=1, description=f"{desc} {PASS}")
