# Gender Pay Gap Prediction API

A production-ready REST API for predicting gender pay gap using Machine Learning, based on ILOSTAT labor market data.

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0.3-red)
![License](https://img.shields.io/badge/license-MIT-blue)

## 📊 Overview

This API provides real-time predictions of gender pay gap percentages based on comprehensive labor market indicators. Built as part of a Master's thesis in Data Science, it transforms academic research into a deployable production system.

**Live Demo:** [API Documentation](https://gender-pay-gap-api.onrender.com/docs)

![API Documentation](docs_screenshot.png)

## ✨ Features

- **RESTful API** with automatic interactive documentation
- **High accuracy predictions** (R² = 0.9509)
- **Professional preprocessing pipeline** with proper handling of categorical and numeric features
- **Comprehensive error handling** and input validation
- **Health check endpoint** for monitoring
- **Production-ready code** following industry best practices

## 🛠️ Tech Stack

- **Framework:** FastAPI
- **ML Model:** XGBoost Regressor
- **Data Processing:** pandas, NumPy, scikit-learn
- **Validation:** Pydantic
- **Deployment:** Uvicorn (ASGI server)

## 📈 Model Performance

The XGBoost model was trained on 7,089 records from ILOSTAT spanning 1969-2024 across 119 countries.

| Metric | Value |
|--------|-------|
| R² Score | 0.9509 |
| RMSE | 0.0412 |
| MSE | 0.0017 |

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/lauradgamez/gender-pay-gap-api.git
cd gender-pay-gap-api
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate     # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the API:
```bash
uvicorn app.main:app --reload
```

5. Access the interactive documentation:
```
http://localhost:8000/docs
```

## 📡 API Endpoints

### `GET /`
Root endpoint with API information.

**Response:**
```json
{
  "message": "Gender Pay Gap Prediction API",
  "version": "1.0.0",
  "endpoints": {
    "docs": "/docs",
    "health": "/health",
    "predict": "/predict"
  }
}
```

### `GET /health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "message": "API is running"
}
```

### `POST /predict`
Predict gender pay gap based on labor market indicators.

**Request body:**
```json
{
  "ref_area": "col",
  "ref_area_label": "colombia",
  "classif1": "ocu_isco08_1",
  "classif1_label": "ocupación (ciuo-08): 1. directores y gerentes",
  "obs_status_label": "",
  "time": 2020,
  "obs_value_employees_women": 1500000,
  "obs_value_employees_men": 1800000,
  "obs_value_earnings_women": 8.5,
  "obs_value_earnings_men": 10.2,
  "obs_value_hours_women": 42.3,
  "obs_value_hours_men": 44.1,
  "earnings_ratio": 0.833,
  "hours_ratio": 0.959,
  "employment_ratio": 0.833,
  "delta_earnings": 1.7,
  "delta_hours": 1.8
}
```

**Response:**
```json
{
  "predicted_pay_gap": 15.596815,
  "message": "Prediction successful"
}
```

## 📁 Project Structure
```
gender-pay-gap-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application and endpoints
│   ├── models.py            # Pydantic schemas for validation
│   └── ml_model.py          # Model loading and preprocessing
├── saved_models/
│   ├── xgboost_model.joblib
│   ├── label_encoders.joblib
│   └── minmax_scaler.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔧 Preprocessing Pipeline

The API implements a robust preprocessing pipeline:

1. **Label Encoding** for categorical variables (country, occupation, status)
2. **MinMaxScaler** for numeric variables only
3. **Column ordering** to match training data

This ensures consistency between training and inference while following ML engineering best practices.

## 🎯 Use Cases

- **Policy Analysis:** Evaluate gender pay gap across different sectors and countries
- **Research:** Support academic studies on labor market inequality
- **Business Intelligence:** Integrate pay gap predictions into HR analytics dashboards
- **Benchmarking:** Compare organizations against predicted market standards

## 🔮 Future Improvements

- [x] Deploy to cloud platform (Render)
- [ ] Add batch prediction endpoint
- [ ] Implement API authentication
- [ ] Add caching for frequent predictions
- [ ] Create monitoring dashboard
- [ ] Expand to include more recent data via ILOSTAT API integration

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Contact

**Laura Daniela Gámez**

- Email: lauradanielag2@hotmail.com
- LinkedIn: [linkedin.com/in/lauradgamez](https://www.linkedin.com/in/lauradgamez/)
- GitHub: [@lauradgamez](https://github.com/lauradgamez)

---

⭐ If you find this project useful, please consider giving it a star!
```

---