from sqlalchemy.orm import Session
from app.models.attendance import Attendance

def get_attendance_by_employee(db: Session, employee_id: int):
    return db.query(Attendance).filter(Attendance.employee_id == employee_id).all()