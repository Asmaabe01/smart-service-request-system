# backend/app/models.py

from sqlalchemy import Column, Integer, String
from passlib.context import CryptContext  # For password hashing
from backend.app.db import Base

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)

    # Method to hash password
    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    # Method to verify password
    def verify_password(self, password: str):
        return pwd_context.verify(password, self.password_hash)
