from sqlalchemy.orm import Session
from app.models.recruitment import JobPost

def get_all_job_posts(db: Session):
    return db.query(JobPost).all()