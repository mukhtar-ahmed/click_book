from sqlalchemy import Column, Integer,String,  ForeignKey, Float
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

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