import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# -----------------------------
# Load Model and Scaler
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent

model = joblib.load(BASE_DIR / "linear_model.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")


# -----------------------------
# Page
# -----------------------------

st.title("🚚 Delivery Time AI")
st.write("Predict food delivery time using machine learning.")


# -----------------------------
# User Inputs
# -----------------------------

distance_km = st.number_input(
    "Distance (km)",
    min_value=0.1,
    max_value=50.0,
    value=10.0
)

weather = st.selectbox(
    "Weather",
    ["Clear", "Rainy", "Foggy", "Snowy", "Windy"]
)

traffic_level = st.selectbox(
    "Traffic Level",
    ["Low", "Medium", "High"]
)

time_of_day = st.selectbox(
    "Time of Day",
    ["Morning", "Afternoon", "Evening", "Night"]
)

vehicle_type = st.selectbox(
    "Vehicle Type",
    ["Bike", "Scooter", "Car"]
)

preparation_time_min = st.number_input(
    "Preparation Time (min)",
    min_value=1.0,
    max_value=60.0,
    value=15.0
)

courier_experience_yrs = st.number_input(
    "Courier Experience (years)",
    min_value=0.0,
    max_value=20.0,
    value=3.0
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Delivery Time"):

    data = pd.DataFrame([{
        "Distance_km": distance_km,
        "Weather": weather,
        "Traffic_Level": traffic_level,
        "Time_of_Day": time_of_day,
        "Vehicle_Type": vehicle_type,
        "Preparation_Time_min": preparation_time_min,
        "Courier_Experience_yrs": courier_experience_yrs
    }])


    # Ordinal Encoding
    data["Traffic_Level"] = data["Traffic_Level"].map({
        "Low": 0,
        "Medium": 1,
        "High": 2
    })


    # One-Hot Encoding
    data = pd.get_dummies(
        data,
        columns=[
            "Weather",
            "Time_of_Day",
            "Vehicle_Type"
        ],
        dtype=int
    )


    # Match training columns
    expected_columns = scaler.feature_names_in_

    data = data.reindex(
        columns=expected_columns,
        fill_value=0
    )


    # Scaling
    data_scaled = scaler.transform(data)


    # Prediction
    prediction = model.predict(data_scaled)


    st.success(
        f"Estimated Delivery Time: {prediction[0]:.2f} minutes"
    )