# app/models/__init__.py
from app.models.notification import Notification
from app.models.user import User
from app.models.employee import Department, JobTitle, Employee
from app.models.attendance import Attendance
from app.models.analytics import Report, Metric
from app.models.audit import Auditlog
from app.models.payroll import Salary, Payslip
from app.models.performance import PerformanceReview, Goal, KPI
from app.models.recruitment import Jobpost, Application, Interview
__all__ = [
    "Notification",
    "User",
    "Employee",
    "Attendance",
    "Report",
    "Metric",
    "Auditlog",
    "Payroll",
    "Performance",
    "Recruitment",
    "department",
    "Jobtitle",
    "Payslip",
    "Salary",
    "PerformanceReview",
    "Goal",
    "KPI",
    "JobPost",
    "Application",
    "Interview"  

]

