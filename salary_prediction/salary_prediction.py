import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.set_page_config(
    page_title="Salary Prediction App",
    layout="centered"
)

st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #145a86;
            color: white;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

model = joblib.load("model.pkl")

st.title("💼 Employee Monthly Salary Prediction")
st.markdown("Enter employee details below to estimate monthly salary.")
st.divider()

st.write("Enter employee details below:")

col1, col2 = st.columns(2)

with col1:
    Age = st.number_input("Age", min_value=18, max_value=60, value=30)
    YearsExperience = st.number_input("YearsExperience", min_value=0, max_value=40, value=5)
    YearsAtCompany = st.number_input("YearsAtCompany", min_value=0, max_value=40, value=3)
    PerformanceRating = st.selectbox("PerformanceRating", [1, 2, 3, 4])

with col2:
    MonthlyHoursWorked = st.number_input("MonthlyHoursWorked", min_value=80, max_value=300, value=160)
    Department = st.selectbox("Department", ["Finance", "HR", "Operations", "Marketing", "Sales"])
    EducationLevel = st.selectbox("EducationLevel", ["SSCE", "Bachelors", "Masters", "PhD"])

user_input_dict = {
    "Age": Age,
    "YearsExperience": YearsExperience,
    "YearsAtCompany": YearsAtCompany,
    "PerformanceRating": PerformanceRating,
    "MonthlyHoursWorked": MonthlyHoursWorked,
    "Department":  Department,
    "EducationLevel": EducationLevel
}
    
input_data = pd.DataFrame([user_input_dict])
input_data = pd.get_dummies(input_data)
input_data = input_data.reindex(columns=feature_columns, fill_value=0)
if st.button("predict salary"):
    prediction = model.predict(input_data)[0]
    predicted_salary = max(0, float(prediction))
    st.success(f"Predicted Monthly Salary: ₦{predicted_salary:,.2f}")   
st.divider()
st.caption("Built by Oluwatosin | Machine Learning Salary Prediction Project")
   
   