from DB.connection import SQLiteConnection
from typing import Any

def pull_posts() -> list[Any]:
    with SQLiteConnection() as sql:
        data = sql.cur.execute('SELECT * FROM posts').fetchall()
    return data