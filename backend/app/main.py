"""
Main FastAPI application entry point.
the system launcher and central hub, the place that will conta
Client (Swagger / Frontend)
        ↓
Routes (API endpoints/ handle HTTP)
        ↓
Services (handle business logic)
        ↓
Schemas (data validation)
        ↓
Models (database structure)
        ↓
db.py (database connection)
        ↓
PostgreSQL

"""

from fastapi import FastAPI

from app.routes import plants
from app.database.db import Base, engine

from app.core.logger import setup_logger
from app.core.error_handler import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler
)

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


# setup logger
logger = setup_logger()

logger.info("Starting Smart Farming API")

# create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Farming API",
    version="1.0"
)


# include routes
app.include_router(plants.router)


# register global exception handlers
app.add_exception_handler(
    StarletteHTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    general_exception_handler
)


@app.get("/")
def root():
    logger.info("Root endpoint accessed")
    return {
        "message": "Smart Farming API running"
    }
