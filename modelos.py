import uuid
from pydantic import BaseModel
from datetime import datetime








class UserResponse(BaseModel):
    """"this class represents the expected data strcuture for an user"""
    id_number: str
    name: str
    last_name: str 
    pasword: str
    phone_number: str
    email: str  
    class Config:
        orm_mode = True

class financial_product_status(BaseModel):
    id_status: str
    name: str
    description: str

class financial_product_type(BaseModel):
    id: str
    name: str
    description: str   

class transaction_status(BaseModel):
    id: str
    name: str
    description: str  

class transaction_type(BaseModel):
    id: str
    name: str
    description: str      

class financial_product(BaseModel):
    id: str
    user_fk: str
    type_fk: str
    status_fk: str
    date: datetime
    amount: float
    has_card: int
 
class banking_card(BaseModel):
    id: str
    card_number: str
    financial_product_fk: str
    password: str
    creation_date: datetime
    expiry_date: datetime 

class movement_history(BaseModel):
    name: str
    description:str
    date: datetime
    amount: float
    financial_product_fk: str 

class transaction(BaseModel):
    id: str
    transaction_type_fk: str
    date: datetime
    status_fk: str
    amount: float
    origin_fk: str
    destination_fk: str



class transaction_code(BaseModel):
    id: str
    transaction_fk: str
    creation_date: datetime
    expiry_date: datetime
    status: int     


