from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    generated_on = Column(Date)

class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    value = Column(Float)
    recorded_on = Column(Date)


