from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.user import User
from app.schemas.user import UserCreate
from datetime import datetime

# Placeholder for password hashing
def fake_hash_password(password: str) -> str:
    return "hashed_" + password

# Get user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Get user by email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

# Get all users
def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# Create a new user
def create_user(db: Session, user: UserCreate):
    hashed_password = fake_hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_password,
        is_active=user.is_active,
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Delete a user
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False