import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('stress_model.pkl', 'rb'))

st.title("🧠 Stress Level Predictor")

working_hours = st.slider("Working Hours per Day", 1, 16)
sleep_hours = st.slider("Sleep Hours", 1, 12)
work_pressure = st.slider("Work Pressure (1-10)", 1, 10)
age = st.slider("Age", 18, 60)
mental_health_history = st.selectbox("Mental Health History", [0, 1]) 

 
gender_val = 0  
job_role_val = 0 
industry_val = 0  
years_of_experience_val = 5 
work_location_val = 0 
number_of_virtual_meetings_val = 5 
access_to_mental_health_resources_val = 0 
productivity_change_val = 1 
social_isolation_rating_val = 2 
satisfaction_with_remote_work_val = 1 
company_support_for_remote_work_val = 1 
physical_activity_val = 0 
region_val = 0 

if st.button("Predict"):
    input_dict = {
        'Age': age,
        'Gender': gender_val,
        'Job_Role': job_role_val,
        'Industry': industry_val,
        'Years_of_Experience': years_of_experience_val,
        'Work_Location': work_location_val,
        'Hours_Worked_Per_Week': working_hours,
        'Number_of_Virtual_Meetings': number_of_virtual_meetings_val,
        'Work_Life_Balance_Rating': work_pressure,
        'Mental_Health_Condition': mental_health_history,
        'Access_to_Mental_Health_Resources': access_to_mental_health_resources_val,
        'Productivity_Change': productivity_change_val,
        'Social_Isolation_Rating': social_isolation_rating_val,
        'Satisfaction_with_Remote_Work': satisfaction_with_remote_work_val,
        'Company_Support_for_Remote_Work': company_support_for_remote_work_val,
        'Physical_Activity': physical_activity_val,
        'Sleep_Quality': sleep_hours,
        'Region': region_val
    }

    input_data = pd.DataFrame([input_dict])
    prediction = model.predict(input_data)

    if prediction == 0:
        st.success("Low Stress 😊")
    elif prediction == 1:
        st.warning("Medium Stress 😐")
    else:
        st.error("High Stress 😰")
