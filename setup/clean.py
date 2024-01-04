import os
import shutil

from conf.constants import PASS
from utils.helper import task_desc_formatter, tw_executable_exists

from rich.progress import Progress


class ProjectCleanup:
    """A controller for handling project cleanup."""
    @staticmethod
    def node_modules() -> None:
        """Removes the `node_modules` folder if `tailwindcss` does not exist."""
        shutil.rmtree(os.path.join(os.getcwd(), 'node_modules'))

    @classmethod
    def run(cls, progress: Progress) -> None:
        """Runs controller sub-tasks."""
        sub_tasks = []

        # If exists, remove node_modules
        if tw_executable_exists(os.getcwd()):
            sub_tasks.append(
                (cls.node_modules, task_desc_formatter("Removing [magenta]node_modules[/magenta]"))
            )

        for task, desc in sub_tasks:
            task_id = progress.add_task(description=desc, total=None)
            task()
            progress.update(task_id, completed=1, description=f"{desc} {PASS}")
