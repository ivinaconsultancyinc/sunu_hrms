from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.analytics_service import generate_summary_report

router = APIRouter()

@router.get("/analytics/summary", response_model=dict)
def get_analytics_summary(db: Session = Depends(get_db)):
    return generate_summary_report(db)