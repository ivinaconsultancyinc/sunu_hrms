from pydantic import BaseModel
from typing import Optional
from datetime import date

class JobPostBase(BaseModel):
    title: str
    description: str

class JobPostCreate(JobPostBase):
    pass

class JobPostResponse(JobPostBase):
    id: int
    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    job_post_id: int
    applicant_name: str
    status: str

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int
    class Config:
        orm_mode = True

class InterviewBase(BaseModel):
    application_id: int
    date: date
    result: str

class InterviewCreate(InterviewBase):
    pass

class InterviewResponse(InterviewBase):
    id: int
    class Config:
        orm_mode = True
