import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM employee")

print("Total Employees:", cur.fetchone()[0])

conn.close()
