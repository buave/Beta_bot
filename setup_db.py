import sqlite3

conn = sqlite3.connect("data.db")

conn.execute("CREATE TABLE SAVE (DATE INT, HOUR INT)")
