import sqlalchemy.types
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, SmallInteger
from sqlalchemy.orm import relationship

from apiRest.db import Base


class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(SmallInteger, primary_key=True)
    store_id = Column(SmallInteger)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    address_id = Column(SmallInteger)
    active = Column(SmallInteger)
    create_date = Column(DateTime)
    last_update = Column(sqlalchemy.types.TIMESTAMP)


class CustomerList(Base):
    __tablename__ = "customer_list"

    ID = Column(SmallInteger, primary_key=True)
    name = Column(String)
    address = Column(String)
    zip_code = Column(String)
    phone = Column(String)
    city = Column(String)
    country = Column(String)
    notes = Column(String)
    SID = Column(SmallInteger)
