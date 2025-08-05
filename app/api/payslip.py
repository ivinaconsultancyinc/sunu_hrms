from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud import payslip as payslip_crud
from app.models.payroll import Payslip

router = APIRouter()

@router.post("/payslips/", response_model=dict)
def create_payslip(payslip_data: dict, db: Session = Depends(get_db)):
    return payslip_crud.create_payslip(db, payslip_data)

@router.get("/payslips/", response_model=list)
def read_all_payslips(db: Session = Depends(get_db)):
    return payslip_crud.get_all_payslips(db)

@router.get("/payslips/{payslip_id}", response_model=dict)
def read_payslip(payslip_id: int, db: Session = Depends(get_db)):
    payslip = payslip_crud.get_payslip_by_id(db, payslip_id)
    if not payslip:
        raise HTTPException(status_code=404, detail="Payslip not found")
    return payslip

@router.put("/payslips/{payslip_id}", response_model=dict)
def update_payslip(payslip_id: int, update_data: dict, db: Session = Depends(get_db)):
    try:
        return payslip_crud.update_payslip(db, payslip_id, update_data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/payslips/{payslip_id}", response_model=dict)
def delete_payslip(payslip_id: int, db: Session = Depends(get_db)):
    success = payslip_crud.delete_payslip(db, payslip_id)
    if not success:
        raise HTTPException(status_code=404, detail="Payslip not found")

    return {"detail": "Payslip deleted successfully"}

