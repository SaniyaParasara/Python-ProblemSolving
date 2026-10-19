# UNIT 5 - Q9: Write a program to connect Python with a database and execute
#               SQL queries.
# SCENARIO: A student-registration app stores data in MySQL: create table,
#           insert, update and delete records through Python.
#
# ---- Using MySQL (on your PC) ----
#   pip install mysqlclient           (imported as MySQLdb)
#   In MySQL:  CREATE DATABASE college;
#   Then set USE_MYSQL = True and enter your user / password below.
# By default this runs on sqlite3 (same steps: connect -> cursor -> execute ->
# commit -> close), so it works without any server.

USE_MYSQL = False

if USE_MYSQL:
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", user="root", passwd="your_password", db="college")
    PH = "%s"
    CREATE = "CREATE TABLE IF NOT EXISTS student(id INT PRIMARY KEY, name VARCHAR(50), course VARCHAR(30), marks INT)"
else:
    import sqlite3
    conn = sqlite3.connect(":memory:")
    PH = "?"
    CREATE = "CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, name TEXT, course TEXT, marks INT)"

cur = conn.cursor()
cur.execute(CREATE)
print("Table created")

cur.execute(f"INSERT INTO student VALUES({PH},{PH},{PH},{PH})", (1, "Amit", "MCA", 82))
cur.executemany(f"INSERT INTO student VALUES({PH},{PH},{PH},{PH})",
                [(2, "Riya", "MCA", 91), (3, "Karan", "BCA", 67), (4, "Neha", "MCA", 74)])
conn.commit()
print("4 rows inserted")

cur.execute(f"UPDATE student SET marks={PH} WHERE id={PH}", (95, 3))
print("Updated rows :", cur.rowcount)
cur.execute(f"DELETE FROM student WHERE id={PH}", (4,))
print("Deleted rows :", cur.rowcount)
conn.commit()

cur.execute("SELECT * FROM student")
print("\nAll records:")
for row in cur.fetchall():
    print("  ", row)

cur.execute(f"SELECT name, marks FROM student WHERE course={PH} ORDER BY marks DESC", ("MCA",))
print("\nMCA students by marks:", cur.fetchall())
cur.execute("SELECT course, AVG(marks), COUNT(*) FROM student GROUP BY course")
print("Course summary       :", cur.fetchall())

try:
    cur.execute(f"INSERT INTO student VALUES({PH},{PH},{PH},{PH})", (1, "Dup", "MCA", 50))
except Exception as e:
    conn.rollback()
    print("\nDuplicate key error handled:", type(e).__name__)

cur.close(); conn.close()
print("Connection closed")
