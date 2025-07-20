# 🚗 Car Damage Detection using Deep Learning

A web application built with **Streamlit** that detects damage in car images using a fine-tuned **ResNet50** convolutional neural network.

![App_Screenshot](App_Screenshot%20.jpg.png)

---
## 🔗 Live Demo

Check out the live app here:  
👉 [Vehicle Damage Detection Streamlit App](https://vehicle-damage-detection-7dg6sazf2s5a4e7lyirg43.streamlit.app/)


## 🔍 Project Overview

This project uses a **deep learning model (ResNet50)** trained on car images to classify whether a car is **damaged or not**. The app allows users to upload a car photo and receive real-time damage detection results with visual feedback.

---

## 📦 Features

- ✅ Upload car images in JPG/PNG format
- 🧠 Uses pretrained ResNet50 model fine-tuned for Multi-Class Image Classification Model
1). Front-Damaged
2). Rear-Damaged
3). Crushed
4). Broken
5). Normal

- 📈 Real-time prediction with clear result display
- 🌐 Lightweight web interface using Streamlit

---

📊 Model Performance
The vehicle damage detection model was evaluated on a test dataset of 575 images. Below are the key performance metrics:

Overall Accuracy: 81%

Macro Average F1-Score: 0.79

Weighted Average F1-Score: 0.81

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: PyTorch, torchvision
- **Model**: ResNet50 (Pretrained on ImageNet, fine-tuned on car damage dataset)
- **Utilities**: PIL, NumPy

---

## 🚀 Getting Started

### 🔧 Requirements

Make sure you have Python 3.11.9

### 📥 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/car-damage-detection.git
   cd car-damage-detection
   

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt




3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py


