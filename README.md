# 💎 GemInsight — AI-Powered Gemstone Scanner

GemInsight is an AI-powered gemstone classification application that uses deep learning and computer vision to identify gemstones from images.

## ✨ Features

- 🔍 Identify gemstones from uploaded images.
- 🤖 Predict gemstone classes using a trained deep learning model.
- 💎 Display gemstone information and details.
- 📊 Train and evaluate the classification model.
- 🖥️ Interactive application built with Streamlit.

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow
- Computer Vision and Deep Learning

## 📁 Project Structure

```text
GemInsight/
├── app.py
├── extract.py
├── predict.py
├── train.py
├── info.json
├── model/
│   └── gemstone_model.h5
├── ml_report.pdf
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/syed-shahan/GemInsight.git
cd GemInsight
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

Install the Python packages required by the application:

```bash
pip install streamlit tensorflow numpy pillow
```

Install any additional dependencies required by the source files.

### 4. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 🧠 How It Works

1. The user uploads a gemstone image.
2. The image is processed into the format expected by the trained model.
3. The deep learning model predicts the gemstone class.
4. The application displays the prediction and associated gemstone information.

## 📄 Project Report

The project report is available in `ml_report.pdf`.

## ⚠️ Disclaimer

GemInsight provides AI-generated gemstone classifications for educational and informational purposes. Its predictions should not be treated as professional gemstone authentication, origin verification, or valuation.

## 👨‍💻 Author

**Syed Shahan Hyder**

GitHub: [@syed-shahan](https://github.com/syed-shahan)
