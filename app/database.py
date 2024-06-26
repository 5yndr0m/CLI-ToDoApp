"""This module provides the ToDo database functionality."""
# app/database.py

import configparser
import json
from pathlib import Path
from typing import Any, Dict, List, NamedTuple
from app import DB_WRITE_ERROR, DB_READ_ERROR, JSON_ERROR, SUCCESS

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

class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]
    error: int

class DatabaseHandler:
    def __init__(self, db_path:Path) -> None:
        self.db_path = db_path

    def read_todos(self) -> DBResponse:
        try:
            with self.db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                except json.JSONDecodeError:#catch wrong JSON format
                    return DBResponse([], JSON_ERROR)
        except OSError:#catch file IO problems
            return DBResponse([], DB_READ_ERROR)

    def write_todos(self, todo_list: List[Dict[str, Any]]) -> DBResponse:
        try:
            with self.db_path.open("w") as db:
                json.dump(todo_list, db, indent=4)
            return DBResponse(todo_list, SUCCESS)
        except OSError:#catch file IO problem
            return DBResponse(todo_list, DB_WRITE_ERROR)
