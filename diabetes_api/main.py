from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] during dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = joblib.load("model.pkl")

class DiabetesInput(BaseModel):
    age: int
    gender: str
    polyuria: str
    polydipsia: str
    sudden_weight_loss: str
    weakness: str
    polyphagia: str
    genital_thrush: str
    visual_blurring: str
    itching: str
    irritability: str
    delayed_healing: str
    partial_paresis: str
    muscle_stiffness: str
    alopecia: str
    obesity: str

@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    df = pd.DataFrame([data.dict()])
    df.rename(columns={
    "age": "Age",
    "gender": "Gender",
    "polyuria": "Polyuria",
    "polydipsia": "Polydipsia",
    "sudden_weight_loss": "sudden weight loss",
    "weakness": "weakness",
    "polyphagia": "Polyphagia",
    "genital_thrush": "Genital thrush",
    "visual_blurring": "visual blurring",
    "itching": "Itching",
    "irritability": "Irritability",
    "delayed_healing": "delayed healing",
    "partial_paresis": "partial paresis",
    "muscle_stiffness": "muscle stiffness",
    "alopecia": "Alopecia",
    "obesity": "Obesity"}, inplace=True)
    df.replace(to_replace=["Male", "Female"], value=[1, 0], inplace=True)
    df.replace(to_replace=["Yes", "No"], value=[1, 0], inplace=True)
    prediction = model.predict(df)[0]
    return {
        "prediction": int(prediction),
        "message": "Diabetic" if prediction == 1 else "Non-Diabetic"
    }
