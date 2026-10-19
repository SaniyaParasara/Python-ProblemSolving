# UNIT 5 - Q10: Write a program to retrieve database records using fetchone(),
#                fetchmany() and fetchall() methods.
# SCENARIO: A results portal shows records page-by-page (fetchmany), the detail
#           of one student (fetchone) or exports the full list (fetchall).
# (MySQL: switch USE_MYSQL = True as shown in p-9.py)

USE_MYSQL = False

if USE_MYSQL:
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", user="root", passwd="your_password", db="college")
    PH = "%s"
else:
    import sqlite3
    conn = sqlite3.connect(":memory:")
    PH = "?"

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS student")
cur.execute("CREATE TABLE student(id INT PRIMARY KEY, name VARCHAR(50), marks INT)")
people = [("Amit", 82), ("Riya", 91), ("Karan", 67), ("Neha", 74),
          ("Dev", 55), ("Sana", 88), ("Om", 60)]
data = [(i, n, m) for i, (n, m) in enumerate(people, 1)]
cur.executemany(f"INSERT INTO student VALUES({PH},{PH},{PH})", data)
conn.commit()

cur.execute("SELECT * FROM student")
print("fetchone() #1 :", cur.fetchone())
print("fetchone() #2 :", cur.fetchone())
print("fetchmany(3)  :", cur.fetchmany(3))
print("fetchall()    :", cur.fetchall(), "<- remaining rows")
print("fetchone() at end:", cur.fetchone())

print("\nPagination using fetchmany(3):")
cur.execute("SELECT * FROM student")
page = 1
while True:
    rows = cur.fetchmany(3)
    if not rows:
        break
    print(f" Page {page}:", rows)
    page += 1

cur.execute(f"SELECT * FROM student WHERE id={PH}", (3,))
print("\nSingle record (id=3):", cur.fetchone())
cur.execute("SELECT name, marks FROM student ORDER BY marks DESC LIMIT 3")
print("Top 3 students      :", cur.fetchall())
cur.execute("SELECT COUNT(*) FROM student")
print("Total records       :", cur.fetchone()[0])

cur.close(); conn.close()
