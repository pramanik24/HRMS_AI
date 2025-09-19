import mysql.connector
from db_connect import get_connection

# db = get_connection()
# # 🔹 Create Database
# def create_database():
#     db = get_connection()
#     cursor = db.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS hrms")
#     print("✅ Database 'hrms' created (if not exists)")
#     db.close()

# 🔹 Create Employee Table
def create_employee_table():
    db = get_connection("hrms")
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        department VARCHAR(100),
        salary DECIMAL(10,2)
    )
    """)
    print("✅ Employee table created (if not exists)")
    db.close()

# 🔹 Add Employee
def add_employee(name, age, department, salary):
    db = get_connection("hrms")
    cursor = db.cursor()
    sql = "INSERT INTO employees (name, age, department, salary) VALUES (%s, %s, %s, %s)"
    val = (name, age, department, salary)
    cursor.execute(sql, val)
    db.commit()
    print(f"✅ Employee {name} added successfully")
    db.close()

# 🔹 Fetch All Employees
def get_employees():
    db = get_connection("hrms")
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    db.close()
    return rows

# 🔹 Update Employee Salary
def update_salary(name, new_salary):
    db = get_connection("hrms")
    cursor = db.cursor()
    sql = "UPDATE employees SET salary = %s WHERE name = %s"
    val = (new_salary, name)
    cursor.execute(sql, val)
    db.commit()
    print(f"✅ Salary updated for {name}")
    db.close()

# 🔹 Delete Employee
def delete_employee(name):
    db = get_connection("hrms")
    cursor = db.cursor()
    sql = "DELETE FROM employees WHERE name = %s"
    val = (name,)
    cursor.execute(sql, val)
    db.commit()
    print(f"✅ Employee {name} deleted")
    db.close()

# 🔹 Example usage
if __name__ == "__main__":
    # Step 1: Create DB & Table
    # create_database()
    create_employee_table()

    # Step 2: Add Employees
    add_employee("Rahul Sharma", 28, "Sales", 40000)
    add_employee("Anita Roy", 30, "HR", 50000)

    # Step 3: Show Employees
    employees = get_employees()
    print("\n📋 Employee List:")
    for emp in employees:
        print(emp)

    # Step 4: Update Salary
    update_salary("Rahul Sharma", 20000)

    # Step 5: Delete Employee
    # delete_employee("Anita Roy")

    # Final List
    print("\n📋 Final Employee List:")
    for emp in get_employees():
        print(emp)


#update database
def add_employee():
    try:
        session = Session()

        # Parse full name
        full_name = request.form.get("fullName")
        first_name, *last_name_parts = full_name.strip().split(" ")
        last_name = " ".join(last_name_parts) if last_name_parts else ""

        employee = Employee(
            employee_id="EMP" + str(int(datetime.datetime.utcnow().timestamp())),
            first_name=first_name,
            last_name=last_name,
            email=request.form.get("email"),
            phone=request.form.get("contactNumber"),
            address=request.form.get("homeAddress"),
            dob=request.form.get("dateOfBirth"),
            role=request.form.get("position"),
            department=request.form.get("department"),
            manager_id=None,  # You may need to map this based on name
            status=EmployeeStatus.active,
            hire_date=datetime.datetime.utcnow().date()
        )

        # Save files (optional)
        resume = request.files.get('resume')
        if resume:
            resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(resume_path)

        id_proof = request.files.get('idProof')
        if id_proof:
            id_proof_path = os.path.join(UPLOAD_FOLDER, id_proof.filename)
            id_proof.save(id_proof_path)

        other_docs = request.files.get('otherDocs')
        if other_docs:
            other_docs_path = os.path.join(UPLOAD_FOLDER, other_docs.filename)
            other_docs.save(other_docs_path)

        session.add(employee)
        session.commit()
        return jsonify({"message": "Employee added successfully"}), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()