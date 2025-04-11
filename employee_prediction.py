import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

# Load model
employee_prediction_model = pickle.load(open("C:/Users/Ramu M/employee_prediction.pkl", "rb"))

# Sidebar with avatar
with st.sidebar:
    import streamlit as st

# Display the image
    st.image(r"C:\Users\Ramu M\Downloads\employee-attrition.webp", width=300,caption="📊 Employee Attrition Analysis")


    selected = option_menu(
        'Employee Attrition Analysis and Prediction',
        ['👩‍💼Employee Attrition Analysis']
    )

# Main Title and Avatar at the top
st.image("C:/Users/Ramu M/Downloads/e83a29_a1665cd45b734150996fa4d40fddea42~mv2.png", width=500)


st.title(":red[Employee Attrition Analysis using ML]")
st.markdown("Fill out the form below.")


# ✅ Start form block
with st.form("📋attrition_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("🎂Age")
        business_travel = st.text_input("✈️Business Travel")
        daily_rate = st.text_input("💵Daily Rate")
        department = st.text_input("🏢Department")
        distance = st.text_input("🏠➡️🏢Distance From Home")
        education = st.text_input("🎓Education Level")

    with col2:
        education_field = st.text_input("📘Education Field")
        employee_count = st.text_input("Employee_count")
        employee_number = st.text_input("🆔Employee Number")
        relationship = st.text_input("💞Relationship Satisfaction")
        standard_hours = st.text_input("Standard_hours")
        stock_option = st.text_input("📈Stock Option Level")
        work_life_balance = st.text_input("⚖️Work Life Balance")

    with col3:
        total_work_years = st.text_input("🛠️ Total Working Years")
        training_times = st.text_input("📚Training Times Last Year")
        years_at_company = st.text_input("🏢Years at Company")
        years_in_role = st.text_input("👩‍💼Years in Current Role")
        years_since_promotion = st.text_input("🚀Years Since Last Promotion")
        years_with_manager = st.text_input("👔Years with Current Manager")

    # ✅ Must be inside the `st.form` block
    submitted = st.form_submit_button("🎯Predict Attrition")

# ✅ Logic after form submission
if submitted:
    user_input = pd.DataFrame({
        'Age': [age],
        'BusinessTravel': [business_travel],
        'DailyRate': [daily_rate],
        'Department': [department],
        'DistanceFromHome': [distance],
        'Education': [education],
        'EducationField': [education_field],
        'EmployeeCount': [employee_count],
        'EmployeeNumber': [employee_number],
        'RelationshipSatisfaction': [relationship],
        'StandardHours': [standard_hours],
        'StockOptionLevel': [stock_option],
        'WorkLifeBalance': [work_life_balance],
        'TotalWorkingYears': [total_work_years],
        'TrainingTimesLastYear': [training_times],
        'YearsAtCompany': [years_at_company],
        'YearsInCurrentRole': [years_in_role],
        'YearsSinceLastPromotion': [years_since_promotion],
        'YearsWithCurrManager': [years_with_manager]
    })

    # Convert types and prepare data
    for col in user_input.columns:
        try:
            user_input[col] = pd.to_numeric(user_input[col])
        except ValueError:
            user_input[col] = user_input[col].astype('category').cat.codes

    user_input = user_input.apply(lambda col: col.astype('category').cat.codes if col.dtypes == 'object' else col)
    user_input = user_input[employee_prediction_model.feature_names_in_]

    # Prediction
    prediction = employee_prediction_model.predict(user_input)

    st.markdown("---")
    st.subheader("🔍 Prediction Outcome")

    with st.container():
        if prediction[0] == 1:
            st.error("🚨 *This employee is likely to leave the company!*", icon="⚠️")
            st.info("""
            **Suggested Actions:**
            - 💬 Initiate a feedback discussion
            - 🧘 Evaluate work-life balance
            - 📈 Provide career growth opportunities
            """)
        else:
            st.success("🎉 *This employee is likely to stay in the company!*", icon="✅")
            st.info("""
            **Recommended:**
            - 🎯 Recognize consistent performance
            - 🌱 Keep offering learning and development
            - 🙌 Continue building strong team culture
            """)
