import sqlite3
import uuid

from fastapi import APIRouter, Depends

from api.db.engine import get_db
from api.operations.projects import get_all_projects_op, get_project_by_id_op

router = APIRouter()


@router.get("/projects")
async def get_all_projects(db: sqlite3.Connection = Depends(get_db)):
    return get_all_projects_op(db)


@router.get("/projects/{id}")
async def get_project_by_id(id: uuid.UUID, db: sqlite3.Connection = Depends(get_db)):
    return get_project_by_id_op(db, id)
