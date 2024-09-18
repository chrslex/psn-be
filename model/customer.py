from typing import Optional
import datetime
from dataclasses import dataclass

@dataclass
class Customer:
    ID:Optional[int]
    title: Optional[str]
    name:str
    gender: str
    phone_number:str
    image:str
    email:str
    created_at:datetime.datetime
    updated_at:datetime.datetime

@dataclass
class Address:
    id:int
    customer_id:int
    address:str
    district:str
    city:str
    province:str
    postal_code:str
    created_at:str
    updated_at:str
