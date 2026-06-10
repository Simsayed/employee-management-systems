import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute(
    "SELECT * FROM employee WHERE salary > 70000"
)

for row in cur.fetchall():
    print(row)

conn.close()