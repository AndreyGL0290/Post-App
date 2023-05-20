from DB.connection import SQLiteConnection

def delete_post(post_id: int) -> None:
    with SQLiteConnection() as sql:
        sql.cur.execute(f"DELETE FROM posts WHERE id={post_id}")