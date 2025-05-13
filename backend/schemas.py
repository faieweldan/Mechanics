from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: str
    name: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class User(UserBase):
    id: int
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Tender schemas
class TenderBase(BaseModel):
    title: str
    description: str

class TenderCreate(TenderBase):
    image_url: Optional[str] = None

class Tender(TenderBase):
    id: int
    user_id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True