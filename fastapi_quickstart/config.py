# Select a static files directory name
# Options: ['static', 'public', 'assets']
STATIC_FILES_DIR = "assets"  

# Configure virtual environment name
VENV_NAME = 'env'

# Define your database URL
DATABASE_URL = 'sqlite:///./sql_app.db'
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Pip packages to install
ADDITIONAL_PIP_PACKAGES = [
    "pytest"
]

# .env file additional parameters
ENV_FILE_ADDITIONAL_PARAMS = [
    # f'example={example}'  # example
]
