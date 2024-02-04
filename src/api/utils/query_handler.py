import sqlite3
from typing import Tuple, Any, Optional, List
import logging

from fastapi import HTTPException


def _cursor_execute(
    conn: sqlite3.Connection, query: str, params: Tuple[Any]
) -> List[dict]:
    # I've not used a context manager to manage the sqlite transactions
    # as only selecting the data, as such non-transactional.
    cur = conn.cursor()
    cur.execute(query, params)
    return cur.fetchall()


def execute_query(
    conn: sqlite3.Connection, query: str, params: Optional[Tuple[Any]] = None
) -> List[dict]:
    if params is None:
        params = []
    try:
        return _cursor_execute(conn, query, params)
    except Exception as e:
        logging.error(
            f" failed to run query due to the following error: {e} with query {query}"
        )
        raise HTTPException(
            status_code=500, detail="Iternal Server error, failed to retrieve data"
        )
