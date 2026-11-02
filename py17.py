import sqlite3

def setup_database():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            emp_id TEXT PRIMARY KEY,
            name TEXT,
            designation TEXT,
            department TEXT,
            salary REAL
        )
    ''')
    conn.commit()
    return conn

def create_employee(conn):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    designation = input("Enter Designation: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?)", 
                       (emp_id, name, designation, department, salary))
        conn.commit()
        print("Employee created successfully!")
    except sqlite3.IntegrityError:
        print("Error: Employee ID already exists.")

def read_employees(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    for row in cursor.fetchall():
        print(f"ID: {row[0]} | Name: {row[1]} | Desig: {row[2]} | Dept: {row[3]} | Salary: {row[4]}")

def update_employee(conn):
    emp_id = input("Enter the Employee ID to update: ")
    new_salary = float(input("Enter new Salary: "))
    
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET salary = ? WHERE emp_id = ?", (new_salary, emp_id))
    if cursor.rowcount > 0:
        conn.commit()
        print("Employee updated successfully!")
    else:
        print("Employee ID not found.")

def delete_employee(conn):
    emp_id = input("Enter the Employee ID to delete: ")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE emp_id = ?", (emp_id,))
    if cursor.rowcount > 0:
        conn.commit()
        print("Employee deleted successfully!")
    else:
        print("Employee ID not found.")

def main():
    conn = setup_database()
    while True:
        print("\n1. Create\n2. Read\n3. Update Salary\n4. Delete\n5. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1': create_employee(conn)
        elif choice == '2': read_employees(conn)
        elif choice == '3': update_employee(conn)
        elif choice == '4': delete_employee(conn)
        elif choice == '5': break
        else: print("Invalid choice.")
    conn.close()

if __name__ == "__main__":
    main()
