from pydantic import BaseModel  # Import BaseModel
from sqlalchemy import Column, Integer, String, Enum
import enum
from backend.app.db import Base

class RequestStatusEnum(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

# Request model (SQLAlchemy)
class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(RequestStatusEnum), default=RequestStatusEnum.pending)
    user_id = Column(Integer)

# RequestCreate (Pydantic model for incoming request data)
class RequestCreate(BaseModel):  # Make sure BaseModel is imported
    title: str
    description: str
    status: RequestStatusEnum = RequestStatusEnum.pending

# RequestUpdate (Pydantic model for updating request data)
class RequestUpdate(BaseModel):  # Make sure BaseModel is imported
    title: str
    description: str
    status: RequestStatusEnum
