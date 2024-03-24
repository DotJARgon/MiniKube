from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_id: int
    store_id: int
    first_name: str
    last_name: str
    email: str
    address_id: int
    active: int
    create_date: str
    last_update: str

    class Config:
        orm_mode = True


class CustomerListBase(BaseModel):
    ID: int
    name: str
    address: str
    zip_code: str
    phone: str
    city: str
    country: str
    notes: str
    SID: int

    class Config:
        orm_mode = True
