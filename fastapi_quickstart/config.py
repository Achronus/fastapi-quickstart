# Define your database URL
DATABASE_URL = 'sqlite:///./database.db'
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Core packages to install
ADDITIONAL_PIP_PACKAGES = [
    "langchain",
    "llama-index"
]

# Development packages to install
DEV_PACKAGES = [
    "pytest",
    "pytest-cov",
    "hypothesis"
]

# .env file additional parameters
ENV_FILE_ADDITIONAL_PARAMS = [
    # f'example={example}'  # example
]
