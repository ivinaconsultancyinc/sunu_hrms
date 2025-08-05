# app/models/__init__.py
from app.models.notification import Notification
from app.models.user import User
from app.models.employee import Department, JobTitle, Employee
from app.models.attendance import Attendance
from app.models.analytics import Report, Metric
from app.models.audit import AuditLog
from app.models.payroll import Salary, Payslip
from app.models.recruitment import JobPost, Application, Interview
__all__ = [
    "Notification",
    "User",
    "Employee",
    "Attendance",
    "Report",
    "Metric",
    "AuditLog",
    "Payroll",
    "Recruitment",
    "department",
    "Jobtitle",
    "Payslip",
    "Salary",
    "JobPost",
    "Application",
    "Interview"  

]

