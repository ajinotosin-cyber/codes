import streamlit as st
import pandas as pd
import joblib
model = joblib.load("model.pkl")
feature_columns = joblib.load("feature_columns.pkl")
st.title("Employee Salary Prediction App")
age = st.number_input("Age", min_value=18, max_value=65, value=25)
experience = st.number_input("Years of Experience", min_value=0, max_value=40, value=1)

department = st.selectbox(
    "Department",
    ["HR", "IT", "Sales", "Marketing", "Finance"]
)

education = st.selectbox(
    "Education Level",
    ["Bachelors", "Masters", "PhD"]
)

if st.button("Predict Salary"):

    input_data = {
        "Age": age,
        "YearsExperience": experience,
        "Department": department,
        "EducationLevel": education
    }

    input_df = pd.DataFrame([input_data])
    input_df = pd.get_dummies(input_df)
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    prediction = model.predict(input_df)

    st.success(f"Predicted Salary: ₦{prediction[0]:,.2f}")