import textwrap

from .filepaths import get_project_name, DockerPaths


class DockerEnvConfig:
    def __init__(self) -> None:
        import importlib.metadata
        self.poetry_version = importlib.metadata.version('poetry')
        self.project_name = get_project_name()

        # Docker-compose
        self.ports = "8080:80"

        # Uvicorn
        self.port = self.ports.split(':')[-1]
        self.host = "0.0.0.0"

        self.python_version = '3.12'
        self.version_extension = '.1'


class DockerContent:
    def __init__(self) -> None:
        self.dotenv_config = DockerEnvConfig()

    @staticmethod
    def __format(content: str) -> str:
        """Helper function for formatting file content."""
        return textwrap.dedent(content)[1:]

    def env_config(self) -> str:
        return self.__format(f"""
        #--------------------------
        # ENVIRONMENT SETTINGS
        #--------------------------
        # !IMPORTANT! CHANGE TO 'prod' WHEN IN PRODUCTION
        # Options: 'dev' or 'prod'
        ENV_TYPE=dev
        
        #--------------------------
        # DOCKER CONFIG SETTINGS
        # -------------------------
        # Docker config
        POETRY_VERSION={self.dotenv_config.poetry_version}
        PROJECT_NAME={self.dotenv_config.project_name}
        PORTS={self.dotenv_config.ports}

        # Uvicorn
        PORT={self.dotenv_config.port}
        HOST={self.dotenv_config.host}
        """)
    
    def backend_df(self) -> str:
        """The content for the backend Dockerfile."""
        start = f"""
        # Dockerfile for FastAPI
        ARG PYTHON_VERSION={self.dotenv_config.python_version}
        ARG BUILD_VERSION=${{PYTHON_VERSION}}{self.dotenv_config.version_extension}
        """

        return self.__format(start + """

        # --- Build Stage ---
        FROM python:${BUILD_VERSION}-slim as builder

        ARG ENV_TYPE
        ARG POETRY_VERSION
        ARG PROJECT_NAME

        # Set environment variables
        ENV YOUR_ENV=${ENV_TYPE} \\
            PYTHONFAULTHANDLER=1 \\
            PYTHONUNBUFFERED=1 \\
            PYTHONHASHSEED=random \\
            PIP_NO_CACHE_DIR=off \\
            PIP_DISABLE_PIP_VERSION_CHECK=on \\
            PIP_DEFAULT_TIMEOUT=100

        # Install system dependencies
        RUN apt-get update && \\
            apt-get install -y gcc libffi-dev libssl-dev curl && \\
            pip install --upgrade pip "poetry==${POETRY_VERSION}" && \\
          rm -rf /var/lib/apt/lists/*

        # Set working directory
        WORKDIR /${PROJECT_NAME}

        # Copy project files (including poetry.lock and pyproject.toml)
        COPY ./poetry.lock* ./pyproject.toml /${PROJECT_NAME}/

        # Create requirements.txt
        RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

        # Install packages and perform clean-up
        RUN pip install --no-cache-dir --upgrade -r requirements.txt


        # --- Production Stage ---
        FROM python:${BUILD_VERSION}-alpine as runner

        ARG PROJECT_NAME
        ARG PORT
        ARG PYTHON_VERSION

        ENV PYTHON_PACKAGE_VERSION=/usr/local/lib/python${PYTHON_VERSION}/site-packages

        # Set the working directory
        WORKDIR /${PROJECT_NAME}

        # Copy app files
        COPY --from=builder /${PROJECT_NAME} /${PROJECT_NAME}
        COPY --from=builder ${PYTHON_PACKAGE_VERSION} ${PYTHON_PACKAGE_VERSION}

        # Expose the port for FastAPI
        EXPOSE ${PORT}

        # Run FastAPI server (uses docker-compose.yml)
        CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
        """)

    def compose_main(self) -> str:
        """The content for the main (entry point) Docker Compose file."""
        return self.__format("""
        version: '1'

        services:
          backend:
            build:
              context: .
              dockerfile: ./config/docker/Dockerfile.backend
              args:
                POETRY_VERSION: ${POETRY_VERSION}
                PROJECT_NAME: ${PROJECT_NAME}
                ENV_TYPE: ${ENV_TYPE}
                PORT: ${PORT}
            ports:
            - "${PORTS}"
            volumes:
            - .:/${PROJECT_NAME}
            env_file:
            - .env
            command: python -m uvicorn ${PROJECT_NAME}.main:app --host ${HOST} --port ${PORT} --reload
        """)


class DockerFileMapper:
    def __init__(self) -> None:
        self.content = DockerContent()
        self.paths = DockerPaths()

    def dockerfiles(self) -> list[tuple[str, str]]:
        """Maps the pairs of filepaths and content for Dockerfiles."""
        return [
            (self.paths.BACKEND_DF, self.content.backend_df())
        ]

    def compose_files(self) -> list[tuple[str, str]]:
        """Maps the pairs of filepaths and content for Docker compose files."""
        return [
            (self.paths.COMPOSE_MAIN, self.content.compose_main())
        ]
