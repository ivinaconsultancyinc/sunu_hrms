from pydantic import BaseModel
from datetime import datetime

class NotificationBase(BaseModel):
    user_id: int
    message: str
    type: str

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: int
    read: bool
    timestamp: datetime

    class Config:
        orm_mode = True
