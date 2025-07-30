from sqlalchemy.orm import Session
from app.models.employee import Employee

def get_employee(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()