from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models, schemas
from weather_service import get_weather, get_air_quality, calculate_risk
from export_service import export_to_csv
from fastapi.responses import FileResponse
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/weather", response_model=schemas.WeatherResponse)
def create_weather(request: schemas.WeatherCreate, db: Session = Depends(get_db)):

    if request.start_date > request.end_date:
        raise HTTPException(status_code=400, detail="Invalid date range")

    try:
        weather_data = get_weather(request.location)
    except:
        raise HTTPException(status_code=404, detail="Location not found")

    # NEW PART
    aqi = get_air_quality(weather_data["lat"], weather_data["lon"])
    risk = calculate_risk(weather_data["temp"], aqi)

    map_url = f"https://www.google.com/maps?q={weather_data['lat']},{weather_data['lon']}"

    record = models.WeatherRecord(
        location=request.location,
        latitude=weather_data["lat"],
        longitude=weather_data["lon"],
        start_date=request.start_date,
        end_date=request.end_date,
        avg_temperature=weather_data["temp"],
        humidity=weather_data["humidity"],
        description=weather_data["description"],
        aqi_index=aqi,
        risk_level=risk,
        map_url=map_url
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    return record

# READ
@app.get("/weather", response_model=List[schemas.WeatherResponse])
def read_weather(db: Session = Depends(get_db)):
    return db.query(models.WeatherRecord).all()

# UPDATE
@app.put("/weather/{id}")
def update_weather(id: int, request: schemas.WeatherCreate, db: Session = Depends(get_db)):
    record = db.query(models.WeatherRecord).filter(models.WeatherRecord.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    weather_data = get_weather(request.location)

    aqi = get_air_quality(weather_data["lat"], weather_data["lon"])
    risk = calculate_risk(weather_data["temp"], aqi)

    record.location = request.location
    record.latitude = weather_data["lat"]
    record.longitude = weather_data["lon"]
    record.avg_temperature = weather_data["temp"]
    record.humidity = weather_data["humidity"]
    record.description = weather_data["description"]
    record.aqi_index = aqi
    record.risk_level = risk

    db.commit()
    return {"message": "Updated successfully"}

# DELETE
@app.delete("/weather/{id}")
def delete_weather(id: int, db: Session = Depends(get_db)):
    record = db.query(models.WeatherRecord).filter(models.WeatherRecord.id == id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()
    return {"message": "Deleted successfully"}

# EXPORT
@app.get("/weather/export")
def export_weather(db: Session = Depends(get_db)):
    records = db.query(models.WeatherRecord).all()
    filename = export_to_csv(records)
    return FileResponse(filename, media_type="text/csv", filename=filename)