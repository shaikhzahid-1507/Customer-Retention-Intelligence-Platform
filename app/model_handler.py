import joblib
from pathlib import Path
import pandas as pd

# ==========================
# Project Root
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# File Paths
# ==========================
MODEL_PATH = BASE_DIR / "models" / "trained_models" / "churn_model.pkl"
SCALER_PATH = BASE_DIR / "models" / "scalers" / "scaler.pkl"
ENCODER_PATH = BASE_DIR / "models" / "encoders" / "label_encoder.pkl"
FEATURE_PATH = BASE_DIR / "models" / "feature_columns.pkl"


# ==========================
# Load Files
# ==========================
def load_model():
    return joblib.load(MODEL_PATH)


def load_scaler():
    return joblib.load(SCALER_PATH)


def load_encoder():
    return joblib.load(ENCODER_PATH)


def load_feature_columns():
    return joblib.load(FEATURE_PATH)


# ==========================
# Prediction Function
# ==========================
def predict_customer(model, scaler, feature_columns, customer_data):

    # Convert dictionary to dataframe
    input_df = pd.DataFrame([customer_data])

    # Remove customerID
    if "customerID" in input_df.columns:
        input_df.drop(columns=["customerID"], inplace=True)

    # One-Hot Encoding
    input_df = pd.get_dummies(input_df, drop_first=True)

    # Add missing columns
    for col in feature_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Remove extra columns
    input_df = input_df[feature_columns]

    # Scale numerical columns
    numerical_cols = [
        "tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]

    input_df[numerical_cols] = scaler.transform(
        input_df[numerical_cols]
    )

    # Prediction
    prediction = model.predict(input_df)[0]

    # Probability
    probability = model.predict_proba(input_df)[0][1]

    return prediction, probability