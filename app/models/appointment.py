from sqlalchemy import Column, DateTime,Integer, func, Enum as saEnum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum
from app.models.base_model import BaseModel
    
class AppointmentStatusEnum(str, Enum):
    pending='pending'
    confirmed='confirmed'
    cancelled='cancelled'
    completed='completed'
    rescheduled='rescheduled'


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
    