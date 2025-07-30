from fastapi import APIRouter
from typing import List

router = APIRouter()

# Dummy recruitment data
recruitment_db = [
    {"id": 1, "position": "Software Engineer", "status": "Open"},
    {"id": 2, "position": "HR Manager", "status": "Closed"},
    {"id": 3, "position": "Data Analyst", "status": "Open"}
]

@router.get("/recruitment")
def list_open_positions() -> List[dict]:
    open_positions = [job for job in recruitment_db if job["status"] == "Open"]
    return open_positions