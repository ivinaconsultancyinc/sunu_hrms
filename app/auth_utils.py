from fastapi import Request, Depends, HTTPException
from jose import jwt, JWTError
from datetime import datetime, timedelta

# Dummy user database
fake_users_db = {
    "alice": {"username": "alice", "password": "secret", "role": "admin"},
    "bob": {"username": "bob", "password": "password", "role": "user"}
}

# JWT configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

# Authenticate user credentials
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return user
    return None

# Create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Get current user from JWT token
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

# Role-based access control
def require_role(role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(status_code=403, detail="Insufficient privileges")
        return user
    return role_checker
