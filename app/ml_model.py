import joblib
import pandas as pd
import numpy as np
from pathlib import Path

# Load trained model and preprocessors
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "saved_models" / "xgboost_model.joblib"
ENCODERS_PATH = BASE_DIR / "saved_models" / "label_encoders.joblib"
SCALER_PATH = BASE_DIR / "saved_models" / "minmax_scaler.joblib"

model = joblib.load(MODEL_PATH)
label_encoders = joblib.load(ENCODERS_PATH)
scaler = joblib.load(SCALER_PATH)


def preprocess_input(data: dict) -> np.ndarray:
    """
    Preprocess input data for model prediction.
    
    Pipeline:
    1. Label encode categorical variables
    2. Scale numeric variables with MinMaxScaler
    3. Reorder columns to match model training
    
    Args:
        data: Dictionary containing input features
        
    Returns:
        Preprocessed feature array ready for model prediction
    """
    df = pd.DataFrame([data])
    
    # Apply label encoding to categorical features
    categorical_cols = ['ref_area', 'ref_area_label', 'classif1', 
                       'classif1_label', 'obs_status_label']
    
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].replace('', np.nan)
            encoder = label_encoders[col]
            df[col] = encoder.transform(df[col])
    
    # Scale numeric features
    numeric_cols = scaler.feature_names_in_
    df[numeric_cols] = scaler.transform(df[numeric_cols])
    
    # Ensure column order matches model expectations
    feature_columns = list(model.feature_names_in_)
    df = df[feature_columns]
    
    return df.values


def predict_pay_gap(data: dict) -> float:
    """
    Predict gender pay gap percentage.
    
    Args:
        data: Dictionary containing input features
        
    Returns:
        Predicted pay gap as a percentage (float)
    """
    processed_data = preprocess_input(data)
    prediction = model.predict(processed_data)
    
    return float(prediction[0])