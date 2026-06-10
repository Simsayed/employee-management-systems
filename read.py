import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("SELECT * FROM employee")

for row in cur.fetchall():
    print(row)

conn.close()