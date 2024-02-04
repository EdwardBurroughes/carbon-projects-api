import sqlite3
from pathlib import Path
from typing import Generator

current_path = Path(__file__)
DB_FILE = current_path.parent.joinpath("carbon-projects.db").as_posix()


def create_conn(db_path: str) -> sqlite3.Connection:
    return sqlite3.connect(db_path, check_same_thread=False)


async def get_db() -> Generator[sqlite3.Connection, None, None]:
    conn = create_conn(DB_FILE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
