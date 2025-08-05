# app/models/__init__.py
from app.models.notification import Notification
from app.models.user import User
from app.models.employee import Department, JobTitle, Employee
from app.models.attendance import Attendance
from app.models.analytics import Report, Metric
from app.models.audit import AuditLog
from app.models.payroll import Salary, PaySlip
from app.models.performance import PerformanceReview, Goal, KPI
from app.models.recruitment import Jobpost, Application, Interview
__all__ = [
    "Notification",
    "User",
    "Employee",
    "Attendance",
    "Report",
    "Metric",
    "AuditLog",
    "Payroll",
    "Performance",
    "Recruitment",
    "department",
    "Jobtitle",
    "PaySlip",
    "Salary",
    "PerformanceReview",
    "Goal",
    "KPI",
    "JobPost",
    "Application",
    "Interview"  

]

