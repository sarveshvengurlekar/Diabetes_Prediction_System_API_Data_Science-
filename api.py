from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI(title="Diabetes Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Allow all websites
    allow_credentials=True,
    allow_methods=["*"],      # Allow GET, POST, PUT, DELETE
    allow_headers=["*"],      # Allow all headers
)

# Load trained model
model = joblib.load("model/diabetes_predict.pkl")

# ================================
# Input Schema (With Range Checks)
# ================================
class DiabetesInput(BaseModel):
    pregnancies: int = Field(..., ge=0, le=20)
    glucose: int = Field(..., ge=50, le=300)
    blood_pressure: int = Field(..., ge=30, le=150)
    skin_thickness: int = Field(..., ge=0, le=100)
    insulin: int = Field(..., ge=0, le=900)
    bmi: float = Field(..., ge=10.0, le=70.0)
    dpf: float = Field(..., ge=0.0, le=3.0)
    age: int = Field(..., ge=10, le=100)

# ================================
# Output Schema
# ================================
class PredictionOutput(BaseModel):
    prediction: int
    result: str

# ================================
# Health Check
# ================================
@app.get("/")
def health():
    return { 
            "API Name" : "Diabetes Prediction API",
            
            "I/P Parameters": "pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age", 

            "pregnancies" : "datatype = int, min = 0, max = 20",
            "glucose" : "datatype = int, min = 50, max = 300",
            "blood_pressure" : "datatype = int, min = 30, max = 150",
            "skin_thickness" : "datatype = int min = 0, max = 100",
            "insulin" : "datatype = int, min = 0, max = 900",
            "bmi" : "datatype = float, min = 10.0, max = 70.0",
            "dpf" : "datatype = float, min = 0.0, max = 3.0",
            "age" : "datatype = int, min = 10, max = 100",

            "O/P Parameters" : "Diabetic, Non-Diabetic",

            "Diabetic": {
                "prediction": "1",
                "result": "Diabetic"
            },

            "Non-Diabetic":{
            "prediction": "0",
            "result": "Non-Diabetic"
            }
            }

# ================================
# Prediction Endpoint
# ================================
@app.post("/predict", response_model=PredictionOutput)
def predict(data: DiabetesInput):

    # Maintain EXACT feature order
    input_array = np.array([[
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.dpf,
        data.age
    ]])

    prediction = int(model.predict(input_array)[0])

    if prediction == 1:
        result = "Diabetic"
    else:
        result = "Non-Diabetic"

    return {
        "prediction": prediction,
        "result": result
    }
