from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database_schemas import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(String, nullable=False)
    type = Column(String, default="info")
    read = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


    user = relationship("User", back_populates="notifications")
