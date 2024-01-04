from conf.constants import PASS
from rich.progress import Progress


class ControllerBase:
    """A parent class for all controllers."""
    def __init__(self, tasks: list[tuple]) -> None:
        self.sub_tasks = tasks

    @staticmethod
    def subtask_desc(desc: str) -> str:
        """Standardises the sub-task description."""
        return f"   {desc}..."

    def format_tasks(self, tasks: list[tuple]) -> list[tuple]:
        """Formats controller tasks into a suitable format and adds them to a `sub_tasks` list. Returns the updated list."""
        sub_tasks = []
        for task, desc in tasks:
            sub_tasks.append((task, self.subtask_desc(desc)))
        return sub_tasks

    def run(self, progress: Progress) -> None:
        for task, desc in self.sub_tasks:
            task_id = progress.add_task(description=desc, total=None)
            task()
            progress.update(task_id, completed=1, description=f"{desc} {PASS}")
