from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from app.core.config import settings

engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False,bind=engine)
Base = declarative_base()


