import os
import shutil
import subprocess
import urllib.request

from conf.constants import (
    AssetFilenames, 
    AssetUrls, 
    STATIC_DIR_NAME, 
    NPM_PACKAGES
)
from setup.base import ControllerBase


class LibraryController(ControllerBase):
    """A controller for handling CSS and JS libraries."""
    def __init__(self) -> None:
        tasks = [
            (self.npm_installs, "Installing NPM packages"),
            (self.get_tw_standalone, "Retrieving Tailwind standalone"),
            (self.get_flowbite, "Storing Flowbite assets"),
            (self.get_htmx, "Storing HTMX assets"),
            (self.get_alpine, "Storing AlpineJS assets")
        ]

        super().__init__(tasks)
        
    @staticmethod
    def npm_installs() -> None:
        """Installed required Node packages (TailwindCSS, Flowbite, and AlpineJS) and creates a TailwindCSS output file."""
        subprocess.run(["npm", "install", "-D", *NPM_PACKAGES], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        subprocess.run(["npx", "tailwindcss", "-i", f"./{STATIC_DIR_NAME}/css/input.css", "-o", f"./{STATIC_DIR_NAME}/css/output.css"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
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

    @staticmethod
    def get_flowbite() -> None:
        """Copies Flowbite CSS and JS from `node_modules`."""
        shutil.copy(AssetUrls.FLOWBITE_CSS, os.path.join(STATIC_DIR_NAME, 'css', AssetFilenames.FLOWBITE_CSS))
        shutil.copy(AssetUrls.FLOWBITE_JS, os.path.join(STATIC_DIR_NAME, 'js', AssetFilenames.FLOWBITE_JS))

    @staticmethod
    def get_htmx() -> None:
        """Retrieves `HTMX` from the official downloads page."""
        with urllib.request.urlopen(AssetUrls.HTMX) as response:
            htmx_content = response.read().decode('utf-8')
        
        with open(os.path.join(STATIC_DIR_NAME, 'js', AssetFilenames.HTMX), 'w') as file:
            file.write(htmx_content)

    @staticmethod
    def get_alpine() -> None:
        """Retrieves `AlpineJS` from `node_modules`."""
        shutil.copy(AssetUrls.ALPINE, os.path.join(STATIC_DIR_NAME, 'js', AssetFilenames.ALPINE))
