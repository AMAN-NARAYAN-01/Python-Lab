import sqlite3

def setup_database():  # function
    conn = sqlite3.connect('student.db') #data base file 
    cursor = conn.cursor()  # object
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            roll_number TEXT PRIMARY KEY, name TEXT,department TEXT, cgpa REAL
        )
    ''')
    conn.commit()  # for save in the table
    return conn

def add_student(conn):
    roll_number = input("Roll Number: ")
    name = input("Name: ")
    department = input("Department: ")
    cgpa = float(input("CGPA: "))
    
    cursor = conn.cursor()
    try: #if rol no. same then it will print Error
        cursor.execute("INSERT INTO students VALUES (?, ?,?, ?)", (roll_number, name, department, cgpa))
        conn.commit()
        print("Student added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Student with this roll number already exists.")

def display_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    
    print("\n student Record \n")
    for row in records:
        print(f"Roll No: {row[0]}, Name: {row[1]}, Dept: {row[2]}, CGPA: {row[3]}")

def main():
    conn = setup_database()
    while True:
        print("1. Add Student\n2. Display Students\n3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_student(conn)
        elif choice == '2':
            display_students(conn)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
    conn.close()

if __name__ == "__main__":
    main()
