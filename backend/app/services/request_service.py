# backend/app/services/request_service.py

from sqlalchemy.orm import Session
from backend.app.models import Request, RequestCreate, RequestUpdate
from backend.app.db import get_db

# Create a new request
def create_request(db: Session, request: RequestCreate, user_id: int):
    db_request = Request(
        title=request.title,
        description=request.description,
        user_id=user_id
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# Get all requests
def get_requests(db: Session):
    return db.query(Request).all()

# Get a request by ID
def get_request(db: Session, request_id: int):
    return db.query(Request).filter(Request.id == request_id).first()

# Update a request
def update_request(db: Session, request_id: int, request: RequestUpdate):
    db_request = db.query(Request).filter(Request.id == request_id).first()
    if db_request:
        db_request.title = request.title
        db_request.description = request.description
        db_request.status = request.status
        db.commit()
        db.refresh(db_request)
    return db_request

# Delete a request
def delete_request(db: Session, request_id: int):
    db_request = db.query(Request).filter(Request.id == request_id).first()
    if db_request:
        db.delete(db_request)
        db.commit()
    return db_request
