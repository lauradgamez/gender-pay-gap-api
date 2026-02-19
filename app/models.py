from pydantic import BaseModel
from typing import Optional


class PredictionInput(BaseModel):
    """
    Input schema for gender pay gap prediction.
    
    Contains labor market indicators from ILOSTAT data including
    employment figures, earnings, and working hours by gender.
    """
    ref_area: str
    ref_area_label: str
    classif1: str
    classif1_label: str
    obs_status_label: str
    time: int
    obs_value_employees_women: float
    obs_value_employees_men: float
    obs_value_earnings_women: float
    obs_value_earnings_men: float
    obs_value_hours_women: float
    obs_value_hours_men: float
    earnings_ratio: float
    hours_ratio: float
    employment_ratio: float
    delta_earnings: float
    delta_hours: float


class PredictionOutput(BaseModel):
    """
    Output schema for prediction response.
    
    Returns the predicted gender pay gap as a percentage
    along with a status message.
    """
    predicted_pay_gap: float
    message: str