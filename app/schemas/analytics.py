from pydantic import BaseModel

class ReportBase(BaseModel):
    name: str
    data: str

class ReportCreate(ReportBase):
    pass

class ReportResponse(ReportBase):
    id: int
    class Config:
        orm_mode = True

class MetricBase(BaseModel):
    name: str
    value: float

class MetricCreate(MetricBase):
    pass

class MetricResponse(MetricBase):
    id: int
    class Config:
        orm_mode = True