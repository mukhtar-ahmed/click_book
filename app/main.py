from typing import Annotated
from fastapi import FastAPI, Depends
from requests import Session
from app.core.database import engine, SessionLocal
from app.models.models import Base
from starlette.middleware.base import BaseHTTPMiddleware
from app.logging.middleware import log_middleware
from sqlalchemy.orm import session
from app.models.models import *


Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
    

app.add_middleware(BaseHTTPMiddleware, dispatch=log_middleware)

@app.get("/")
async def health():
    return "Working"

@app.get("/users")
async def get_users(db: Annotated[Session, Depends(get_db)]):
    return db.query(User).all()

@app.get("/roles")
async def get_roles(db: Annotated[Session, Depends(get_db)]):
    return db.query(Role).all()
    


# POST endpoint to add a user
@app.post("/users/test-add")
async def create_test_user(db: Annotated[Session, Depends(get_db)],name:str, email:str,password:str,role_id:int):
    new_user = User(
        name=name,
        email=email,
        password=password,  # For testing; in real cases, hash this!
        role_id=role_id,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/role")
async def create_test_user(db: Annotated[Session, Depends(get_db)],name:str):
    new_role = Role(
        name=name,
        
    )
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

# Todos
# models
# env and 
# Move to postgres
# database migration , alembic
# add logs