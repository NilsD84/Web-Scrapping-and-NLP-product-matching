import sqlite3


class SQLiteDB:
    def __init__(self, db_path="products.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self, query):
        with self.connect() as conn:
            conn.execute(query)

    def insert(self, query, params):
        with self.connect() as conn:
            conn.execute(query, params)
            conn.commit()

    def fetch(self, query, params=None):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()

    def update(self, query, params):
        with self.connect() as conn:
            conn.execute(query, params)
            conn.commit()

    def delete(self, query, params):
        with self.connect() as conn:
            conn.execute(query, params)
            conn.commit()