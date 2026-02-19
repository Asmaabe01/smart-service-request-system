# backend/app/security/auth.py

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from backend.app.db import get_db
from backend.app.services.user_service import create_user, login_user

router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    user = create_user(db, username=request.username, password=request.password)
    if not user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return {"username": user.username, "id": user.id}

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    login_response = login_user(db, username=request.username, password=request.password)
    if not login_response:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return login_response
