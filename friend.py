# Import required libraries
import streamlit as st
import pickle
import pandas as pd

# Load the trained model from the pickle file
with open('stroke_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the user interface elements
st.title('Stroke Prediction App')
age = st.slider('Age', 0, 100, 50)
gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
hypertension = st.selectbox('Hypertension', [0, 1])
heart_disease = st.selectbox('Heart Disease', [0, 1])
ever_married = st.selectbox('Ever Married', ['Yes', 'No'])
work_type = st.selectbox('Work Type', ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
Residence_type = st.selectbox('Residence Type', ['Urban', 'Rural'])
avg_glucose_level = st.number_input('Average Glucose Level', min_value=0.00, max_value=300.00, value=100.00)
bmi = st.number_input('BMI', min_value=0.00, max_value=100.00, value=25.00)
smoking_status = st.selectbox('Smoking Status', ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

# Preprocess the input data
gender_dict = {'Male': 1, 'Female': 0, 'Other': 2}
ever_married_dict = {'Yes': 1, 'No': 0}
work_type_dict = {'Private': 0, 'Self-employed': 1, 'Govt_job': 2, 'children': 3, 'Never_worked': 4}
Residence_type_dict = {'Urban': 1, 'Rural': 0}
smoking_status_dict = {'formerly smoked': 1, 'never smoked': 0, 'smokes': 2, 'Unknown': 3}

gender_val = gender_dict[gender]
ever_married_val = ever_married_dict[ever_married]
work_type_val = work_type_dict[work_type]
Residence_type_val = Residence_type_dict[Residence_type]
smoking_status_val = smoking_status_dict[smoking_status]

input_data = pd.DataFrame({'age': age,
                           'gender_Male': 1 if gender == 'Male' else 0,
                           'gender_Other': 1 if gender == 'Other' else 0,
                           'hypertension': hypertension,
                           'heart_disease': heart_disease,
                           'ever_married_Yes': ever_married_val,
                           'work_type_Never_worked': 1 if work_type == 'Never_worked' else 0,
                           'work_type_Private': 1 if work_type == 'Private' else 0,
                           'work_type_Self-employed': 1 if work_type == 'Self-employed' else 0,
                           'work_type_children': 1 if work_type == 'children' else 0,
                           'Residence_type_Urban': 1 if Residence_type == 'Urban' else 0,
                           'smoking_status_formerly smoked': 1 if smoking_status == 'formerly smoked' else 0,
                           'smoking_status_never smoked': 1 if smoking_status == 'never smoked' else 0,
                           'smoking_status_smokes': 1 if smoking_status == 'smokes' else 0,
                           'avg_glucose_level': avg_glucose_level,
                           'bmi': bmi
                          }, index=[0])
# Make predictions and display the results
if st.button('Predict'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error('This person is at risk of stroke.')
    else:
        st.success('This person is not at risk of stroke.')
