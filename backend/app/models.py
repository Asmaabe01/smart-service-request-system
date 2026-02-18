# backend/app/models.py

from sqlalchemy import Column, Integer, String, Enum
from passlib.context import CryptContext
from backend.app.db import Base
import enum

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Request Status Enum
class RequestStatusEnum(enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password_hash)

# Request model
class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(RequestStatusEnum), default=RequestStatusEnum.pending)
    user_id = Column(Integer)
