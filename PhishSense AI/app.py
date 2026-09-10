import streamlit as st
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

vectorizer = joblib.load(BASE_DIR / "ngram_vectorizer.pkl")
model = joblib.load(BASE_DIR / "spam_model.pkl")

st.set_page_config(
    page_title="PhishSense AI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ PhishSense AI")
st.write("AI-Powered Email Spam Detection System")

email_text = st.text_area(
    "📧 Enter Email Text",
    height=200,
    placeholder="Paste your email here..."
)

if st.button("🔍 Analyze Email", use_container_width=True):

    if not email_text.strip():
        st.warning("Please enter an email.")

    else:
        text_vector = vectorizer.transform([email_text])
        prediction = model.predict(text_vector)[0]

        if prediction == 1:
            st.error("🚨 SPAM EMAIL DETECTED")
        else:
            st.success("✅ HAM / SAFE EMAIL")