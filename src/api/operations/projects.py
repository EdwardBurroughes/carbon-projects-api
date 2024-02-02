import sqlite3
import uuid
from fastapi import HTTPException
from typing import List

from api.db.models import get_all_projects_query, get_project_by_id_query
from api.operations.models import ProjectsResult


def get_all_projects_op(db: sqlite3.Connection) -> List[ProjectsResult]:
    projects = get_all_projects_query(db)
    return [ProjectsResult(**project) for project in projects]


def get_project_by_id_op(db: sqlite3.Connection, id: uuid.UUID) -> ProjectsResult:
    project = get_project_by_id_query(db, id)
    if not project:
        raise HTTPException(status_code=404, detail=f"No project returned for id, {id}")
    return ProjectsResult(**project[0])
