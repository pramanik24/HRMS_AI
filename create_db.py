# import datetime
# from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Enum, Numeric, Text
# from sqlalchemy.orm import relationship
# # from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base

# from sqlalchemy import create_engine
# import enum

# Base = declarative_base()

# # Enum for employee status
# class EmployeeStatus(enum.Enum):
#     active = "Active"
#     probation = "Probation"
#     resigned = "Resigned"
#     terminated = "Terminated"


# # Employee Table
# class Employee(Base):
#     __tablename__ = 'tbl_employee'

#     id = Column(Integer, primary_key=True)
#     employee_id = Column(String(50), unique=True, nullable=False)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     phone = Column(String(15))
#     address = Column(Text)
#     dob = Column(Date)
#     role = Column(String(100))
#     department = Column(String(100))
#     manager_id = Column(Integer, ForeignKey('tbl_employee.id'), nullable=True)  # Self-referential foreign key
#     status = Column(Enum(EmployeeStatus), default=EmployeeStatus.active, nullable=False)
#     salary = Column(Numeric(10, 2))
#     hire_date = Column(Date, nullable=False)
#     termination_date = Column(Date, nullable=True)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

#     # Relationship to manager (self-referencing)
#     manager = relationship("Employee", remote_side=[id], backref="subordinates")

#     def __init__(self, first_name, last_name, email, employee_id, role, department, hire_date, status=EmployeeStatus.active):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.employee_id = employee_id
#         self.role = role
#         self.department = department
#         self.hire_date = hire_date
#         self.status = status


# # Documents Table
# class EmployeeDocument(Base):
#     __tablename__ = 'tbl_employee_documents'

#     id = Column(Integer, primary_key=True)
#     employee_id = Column(Integer, ForeignKey('tbl_employee.id'), nullable=False)
#     document_type = Column(String(100), nullable=False)
#     file_path = Column(String(255), nullable=False)
#     upload_date = Column(DateTime, default=datetime.datetime.utcnow)

#     # Relationship to Employee
#     employee = relationship("Employee", backref="documents")

#     def __init__(self, employee_id, document_type, file_path):
#         self.employee_id = employee_id
#         self.document_type = document_type
#         self.file_path = file_path


# # Audit Table
# class EmployeeAudit(Base):
#     __tablename__ = 'tbl_employee_audit'

#     id = Column(Integer, primary_key=True)
#     employee_id = Column(Integer, ForeignKey('tbl_employee.id'), nullable=False)
#     action = Column(String(50), nullable=False)  # e.g., "Added", "Updated", "Deleted"
#     changed_by = Column(String(100), nullable=False)
#     change_date = Column(DateTime, default=datetime.datetime.utcnow)

#     # Relationship to Employee
#     employee = relationship("Employee", backref="audits")

#     def __init__(self, employee_id, action, changed_by):
#         self.employee_id = employee_id
#         self.action = action
#         self.changed_by = changed_by


# # Create the tables
# engine = create_engine('sqlite:///hrms_db.db')  # Replace with your preferred DB URI
# Base.metadata.create_all(engine)
from models.base import Base, engine
from models import employee, employee_document, employee_audit  # This ensures models are registered

Base.metadata.create_all(engine)
print("✅ Tables created successfully in MySQL.")
