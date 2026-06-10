import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute(
    "DELETE FROM employee WHERE emp_id=?",
    (120,)
)

conn.commit()
conn.close()

print("Employee deleted")