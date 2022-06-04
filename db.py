import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS homeworks (id INTEGER PRIMARY KEY, task text, description text, submission text, date date)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM homeworks")
        rows = self.cur.fetchall()
        return rows