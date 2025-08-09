from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import numpy as np
import pickle
import os

# Initialize app
app = FastAPI(title="Car Price Predictor")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "lm_use_2nd.pkl")
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

# Feature constraints
FEATURE_LIMITS = {
    "curbweight": (520, 4066),
    "horsepower": (48, 288)
}

CYLINDER_FEATURES = [
    'cylindernumber_five', 'cylindernumber_four',
    'cylindernumber_six', 'cylindernumber_twelve', 'cylindernumber_two'
]

ALL_FEATURES = [
    'curbweight', 'horsepower', 'enginelocation_rear',
    'enginetype_ohcv', *CYLINDER_FEATURES, 'fuelsystem_spdi'
]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "feature_limits": FEATURE_LIMITS
    })

@app.post("/predict")
async def predict(request: Request):
    try:
        # Get JSON data
        data = await request.json()
        
        # Validation
        errors = []
        
        # Check required fields
        required_fields = ALL_FEATURES
        for field in required_fields:
            if field not in data:
                errors.append(f"Missing field: {field}")
        
        if errors:
            return JSONResponse(
                status_code=400,
                content={"error": " | ".join(errors)}
            )
        
        # Extract values
        curbweight = data['curbweight']
        horsepower = data['horsepower']
        enginelocation_rear = data['enginelocation_rear']
        enginetype_ohcv = data['enginetype_ohcv']
        cylindernumber_five = data['cylindernumber_five']
        cylindernumber_four = data['cylindernumber_four']
        cylindernumber_six = data['cylindernumber_six']
        cylindernumber_twelve = data['cylindernumber_twelve']
        cylindernumber_two = data['cylindernumber_two']
        fuelsystem_spdi = data['fuelsystem_spdi']
        
        # Numerical value validation
        if not (FEATURE_LIMITS["curbweight"][0] <= curbweight <= FEATURE_LIMITS["curbweight"][1]):
            errors.append(f"Curb weight must be between {FEATURE_LIMITS['curbweight'][0]} and {FEATURE_LIMITS['curbweight'][1]}")
        
        if not (FEATURE_LIMITS["horsepower"][0] <= horsepower <= FEATURE_LIMITS["horsepower"][1]):
            errors.append(f"Horsepower must be between {FEATURE_LIMITS['horsepower'][0]} and {FEATURE_LIMITS['horsepower'][1]}")
        
        # Cylinder validation
        cylinder_values = [
            cylindernumber_five, cylindernumber_four, cylindernumber_six,
            cylindernumber_twelve, cylindernumber_two
        ]
        selected_cylinders = sum(1 for val in cylinder_values if val == 1.0)
        
        if selected_cylinders == 0:
            errors.append("Please select one cylinder type")
        elif selected_cylinders > 1:
            errors.append("Only one cylinder type can be selected")
        
        if errors:
            return JSONResponse(
                status_code=400,
                content={"error": " | ".join(errors)}
            )
        
        # Prepare input
        input_data = np.array([
            1, curbweight, horsepower, enginelocation_rear,
            enginetype_ohcv, cylindernumber_five, cylindernumber_four,
            cylindernumber_six, cylindernumber_twelve, cylindernumber_two,
            fuelsystem_spdi
        ]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        prediction = round(float(prediction), 2)
        return JSONResponse(
            content={"prediction": prediction}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Server error: {str(e)}"}
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True
    )
