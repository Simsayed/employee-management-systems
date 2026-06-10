import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute(
    "UPDATE employee SET salary=? WHERE emp_id=?",
    (90000, 101)
)

conn.commit()
conn.close()

print("Employee salary updated")