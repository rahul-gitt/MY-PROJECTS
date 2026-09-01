# 🏠 Smart Property Price Predictor

An end-to-end Machine Learning project that predicts residential property prices using important property features.

## 📌 Overview

This project follows a complete Machine Learning workflow:

**Data Preprocessing → Feature Engineering → Model Training → Evaluation → Hyperparameter Tuning → Feature Importance → Model Saving → Streamlit Application**

## 📊 Dataset

The project uses the **House Prices: Advanced Regression Techniques** dataset.

- **Target:** `SalePrice`
- **Rows:** 1460
- **Features after preprocessing:** 213

Important features include `OverallQual`, `GrLivArea`, `TotalSF`, `LotArea`, `YearBuilt`, `GarageCars`, `GarageArea`, and `TotalBathrooms`.

## 🧹 Data Preprocessing

- Missing value analysis
- Categorical feature encoding
- Feature engineering
- Train-test split
- Feature scaling
- Data type validation

### Feature Engineering

Created features such as:

- `TotalSF`
- `TotalBathrooms`
- `HouseAge`

## 🤖 Models

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor

## 🏆 Model Performance

| Model | R² | RMSE | MAE |
|---|---:|---:|---:|
| Linear Regression | 0.6740 | 50,001 | 21,685 |
| Ridge Regression | 0.7030 | 47,719 | 21,441 |
| Lasso Regression | 0.6740 | 49,974 | 21,650 |
| Decision Tree | 0.7680 | 42,155 | 26,551 |
| **Random Forest** | **0.8845** | **29,761** | **17,935** |

**Final Model:** Random Forest Regressor

The model achieved an R² score of approximately **0.88**, explaining around 88% of the variation in house prices on the test dataset.

## 🎯 Hyperparameter Tuning

Grid Search was used for Random Forest.

Selected configuration:

- `n_estimators = 100`
- `max_depth = None`
- `min_samples_split = 2`
- `min_samples_leaf = 2`

The original Random Forest performed slightly better on the current test split and was retained as the final application model.

## 🔍 Feature Importance

Top features:

1. `OverallQual`
2. `TotalSF`
3. `2ndFlrSF`
4. `YearBuilt`
5. `LotArea`
6. `TotalBathrooms`
7. `BsmtFinSF1`
8. `HouseAge`
9. `LotFrontage`
10. `GarageCars`

## 🖥️ Streamlit Application

The project includes an interactive Streamlit interface where users can enter property details and receive an estimated house price.

Main inputs include:

- Overall Quality
- Living Area
- Year Built
- Lot Area
- Garage Cars
- Basement Area
- 1st Floor Area
- 2nd Floor Area
- Garage Area
- Full Bathrooms

## 📁 Project Structure

```text
Smart Property Price Predictor/
│
├── app.py
├── main.ipynb
├── houseprice.csv
├── house_price_model.pkl
├── feature_columns.pkl
├── default_values.pkl
└── README.md
```

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## ▶️ Run Locally

Install dependencies:

```bash
pip install pandas numpy scikit-learn joblib streamlit
```

Run the application:

```bash
streamlit run app.py
```

## 📚 Key Learning Outcomes

- Data preprocessing
- Feature engineering
- Regression
- Model evaluation
- Model comparison
- Hyperparameter tuning
- Feature importance
- Model serialization with Joblib
- Streamlit application development

## 👨‍💻 Author

**Rahul Mondal**

Machine Learning Project — Smart Property Price Predictor
