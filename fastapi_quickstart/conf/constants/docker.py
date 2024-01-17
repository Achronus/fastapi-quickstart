import textwrap

from .filepaths import get_project_name


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


class DockerContent:
    def __init__(self) -> None:
        self.dotenv_config = DockerEnvConfig()

    def env_config(self) -> str:
        return textwrap.dedent(f"""
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
        """)[1:]
    
    