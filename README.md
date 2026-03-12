
# Diabetes Prediction System API

A machine learning-powered REST API for predicting diabetes risk based on medical parameters. Built with FastAPI and scikit-learn, this system provides fast, accurate predictions using a trained predictive model.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Input Parameters](#input-parameters)
- [Output Format](#output-format)
- [Example Requests](#example-requests)
- [Testing](#testing)
- [Technologies](#technologies)
- [License](#license)

## 🎯 Overview

This project implements a diabetes prediction system using machine learning. The system takes various medical parameters as input and predicts whether a patient is likely to have diabetes or not. The predictions are exposed through a FastAPI REST API for easy integration with frontend applications or other services.

## ✨ Features

- **Fast Predictions**: Real-time diabetes risk prediction using pre-trained ML model
- **Input Validation**: Comprehensive validation with min/max constraints on all parameters
- **CORS Enabled**: Cross-Origin Resource Sharing support for frontend integration
- **Interactive Documentation**: Auto-generated Swagger UI for API testing
- **Type-Safe**: Uses Pydantic models for request/response validation
- **Health Check Endpoint**: API status and documentation endpoint

## 📁 Project Structure

```
Diabetes_Prediction_System_API_Data_Science-/
├── README.md                 # Project documentation
├── api.py                    # FastAPI application
├── requirements.txt          # Python dependencies
├── model/                    # Directory containing trained models
│   └── diabetes_predict.pkl  # Trained prediction model
└── LICENSE                   # Project license
```

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sarveshvengurlekar/Diabetes_Prediction_System_API_Data_Science-.git
   cd Diabetes_Prediction_System_API_Data_Science-
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Start the API server**
   ```bash
   uvicorn api:app --reload
   ```
   The server will start at `http://localhost:8000`

2. **Access the interactive API documentation**
   - Open your browser and go to: `http://localhost:8000/docs`
   - This opens the Swagger UI where you can test all endpoints

3. **Check API health**
   ```bash
   curl http://localhost:8000/
   ```

## 🔌 API Endpoints

### 1. Health Check Endpoint
- **Method**: `GET`
- **URL**: `/`
- **Description**: Returns API information and parameter documentation
- **Response**: JSON object with API details, parameter specifications, and testing instructions

### 2. Prediction Endpoint
- **Method**: `POST`
- **URL**: `/predict`
- **Description**: Predicts diabetes risk based on input medical parameters
- **Request Body**: JSON with medical parameters
- **Response**: JSON with prediction result

## 📥 Input Parameters

All input parameters have strict validation constraints:

| Parameter | Type | Min | Max | Description |
|-----------|------|-----|-----|-------------|
| `pregnancies` | int | 0 | 20 | Number of pregnancies |
| `glucose` | int | 50 | 300 | Blood glucose level (mg/dL) |
| `blood_pressure` | int | 30 | 150 | Diastolic blood pressure (mmHg) |
| `skin_thickness` | int | 0 | 100 | Triceps skin thickness (mm) |
| `insulin` | int | 0 | 900 | Serum insulin level (mu U/ml) |
| `bmi` | float | 10.0 | 70.0 | Body Mass Index (weight in kg / height in m²) |
| `dpf` | float | 0.0 | 3.0 | Diabetes Pedigree Function |
| `age` | int | 10 | 100 | Age in years |

## 📤 Output Format

The prediction endpoint returns a JSON response:

```json
{
  "prediction": 0 or 1,
  "result": "Non-Diabetic" or "Diabetic"
}
```

- **prediction**: `0` = Non-Diabetic, `1` = Diabetic
- **result**: Human-readable prediction result

## 📝 Example Requests

### Example 1: Non-Diabetic Prediction
**Request**:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 1,
    "glucose": 120,
    "blood_pressure": 80,
    "skin_thickness": 25,
    "insulin": 150,
    "bmi": 25.5,
    "dpf": 0.5,
    "age": 35
  }'
```

**Response**:
```json
{
  "prediction": 0,
  "result": "Non-Diabetic"
}
```

### Example 2: Diabetic Prediction
**Request**:
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 8,
    "glucose": 200,
    "blood_pressure": 90,
    "skin_thickness": 40,
    "insulin": 500,
    "bmi": 35.0,
    "dpf": 1.5,
    "age": 50
  }'
```

**Response**:
```json
{
  "prediction": 1,
  "result": "Diabetic"
}
```

## 🧪 Testing

### Using Swagger UI
1. Navigate to `http://localhost:8000/docs`
2. Click on the `/predict` endpoint
3. Click "Try it out"
4. Fill in the medical parameters
5. Click "Execute" to see the prediction

### Using Python Requests
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "pregnancies": 1,
    "glucose": 120,
    "blood_pressure": 80,
    "skin_thickness": 25,
    "insulin": 150,
    "bmi": 25.5,
    "dpf": 0.5,
    "age": 35
}

response = requests.post(url, json=data)
print(response.json())
```

## 🛠 Technologies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI web server
- **Pydantic**: Data validation using Python type annotations
- **scikit-learn**: Machine learning library for the predictive model
- **joblib**: Model serialization and deserialization
- **NumPy**: Numerical computing library
- **CORS**: Cross-Origin Resource Sharing for frontend integration

## 📋 Dependencies

See `requirements.txt` for complete list:
- fastapi
- uvicorn
- scikit-learn==1.6.1
- joblib
- numpy
- pydantic

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request with improvements or bug fixes.

## ⚠️ Disclaimer

This API is for educational and research purposes. It should not be used as a substitute for professional medical advice. Always consult with qualified healthcare professionals for medical diagnosis and treatment.

## 📧 Contact

For questions or feedback, please reach out to the project maintainer.

---
