import os
import sys
import subprocess
import venv

from conf.constants import (
    VENV, 
    VENV_LOCATION,
    CLI_PIP_PACKAGES
)

if __name__ == '__main__':
    # If first load, create virtual environment for the CLI
    if not os.path.exists(VENV_LOCATION):
        venv.create(VENV_LOCATION, with_pip=True)

        subprocess.run([os.path.join(VENV, "pip"), "install", *CLI_PIP_PACKAGES], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    activate_script = os.path.join(VENV, 'activate')
    activate_cmd = f"source {activate_script}" if sys.platform.startswith('linux') or sys.platform == 'darwin' else f"{activate_script}"
    subprocess.run(activate_cmd, shell=True)

    # subprocess.run([os.path.join(VENV, 'activate')], shell=True)
    print(hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))    
