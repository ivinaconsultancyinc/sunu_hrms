from pydantic import BaseModel
from datetime import datetime

class AuditLogBase(BaseModel):
    user_id: int
    action: str
    timestamp: datetime

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogResponse(AuditLogBase):
    id: int
    class Config:
        orm_mode = True