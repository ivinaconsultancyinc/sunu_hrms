from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
router = APIRouter()
# Sample Pydantic models
class JobApplicationCreate(BaseModel):
    name: str
    email: str
    position: str
class JobApplicationResponse(JobApplicationCreate):
    id: int
# In-memory store for demonstration
fake_db = []
next_id = 1
@router.post("/recruitment/applications/", response_model=JobApplicationResponse)
def create_application(application: JobApplicationCreate):
    global next_id
    new_app = JobApplicationResponse(id=next_id, **application.dict())
    fake_db.append(new_app)
    next_id += 1
    return new_app
@router.get("/recruitment/applications/", response_model=List[JobApplicationResponse])
def list_applications():
    return fake_db


