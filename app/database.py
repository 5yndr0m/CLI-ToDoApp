"""This module provides the ToDo database functionality."""
# app/database.py

import configparser
from pathlib import Path
from app import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path:
    """Return the current path to the ToDo database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    """Create the ToDo database."""
    try:
        db_path.write_text("[]") #empty todo list
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR