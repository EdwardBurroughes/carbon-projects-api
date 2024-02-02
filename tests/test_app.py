import sqlite3

from fastapi.testclient import TestClient
from pathlib import Path
from api.db.engine import create_conn, get_db
from main import app

DB_FILE = Path(__file__).parent.joinpath("test-carbon-projects.db").as_posix()

client = TestClient(app)


async def override_get_db():
    conn = create_conn(DB_FILE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


app.dependency_overrides[get_db] = override_get_db


def test_get_projects():
    res = client.get("/projects")
    data = res.json()
    assert data[1] == {
        "id": "04d89783-9304-4daf-9130-04aa9f17cd64",
        "url": "https://fake-url-2.org",
        "status": "Under validation",
        "country": "Myanmar",
    }


def test_get_projects_by_id():
    res = client.get("/projects/04d89783-9304-4daf-9130-04aa9f17cd64")
    data = res.json()
    assert data == {
        "id": "04d89783-9304-4daf-9130-04aa9f17cd64",
        "url": "https://fake-url-2.org",
        "status": "Under validation",
        "country": "Myanmar",
    }


def test_get_projects_by_id__not_a_uuid():
    res = client.get("/projects/hello")
    assert res.status_code == 422


def test_get_projects_by_id__id_does_not_exist():
    res = client.get("/projects/c4e9ffb7-76af-4b88-af69-a2b06e2eb319")
    assert res.status_code == 404
    assert res.json()["detail"].startswith("No project returned")
