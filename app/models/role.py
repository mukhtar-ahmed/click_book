from sqlalchemy import Column,Integer,Enum as saEnum
from enum import Enum
from app.models.base_model import BaseModel

class RoleEnum(str, Enum):
    admin='admin'
    staff='staff'
    client='client'
    
class Role(BaseModel):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(saEnum(RoleEnum, create_type=True),nullable=False, index=True, unique=True)