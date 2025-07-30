from sqlalchemy.orm import Session
from app.models.performance import PerformanceReview

def get_reviews_by_employee(db: Session, employee_id: int):
    return db.query(PerformanceReview).filter(PerformanceReview.employee_id == employee_id).all()