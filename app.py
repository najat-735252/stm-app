
import streamlit as st
import pandas as pd
from dummies import *
import joblib


scaler = joblib.load('scaler.h5')
model = joblib.load('model.h5')

st.title('Diabetes Prediction')
st.info('Just predict if the patient has dibetes or not')



gender_sel = st.radio('Gender', ['Male', 'Female'])
gender=gender_dummies[gender_sel]
age = st.slider('Age', min_value=1, max_value=120, value=30, step=1)
hypertension = st.selectbox('Hypertension', [1, 0])
heart_disease = st.selectbox('Heart Disease', [1, 0])
smoking_history_sel= st.selectbox('Smoking History', ['current','ever','former','never','not current','No info'])
smoking_history=smoking_history_dummies[smoking_history_sel]
bmi = st.number_input('BMI (Body Mass Index)')
HbA1c_level = st.number_input('HbA1c Level')
blood_glucose_level = st.number_input('Blood Glucose Level')
st.write('If HbA1c level < 5.7: Initial Diagnosis: Normal')
st.write('If 5.7 <= HbA1c level <= 6.4: Initial Diagnosis: Prediabetes')
st.write('If HbA1c level >= 6.5: Initial Diagnosis: Diabetes')


initial_diagnosis_sel = st.selectbox('Initial Diagnosis',['normal','diabetes','prediabetes'])
initial_diagnosis=initial_diagnosis_dummies[initial_diagnosis_sel]
st.write('If BMI <= 18.5: Weight Type: Underweight')
st.write('If 18.5 < BMI <= 24.9: Weight Type: Normal')
st.write('If 24.9 < BMI <= 29.9: Weight Type: Overweight')
st.write('If BMI > 29.9: Weight Type: Obesity')

weight_type_sel= st.selectbox('Weight Type',['obesity','overweight','underweight','normal'] )
weight_type=weight_type_dummies[weight_type_sel]

st.write('blood_glucose_level	Category')
st.write ('=< 99	normal')
st.write ('100 – 125	Prediabetes')
st.write('>= 126	Diabetes')
sugar_test_sel= st.selectbox('Sugar Test', ['normal','prediabetes','diabetes'])
sugar_test=sugar_test_dummies[sugar_test_sel]

data=[age,bmi,blood_glucose_level,HbA1c_level]
data_scaled=scaler.transform([data])
data2=[gender,hypertension,heart_disease]
data1 = data_scaled.tolist()[0] + initial_diagnosis+data2+smoking_history+weight_type+sugar_test

data1=data1[:-4]



prediction = model.predict([data1])
if prediction == 0:
    st.write('The patient is predicted to be non-diabetic.')
elif prediction == 1:
    st.write('The patient is predicted to have diabetes.')

