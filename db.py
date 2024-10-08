import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS homeworks (id INTEGER PRIMARY KEY, task text, description text, submission text, ddate date, subject text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM homeworks")
        rows = self.cur.fetchall()
        return rows

    def add(self, name, description, mob, dd, sub):
        self.cur.execute("INSERT INTO homeworks (task, description, submission, ddate, subject) VALUES (?,?,?,?,?)", (name, description, mob, dd, sub))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM homeworks WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, task, des, method, ddat, subject):
        self.cur.execute("UPDATE homeworks SET task = ?, description = ?, submission = ?, ddate = ?, subject = ? WHERE id = ?",
                         (task, des, method, ddat, subject, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
