from flask import Flask, render_template
from add_employee_with_details import get_employees   # import function from your hrms.py
from employee_routes import register_submit_employee_route  # 👈 import

app = Flask(__name__)

register_submit_employee_route(app) 

@app.route("/")
def home():
    employees = get_employees()
    return render_template("base.html", employees=employees)

@app.route("/employees")  # 👈 NEW ROUTE
def employee_list():
    employees = get_employees()
    return render_template("employee_list.html", employees=employees) 

@app.route("/add_employee")  # 👈 NEW ROUTE
def add_employee():
    employees = get_employees()
    return render_template("add_employee.html", employees=employees) 


if __name__ == "__main__":
    app.run(debug=True)
