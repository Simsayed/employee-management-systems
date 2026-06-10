import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS department(
    department_id INTEGER PRIMARY KEY,
    department_name TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary INTEGER,
    department_id INTEGER,
    FOREIGN KEY(department_id)
    REFERENCES department(department_id)
)
""")

conn.commit()
conn.close()

print("Tables created successfully")