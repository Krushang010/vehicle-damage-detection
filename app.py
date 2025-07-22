import streamlit as st
from model_helper import predict
from PIL import Image
import base64

# ----- Page Config -----
st.set_page_config(page_title="Car Damage Detector", page_icon="🚗", layout="centered")

# ----- Custom CSS Styling -----
def add_custom_background():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Roboto', sans-serif;
            background-color: #0f1117;
            color: #FAFAFA;
        }

        .title {
            text-align: center;
            font-size: 2.6rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }

        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            margin-bottom: 2rem;
            color: #B0B0B0;
        }

        .stButton > button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: bold;
        }

        .stFileUploader {
            border: 2px dashed #666;
            border-radius: 10px;
            padding: 1rem;
        }

        .stImage {
            border-radius: 10px;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        .result {
            font-size: 1.4rem;
            font-weight: 600;
            color: #00FFAA;
            text-align: center;
            margin-top: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

add_custom_background()

# ----- App UI -----
st.markdown('<div class="title">🚘 Car Damage Detection App</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Upload a car image and let AI detect whether it is <strong>Front or Rear</strong>, and if it is <strong>Crushed / Broken / Normal</strong>.</div>',
    unsafe_allow_html=True
)

# ----- Upload -----
uploaded_file = st.file_uploader("📂 Upload your car image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="📸 Uploaded Image")


        # Save to a temporary path for prediction
        image_path = "temp_image.jpg"
        image.save(image_path)

        with st.spinner("🧠 Analyzing damage... please wait"):
            prediction = predict(image_path)

        st.markdown(f'<div class="result">🧾 Prediction: <span style="color:#FFD700;">{prediction}</span></div>', unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error processing image: {e}")
