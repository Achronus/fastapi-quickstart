import os
import shutil

from ..conf.helper import tw_executable_exists
from .base import ControllerBase


class CleanupController(ControllerBase):
    """A controller for handling project cleanup."""
    def __init__(self) -> None:
        tasks = [
            (self.node_modules, "Removing [magenta]node_modules[/magenta]")
        ]

        super().__init__(tasks)
    
    @staticmethod
    def node_modules() -> None:
        """Removes the `node_modules` folder if `tailwindcss` does not exist."""
        # If exists, remove node_modules
        if tw_executable_exists(os.getcwd()):
            shutil.rmtree(os.path.join(os.getcwd(), 'node_modules'))
