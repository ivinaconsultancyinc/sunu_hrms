from fastapi import APIRouter, Form, HTTPException
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()

# Dummy mobile user database
mobile_users = {
    "mobile_user1": {"username": "mobile_user1", "password": "1234", "role": "agent"},
    "mobile_user2": {"username": "mobile_user2", "password": "abcd", "role": "field_officer"}
}

# JWT settings
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_mobile_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def mobile_login(username: str = Form(...), password: str = Form(...)):
    user = mobile_users.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid mobile credentials")
   
    token = create_mobile_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}