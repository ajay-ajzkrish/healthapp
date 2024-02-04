import streamlit as st
import pickle as pkl
from sklearn.preprocessing import StandardScaler
import pandas as pd

heart = pkl.load(open('heart.pkl','rb'))
diabetes = pkl.load(open('diabetes.pkl','rb'))



disease = st.radio(
    "What' disease do u want to predict?",
    ["Heart Disease","Diabetes"])

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
else:
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



