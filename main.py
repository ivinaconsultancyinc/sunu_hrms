from fastapi import FastAPI, Request, Form, status, Depends, HTTPException
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt, JWTError
from datetime import datetime, timedelta
# Import routers BEFORE using them
from app.api import (
    auth, admin, hr, finance, audit, notifications, analytics,
    mobile_api, payslip, performance, recruitment, payroll,
    attendance, employee, user
)
from app.config import settings
from app.database import SessionLocal, engine, Base
from app.websockets import updates
from app.api import recruitment
# Initialize FastAPI app and templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")
# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(hr.router, prefix="/hr", tags=["HR"])
app.include_router(finance.router, prefix="/finance", tags=["Finance"])
app.include_router(audit.router, prefix="/audit", tags=["Audit"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
app.include_router(mobile_api.router, prefix="/mobile", tags=["Mobile"])
app.include_router(payslip.router, prefix="/api", tags=["Payslip"])
app.include_router(analytics.router, prefix="/api", tags=["Analytics"])  # Consider removing duplicate
app.include_router(performance.router, prefix="/performance", tags=["Performance"])
app.include_router(recruitment.router, prefix="/recruitment", tags=["Recruitment"])
app.include_router(payroll.router, prefix="/payroll", tags=["Payroll"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])
app.include_router(employee.router, prefix="/employees", tags=["Employees"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(recruitment.router)
# JWT settings
SECRET_KEY = settings.secret_key
ALGORITHM = settings.jwt_algorithm
# Dummy user database
fake_users_db = {
    "admin": {"username": "admin", "password": "admin123", "role": "admin"},
    # Add more users as needed
}
# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Create database tables
Base.metadata.create_all(bind=engine)
# Authentication helpers
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
def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if user and user["password"] == password:
        return user
    return None
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
# Logout
@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login")
    response.delete_cookie("access_token")
    return response


