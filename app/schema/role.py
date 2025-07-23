from typing import List
from pydantic import BaseModel
from app.models.role import RoleEnum
from datetime import datetime

class RoleIn(BaseModel):
    name: RoleEnum
    
    model_config = {
        'json_schema_extra':{
            'example':{
                'name':'client'
            }
        }
    }
    
class RoleOut(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime | None
    
    model_config = {
        'from_attributes': True
    }
    
class RoleListOut(BaseModel):
    total:int
    roles:List[RoleOut]
    
    model_config = {
        'from_attributes': True
    }