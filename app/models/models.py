from app.core.database import Base
from sqlalchemy import Column, DateTime,Integer,String, func, Enum as saEnum, Boolean, ForeignKey, Date, Time, Float
from sqlalchemy.orm import relationship
from enum import Enum

class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class BaseModel(Base, TimestampMixin):
    __abstract__ = True
    
class RoleEnum(str, Enum):
    admin='admin'
    staff='staff'
    client='client'

class AppointmentStatusEnum(str, Enum):
    pending='pending'
    confirmed='confirmed'
    cancelled='cancelled'
    completed='completed'
    rescheduled='rescheduled'

class Role(BaseModel):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(saEnum(RoleEnum, create_type=True),nullable=False, index=True, unique=True)
    

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
    
class WorkingHour(BaseModel):
    __tablename__ = 'working_hours'
    
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff_profiles.id', ondelete='CASCADE'), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    
    staff_profile = relationship('StaffProfile', back_populates='working_hours')
    
class TimeOff(BaseModel):
    __tablename__ = 'time_offs'
    
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff_profiles.id'), nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    reason = Column(String)
    
    staff_profile = relationship('StaffProfile', back_populates='time_off')
    
class Service(BaseModel): 
    __tablename__ = 'services'
    
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff_profiles.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    duration_minutes = Column(Integer)
    price = Column(Float)
    
    appointments = relationship('Appointment', back_populates='service')
    staff_profile = relationship('StaffProfile', back_populates='services')

class Appointment(BaseModel):
    __tablename__ = 'appointments'
    
    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    staff_id = Column(Integer, ForeignKey('staff_profiles.id'), nullable=False, index=True)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False, index=True)
    date_time = Column(DateTime, nullable=False)
    status = Column(saEnum(AppointmentStatusEnum, create_type = True), nullable=False, index=True)
    
    client = relationship('User', back_populates='appointments')   
    staff = relationship('StaffProfile', back_populates='appointments')
    service = relationship('Service', back_populates='appointments') 
    