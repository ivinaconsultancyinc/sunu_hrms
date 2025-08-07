from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.job_application import JobApplication
from app.schemas.job_application import JobApplicationCreate, JobApplicationResponse

router = APIRouter()

@router.post("/recruitment/applications/", response_model=JobApplicationResponse)
def create_application(application: JobApplicationCreate, db: Session = Depends(get_db)):
    db_app = JobApplication(**application.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

@router.get("/recruitment/applications/", response_model=List[JobApplicationResponse])
def list_applications(db: Session = Depends(get_db)):
    return db.query(JobApplication).all()



