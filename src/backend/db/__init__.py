import psycopg

# PostgreSQL connection string
DB_CONNECTION_STRING = "postgresql://bed_user:bed_password@postgres:5432/bed_db"

class DB:
    def __init__(self):
        self.con = psycopg.connect(DB_CONNECTION_STRING)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS messages(title VARCHAR, paragraph VARCHAR);")
        self.cur.execute("""
            INSERT INTO messages VALUES
            ('BED', 'This is BED, a website by B, E and D');
        """)
        self.con.commit()
    def get_messages(self):
        return self.cur.execute("SELECT * FROM messages;").fetchall()

if __name__ == "__main__":
    db = DB()
    print(db.get_messages())