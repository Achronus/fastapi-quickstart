import os
import shutil
import subprocess
import urllib.request

from ..conf.constants import NPM_PACKAGES
from ..conf.constants.filepaths import AssetFilenames, AssetUrls
from .base import ControllerBase


class LibraryController(ControllerBase):
    """A controller for handling CSS and JS libraries."""
    def __init__(self) -> None:
        tasks = [
            (self.npm_installs, "Installing [red]NPM[/red] packages"),
            (self.get_tw_standalone, "Retrieving [bright_blue]TailwindCSS[/bright_blue] standalone CLI"),
            (self.get_flowbite, "Storing [bright_blue]Flowbite[/bright_blue] assets"),
            (self.get_htmx, "Storing [bright_cyan]HTMX[/bright_cyan] assets"),
            (self.get_alpine, "Storing [bright_cyan]AlpineJS[/bright_cyan] assets")
        ]

        super().__init__(tasks)
        
    @staticmethod
    def npm_installs() -> None:
        """Installed required Node packages (TailwindCSS, Flowbite, and AlpineJS) and creates a TailwindCSS output file."""
        from ..conf.constants.poetry import TW_CMD

        subprocess.run(["npm", "install", "-D", *NPM_PACKAGES], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        subprocess.run(["npx", *TW_CMD.split(' ')], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    @staticmethod
    def get_tw_standalone() -> None:
        filename = AssetFilenames.TW_STANDALONE

        if filename != 'unsupported':
            try:
                with urllib.request.urlopen(AssetUrls.TW_STANDALONE + filename) as response, open(filename, 'wb') as file:
                    file.write(response.read())

                # Make executable if not windows exe
                if not filename.endswith('.exe'):
                    os.chmod(filename, 0o755)

                _, extension = os.path.splitext(filename)
                os.rename(filename, f'tailwindcss{extension}')

            except Exception as e:
                print(f"Error: {e}")

    def get_flowbite(self) -> None:
        """Copies Flowbite CSS and JS from `node_modules`."""
        shutil.copy(AssetUrls.FLOWBITE_CSS, os.path.join(self.project_paths.CSS, AssetFilenames.FLOWBITE_CSS))
        shutil.copy(AssetUrls.FLOWBITE_JS, os.path.join(self.project_paths.JS, AssetFilenames.FLOWBITE_JS))

    def get_htmx(self) -> None:
        """Retrieves `HTMX` from the official downloads page."""
        with urllib.request.urlopen(AssetUrls.HTMX) as response:
            htmx_content = response.read().decode('utf-8')
        
        with open(os.path.join(self.project_paths.JS, AssetFilenames.HTMX), 'w') as file:
            file.write(htmx_content)

    def get_alpine(self) -> None:
        """Retrieves `AlpineJS` from `node_modules`."""
        shutil.copy(AssetUrls.ALPINE, os.path.join(self.project_paths.JS, AssetFilenames.ALPINE))
