# backend/app/main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.app.db import get_db  # Ensure this import is correct
from backend.app.services.request_service import create_request, get_requests, get_request, update_request, delete_request
from backend.app.models import RequestCreate, RequestUpdate

app = FastAPI()

# Add routes...
# Route to create a new service request
@app.post("/requests/")
def create_new_request(request: RequestCreate, db: Session = Depends(get_db)):
    user_id = 1  # This should be replaced by the logged-in user's ID
    db_request = create_request(db=db, request=request, user_id=user_id)
    return db_request

# Route to get all service requests
@app.get("/requests/")
def read_requests(db: Session = Depends(get_db)):
    return get_requests(db=db)

# Route to get a single service request by ID
@app.get("/requests/{request_id}")
def read_request(request_id: int, db: Session = Depends(get_db)):
    db_request = get_request(db=db, request_id=request_id)
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return db_request

# Route to update a service request
@app.put("/requests/{request_id}")
def update_service_request(request_id: int, request: RequestUpdate, db: Session = Depends(get_db)):
    db_request = update_request(db=db, request_id=request_id, request=request)
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return db_request

# Route to delete a service request
@app.delete("/requests/{request_id}")
def delete_service_request(request_id: int, db: Session = Depends(get_db)):
    db_request = delete_request(db=db, request_id=request_id)
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return {"message": "Request deleted successfully"}
