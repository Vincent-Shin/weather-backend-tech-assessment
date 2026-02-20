from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from database import Base
from datetime import datetime

class WeatherRecord(Base):
    __tablename__ = "weather_records"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    avg_temperature = Column(Float)
    humidity = Column(Float)
    description = Column(String)
    aqi_index = Column(Integer)         
    risk_level = Column(String)         
    map_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)