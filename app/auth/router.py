from fastapi import APIRouter,status, Depends
from app.schema.user import UserIn
from app.schema.role import RoleIn
from app.schema.api_response import APIResponse
from app.dependencies import db_session_dp
from app.auth.service import create_role,create_user,get_roles,login_user
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/role',status_code=status.HTTP_201_CREATED,response_model=APIResponse)
async def register_role(db:db_session_dp, role:RoleIn):
    return create_role(db,role)

@router.get('/roles',status_code=status.HTTP_200_OK,response_model=APIResponse)
async def roles(db:db_session_dp):
    return get_roles(db)

@router.post('/register',status_code=status.HTTP_201_CREATED,response_model=APIResponse)
async def register_user(db:db_session_dp, user:UserIn):
    return create_user(db, user)

@router.post('/login', status_code = status.HTTP_200_OK , response_model=APIResponse)
async def login(db:db_session_dp,login_data: Annotated[OAuth2PasswordRequestForm,Depends()]):
    # user login 
    return login_user(db,login_data.username,login_data.password)