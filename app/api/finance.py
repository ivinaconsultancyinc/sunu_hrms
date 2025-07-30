from fastapi import APIRouter
from typing import List

router = APIRouter()

# Dummy salary data
salaries_db = [
    {"employee_id": 1, "name": "Alice", "amount": 5000, "month": "July"},
    {"employee_id": 2, "name": "Bob", "amount": 4000, "month": "July"},
    {"employee_id": 3, "name": "Charlie", "amount": 4500, "month": "July"}
]

@router.get("/salaries")
def list_salaries() -> List[dict]:
    return salaries_db