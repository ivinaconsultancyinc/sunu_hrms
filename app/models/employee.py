from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    employees = relationship("Employee", back_populates="department")

class JobTitle(Base):
    __tablename__ = "job_titles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, nullable=False)

    employees = relationship("Employee", back_populates="job_title")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    department_id = Column(Integer, ForeignKey("departments.id"))
    job_title_id = Column(Integer, ForeignKey("job_titles.id"))

    department = relationship("Department", back_populates="employees")
    job_title = relationship("JobTitle", back_populates="employees")



