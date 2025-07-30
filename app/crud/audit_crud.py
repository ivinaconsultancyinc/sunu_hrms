from sqlalchemy.orm import Session
from app.models.audit import AuditLog

def get_audit_logs(db: Session):
    return db.query(AuditLog).order_by(AuditLog.timestamp.desc()).all()