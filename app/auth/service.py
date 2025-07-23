from sqlalchemy.orm import Session
from app.schema.user import UserIn,UserOut
from app.schema.role import RoleIn,RoleListOut,RoleOut
from app.schema.api_response import APIResponse
from app.models.user import User
from app.models.role import Role
from fastapi import HTTPException,status
from app.logging.logger import logger
from app.auth.hashing import hash_password,verify_hash_password
from sqlalchemy.exc import SQLAlchemyError

def create_role(db:Session, role:RoleIn):
    # Check if role already exist
    db_role = db.query(Role).filter(Role.name == role.name).first()
    if db_role is not None:
        logger.error('Role already exist')
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Role already exist")
    # add new role
    new_role = Role(**role.model_dump())
    # push into db
    try:
        db.add(new_role)
        db.commit()
        db.refresh(new_role)
        return APIResponse(
            message="New Role added Successfully",
            data=RoleOut.model_validate(new_role)
        )
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error While adding Role ;{e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Error while adding new Role")
        
def get_roles(db:Session):
    roles = db.query(Role).all()
    response_data = RoleListOut(
        total=len(roles),
        roles=[RoleOut.model_validate(role) for role in roles]
    )
    return APIResponse(
        message="Role Featch Successfully",
        data=response_data
    )

def create_user(db:Session, user:UserIn):
    # check if user alredy exist
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user is not None:
        logger.warning("Try to add existing user")
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User with this email already exist")
    # Check if role exist
    new_user_role = db.query(Role).filter(Role.id == user.role_id).first()
    if not new_user_role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "User Role Not Exist")
    # Hash password
    hashed_password = hash_password(user.password)
    new_user = User(**user.model_dump())
    new_user.password = hashed_password
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return APIResponse(
            message='New user added successfully',
            data=UserOut.model_validate(new_user)
        )
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error While adding user ;{e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Error while adding new user")
        
def login_user(db:Session,email:str,password:str):
    # Check if user exist
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        logger.warning("User not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
    # Check password
    hashed_password = verify_hash_password(password, db_user.password)
    if not hashed_password:
        logger.warning("User not found")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="User not found")
    return APIResponse(
        message='User data featched',
        data=UserOut.model_validate(db_user)
    )
    