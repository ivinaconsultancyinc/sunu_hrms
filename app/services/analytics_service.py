 """
Analytics Service Module for SUNU HRMS

This module provides functions to compute key HR metrics such as:
- Total employee count
- Average salary
- Total payroll cost
- Summary report generation

Author: SUNU HRMS Team
"""

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.employee import Employee
from app.models.payslip import Payslip

def get_employee_count(db: Session) -> int:
    """Returns the total number of employees."""
    return db.query(func.count(Employee.id)).scalar()

def get_average_salary(db: Session) -> float:
    """Returns the average base salary of employees."""
    return db.query(func.avg(Employee.base_salary)).scalar()

def get_total_payroll(db: Session) -> float:
    """Returns the total payroll cost from all payslips."""
    return db.query(func.sum(Payslip.net_salary)).scalar()

def generate_summary_report(db: Session) -> dict:
    """Generates a summary report with key HR metrics."""
    return {
        "employee_count": get_employee_count(db),
        "average_salary": get_average_salary(db),
        "total_payroll": get_total_payroll(db)
    }