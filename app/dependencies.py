# app/dependencies.py
from fastapi import Request, Depends, HTTPException
from jose import jwt, JWTError
from app.config import settings
from app.database import SessionLocal
from sqlalchemy.orm import Session
SECRET_KEY = settings.secret_key
ALGORITHM = settings.jwt_algorithm
# Dummy user database (replace with actual user lookup in production)
fake_users_db = {
    "admin": {"id": 1, "username": "admin", "role": "admin", "password": "adminpass"},
    "user": {"id": 2, "username": "user", "role": "user", "password": "userpass"}
}
def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return fake_users_db[username]
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


