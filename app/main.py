from fastapi import FastAPI, Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from jose import jwt
from datetime import datetime, timedelta

# Initialize FastAPI app and templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(hr.router, prefix="/hr", tags=["HR"])
app.include_router(finance.router, prefix="/finance", tags=["Finance"])
app.include_router(audit.router, prefix="/audit", tags=["Audit"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(mobile_api.router, prefix="/mobile", tags=["Mobile"])
app.include_router(payslip.router, prefix="/api", tags=["Payslip"])
app.include_router(analytics.router, prefix="/api", tags=["Analytics"])
app.include_router(performance.router, prefix="/performance", tags=["Performance"])
app.include_router(recruitment.router, prefix="/recruitment", tags=["Recruitment"])
app.include_router(payroll.router, prefix="/payroll", tags=["Payroll"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(employee.router, prefix="/employees", tags=["Employees"])
app.include_router(user.router, prefix="/users", tags=["Users"])

# Dummy user database

# Secret key and algorithm for JWT
from app.config import settings
SECRET_KEY = settings.secret_key
ALGORITHM = settings.jwt_algorithm

from fastapi import Depends, HTTPException
from jose import JWTError
from app.database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
from app.api import auth
from app.api import admin
from app.api import hr
from app.api import finance
from app.api import audit
from app.api import notifications
from app.api import analytics
from app.api import mobile_api
from app.api import payslip
from app.api import performance
from app.api import recruitment
from app.api import payroll
from app.api import attendance
from app.api import employee
from app.api import user

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

def require_role(role: str):
    def role_checker(user: dict = Depends(get_current_user)):
        if user["role"] != role:
            raise HTTPException(status_code=403, detail="Insufficient privileges")
        return user
    return role_checker


# Function to authenticate user
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return user
    return None

# Function to create JWT token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Login form (GET)
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

# Login form submission (POST)
@app.post("/login", response_class=HTMLResponse)
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    user = authenticate_user(username, password)
    if not user:
        return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Invalid credentials"
    })

@app.get("/logout")
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=token, httponly=True)
    return response

@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)
    response.delete_cookie("access_token")
    return response

            "request": request,
            "error": "Invalid credentials"
        })
    token = create_access_token({"sub": user["username"], "role": user["role"]})
    response = RedirectResponse(url="/dashboard", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="access_token", value=token, httponly=True)
    return response

# Save the updated file
with open("main_updated.py", "w") as f:


# Create database tables
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
