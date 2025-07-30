from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.notification_service import NotificationService
from app.dependencies import get_db, get_current_user

router = APIRouter()

@router.get("/")
def list_notifications(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return NotificationService.get_notifications(db, user_id=user["id"])

@router.post("/send")
def send_notification(message: str, type: str = "info", db: Session = Depends(get_db), user=Depends(get_current_user)):
    return NotificationService.send_notification(db, user_id=user["id"], message=message, type=type)

@router.post("/{notification_id}/read")
def mark_read(notification_id: int, db: Session = Depends(get_db)):
    return NotificationService.mark_as_read(db, notification_id)

