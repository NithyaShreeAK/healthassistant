# 🩺 Multi-Disease Prediction System

A unified machine learning-based tool for the **early prediction of chronic diseases** — **Diabetes**, **Heart Disease**, **Parkinson’s Disease**, and **Autism Spectrum Disorder (ASD)** — using patient medical data.

---

## 🔍 Project Overview

Chronic illnesses like Diabetes, Heart Disease, Parkinson's, and ASD impact millions globally. Early detection is crucial, yet many symptoms are subtle in the initial stages and often go undiagnosed. This project aims to streamline preliminary screening by offering a **single platform that predicts the likelihood of multiple diseases** from user input using trained ML models.

---

## 🚀 Features

- 🔹 Predicts 4 diseases using individual ML models
- 🔹 Integrated UI for user-friendly medical input
- 🔹 Instant predictions based on trained models
- 🔹 Reduces manual diagnostic errors
- 🔹 Useful for remote healthcare, general clinics, and health apps

---

## 🏥 Diseases Covered

- ✅ **Diabetes**
- ✅ **Heart Disease**
- ✅ **Parkinson’s Disease**
- ✅ **Autism Spectrum Disorder (ASD)**

---

## 🧠 Technologies Used

- **Python**
- **Scikit-learn**
- **Pandas**
- **Streamlit** (for UI)

---

## 🛠️ Project Structure

multi-disease-predictor/
├── diabetes_model/
├── heart_model/
├── parkinson_model/
├── asd_model/
├── utils/
│ └── preprocessing.py
├── app.py
├── requirements.txt
└── README.md


---

## 🔄 Workflow

User Input → Feature Preprocessing → Disease-specific ML Models → Predictions


---

## 📦 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/multi-disease-predictor.git
cd multi-disease-predictor


Create a virtual environment:
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux

Install the required packages:
pip install -r requirements.txt

Run the Streamlit app:
streamlit run app.py

Datasets Used
Public datasets relevant to each disease were used and preprocessed to train the ML models.

Data sources include:

Kaggle

UCI Machine Learning Repository

Other open medical data platforms


 Use Cases
🏥 General clinics for rapid screening

🌐 Telemedicine and remote diagnostics

👨‍⚕️ Family physicians needing multi-disease checks

📱 Health & wellness applications

🙌 Contributions
Pull requests are welcome!
Please fork the repository, make your changes, and open a PR with a clear description.

📃 License
This project is licensed under the MIT License.






