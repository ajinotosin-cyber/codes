import streamlit as st
import pandas as pd
import joblib

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
    Department = st.selectbox("Department", ["Finance", "HR", "IT", "Marketing", "Sales"])
    EducationLevel = st.selectbox("EducationLevel", ["SSCE", "Bachelors", "Masters", "PhD"])

if st.button("Predict Salary"):

   input_data = pd.DataFrame ({
       "Age": [Age],
       "YearsExperience": [YearsExperience],
       "YearsAtCompany": [YearsAtCompany],
       "PerformanceRating": [PerformanceRating],
       "MonthlyHoursWorked": [MonthlyHoursWorked],
       
       "Department_Finance": [0],
       "Department_HR": [0],
       "Department_Marketing": [0],
       "Department_Operations": [0],
       "Department_Sales": [0],
       
       "EducationLevel_Masters": [0],
       "EducationLevel_PhD": [0],
       "EducationLevel_SSCE": [0],
   })
   
   input_data[f"Department_{Department}"] = 1
       
   if EducationLevel != "Bachelors":
           input_data[f"EducationLevel_{EducationLevel}"] = 1
   
   prediction = model.predict(input_data)

   st.success(f"Predicted Monthly Salary: ₦{float(prediction[0]):,.2f}")
    
   st.divider()
   st.caption("Built by Oluwatosin | Machine Learning Salary Prediction Project")