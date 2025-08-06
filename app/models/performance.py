from sqlalchemy import Column, Integer, Float, Text, ForeignKey, Date, String
from sqlalchemy.orm import relationship
from app.database import Base
class PerformanceReview(Base):
    __tablename__ = "performance_reviews"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), index=True)
    review_date = Column(Date, index=True)
    score = Column(Float)
    comments = Column(Text)
    employee = relationship("Employee", back_populates="performance_reviews")
class Goal(Base):
    __tablename__ = "goals"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    description = Column(Text)
    status = Column(String)
class KPI(Base):
    __tablename__ = "kpis"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    metric = Column(String)
    value = Column(Float)
