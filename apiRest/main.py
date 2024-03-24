from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from apiRest import crud
from apiRest import models
from apiRest import schemas
from apiRest.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/customers/{customer_id}", response_model=schemas.CustomerBase)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer(db, cust_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@app.get("/customerList/", response_model=list[schemas.CustomerListBase])
def read_customer_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customer_list = crud.get_customer_list(db, skip=skip, limit=limit)
    return customer_list


@app.get("/customerList/{country}", response_model=list[schemas.CustomerListBase])
def read_customer_list(country: str, db: Session = Depends(get_db)):
    customer_list = crud.get_customer_list_by_country(db, country=country)
    return customer_list
