from pydantic import BaseModel
from typing import Optional

# Schema for incoming performance data
class PerformanceCreate(BaseModel):
    employee_id: int
    review_period: str
    score: float
    comments: Optional[str] = None

# Schema for outgoing performance data with ID
class PerformanceResponse(PerformanceCreate):
    id: int

