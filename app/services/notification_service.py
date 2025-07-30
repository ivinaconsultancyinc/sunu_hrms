from datetime import datetime
from app.models import Notification  # Assuming you have a Notification model
from app.database import SessionLocal

class NotificationService:
    @staticmethod
    def send_notification(db, user_id: int, message: str, type: str = "info"):
        notification = Notification(
            user_id=user_id,
            message=message,
            type=type,
            timestamp=datetime.utcnow(),
            read=False
        )
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return notification

    @staticmethod
    def get_notifications(db, user_id: int, unread_only: bool = False):
        query = db.query(Notification).filter(Notification.user_id == user_id)
        if unread_only:
            query = query.filter(Notification.read == False)
        return query.order_by(Notification.timestamp.desc()).all()

    @staticmethod
    def mark_as_read(db, notification_id: int):
        notification = db.query(Notification).get(notification_id)
        if notification:
            notification.read = True
            db.commit()
        return notification
