# 🚚 DeliveryTime AI

A machine learning project that predicts **food delivery time in
minutes** using distance, weather, traffic, time of day, vehicle type,
preparation time, and courier experience.

## 📌 Project Overview

DeliveryTime AI is an end-to-end regression project covering data
cleaning, exploratory data analysis, preprocessing, model comparison,
and a Streamlit prediction application.

**Objective:** Predict `Delivery_Time_min` for a food delivery order.

## 📊 Dataset

The project uses the **Food Delivery Time Prediction** dataset.

### Features

  Feature                    Description
  -------------------------- ---------------------------------
  `Order_ID`                 Unique order identifier
  `Distance_km`              Delivery distance in kilometers
  `Weather`                  Weather condition
  `Traffic_Level`            Traffic intensity
  `Time_of_Day`              Time period
  `Vehicle_Type`             Delivery vehicle
  `Preparation_Time_min`     Food preparation time
  `Courier_Experience_yrs`   Courier experience in years
  `Delivery_Time_min`        Target variable

## 🔍 Exploratory Data Analysis

Key observations:

-   Distance has a strong positive relationship with delivery time.
-   Preparation time contributes to longer delivery times.
-   Higher traffic generally leads to longer delivery times.
-   Weather, time of day, and vehicle type show comparatively weaker
    relationships.
-   `Order_ID` was removed because it is only an identifier.

## ⚙️ Preprocessing

### Categorical Features

**One-Hot Encoding** - `Weather` - `Time_of_Day` - `Vehicle_Type`

**Ordinal Encoding** - `Traffic_Level`

Traffic mapping:

``` text
Low → 0
Medium → 1
High → 2
```

### Numerical Features

`StandardScaler` was used for:

-   `Distance_km`
-   `Preparation_Time_min`
-   `Courier_Experience_yrs`

## 🤖 Model Comparison

The following regression models were evaluated using MAE, RMSE, and R².

  Model                       MAE (min)   RMSE (min)          R²
  ------------------------- ----------- ------------ -----------
  🏆 Linear Regression         **5.90**     **8.82**   **0.827**
  Ridge Regression                 5.90         8.82       0.826
  Lasso Regression                 6.57         9.36       0.805
  Random Forest Regressor          6.88         9.70       0.790
  Decision Tree Regressor         10.92        15.59       0.457

## 🏆 Final Model

**Linear Regression** was selected as the final model because it
achieved the best test performance.

-   **MAE:** \~5.90 minutes
-   **RMSE:** \~8.82 minutes
-   **R²:** \~0.827

The model's average absolute prediction error is approximately **6
minutes** on the test set.

## 🖥️ Streamlit Application

The Streamlit app allows users to enter:

-   Distance
-   Weather
-   Traffic level
-   Time of day
-   Vehicle type
-   Preparation time
-   Courier experience

The application returns the estimated delivery time.

### Application Flow

``` text
User Input
    ↓
Feature Encoding
    ↓
Feature Scaling
    ↓
Linear Regression Model
    ↓
Predicted Delivery Time
```

## 📁 Project Structure

``` text
DeliveryTime AI/
│
├── app.py
├── main.ipynb
├── Food_Delivery_Times.csv
├── linear_model.pkl
├── scaler.pkl
├── README.md
└── .gitignore
```

## 🛠️ Tech Stack

-   **Python**
-   **Pandas** --- Data manipulation
-   **NumPy** --- Numerical operations
-   **Matplotlib** --- Visualization
-   **Seaborn** --- Exploratory visualization
-   **Scikit-learn** --- Preprocessing, modeling, and evaluation
-   **Joblib** --- Model serialization
-   **Streamlit** --- Web application

## 🚀 Installation & Setup

### 1. Clone the repository

``` bash
git clone <your-repository-url>
cd "DeliveryTime AI"
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

``` bash
.venv\Scripts\activate
```

**macOS/Linux:**

``` bash
source .venv/bin/activate
```

### 4. Install dependencies

``` bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib streamlit
```

### 5. Run the application

``` bash
streamlit run app.py
```

## 📈 Evaluation Metrics

**MAE (Mean Absolute Error):** Average absolute difference between
actual and predicted delivery time. Lower is better.

**RMSE (Root Mean Squared Error):** Penalizes larger prediction errors
more strongly. Lower is better.

**R² Score:** Measures how well the model explains variation in the
target. Higher is better.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

-   Regression
-   EDA
-   Missing-value handling
-   Feature encoding
-   Feature scaling
-   Train-test splitting
-   Model evaluation
-   Model comparison
-   Model serialization
-   Streamlit application development

## 🔮 Future Improvements

-   Hyperparameter tuning
-   Cross-validation
-   Advanced ensemble models
-   Better preprocessing pipelines
-   Feature importance and explainability
-   Improved UI/UX
-   Cloud deployment

## 👨‍💻 Author

**Rahul Mondal**

Built as part of an AI/ML learning and project portfolio.

## ⭐ Acknowledgements

Dataset: **Food Delivery Time Prediction** by denkuznetz on Kaggle.

If you find this project useful, consider giving the repository a ⭐.
