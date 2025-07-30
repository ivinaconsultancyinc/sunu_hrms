from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentResponse(DepartmentBase):
    id: int
    class Config:
        orm_mode = True

class JobTitleBase(BaseModel):
    title: str

class JobTitleCreate(JobTitleBase):
    pass

class JobTitleResponse(JobTitleBase):
    id: int
    class Config:
        orm_mode = True

class EmployeeBase(BaseModel):
    name: str
    department_id: int
    job_title_id: int

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    class Config:
        orm_mode = True