from sqlalchemy.orm import Session
from app.models.payroll import Salary

def get_salary_by_employee(db: Session, employee_id: int):
    return db.query(Salary).filter(Salary.employee_id == employee_id).all()