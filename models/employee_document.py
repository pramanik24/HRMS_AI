import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class EmployeeDocument(Base):
    __tablename__ = 'tbl_employee_documents'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('tbl_employee.id'), nullable=False)
    document_type = Column(String(100), nullable=False)
    file_path = Column(String(255), nullable=False)
    upload_date = Column(DateTime, default=datetime.datetime.utcnow)

    employee = relationship("Employee", backref="documents")
