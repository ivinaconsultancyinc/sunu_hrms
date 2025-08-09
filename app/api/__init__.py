from .auth import router as auth_router
from .admin import router as admin_router
from .hr import router as hr_router
from .finance import router as finance_router
from .audit import router as audit_router
from .notifications import router as notifications_router
from .analytics import router as analytics_router
from .mobile_api import router as mobile_api_router
from .payslip import router as payslip_router
from .performance import router as performance_router
from .recruitment import router as recruitment_router
from .payroll import router as payroll_router
from .attendance import router as attendance_router
from .employee import router as employee_router
from .user import router as user_router
__all__ = [
    "auth_router",
    "admin_router",
    "hr_router",
    "finance_router",
    "audit_router",
    "notifications_router",
    "analytics_router",
    "mobile_api_router",
    "payslip_router",
    "performance_router",
    "recruitment_router",
    "payroll_router",
    "attendance_router",
    "employee_router",
    "user_router"
]


