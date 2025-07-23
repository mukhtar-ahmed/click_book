
from sqlalchemy import Column, DateTime,Integer,String,  ForeignKey
from sqlalchemy.orm import relationship

from app.models.base_model import BaseModel

class TimeOff(BaseModel):
    __tablename__ = 'time_offs'
    
    id = Column(Integer, primary_key=True, index=True)
    staff_id = Column(Integer, ForeignKey('staff_profiles.id'), nullable=False)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)
    reason = Column(String)
    
    staff_profile = relationship('StaffProfile', back_populates='time_off')