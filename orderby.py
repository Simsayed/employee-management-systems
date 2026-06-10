import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute(
    "SELECT * FROM employee ORDER BY salary DESC"
)

for row in cur.fetchall():
    print(row)

conn.close()