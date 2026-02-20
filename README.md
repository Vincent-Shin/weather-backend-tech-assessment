# Weather Backend API -- PM Accelerator Tech Assessment

**Author:** TRUNG TUAN MAI

------------------------------------------------------------------------

## Project Overview

This project is a backend Weather API built using FastAPI.\
It allows users to:

-   Enter a location and date range
-   Retrieve real-time weather data from OpenWeather API
-   Store weather data in a database
-   Perform full CRUD operations
-   Export stored records to CSV format
-   Retrieve Air Quality Index (AQI)
-   Calculate a rule-based weather risk score

This project demonstrates backend engineering skills aligned with
AI-driven product development.

------------------------------------------------------------------------

## Features

-   RESTful API using FastAPI
-   Full CRUD (Create, Read, Update, Delete)
-   Date range validation
-   Location validation via external API
-   Air Quality API integration
-   Risk scoring logic (rule-based)
-   Google Maps integration
-   CSV data export
-   Error handling and validation

------------------------------------------------------------------------

## Tech Stack

-   Python 3
-   FastAPI
-   SQLAlchemy
-   SQLite
-   Uvicorn
-   OpenWeather API
-   Air Pollution API
-   python-dotenv

------------------------------------------------------------------------

## How to Run

### 1. Clone the repository

    git clone https://github.com/Vincent-Shin/weather-backend-tech-assessment.git
    cd weather-backend-tech-assessment

### 2. Create virtual environment

    python -m venv venv
    venv\Scripts\activate

### 3. Install dependencies

    pip install -r requirements.txt

### 4. Configure environment variables

Create a `.env` file in the project root:

    DATABASE_URL=sqlite:///./weather.db
    WEATHER_API_KEY=your_openweather_api_key_here

### 5. Run the server

    uvicorn main:app --reload

Access Swagger UI at:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## API Endpoints

-   POST /weather → Create weather record
-   GET /weather → Read all records
-   PUT /weather/{id} → Update record
-   DELETE /weather/{id} → Delete record
-   GET /weather/export → Export data to CSV

------------------------------------------------------------------------

## Architecture Overview

Client → FastAPI → External APIs (Weather + AQI) → SQLite Database

------------------------------------------------------------------------

## Extra Enhancements

-   Integrated Air Quality Index
-   Implemented rule-based Risk Score system
-   Added CSV export functionality

------------------------------------------------------------------------

This project was developed as part of the PM Accelerator AI/ML
Engineering Technical Assessment.
