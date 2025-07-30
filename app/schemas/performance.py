from pydantic import BaseModel
from typing import Optional

class PerformanceReviewBase(BaseModel):
    employee_id: int
    score: float
    comments: Optional[str]

class PerformanceReviewCreate(PerformanceReviewBase):
    pass

class PerformanceReviewResponse(PerformanceReviewBase):
    id: int
    class Config:
        orm_mode = True

class GoalBase(BaseModel):
    employee_id: int
    description: str
    achieved: bool

class GoalCreate(GoalBase):
    pass

class GoalResponse(GoalBase):
    id: int
    class Config:
        orm_mode = True

class KPIBase(BaseModel):
    employee_id: int
    metric: str
    value: float

class KPICreate(KPIBase):
    pass

class KPIResponse(KPIBase):
    id: int
    class Config:
        orm_mode = True