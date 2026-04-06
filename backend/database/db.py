"""
Database connection and session management.

This file is responsible for:

1. Connecting FastAPI to PostgreSQL
2. Creating SQLAlchemy engine
3. Creating database session
4. Providing Base class for models
5. Managing database dependency for API routes
"""

# SQLAlchemy core tools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Import DATABASE_URL from config
from app.config import DATABASE_URL


# ===============================
# CREATE DATABASE ENGINE
# ===============================

"""
Engine is the core connection between Python and PostgreSQL.

It uses the DATABASE_URL from .env

Example:
postgresql://postgres:password@localhost:5432/smart_farming
"""
engine = create_engine(
    DATABASE_URL,
    echo=False  # set True if you want SQL logs in terminal
)


# ===============================
# CREATE SESSION
# ===============================

"""
Session is used to talk to the database.

Every API request will open a session,
do database operations,
and then close the session.

Think of it like:

Open connection → Do work → Close connection
"""

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# ===============================
# BASE MODEL
# ===============================

"""
Base is the parent class for all database models.

Example:

class Plant(Base):
    __tablename__ = "plants"

This allows SQLAlchemy to create tables.
"""

Base = declarative_base()


# ===============================
# DATABASE DEPENDENCY
# ===============================

"""
This function will be used in FastAPI routes.

Example:

def get_plants(db: Session = Depends(get_db)):

It ensures:

1. Open database session
2. Use it
3. Close it safely
"""

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
