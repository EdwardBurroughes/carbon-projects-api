import sqlite3
import uuid
from typing import List

from api.utils.query_handler import execute_query


def get_all_projects_query(db: sqlite3.Connection) -> List[dict]:
    return execute_query(db, "SELECT * FROM projects")


def get_project_by_id_query(
    db: sqlite3.Connection, project_id: uuid.UUID
) -> List[dict]:
    # sqlite does not support uuid types so it's needed to be converted to a string
    return execute_query(db, "SELECT * FROM projects WHERE id=?", (str(project_id),))
