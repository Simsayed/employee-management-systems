import sqlite3

conn = sqlite3.connect("employee.db")
cur = conn.cursor()

# Departments
departments = [
    (1, "IT"),
    (2, "HR"),
    (3, "Finance"),
    (4, "Marketing")
]

cur.executemany(
    "INSERT INTO department VALUES (?, ?)",
    departments
)

# Employees
employees = [
    (101, 'Amit', 21, 50000, 1),
    (102, 'Bhavna', 22, 60000, 2),
    (103, 'Charan', 23, 55000, 1),
    (104, 'Divya', 24, 70000, 3),
    (105, 'Esha', 25, 65000, 4),
    (106, 'Farhan', 22, 52000, 1),
    (107, 'Gauri', 23, 58000, 2),
    (108, 'Harsh', 24, 62000, 3),
    (109, 'Isha', 21, 54000, 4),
    (110, 'Jay', 26, 80000, 1),
    (111, 'Karan', 27, 75000, 2),
    (112, 'Lavanya', 22, 57000, 3),
    (113, 'Manoj', 23, 61000, 4),
    (114, 'Neha', 24, 68000, 1),
    (115, 'Om', 25, 72000, 2),
    (116, 'Priya', 21, 53000, 3),
    (117, 'Rahul', 22, 59000, 4),
    (118, 'Sneha', 23, 64000, 1),
    (119, 'Tanvi', 24, 71000, 2),
    (120, 'Vikram', 26, 85000, 3)
]

cur.executemany(
    "INSERT INTO employee VALUES (?, ?, ?, ?, ?)",
    employees
)

conn.commit()
conn.close()

print("20 Employee Records Inserted Successfully")