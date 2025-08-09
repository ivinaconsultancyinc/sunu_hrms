from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.crud import employee as crud_employee
router = APIRouter()
@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud_employee.get_employee_by_email(db, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_employee.create_employee(db=db, employee=employee)
@router.get("/employees/", response_model=List[EmployeeResponse])
def read_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_employee.get_all_employees(db, skip=skip, limit=limit)
@router.get("/employees/{employee_id}", response_model=EmployeeResponse)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud_employee.get_employee_by_id(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
@router.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    success = crud_employee.delete_employee(db, employee_id=employee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


