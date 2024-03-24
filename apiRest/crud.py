# This will only have read functionality for this assignment
from sqlalchemy.orm import Session

import models
import schemas


def get_customer(db: Session, cust_id: int):
    return db.query(models.Customer).filter(models.Customer.customer_id == cust_id).first()

def get_customer_list_by_country(db: Session, country: str):
    return db.query(models.CustomerList).filter(models.CustomerList.country == country).all().order_by(models.CustomerList.city.desc())

