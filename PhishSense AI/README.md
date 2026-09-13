# 🛡️ PhishSense AI

### AI-Powered Email Spam Detection System

PhishSense AI is a machine learning-based email spam detection project that classifies email messages as **Spam** or **Ham (Safe)**.

The project uses **TF-IDF with N-grams** to convert email text into numerical features and **Logistic Regression** as the final classification model.

---

## 🚀 Features

- 📧 Enter any email/message text
- 🔍 Detect whether the message is **Spam** or **Ham**
- 🤖 Machine Learning powered prediction
- 🧠 TF-IDF + N-gram text feature extraction
- 📊 Logistic Regression classification
- 🌐 Interactive Streamlit web interface
- ⚡ Fast real-time prediction

---

## 🧠 Machine Learning Pipeline

```text
Email Text
    ↓
Text Cleaning
    ↓
Stopword Removal
    ↓
TF-IDF Vectorization
    ↓
N-gram Features
    ↓
Logistic Regression
    ↓
Spam / Ham Prediction
```

---

## 📊 Model

### TF-IDF + N-gram + Logistic Regression

The final model uses:

- **TF-IDF Vectorizer** — converts text into numerical feature vectors.
- **N-grams** — captures combinations of words instead of considering only individual words.
- **Logistic Regression** — performs binary classification between Spam and Ham.

The N-gram Logistic Regression model achieved approximately **99.53% accuracy** on the test dataset.

### Confusion Matrix

```text
                 Predicted
              Ham       Spam

Actual Ham    3477       13
Actual Spam     24     4317
```

This shows that the model correctly classified the vast majority of test emails.

---

## 🖥️ Streamlit Application

The project includes a simple and interactive Streamlit interface called **PhishSense AI**.

Users can paste an email or message into the input box and click **Analyze Email**.

The application then displays:

- ✅ **HAM / SAFE EMAIL**
- 🚨 **SPAM / PHISHING EMAIL**

---

## 📁 Project Structure

```text
PhishSense AI/
│
├── app.py
├── main.ipynb
├── CEAS_08.csv
├── ngram_vectorizer.pkl
├── spam_model.pkl
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit
- Joblib

---

## 📦 Installation

Clone the repository and install the required libraries:

```bash
pip install pandas numpy nltk scikit-learn matplotlib seaborn streamlit joblib
```

Download the required NLTK resources:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
```

---

## ▶️ Run the Application

Open the project folder in the terminal:

```bash
cd "PhishSense AI"
```

Then run:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🔬 Dataset

The project uses the **CEAS 2008 email dataset** for spam/ham classification.

The dataset contains email text that is used to train and evaluate the machine learning model.

---

## 🎯 Project Goal

The main goal of PhishSense AI is to demonstrate how **Natural Language Processing (NLP)** and **Machine Learning** can be combined to automatically identify potentially unwanted or malicious email messages.

---

## ⚠️ Disclaimer

PhishSense AI is an educational machine learning project. A prediction of **Ham** does not guarantee that an email is completely safe, and a **Spam** prediction does not necessarily mean that an email is malicious.

Users should always verify suspicious emails independently and avoid sharing sensitive information through untrusted messages.

---

## 👨‍💻 Author

**Rahul Mondal**

Building practical AI/ML projects while continuously learning and improving.
