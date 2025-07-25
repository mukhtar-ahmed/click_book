from app.core.database import Base
from sqlalchemy import Column, DateTime,func

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class BaseModel(Base, TimestampMixin):
    __abstract__ = True