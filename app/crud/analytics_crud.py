from sqlalchemy.orm import Session
from app.models.analytics import Report

def get_reports(db: Session):
    return db.query(Report).all()