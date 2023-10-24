import sqlite3
import os

def create_db():
    script_file_path = os.path.join("sql_db", "_create_tables.sql")
    with open(script_file_path, "r") as f:
        sql = f.read()

    # if db one -> create db
    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()


# first.py