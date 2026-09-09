from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel


APP_NAME = "student-ml-api"


def get_version() -> str:
    version_file = Path(__file__).with_name("VERSION")
    return version_file.read_text(encoding="utf-8").strip()


app = FastAPI(
    title="Student ML API",
    description="A simple prediction API used to demonstrate an MLOps workflow.",
    version=get_version(),
)


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": APP_NAME,
        "application_version": get_version(),
        "model_version": "model-1",
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = request.value * 2

    return {
        "input": request.value,
        "prediction": prediction,
    }