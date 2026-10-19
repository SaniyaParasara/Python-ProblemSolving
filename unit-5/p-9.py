# 49. Write a Python program to connect Python with a database and execute SQL queries.

import sqlite3

conn = sqlite3.connect("college.db")            # Connect (creates file if absent)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS students")
cur.execute("""CREATE TABLE students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                marks INTEGER)""")

cur.execute("INSERT INTO students VALUES (1, 'Saniya', 85)")
cur.executemany("INSERT INTO students VALUES (?, ?, ?)",
                [(2, "Rahul", 78), (3, "Priya", 92), (4, "Amit", 66)])
conn.commit()

cur.execute("UPDATE students SET marks = 80 WHERE id = 2")
cur.execute("DELETE FROM students WHERE id = 4")
conn.commit()

cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

conn.close()
