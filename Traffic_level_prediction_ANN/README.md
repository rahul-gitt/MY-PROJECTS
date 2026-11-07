# 🚦 Traffic Situation Classification Using Artificial Neural Network (ANN)

An Artificial Neural Network (ANN) based Machine Learning project that predicts traffic situations based on vehicle counts and time-related features. The model classifies traffic into four categories: **Heavy, High, Low, and Normal**.

The project uses TensorFlow/Keras for deep learning and Keras Tuner (RandomSearch) for hyperparameter optimization.

---

## 📌 Project Overview

Traffic congestion is a common problem in urban areas. Understanding traffic conditions can help improve traffic management and transportation planning.

In this project, an ANN classification model is developed to identify traffic situations using vehicle count information and time-based features.

**Objective:** Build and optimize a multiclass ANN model that accurately classifies traffic situations.

### 🎯 Prediction Classes

- Heavy
- High
- Low
- Normal

---

## 📂 Dataset Information

The dataset contains traffic observations with vehicle counts and time-related information.

| Feature | Description |
|---|---|
| Time | Time of traffic observation |
| Date | Date of observation |
| Day of the week | Day of the observation |
| CarCount | Number of cars |
| BikeCount | Number of bikes |
| BusCount | Number of buses |
| TruckCount | Number of trucks |
| Total | Total number of vehicles |
| Traffic Situation | Target variable |

**Dataset Statistics**

- Total Records: 2,976
- Initial Features: 9
- Missing Values: 0
- Duplicate Records: 0
- Target Classes: 4

*Note: The Total feature was removed because it was redundant with the individual vehicle counts.*

---

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Scikit-learn | Preprocessing and evaluation |
| TensorFlow | Deep learning framework |
| Keras | ANN model development |
| Keras Tuner | Hyperparameter optimization |
| Joblib | Saving preprocessing objects |

---

## 🔄 Project Workflow

1. Data Loading and Exploration
2. Data Cleaning and Preprocessing
3. Feature Engineering
4. One-Hot Encoding of weekdays
5. Feature Selection
6. Train-Test Split
7. Feature Scaling using StandardScaler
8. Target Encoding using LabelEncoder
9. ANN Model Development
10. Hyperparameter Tuning using RandomSearch
11. Model Training
12. Model Evaluation
13. Model Saving

---

## 🧹 Data Preprocessing

The following preprocessing techniques were applied:

**1. Feature Engineering**

- Converted the Time column into datetime format.
- Extracted Hour and Minute features.
- Removed the original Time column.
- Removed Total because it was the sum of CarCount, BikeCount, BusCount, and TruckCount.

**2. Categorical Encoding**

- Applied OneHotEncoder to the Day of the week feature.
- Applied LabelEncoder to the target variable.

**3. Feature Scaling**

Used StandardScaler to standardize numerical input features.

**4. Train-Test Split**

- Training Data: 80%
- Testing Data: 20%
- Random State: 42
- Stratified splitting to maintain class distribution.

Final input feature count: **14**

---

## 🧠 ANN Model Architecture

The model was developed using TensorFlow/Keras with a dynamic architecture optimized through Keras Tuner.

### Architecture

| Layer | Neurons |
|---|---:|
| Input Layer | 14 features |
| Hidden Layer 1 | 76 |
| Hidden Layer 2 | 54 |
| Hidden Layer 3 | 22 |
| Hidden Layer 4 | 58 |
| Hidden Layer 5 | 90 |
| Output Layer | 4 |

**Model Configuration**

- Hidden Layer Activation Functions: ReLU, ELU, and Tanh
- Output Activation: Softmax
- Optimizer: RMSprop
- Loss Function: Sparse Categorical Crossentropy
- Evaluation Metric: Accuracy
- Dropout Regularization: Used across hidden layers

### Hyperparameter Optimization

Keras Tuner's RandomSearch was used to find suitable ANN hyperparameters.

Parameters explored:

- Number of hidden layers
- Number of neurons
- Activation functions
- Dropout rates
- Optimizer selection

The best hyperparameter configuration was used to build and train the final ANN model.

---

## 📊 Model Performance

The model was trained for 100 epochs.

### Final Results

| Metric | Score |
|---|---:|
| Training Accuracy | 97.61% |
| Validation Accuracy | 94.30% |
| Test Accuracy | **94.30%** |
| Test Loss | 0.2288 |

<details>
<summary>Confusion Matrix</summary>

| Actual / Predicted | Heavy | High | Low | Normal |
|---|---:|---:|---:|---:|
| Heavy | 124 | 2 | 0 | 1 |
| High | 2 | 57 | 0 | 4 |
| Low | 0 | 0 | 66 | 0 |
| Normal | 6 | 16 | 3 | 315 |

</details>

The model achieved 94.30% test accuracy, demonstrating promising performance across the four traffic categories.

---

## 💾 Saved Model Files

The following files are saved for future predictions and deployment.

| File | Description |
|---|---|
| `traffic_classification_model.keras` | Trained ANN model |
| `scaler.pkl` | StandardScaler object |
| `label_encoder.pkl` | Target LabelEncoder |
| `day_encoder.pkl` | Weekday OneHotEncoder |

---

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd traffic-situation-classification
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install numpy pandas matplotlib scikit-learn tensorflow keras-tuner joblib
```

### 5. Run the Notebook

Open the project notebook in Jupyter Notebook or VS Code and execute the cells.

---

## 🔮 Future Improvements

- Develop an interactive Streamlit web application.
- Deploy the trained model using a cloud platform.
- Integrate real-time traffic sensor data.
- Improve classification performance for minority classes.
- Build a user-friendly traffic prediction interface.

---

## 👨‍💻 Author

**Rahul Mondal**

B.Tech – Computer Science and Engineering (AI & ML)

Interested in Artificial Intelligence, Machine Learning, Deep Learning, and real-world AI applications.

---

## ⭐ Acknowledgements

This project was developed as part of my continuous learning journey in Machine Learning and Deep Learning.

If you find this project useful, feel free to star the repository!

**#Python #MachineLearning #DeepLearning #ANN #TensorFlow #Keras #KerasTuner #ArtificialIntelligence**