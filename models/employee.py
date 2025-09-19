import datetime
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Enum, Numeric, Text
from sqlalchemy.orm import relationship
from models.base import Base
import enum

class EmployeeStatus(enum.Enum):
    active = "Active"
    probation = "Probation"
    resigned = "Resigned"
    terminated = "Terminated"

class Employee(Base):
    __tablename__ = 'tbl_employee'

    id = Column(Integer, primary_key=True)
    employee_id = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15))
    address = Column(Text)
    dob = Column(Date)
    role = Column(String(100))
    department = Column(String(100))
    manager_id = Column(Integer, ForeignKey('tbl_employee.id'), nullable=True)
    status = Column(Enum(EmployeeStatus), default=EmployeeStatus.active, nullable=False)
    salary = Column(Numeric(10, 2))
    hire_date = Column(Date, nullable=False)
    termination_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    manager = relationship("Employee", remote_side=[id], backref="subordinates")
