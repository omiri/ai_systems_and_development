from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Titanic AI API")

# Load the serialized model safely
model = joblib.load('titanic_model.joblib')

class PassengerInput(BaseModel):
    Pclass: int
    Sex: int  
    Age: float
    SibSp: int
    Parch: int
    Fare: float

@app.get("/")
def home():
    return {"message": "Titanic API is Online!"}

@app.post("/predict")
def predict(passenger: PassengerInput):
    data = pd.DataFrame([passenger.dict()])
    prediction = int(model.predict(data)[0])
    probability = float(model.predict_proba(data)[0][1])
    
    return {
        "status": "Survived" if prediction == 1 else "Perished",
        "survival_probability": f"{probability * 100:.2f}%"
    }