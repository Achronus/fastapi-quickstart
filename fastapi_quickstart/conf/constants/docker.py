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

        self.python_version = '3.12.1'


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
        # DOCKER CONFIG SETTINGS
        # -------------------------
        # Docker config
        POETRY_VERSION={self.dotenv_config.poetry_version}
        PROJECT_NAME={self.dotenv_config.project_name}
        PORTS={self.dotenv_config.ports}

        # Uvicorn
        PORT={self.dotenv_config.port}
        HOST={self.dotenv_config.host}

        #--------------------------
        # CUSTOM CONFIG SETTINGS
        #--------------------------
        """)
    
    def backend_df(self) -> str:
        """The content for the backend Dockerfile."""
        start = f"""
        # Dockerfile for FastAPI
        FROM python:{self.dotenv_config.python_version}-slim
        """

        return self.__format(start + """
        ARG ENV_TYPE
        ARG POETRY_VERSION
        ARG PROJECT_NAME
        ARG PORT

        ENV YOUR_ENV=${ENV_TYPE} \\
        \tPYTHONFAULTHANDLER=1 \\
        \tPYTHONUNBUFFERED=1 \\
        \tPYTHONHASHSEED=random \\
        \tPIP_NO_CACHE_DIR=off \\
        \tPIP_DISABLE_PIP_VERSION_CHECK=on \\
        \tPIP_DEFAULT_TIMEOUT=100

        # System deps:
        RUN pip install "poetry==${POETRY_VERSION}"

        # Copy only requirements to cache them in docker layer
        WORKDIR /${PROJECT_NAME}

        COPY poetry.lock pyproject.toml /${PROJECT_NAME}/

        # Project initialization:
        RUN poetry config virtualenvs.create false \\
        \t&& poetry install $(test "$YOUR_ENV" == prod && echo "--no-dev") --no-interaction --no-ansi

        # Creating folders, and files for a project:
        COPY . /${PROJECT_NAME}

        # Expose the port for FastAPI
        EXPOSE ${PORT}

        # Command to run the FastAPI application
        RUN poetry install
        CMD ["run"]
        """)

    def compose_base(self) -> str:
        """The content for the Docker Compose base file."""
        return self.__format("""
        services:
          base:
            build:
              context: .
              dockerfile: ./config/docker/Dockerfile.backend
              args:
                POETRY_VERSION: ${POETRY_VERSION}
                PROJECT_NAME: ${PROJECT_NAME}
                PORT: ${PORT}
            ports:
            - "${PORTS}"
            volumes:
            - .:/${PROJECT_NAME}
            env_file:
            - .env
        """)

    def compose_main(self) -> str:
        """The content for the main (entry point) Docker Compose file."""
        return self.__format("""
        version: '1'

        services:
          dev:
            container_name: backend
            extends:
              file: docker-compose.base.yml
              service: base
            build:
              args:
                ENV_TYPE: dev
            command: uvicorn ${PROJECT_NAME}.main:app --host ${HOST} --port ${PORT} --reload

          prod:
            container_name: backend
            extends:
              file: docker-compose.base.yml
              service: base
            build:
              args:
                ENV_TYPE: prod
            command: uvicorn ${PROJECT_NAME}.main:app --host ${HOST} --port ${PORT}
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
            (self.paths.COMPOSE_BASE, self.content.compose_base()),
            (self.paths.COMPOSE_MAIN, self.content.compose_main())
        ]
