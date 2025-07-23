from pydantic import BaseModel,EmailStr, Field
from app.schema.role import RoleOut

class UserIn(BaseModel):
    name:str = Field(min_length=3)
    email:EmailStr
    password:str = Field(min_length=8)
    role_id:int
    
    model_config ={
        'json_schema_extra':{
            'example':{
                'name':'Mukhtar',
                'email':'mukhtar@gmail.com',
                'password':'12345678',
                'role_id':1
            }
        }
    }
    
class UserOut(BaseModel):
    id:int
    name:str
    email:str
    is_active:bool
    role_id:int
    
    model_config = {
        'from_attributes':True
    }