from os import getenv
import sqlite3

class SQLiteConnection():
    def __init__(self) -> None:
        self.conn = sqlite3.connect(getenv('DB_PATH'))
        self.cur = sqlite3.Cursor(self.conn)
    
    def __enter__(self, *args, **kwargs):
        return self
    
    def __exit__(self, *args, **kwargs):
        self.conn.commit()
        self.conn.close()