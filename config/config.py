import os
from pathlib import Path

from dotenv import dotenv_values

__project__ = "project-x"

BASE_DIR = Path(__file__).parent.parent.absolute()
DATA_DIR = BASE_DIR / "data"

ENV_VARIABLES = {
    **dotenv_values(dotenv_path=BASE_DIR / ".env"),
    **os.environ,
}


os.environ["API_BASE"] = ENV_VARIABLES.get("API_BASE", "http://ollama:11434")
