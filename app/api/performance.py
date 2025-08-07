from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db
from app.schemas.performance import PerformanceCreate, PerformanceResponse
from app.crud import performance_crud as crud_performance

router = APIRouter()

@router.post("/performance/", response_model=PerformanceResponse)
def create_performance(perf: PerformanceCreate, db: Session = Depends(get_db)):
    return crud_performance.create_performance(db=db, perf=perf)

@router.get("/performance/", response_model=List[PerformanceResponse])
def get_all_performances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_performance.get_all_performances(db, skip=skip, limit=limit)

@router.get("/performance/{perf_id}", response_model=PerformanceResponse)
def get_performance(perf_id: int, db: Session = Depends(get_db)):
    perf = crud_performance.get_performance_by_id(db, perf_id=perf_id)
    if not perf:
        raise HTTPException(status_code=404, detail="Performance record not found")
    return perf

