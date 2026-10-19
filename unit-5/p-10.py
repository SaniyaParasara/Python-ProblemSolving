# 50. Write a Python program to retrieve database records using fetchone, fetchmany and fetchall methods.

import sqlite3
import os

conn = sqlite3.connect("college.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS students")
cur.execute("CREATE TABLE students (id INTEGER, name TEXT, marks INTEGER)")
cur.executemany("INSERT INTO students VALUES (?, ?, ?)",
                [(1, "Saniya", 85), (2, "Rahul", 78), (3, "Priya", 92),
                 (4, "Amit", 66), (5, "Neha", 88)])
conn.commit()

cur.execute("SELECT * FROM students")
print("fetchone :", cur.fetchone())             # Next 1 record
print("fetchmany:", cur.fetchmany(2))           # Next 2 records
print("fetchall :", cur.fetchall())             # All remaining records

conn.close()
os.remove("college.db")
