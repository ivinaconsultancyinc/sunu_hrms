from fastapi import APIRouter, Form, HTTPException
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

# Dummy user database
fake_users_db = {
    "alice": {"username": "alice", "password": "secret", "role": "admin"},
    "bob": {"username": "bob", "password": "password", "role": "user"}
}

# JWT settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
   
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
