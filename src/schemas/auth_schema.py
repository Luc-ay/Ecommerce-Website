from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum as PyEnum


class USERROLE(PyEnum):
    ADMIN = "ADMIN"
    USER = "USER"
    VENDOR = "VENDOR"


class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=6)
    username: str = Field(min_length=3, max_length=50)
    role: USERROLE


class UserCreateResponse(BaseModel):
    email: str
    username: str
    id: Optional[int] = None
    role: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: str
    password: str = Field(min_length=6)
