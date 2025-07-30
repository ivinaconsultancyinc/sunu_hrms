from fastapi import APIRouter
from typing import List
from datetime import datetime

router = APIRouter()

# Dummy audit log data
audit_logs = [
    {"timestamp": datetime.now().isoformat(), "user": "alice", "action": "Logged in"},
    {"timestamp": datetime.now().isoformat(), "user": "bob", "action": "Viewed salary report"},
    {"timestamp": datetime.now().isoformat(), "user": "charlie", "action": "Updated profile"}
]

@router.get("/logs")
def get_audit_logs() -> List[dict]:
    return audit_logs