import sqlite3
import uuid
from fastapi import HTTPException
from typing import List

from src.api.db.models import get_all_projects_query, get_project_by_id_query
from src.api.operations.models import ProjectsResult


def get_all_projects_op(db: sqlite3.Connection) -> List[ProjectsResult]:
    projects = get_all_projects_query(db)
    return [ProjectsResult(**project) for project in projects]


def get_project_by_id_op(db: sqlite3.Connection, id: uuid.UUID) -> ProjectsResult:
    if not isinstance(id, uuid.UUID):
        raise HTTPException(
            status_code=422, detail="Invalid Project Parameter: id must be a uuid"
        )
    project = get_project_by_id_query(db, id)
    if not project:
        raise HTTPException(status_code=404, detail=f"no project returned for id, {id}")
    return ProjectsResult(**project[0])
