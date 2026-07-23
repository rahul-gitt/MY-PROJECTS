# 🚢 Titanic Survival Analysis

A complete **Exploratory Data Analysis (EDA)** project on the famous Titanic dataset using **Python, Pandas, NumPy, and Matplotlib**. This project explores passenger demographics, cleans missing data, visualizes trends, and uncovers the factors that influenced survival during the Titanic disaster.

---

## 📖 Project Overview

The sinking of the RMS Titanic remains one of history's most well-known maritime disasters. This project analyzes passenger data to answer an important question:

> **What factors increased a passenger's chances of surviving the Titanic disaster?**

The project follows a complete data analysis workflow, including data loading, cleaning, exploration, visualization, and insight generation.

---

## 🎯 Objectives

* Understand the dataset structure
* Perform data cleaning and preprocessing
* Handle missing and duplicate values
* Explore relationships between different features
* Visualize trends using charts
* Generate meaningful insights

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

## 📂 Project Structure

```text
Titanic-Survival-Analysis/
│
├── data/
│   └── train.csv
│
├── notebooks/
│   └── Titanic_Survival_Analysis.ipynb
│
├── images/
│   ├── survival_count.png
│   ├── survival_by_gender.png
│   ├── survival_by_class.png
│   └── age_distribution.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset Information

| Feature     | Description                       |
| ----------- | --------------------------------- |
| PassengerId | Unique passenger ID               |
| Survived    | Survival status (0 = No, 1 = Yes) |
| Pclass      | Passenger class                   |
| Name        | Passenger name                    |
| Sex         | Gender                            |
| Age         | Passenger age                     |
| SibSp       | Number of siblings/spouses aboard |
| Parch       | Number of parents/children aboard |
| Ticket      | Ticket number                     |
| Fare        | Ticket fare                       |
| Cabin       | Cabin number                      |
| Embarked    | Port of embarkation               |

---

## 🔍 Project Workflow

### 1️⃣ Data Loading

* Import dataset
* Load CSV file
* Display sample records

### 2️⃣ Data Understanding

* Dataset shape
* Data types
* Summary statistics
* Missing values
* Duplicate values

### 3️⃣ Data Cleaning

* Handle missing values
* Remove unnecessary columns
* Fix inconsistent data

### 4️⃣ Exploratory Data Analysis (EDA)

* Survival Distribution
* Gender-wise Survival
* Passenger Class Analysis
* Age Analysis
* Fare Analysis
* Embarkation Analysis
* Family Size Analysis

### 5️⃣ Data Visualization

* 📊 Bar Charts
* 🥧 Pie Charts
* 📈 Histograms
* 📉 Scatter Plots
* 📦 Box Plots
* 📑 Subplots

---

## 📈 Key Insights

* Female passengers had a significantly higher survival rate.
* First-class passengers were more likely to survive.
* Children showed better survival rates than many adults.
* Higher ticket fares were associated with higher survival chances.
* Most passengers boarded from Southampton.
* The `Cabin` column contained a large number of missing values.
* Passenger class strongly influenced survival probability.

---

## 📸 Sample Visualizations

The project includes visualizations such as:

* Survival Count
* Survival by Gender
* Survival by Passenger Class
* Age Distribution
* Fare Distribution
* Embarkation Distribution
* Family Size Analysis

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/Titanic-Survival-Analysis.git
```

### Navigate to the Project

```bash
cd Titanic-Survival-Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
notebooks/Titanic_Survival_Analysis.ipynb
```

---

## 📦 Requirements

```text
pandas
numpy
matplotlib
jupyter
```

Or install them manually:

```bash
pip install pandas numpy matplotlib jupyter
```

---

## 🎓 Learning Outcomes

This project helped strengthen practical skills in:

* Data Cleaning
* Data Analysis
* Exploratory Data Analysis (EDA)
* Data Visualization
* Pandas Operations
* Real-world Dataset Handling
* Git & GitHub Project Management

---

## 🔮 Future Improvements

* Add Seaborn visualizations
* Perform Feature Engineering
* Build Machine Learning models
* Compare classification algorithms
* Deploy as a web application

---

## 👨‍💻 Author

**Rahul Mondal**

B.Tech CSE (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, Data Science, and Python Development.

---

## ⭐ Show Your Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is intended for educational and portfolio purposes.
