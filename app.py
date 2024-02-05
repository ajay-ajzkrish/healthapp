import streamlit as st
import pickle as pkl
from sklearn.preprocessing import StandardScaler
import pandas as pd

heart = pkl.load(open('heart.pkl','rb'))
diabetes = pkl.load(open('diabetes.pkl','rb'))
mental = pkl.load(open('mental_health.pkl','rb'))

st.title("Health App")
st.warning('"This project aims to demonstrate and enhance my data science skills. For precise results, consider consulting a professional, as the dataset used is relatively small."')
disease = st.radio(
    "Choose the disease do u want to predict?",
    ["Heart Disease","Diabetes","Mental Health"])

if disease == 'Heart Disease':
    st.text("Example input of person with heart disease : 124,163,62,209,2,0")
    st.text("Example input of person without heart disease : 160,145,55,289,3,1")
    st.write('Enter your HEART diagonostics results here.')
    trestbps = st.number_input('Enter resting blood pressure')
    thalach = st.number_input('Enter maximum heart rate achieved')
    age = st.number_input('Enter age')
    chol = st.number_input('Enter serum cholestoral in mg/dl')
    thal = st.number_input('0 = normal; 1 = fixed defect; 2 = reversable defect')
    sex = st.number_input('Enter 1 for male 0 for female')

    if st.button("Predict Heart Disease"):
        pred = heart.predict([[trestbps,thalach,age,chol,thal,sex]])
        if pred == 0:
            st.write("You are at a lower risk of developing heart disease.")
        else:
            st.warning("Consult a Doactor immediately")
# trestbps-resting blood pressure
# thalach-maximum heart rate achieved
# age
# chol-serum cholestoral in mg/dl
elif disease == "Diabetes":
    st.text("Example input of person with Diabetes disease :6,148,72,35,32,33.6,0.627,50")
    st.text("Example input of person without Diabetes disease : 1,85,66,29,32.45,26.6,0.351,31")

    st.write('Enter your DIABETES diagonostics results here.')
    Pregnancies = st.number_input('Enter Number of times pregnant')
    Glucose = st.number_input('Enter Plasma glucose concentration a 2 hours in an oral glucose tolerance test')
    BloodPressure = st.number_input('Enter Diastolic blood pressure (mm Hg)')
    SkinThickness = st.number_input('Enter Triceps skin fold thickness (mm)')
    Insulin = st.number_input('Enter 2-Hour serum insulin (mu U/ml)')
    BMI = st.number_input('Body mass index (weight in kg/(height in m)^2)')
    DiabetesPedigreeFunction = st.number_input(' Diabetes pedigree function')
    Age = st.number_input('Enter Age')

    if st.button("Predict Diabetes"):
        data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        pred = diabetes.predict([data])
        if pred == 0:
            st.write("You are at a lower risk of developing diabetes disease.")
        else:
            st.warning("Consult a Doactor immediately, you have a higher risk of Diabetes")
# Pregnancies: Number of times pregnant
# Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# BloodPressure: Diastolic blood pressure (mm Hg)
# SkinThickness: Triceps skin fold thickness (mm)
# Insulin: 2-Hour serum insulin (mu U/ml)
# BMI: Body mass index (weight in kg/(height in m)^2)
# DiabetesPedigreeFunction: Diabetes pedigree function
# Age: Age (years)
# Outcome: Class variable (0 or 1)



elif disease == "Mental Health":
    st.write('Please answer the following questions')
# ['Age', 'Gender', 'family_history', 'benefits', 'care_options', 'anonymity', 'leave', 'work_interfere']
    Age = st.number_input('Please enter your age',step=1)

    Gender = st.selectbox('Select your gender',('Male', 'Female', 'Others'))
    gender_mapping = {'Male': 0, 'Female': 1, 'Others': 2}
    gender_value = gender_mapping[Gender]  # Use this for 'Male', 'Female', 'Others'
    # st.write(gender_value)


    family_history = st.selectbox('Do you have a family history of mental illness?' , ('Yes','No'))
    family_history_mapping = {'No': 0, 'Yes': 1}
    family_history_value = family_history_mapping[family_history]  # Use this for 'Male', 'Female', 'Others'
    # st.write(family_history_value)


    benefits = st.selectbox('Does your employer provide mental health benefits?',('Yes','No','Do not Know'))
    benefits_mapping = {'Do not Know':0, 'No': 1, 'Yes': 2}
    benefits_value = benefits_mapping[benefits]  # Use this for 'Male', 'Female', 'Others'
    # st.write(benefits_value)

    care_options = st.selectbox('Do you know the options for mental health care your employer provides?',('Yes','No','Not Sure'))
    care_options_mapping = {'Not Sure':1, 'No': 0, 'Yes': 2}
    care_options_value = care_options_mapping[care_options]  # Use this for 'Male', 'Female', 'Others'
    # st.write(care_options_value)

    anonymity = st.selectbox('Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources?',('Yes','No','Do not Know'))
    anonymity_mapping = {'Do not Know':0, 'No': 1, 'Yes': 2}
    anonymity_value = anonymity_mapping[anonymity]  # Use this for 'Male', 'Female', 'Others'
    # st.write(anonymity_value)

    leave = st.selectbox('How easy is it for you to take medical leave for a mental health condition?',('Very easy','Somewhat easy', "Don't know", 'Somewhat difficult','Very difficult'))
    leave_mapping = {'Somewhat easy':2, "Don't know":0, 'Somewhat difficult':1,'Very difficult':3, 'Very easy':4}
    leave_value = leave_mapping[leave]  # Use this for 'Male', 'Female', 'Others'
    # st.write(leave_value)

    work_interfere = st.selectbox('If you have a mental health condition, do you feel that it interferes with your work?',('Often', 'Rarely', 'Sometimes','Never'))
    work_interfere_mapping = {'Often':2, 'Rarely':3, 'Never':1, 'Sometimes':5}
    work_interfere_value = work_interfere_mapping[work_interfere]  # Use this for 'Male', 'Female', 'Others'
    # st.write(work_interfere_value)
    

    if st.button("Predict Mental health Status"):
        data = [Age,gender_value,family_history_value,benefits_value,care_options_value,anonymity_value,leave_value,work_interfere_value]
        pred = mental.predict([data])
        if pred == 0:
            st.write("Your mental health seems to be alright.")
        else:
            st.warning("You might consider seeking professional advice!")

st.write('*******************************************')

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("Heart Disease Dataset", "https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset")

with col2:
    st.link_button("Diabetes Dataset", "https://www.kaggle.com/datasets/mathchi/diabetes-data-set")

with col3:
    st.link_button("Mental Health Dataset", "https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey/data")
