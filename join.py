import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("""
SELECT employee.name,
       employee.salary,
       department.department_name
FROM employee
INNER JOIN department
ON employee.department_id =
department.department_id
""")

for row in cur.fetchall():
    print(row)

conn.close()