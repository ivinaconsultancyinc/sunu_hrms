 """
Payroll Service Module for SUNU HRMS

This module provides functions to calculate gross salary, deductions,
net salary, and generate a payslip dictionary for employees.

Author: SUNU HRMS Team
"""

from typing import Dict

def calculate_gross_salary(base_salary: float, allowances: Dict[str, float]) -> float:
    """
    Calculate gross salary by summing base salary and all allowances.

    Args:
        base_salary (float): The base salary of the employee.
        allowances (Dict[str, float]): A dictionary of allowance names and amounts.

    Returns:
        float: The gross salary.
    """
    return base_salary + sum(allowances.values())

def calculate_deductions(deductions: Dict[str, float]) -> float:
    """
    Calculate total deductions.

    Args:
        deductions (Dict[str, float]): A dictionary of deduction names and amounts.

    Returns:
        float: The total deductions.
    """
    return sum(deductions.values())

def calculate_net_salary(gross_salary: float, total_deductions: float) -> float:
    """
    Calculate net salary by subtracting deductions from gross salary.

    Args:
        gross_salary (float): The gross salary.
        total_deductions (float): The total deductions.

    Returns:
        float: The net salary.
    """
    return gross_salary - total_deductions

def generate_payslip(employee_id: int, base_salary: float, allowances: Dict[str, float], deductions: Dict[str, float]) -> Dict:
    """
    Generate a payslip dictionary for an employee.

    Args:
        employee_id (int): The ID of the employee.
        base_salary (float): The base salary of the employee.
        allowances (Dict[str, float]): A dictionary of allowance names and amounts.
        deductions (Dict[str, float]): A dictionary of deduction names and amounts.

    Returns:
        Dict: A dictionary containing payslip details.
    """
    gross_salary = calculate_gross_salary(base_salary, allowances)
    total_deductions = calculate_deductions(deductions)
    net_salary = calculate_net_salary(gross_salary, total_deductions)

    return {
        "employee_id": employee_id,
        "base_salary": base_salary,
        "allowances": allowances,
        "deductions": deductions,
        "gross_salary": gross_salary,
        "total_deductions": total_deductions,
        "net_salary": net_salary
    }


