# backend/app/main.py

from fastapi import FastAPI
from backend.app.security.auth import router as auth_router
from backend.app.db import engine, Base
from backend.app.services.request_service import create_request, get_requests, get_request, update_request, delete_request
from backend.app.models import RequestCreate, RequestUpdate

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Register auth router
app.include_router(auth_router, prefix="/auth", tags=["authentication"])

# Add routes for requests
@app.post("/requests/")
def create_new_request(request: RequestCreate, db: Session = Depends(get_db)):
    user_id = 1  # Replace this with actual logged-in user ID
    db_request = create_request(db=db, request=request, user_id=user_id)
    return db_request

@app.get("/requests/")
def read_requests(db: Session = Depends(get_db)):
    return get_requests(db=db)

@app.get("/requests/{request_id}")
def read_request(request_id: int, db: Session = Depends(get_db)):
    db_request = get_request(db=db, request_id=request_id)
    if not db_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return db_request
