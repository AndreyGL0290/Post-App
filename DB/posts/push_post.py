from DB.connection import SQLiteConnection

def push_post(post_text: str) -> None:
    with SQLiteConnection() as sql:
        sql.cur.execute(f"INSERT INTO posts (post_text) VALUES ('{post_text}')")