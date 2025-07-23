from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

class StaffProfile(BaseModel):
    __tablename__ = 'staff_profiles'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, unique=True)
    bio = Column(String)
    specialization = Column(String) 
    
    user = relationship('User', back_populates='staff_profile')
    working_hours = relationship('WorkingHour', back_populates='staff_profile', cascade='all, delete-orphan')
    time_off = relationship('TimeOff',back_populates='staff_profile', cascade='all, delete-orphan' )
    services = relationship('Service', back_populates='staff_profile', cascade='all, delete-orphan')
    appointments = relationship('Appointment', back_populates='staff', cascade='all, delete-orphan')