# backend/app/services/user_service.py

from sqlalchemy.orm import Session
from backend.app.models import User
from backend.app.security.jwt import create_access_token

# Create a new user (registration)
def create_user(db: Session, username: str, password: str):
    # Check if the user already exists
    existing_user = db.query(User).filter(User.username == username).first()
    if existing_user:
        return None  # User already exists

    user = User(username=username)
    user.set_password(password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Get user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# User login (return JWT token)
def login_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if user and user.verify_password(password):
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}
    return None
