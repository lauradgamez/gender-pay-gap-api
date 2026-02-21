from fastapi import FastAPI, HTTPException
from app.models import PredictionInput, PredictionOutput
from app.ml_model import predict_pay_gap

app = FastAPI(
    title="Gender Pay Gap Prediction API",
    description="Machine Learning API for predicting gender pay gap based on ILOSTAT labor market data",
    version="1.0.0"
)


@app.get("/")
def root():
    """Root endpoint with API information."""
    return {
        "message": "Gender Pay Gap Prediction API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "predict": "/predict"
        }
    }


@app.get("/health")
def health_check():
    """Health check endpoint for monitoring."""
    return {
        "status": "healthy",
        "message": "API is running"
    }


@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput) -> PredictionOutput:
    """
    Predict gender pay gap percentage.
    
    Uses a XGBoost model trained on ILOSTAT data to predict
    the gender pay gap based on employment, earnings, and hours worked.
    
    Args:
        input_data: Labor market indicators validated by Pydantic
        
    Returns:
        Predicted pay gap percentage with status message
        
    Raises:
        HTTPException: 500 if prediction fails
    """
    try:
        data_dict = input_data.model_dump(by_alias=False)
        prediction = predict_pay_gap(data_dict)
        
        return PredictionOutput(
            predicted_pay_gap=prediction,
            message="Prediction successful"
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )