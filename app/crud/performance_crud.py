from sqlalchemy.orm import Session
from app.models.performance import PerformanceReview
from app.schemas.performance import PerformanceCreate

def create_performance(db: Session, perf: PerformanceCreate):
    db_perf = PerformanceReview(**perf.dict())
    db.add(db_perf)
    db.commit()
    db.refresh(db_perf)
    return db_perf

def get_all_performances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PerformanceReview).offset(skip).limit(limit).all()

def get_performance_by_id(db: Session, perf_id: int):
    return db.query(PerformanceReview).filter(PerformanceReview.id == perf_id).first()

def delete_performance(db: Session, perf_id: int):
    perf = db.query(PerformanceReview).filter(PerformanceReview.id == perf_id).first()
    if perf:
        db.delete(perf)
        db.commit()
        return True
    return False



