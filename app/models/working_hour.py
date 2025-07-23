from sqlalchemy import Column, DateTime,Integer,func,  ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

class WorkingHour(BaseModel):
    __tablename__ = 'working_hours'
    
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff_profiles.id', ondelete='CASCADE'), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    
    staff_profile = relationship('StaffProfile', back_populates='working_hours')