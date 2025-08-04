 # app/models/__init__.py
from app.models.notification import notifications
from app.models.user import users
from app.models.employee import departments, job_titles, employees
from app.models.attendance import Attendance
from app.models.analytics import Report, Metric
from app.models.audit import audit_logs
from app.models.payroll import salaries, payslips
from app.models.performance import performance_reviews, goals, kpis
from app.models.recruitment import job_posts, applications, interviews
__all__ = [
    "notifications",
    "users",
    "Employees",
    "Attendance",
    "Report",
    "Metric",
    "audit_logs",
    "Payroll",
    "Performance",
    "Recruitment",
    "departments",
    "job_titles",
    "payslips",
    "salaries",
    "performance_reviews",
    "goals",
    "kpis",
    "job_posts",
    "applications",
    "interviews"  

]

