# import streamlit as st
# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from fpdf import FPDF
# from io import BytesIO

# # Load and train model
# df = pd.read_csv("heart_disease_data.csv")
# X = df.drop(columns="target", axis=1)
# Y = df["target"]
# X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)
# model = LogisticRegression()
# model.fit(X_train, y_train)

# # Streamlit UI
# st.set_page_config(page_title="Heart Disease App", layout="centered")
# tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "ℹ️ Info", "🧪 Prediction", "📄 Health Report"])

# patient_data = {}
# prediction_result = None

# # Home
# with tab1:
#     st.title("❤️ Heart Disease Prediction App")
#     st.markdown("""
# Welcome to the **Heart Disease Prediction App**, built using **Streamlit** and a **Logistic Regression model**.

# This tool allows users to:
# - Predict the risk of heart disease
# - Understand key medical parameters
# - Download a health report

# > ⚠️ This tool is for demonstration purposes only. Please consult a doctor for medical advice.
# """)

# # Info
# with tab2:
#     st.title("ℹ️ Dataset Information")
#     st.markdown("""
# **Dataset**: UCI Heart Disease Dataset  
# **Records**: 303 patients  
# **Target Variable**: Heart Disease  

# **Used Features**:
# - Age  
# - Sex (1 = Male, 0 = Female)  
# - Chest Pain Type (0–3)  
# - Resting Blood Pressure  
# - Cholesterol  
# - Fasting Blood Sugar > 120 mg/dl  
# - Resting ECG  
# - Max Heart Rate  
# - Exercise-induced Angina  
# - ST Depression (Oldpeak)  
# - Slope of ST Segment  
# - No. of Major Vessels  
# - Thalassemia  
# - Target: 0 (Healthy), 1 (Heart Disease)
# """)

# # Prediction
# with tab3:
#     st.header("🧪 Heart Disease Risk Prediction")

#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.number_input("Age", 1, 120, 45)
#         sex = st.selectbox("Sex", [(1, "Male"), (0, "Female")], format_func=lambda x: x[1])[0]
#         cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
#         trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
#         chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
#         fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
#     with col2:
#         restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
#         thalach = st.number_input("Max Heart Rate Achieved", 60, 250, 150)
#         exang = st.selectbox("Exercise-induced Angina", [0, 1])
#         oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 10.0, 1.0)
#         slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
#         ca = st.selectbox("No. of Major Vessels Colored", [0, 1, 2, 3])
#         thal = st.selectbox("Thalassemia Type", [0, 1, 2, 3])

#     if st.button("🔍 Predict"):
#         input_array = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
#                                 thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
#         prediction_result = model.predict(input_array)[0]

#         patient_data = {
#             "Age": age,
#             "Sex": "Male" if sex == 1 else "Female",
#             "Chest Pain Type": cp,
#             "Resting BP": trestbps,
#             "Cholesterol": chol,
#             "Fasting Blood Sugar": "Yes" if fbs == 1 else "No",
#             "ECG Result": restecg,
#             "Max Heart Rate": thalach,
#             "Exercise Angina": "Yes" if exang == 1 else "No",
#             "Oldpeak": oldpeak,
#             "Slope": slope,
#             "CA": ca,
#             "Thal": thal,
#             "Prediction": prediction_result
#         }

#         st.success("Prediction completed! Go to the '📄 Health Report' tab to view and download your report.")

# # Report
# with tab4:
#     st.title("📄 Patient Health Report")

#     if not patient_data:
#         st.info("Please generate a prediction first in the 'Prediction' tab.")
#     else:
#         st.subheader("🧍 Patient Details")
#         for key, value in patient_data.items():
#             if key != "Prediction":
#                 st.markdown(f"**{key}**: {value}")

#         st.subheader("🔬 Prediction Result")
#         if patient_data["Prediction"] == 0:
#             st.success("The patient is unlikely to have heart disease.")
#             advice = "Maintain a healthy lifestyle. Eat well, exercise, and get regular checkups."
#         else:
#             st.error("The patient may have heart disease.")
#             advice = "Consult a cardiologist for further diagnosis and tests immediately."

#         st.subheader("📌 Health Advisory")
#         st.write(advice)

#         # Generate text report
#         report_text = f"""
# PATIENT HEALTH REPORT

# Age: {patient_data['Age']}
# Sex: {patient_data['Sex']}
# Chest Pain Type: {patient_data['Chest Pain Type']}
# Resting Blood Pressure: {patient_data['Resting BP']} mm Hg
# Cholesterol: {patient_data['Cholesterol']} mg/dl
# Fasting Blood Sugar > 120: {patient_data['Fasting Blood Sugar']}
# ECG Result: {patient_data['ECG Result']}
# Max Heart Rate: {patient_data['Max Heart Rate']} bpm
# Exercise-induced Angina: {patient_data['Exercise Angina']}
# ST Depression (Oldpeak): {patient_data['Oldpeak']}
# Slope of ST Segment: {patient_data['Slope']}
# Number of Major Vessels (ca): {patient_data['CA']}
# Thalassemia Type: {patient_data['Thal']}

# PREDICTION RESULT:
# {'No Heart Disease Likely' if patient_data['Prediction'] == 0 else 'Possible Heart Disease'}

# HEALTH ADVICE:
# {advice}

# Generated by Heart Risk App
# """

#         # TXT download
#         st.download_button(
#             label="⬇️ Download Report (.txt)",
#             data=report_text.encode("utf-8"),
#             file_name="Heart_Health_Report.txt",
#             mime="text/plain"
#         )

#         # PDF generation
#         def create_pdf(data):
#             pdf = FPDF()
#             pdf.add_page()
#             pdf.set_font("Arial", size=12)
#             pdf.set_title("Heart Health Report")

#             pdf.set_font("Arial", style='B', size=14)
#             pdf.cell(0, 10, "Patient Health Report", ln=True, align='C')
#             pdf.ln(10)

#             pdf.set_font("Arial", size=12)
#             for key, value in data.items():
#                 if key != "Prediction":
#                     pdf.cell(0, 10, f"{key}: {value}", ln=True)

#             pdf.ln(5)
#             result_text = "No Heart Disease Likely" if data["Prediction"] == 0 else "Possible Heart Disease"
#             pdf.cell(0, 10, f"Prediction Result: {result_text}", ln=True)
#             pdf.multi_cell(0, 10, f"\nHealth Advice:\n{advice}")
#             pdf.ln(5)
#             pdf.cell(0, 10, "Generated by Heart Risk App", ln=True, align='C')

#             # Use dest='S' to return string, then encode and wrap in BytesIO
#             pdf_bytes = pdf.output(dest='S').encode('latin-1')
#             return BytesIO(pdf_bytes)

#         pdf_file = create_pdf(patient_data)

#         st.download_button(
#             label="⬇️ Download Report (.pdf)",
#             data=pdf_file,
#             file_name="Heart_Health_Report.pdf",
#             mime="application/pdf"
#         )




import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from fpdf import FPDF
from io import BytesIO

# Load dataset and train model
df = pd.read_csv("heart_disease_data.csv")
X = df.drop(columns="target", axis=1)
Y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Streamlit config
st.set_page_config(page_title="Heart Disease App", layout="centered")
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "ℹ️ Info", "🧠 Prediction", "📄 Health Report"])

patient_data = {}
prediction_result = None

# HOME TAB
tab1.markdown("""
# 🫀 Heart Disease Prediction App

Welcome to the **Heart Disease Prediction App**, built using **Streamlit** and a **Logistic Regression model**.

This app is designed to help individuals and healthcare professionals assess the likelihood of heart disease based on 13 medical parameters. Enter the values and get a prediction instantly.

### 🌟 Key Features:
- Simple & interactive prediction form
- Machine learning powered risk analysis
- Auto-generated personalized PDF report
- Detailed dataset info and health guidance

### 💡 Purpose:
Heart disease is the leading cause of death globally. Early prediction and preventive action can save lives. This tool empowers users with instant analysis and awareness.

👉 Head to the **Prediction** tab to get started.

> ⚠️ **Disclaimer**: This tool is for educational and awareness purposes only. It does not replace professional medical advice.
""")

# INFO TAB
tab2.title("📊 Dataset Information")
tab2.markdown("""
The model uses the **UCI Heart Disease Dataset**.

- **Total Records**: 303 patients
- **Target Variable**: `target` (1 = Heart Disease, 0 = Healthy)

### 📌 Features Used:
1. Age
2. Sex (1 = Male, 0 = Female)
3. Chest Pain Type (0–3)
4. Resting Blood Pressure (mm Hg)
5. Cholesterol (mg/dl)
6. Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)
7. Resting ECG Results (0, 1, 2)
8. Max Heart Rate Achieved
9. Exercise-induced Angina (1 = Yes, 0 = No)
10. ST Depression (Oldpeak)
11. Slope of Peak ST Segment
12. Number of Major Vessels (0–3)
13. Thalassemia (0–3)
""")

# PREDICTION TAB
tab3.header("🧠 Heart Disease Risk Prediction")

col1, col2 = tab3.columns(2)
with col1:
    age = st.number_input("Age", 1, 120, 45)
    sex = st.selectbox("Sex", [(1, "Male"), (0, "Female")], format_func=lambda x: x[1])[0]
    cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])

with col2:
    restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", 60, 250, 150)
    exang = st.selectbox("Exercise-induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 10.0, 1.0)
    slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
    ca = st.selectbox("No. of Major Vessels Colored", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia Type", [0, 1, 2, 3])

if tab3.button("🔍 Predict"):
    input_array = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
    prediction_result = model.predict(input_array)[0]

    patient_data = {
        "Age": age,
        "Sex": "Male" if sex == 1 else "Female",
        "Chest Pain Type": cp,
        "Resting BP": trestbps,
        "Cholesterol": chol,
        "Fasting Blood Sugar": "Yes" if fbs == 1 else "No",
        "ECG Result": restecg,
        "Max Heart Rate": thalach,
        "Exercise Angina": "Yes" if exang == 1 else "No",
        "Oldpeak": oldpeak,
        "Slope": slope,
        "CA": ca,
        "Thal": thal,
        "Prediction": prediction_result
    }

    st.success("✅ Prediction completed! Check the Health Report tab.")

# REPORT TAB
tab4.title("📄 Patient Health Report")

if not patient_data:
    tab4.info("ℹ️ Please generate a prediction first from the Prediction tab.")
else:
    tab4.subheader("👤 Patient Details")
    for key, value in patient_data.items():
        if key != "Prediction":
            tab4.markdown(f"**{key}**: {value}")

    tab4.subheader("🩺 Prediction Result")
    if patient_data["Prediction"] == 0:
        tab4.success("The patient is unlikely to have heart disease.")
        advice = "Maintain a healthy lifestyle. Eat well, exercise, and get regular checkups."
    else:
        tab4.error("The patient may have heart disease.")
        advice = "Consult a cardiologist for further diagnosis and tests immediately."

    tab4.subheader("💡 Health Advisory")
    tab4.write(advice)

    def create_pdf(data):
        def clean_text(text):
            return ''.join(char for char in str(text) if 0 <= ord(char) <= 255)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, clean_text("Patient Health Report"), ln=True, align='C')
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, clean_text("Generated by Heart Risk App"), ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, clean_text("1. Patient Details"), ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

        pdf.set_font("Arial", '', 12)
        for key, value in data.items():
            if key != "Prediction":
                pdf.cell(60, 10, clean_text(f"{key}:"), border=0)
                pdf.cell(0, 10, clean_text(f"{value}"), ln=True)

        pdf.ln(5)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, clean_text("2. Prediction Result"), ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

        result_text = "No Heart Disease Likely" if data["Prediction"] == 0 else "Possible Heart Disease"
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, clean_text(f"Prediction result based on the input data is: {result_text}."))

        pdf.ln(5)
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, clean_text("3. Health Advice"), ln=True)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)

        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, clean_text(advice))

        pdf.ln(10)
        pdf.set_font("Arial", 'I', 10)
        pdf.cell(0, 10, clean_text("Note: This is a predictive tool. For clinical diagnosis, consult a healthcare provider."), ln=True, align='C')

        pdf_bytes = pdf.output(dest='S').encode('latin-1', errors='ignore')
        return BytesIO(pdf_bytes)

    pdf_file = create_pdf(patient_data)

    tab4.download_button(
        label="📥 Download Report (.pdf)",
        data=pdf_file,
        file_name="Heart_Health_Report.pdf",
        mime="application/pdf"
    )
