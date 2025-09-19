import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class EmployeeAudit(Base):
    __tablename__ = 'tbl_employee_audit'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('tbl_employee.id'), nullable=False)
    action = Column(String(50), nullable=False)
    changed_by = Column(String(100), nullable=False)
    change_date = Column(DateTime, default=datetime.datetime.utcnow)

    employee = relationship("Employee", backref="audits")
