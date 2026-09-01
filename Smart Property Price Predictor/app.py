import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load("house_price_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")
default_values = joblib.load("default_values.pkl")


st.set_page_config(
    page_title="Smart Property Price Predictor",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 Smart Property Price Predictor")
st.write("Enter the property details to estimate the house price.")


# Main inputs
overall_qual = st.slider(
    "Overall Quality",
    min_value=1,
    max_value=10,
    value=5
)

gr_liv_area = st.number_input(
    "Living Area (sq ft)",
    min_value=100,
    max_value=10000,
    value=1500
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2000
)

lot_area = st.number_input(
    "Lot Area (sq ft)",
    min_value=100,
    max_value=100000,
    value=8000
)

garage_cars = st.number_input(
    "Garage Cars",
    min_value=0,
    max_value=5,
    value=2
)

total_bsmt_sf = st.number_input(
    "Total Basement Area",
    min_value=0,
    max_value=5000,
    value=1000
)

first_flr_sf = st.number_input(
    "1st Floor Area",
    min_value=0,
    max_value=5000,
    value=1000
)

second_flr_sf = st.number_input(
    "2nd Floor Area",
    min_value=0,
    max_value=5000,
    value=500
)

garage_area = st.number_input(
    "Garage Area",
    min_value=0,
    max_value=2000,
    value=400
)

full_bath = st.number_input(
    "Full Bathrooms",
    min_value=0,
    max_value=5,
    value=2
)


if st.button("🔮 Predict House Price"):

    # Start with default values
    input_data = default_values.copy()

    # Replace important features with user inputs
    values = {
        "OverallQual": overall_qual,
        "GrLivArea": gr_liv_area,
        "YearBuilt": year_built,
        "LotArea": lot_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "1stFlrSF": first_flr_sf,
        "2ndFlrSF": second_flr_sf,
        "GarageArea": garage_area,
        "FullBath": full_bath
    }

    for column, value in values.items():
        if column in input_data.index:
            input_data[column] = value

    # Convert to DataFrame
    input_df = pd.DataFrame(
        [input_data],
        columns=feature_columns
    )

    # Prediction
    prediction = model.predict(input_df)[0]

    st.success(
        f"🏠 Estimated House Price: ${prediction:,.0f}"
    )