
from sqlalchemy import Column, Integer,String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id= Column(Integer,primary_key=True,index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    
    staff_profile = relationship('StaffProfile', back_populates='user', uselist=False)
    appointments = relationship('Appointment', back_populates='client')