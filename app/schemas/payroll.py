from pydantic import BaseModel
from typing import Optional
from datetime import date

class SalaryBase(BaseModel):
    employee_id: int
    amount: float

class SalaryCreate(SalaryBase):
    pass

class SalaryResponse(SalaryBase):
    id: int
    class Config:
        orm_mode = True

class PayslipBase(BaseModel):
    employee_id: int
    month: str
    net_pay: float

class PayslipCreate(PayslipBase):
    pass

class PayslipResponse(PayslipBase):
    id: int
    class Config:
        orm_mode = True