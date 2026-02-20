from pydantic import BaseModel
from datetime import date

class WeatherCreate(BaseModel):
    location: str
    start_date: date
    end_date: date

class WeatherResponse(BaseModel):
    id: int
    location: str
    avg_temperature: float
    humidity: float
    description: str
    map_url: str
    aqi_index: int
    risk_level: str
    
    model_config = {
    "from_attributes": True
    }