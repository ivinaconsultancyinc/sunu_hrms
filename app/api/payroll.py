 from fastapi import APIRouter

router = APIRouter()

@router.get("/status")
def get_payroll_status():
    return {"message": "Payroll module is active and responding."}
