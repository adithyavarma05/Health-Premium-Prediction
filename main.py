import streamlit as st
from make_prediction import prediction

st.title("Health Premium Form")

# -------------------------
# NUMERIC INPUTS (ROW 1)
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, step=1)

with col2:
    number_of_dependants = st.number_input(
        "Number of Dependants", min_value=0, max_value=3, step=1
    )

with col3:
    genetical_risk = st.number_input(
        "Genetical Risk (0–5)", min_value=0, max_value=5, step=1
    )


# -------------------------
# ROW 2
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Select", "Male", "Female"]
    )

with col2:
    region = st.selectbox(
        "Region",
        ["Select", "Northeast", "Northwest", "Southeast", "Southwest"]
    )

with col3:
    marital_status = st.selectbox(
        "Marital Status",
        ["Select", "Unmarried", "Married"]
    )


# -------------------------
# ROW 3
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    bmi_category = st.selectbox(
        "BMI Category",
        ["Select", "Overweight", "Underweight", "Normal", "Obesity"]
    )

with col2:
    smoking_status = st.selectbox(
        "Smoking Status",
        ["Select", "Regular", "No Smoking", "Occasional"]
    )

with col3:
    employment_status = st.selectbox(
        "Employment Status",
        ["Select", "Self-Employed", "Freelancer", "Salaried"]
    )


# -------------------------
# ROW 4
# -------------------------
col1, col2, col3 = st.columns(3)

with col1:
    # replaced the selectbox with a numeric input for income in lakhs
    income_lakhs = st.number_input(
        "Income (in Lakhs)", min_value=1, max_value=100, step=1
    )

with col2:
    medical_history = st.selectbox(
        "Medical History",
        [
            "Select",
            "High blood pressure", "No Disease",
            "Diabetes & High blood pressure", "Diabetes & Heart disease",
            "Diabetes", "Diabetes & Thyroid", "Heart disease",
            "Thyroid", "High blood pressure & Heart disease"
        ]
    )

with col3:
    insurance_plan = st.selectbox(
        "Insurance Plan",
        ["Select", "Silver", "Bronze", "Gold"]
    )


values = {
    "age": age,
    "number_of_dependants": number_of_dependants,
    "genetical_risk": genetical_risk,
    "gender": gender,
    "region": region,
    "marital_status": marital_status,
    "bmi_category": bmi_category,
    "smoking_status": smoking_status,
    "employment_status": employment_status,
    "income_lakhs": income_lakhs,
    "income_level":0,
    "medical_history": medical_history,
    "insurance_plan": insurance_plan
}
# -------------------------
# Predict
# -------------------------

if st.button("Predict"):

    # check for unselected dropdowns
    dropdown_fields = [gender, region, marital_status, bmi_category,
                       smoking_status, employment_status, medical_history, insurance_plan]

    if "Select" in dropdown_fields:
        st.warning("⚠️ Please select all the fields before predicting.")
    else:
        predict = prediction(values)
        st.success(f"Estimated Annual Price : {predict}")