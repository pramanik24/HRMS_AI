# employee_routes.py

from flask import request, jsonify
from models.employee import Employee, EmployeeStatus
from sqlalchemy.orm import sessionmaker
from models.base import engine  # ✅ CORRECT
import datetime
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'}
Session = sessionmaker(bind=engine)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# This is the function you will register manually in ui.py
def register_submit_employee_route(app):
    @app.route("/submit_employee", methods=["POST"])
    def submit_employee():
        session = Session()
        try:
            # Handle files
            resume = request.files.get('resumeUpload')
            id_proof = request.files.get('idProofUpload')
            other_docs = request.files.get('otherDocsUpload')

            for file_obj in [resume, id_proof, other_docs]:
                if file_obj and allowed_file(file_obj.filename):
                    filename = secure_filename(file_obj.filename)
                    filepath = os.path.join(UPLOAD_FOLDER, filename)
                    file_obj.save(filepath)

            # Handle form data
            full_name = request.form['fullName'].strip().split(" ", 1)
            first_name = full_name[0]
            last_name = full_name[1] if len(full_name) > 1 else ""

            new_employee = Employee(
                employee_id="EMP" + str(int(datetime.datetime.now().timestamp())),
                first_name=first_name,
                last_name=last_name,
                email=request.form['email'],
                phone=request.form['contactNumber'],
                address=request.form['homeAddress'],
                dob=request.form['dateOfBirth'],
                role=request.form['position'],
                department=request.form['department'],
                manager_id=None,
                status=EmployeeStatus.active,
                salary=None,
                hire_date=datetime.date.today(),
            )

            session.add(new_employee)
            session.commit()

            return jsonify({"message": "Employee added successfully!"}), 200

        except Exception as e:
            session.rollback()
            return jsonify({"error": str(e)}), 500

        finally:
            session.close()
