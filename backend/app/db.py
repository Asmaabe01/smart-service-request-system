# backend/app/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL (adjust according to your database settings)
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://username:password@localhost/dbname"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"charset": "utf8mb4"})

# SessionLocal class will serve as a session maker for creating DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the models
Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
