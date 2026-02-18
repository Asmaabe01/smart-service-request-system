# backend/app/schemas.py

from pydantic import BaseModel
from enum import Enum

# Request Status Enum for Pydantic
class RequestStatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

# User Schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True

# Request Schemas
class RequestBase(BaseModel):
    title: str
    description: str

class RequestCreate(RequestBase):
    pass

class RequestUpdate(RequestBase):
    status: RequestStatusEnum

class Request(RequestBase):
    id: int
    status: RequestStatusEnum
    user_id: int

    class Config:
        from_attributes = True
