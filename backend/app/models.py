# backend/app/models.py

from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.app.db import Base

# Request model for the database
class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="Pending")  # Status: Pending, In Progress, Completed

    # User who submitted the request (for now using a mock user)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="requests")

# Pydantic model for Request input validation
class RequestCreate(BaseModel):
    title: str
    description: str

class RequestUpdate(BaseModel):
    title: str
    description: str
    status: str
