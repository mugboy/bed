import sqlite3

class DB:
    def __init__(self):
        con = sqlite3.connect("db.db")
        self.cur = con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS messages(title,paragraph)")
        self.cur.execute("""
            INSERT INTO messages VALUES
            ('BED', 'This is BED, a website by Ben, Ethan and Daniel')
        """)
    def get_messages(self):
        return self.cur.execute("SELECT * FROM messages").fetchall()

if __name__ == "__main__":
    db = DB()
    print(db.get_messages())