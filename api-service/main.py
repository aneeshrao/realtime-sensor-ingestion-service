from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI(title="Sensor Ingestion Service")

class SensorReading(BaseModel):
    sensor_id: str
    value: float
    metric_type: Literal["temperature", "pressure"]
    timestamp: str # ISO 8601 format

@app.get("/")
async def root():
    return {"message": "Realtime Service API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/ingest")
async def ingest_data(reading: SensorReading):
    return {"status": "SUCCESS", "message": "Data received"}