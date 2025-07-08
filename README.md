
# 🧠 Stroke Risk Prediction App

   The primary objective of this project is to develop a predictive model that can accurately determine the presence of **heart disease** in patients based on a set of medical attributes. This model aims to assist in early diagnosis and potential intervention, improving patient outcomes and healthcare efficiency.

   The project involves analyzing the Heart Disease dataset from the**UCI Machine Learning Repository using Python and Jupyter Notebook**. The analysis will leverage libraries such as numpy and pandas for data manipulation, and sklearn.model_selection for splitting the dataset into training and test sets. Logistic Regression will be used to build a predictive model to determine the presence of heart disease based on various medical attributes.

   A **Streamlit-powered web application** that predicts the risk of stroke using machine learning. Users can input key medical parameters and receive real-time stroke risk assessments along with a downloadable PDF health report.

## 🚀 Features

- 🔍 **Stroke Risk Prediction** using a trained ML model (Logistic Regression)
- 📊 **Interactive Streamlit UI** for user input
- 📄 **Downloadable PDF Health Report**
- ℹ️ **Informative Tabs** for app usage and dataset understanding
- 💡 Built for awareness and early risk screening

## 🧬 Input Features

The app uses the following health indicators:
- Age
- Gender
- Hypertension
- Heart Disease
- Marital Status
- Work Type
- Residence Type
- Average Glucose Level
- BMI
- Smoking Status

## 🗂 Dataset

This app uses the [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset) from Kaggle. It contains health records of individuals along with a binary target indicating the occurrence of stroke.

## 🛠 Tech Stack

- **Python**
- **Pandas**, **NumPy**
- **Scikit-learn** – for training the ML model
- **Streamlit** – for the web app UI
- **FPDF** – for generating PDF reports

---

## 🖥 How to Run Locally

### 1. Clone the repository:
   ```bash
   git clone https://github.com/KadariGSVMohan/stroke-risk-prediction.git
   cd stroke-risk-prediction
````
### 2. Install dependencies:
   ```bash
   pip install -r requirements.txt
````
### 3. Run the Streamlit app:
   ```bash
   streamlit run app.py
````

## 📄 Folder Structure

```
stroke-risk-prediction/
│
├── app.py                  # Streamlit UI code
├── stroke_data.csv         # Dataset file
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## 🛑 Disclaimer

> ⚠️ This tool is built for **educational and awareness purposes** only. It is **not a substitute for professional medical advice**. Always consult a certified healthcare provider for diagnosis or treatment.


