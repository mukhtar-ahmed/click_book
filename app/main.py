from fastapi import FastAPI
from app.core.database import engine
from app.models.models import Base


Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def health():
    return "Working"

# Todos
# models
# env and 
# Move to postgres
# database migration , alembic
# add logs