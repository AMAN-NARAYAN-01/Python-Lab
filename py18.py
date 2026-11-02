import sqlite3

def generate_report():
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
    dept_name = input("Enter the Department Name to generate the salary report: ")
    cursor.execute("SELECT name, designation, salary FROM employees WHERE department = ?", (dept_name,))
    records = cursor.fetchall()
    
    if not records:
        print(f"No employees found in the '{dept_name}' department.")
    else:
        print(f"\n--- Salary Report for Department: {dept_name} ---")
        total_salary = 0
        for row in records:
            print(f"Name: {row[0]}, Designation: {row[1]}, Salary: {row[2]}")
            total_salary += row[2]
        
        print("-" * 40)
        print(f"Total Salary Payout for {dept_name}: {total_salary}")
        print(f"Average Salary: {total_salary / len(records):.2f}")
    
    conn.close()

if __name__ == "__main__":
    generate_report()
