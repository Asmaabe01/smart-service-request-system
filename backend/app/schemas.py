# backend/app/schemas.py

from pydantic import BaseModel
from enum import Enum

class RequestStatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

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
        orm_mode = True
