from sqlalchemy import Column, Integer, String
from app.database import Base
class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    position = Column(String, index=True)
