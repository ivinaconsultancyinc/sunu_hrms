from fastapi import APIRouter
router = APIRouter()
@router.get("/status")
def get_attendance_status():
    return {"message": "Attendance module is active"}
