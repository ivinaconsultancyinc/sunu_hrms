from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.models.payroll import Payslip

# Create a new payslip record
def create_payslip(db: Session, payslip_data: dict) -> Payslip:
    payslip = Payslip(**payslip_data)
    db.add(payslip)
    db.commit()
    db.refresh(payslip)
    return payslip

# Get a payslip by ID
def get_payslip_by_id(db: Session, payslip_id: int) -> Payslip:
    return db.query(Payslip).filter(Payslip.id == payslip_id).first()

# Get all payslips
def get_all_payslips(db: Session):
    return db.query(Payslip).all()

# Update a payslip by ID
def update_payslip(db: Session, payslip_id: int, update_data: dict) -> Payslip:
    payslip = db.query(Payslip).filter(Payslip.id == payslip_id).first()
    if not payslip:
        raise NoResultFound(f"Payslip with ID {payslip_id} not found")
    for key, value in update_data.items():
        setattr(payslip, key, value)
    db.commit()
    db.refresh(payslip)
    return payslip

# Delete a payslip by ID
def delete_payslip(db: Session, payslip_id: int) -> bool:
    payslip = db.query(Payslip).filter(Payslip.id == payslip_id).first()
    if not payslip:
        return False
    db.delete(payslip)
    db.commit()

    return True
