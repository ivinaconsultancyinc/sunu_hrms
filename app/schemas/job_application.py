from pydantic import BaseModel
class JobApplicationCreate(BaseModel):
    name: str
    email: str
    position: str
class JobApplicationResponse(JobApplicationCreate):
    id: int
    class Config:
        orm_mode = True


