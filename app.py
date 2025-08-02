
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open('C:/Users/Niranjan/Downloads/P/working apps/multiple-disease-prediction-streamlit-app-main/saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/Niranjan/Downloads/P/working apps/multiple-disease-prediction-streamlit-app-main/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('C:/Users/Niranjan/Downloads/P/working apps/multiple-disease-prediction-streamlit-app-main/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Autism Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'emoji-smile'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                         BMI, DiabetesPedigreeFunction, Age]]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                         exang, oldpeak, slope, ca, thal]]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    inputs = ["MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP",
              "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5",
              "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"]
    user_input = [st.text_input(label) for label in inputs]

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
    st.success(parkinsons_diagnosis)

# Load the autism model
autism_model = pickle.load(open('C:/Users/Niranjan/Downloads/P/working apps/multiple-disease-prediction-streamlit-app-main/saved_models/autism_model.sav', 'rb'))

def autism_prediction():
    st.title("Autism Spectrum Disorder Prediction")
    st.subheader("Answer the following 10 questions (0 = No, 1 = Yes):")

    q1 = st.selectbox("1. Does your child look at you when you call their name?", [0, 1])
    q2 = st.selectbox("2. Does your child point at things to show interest?", [0, 1])
    q3 = st.selectbox("3. Does your child enjoy playing pretend games?", [0, 1])
    q4 = st.selectbox("4. Does your child follow simple instructions?", [0, 1])
    q5 = st.selectbox("5. Does your child use single words by 16 months?", [0, 1])
    q6 = st.selectbox("6. Does your child show interest in other children?", [0, 1])
    q7 = st.selectbox("7. Does your child bring objects to show you?", [0, 1])
    q8 = st.selectbox("8. Does your child respond to emotions?", [0, 1])
    q9 = st.selectbox("9. Does your child like routines and get upset with change?", [0, 1])
    q10 = st.selectbox("10. Does your child make eye contact?", [0, 1])

    st.subheader("Additional Information:")
    age = st.number_input("Age", min_value=1, max_value=100, value=3)
    gender = st.selectbox("Gender", ["male", "female"])
    jaundice = st.selectbox("Jaundice (yellowing of the skin)", ["yes", "no"])
    used_app_before = st.selectbox("Used Autism Screening App Before?", ["yes", "no"])

    if st.button("Predict"):
        gender_encoded = 1 if gender == "male" else 0
        jaundice_encoded = 1 if jaundice == "yes" else 0
        used_app_before_encoded = 1 if used_app_before == "yes" else 0

        user_input = [
            q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,
            age, gender_encoded, jaundice_encoded, used_app_before_encoded
        ]

        prediction = autism_model.predict([user_input])[0]

        if prediction == 1:
            st.error("The model predicts a high risk of Autism Spectrum Disorder.")
        else:
            st.success("The model predicts a low risk of Autism Spectrum Disorder.")

if selected == "Autism Prediction":
    autism_prediction()

