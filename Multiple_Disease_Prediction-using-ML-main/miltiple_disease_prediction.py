# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained models
diabetes_model = pickle.load(open('Multiple_Disease_Prediction-using-ML-main\diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('Multiple_Disease_Prediction-using-ML-main\heart_prediction.sav', 'rb'))
parkinson_model = pickle.load(open('Multiple_Disease_Prediction-using-ML-main\parkinson_prediction.sav', 'rb'))

# Create a sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Heart Disease Prediction', 'Diabetes Prediction', 'Parkinson Prediction'],
                           icons=['heart', 'activity', 'person'],
                           default_index=0)

if selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML")
    
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.text_input("Enter Your Age", "0")
    with col2:
        sex = st.text_input("Sex (1 for Male, 0 for Female)", "1")
    with col3:
        cp = st.text_input("Enter your Cp", "0")
    with col1:
        trestbps = st.text_input("Enter your trestbps", '0')
    with col2:
        chol = st.text_input("Enter your chol", "0")
    with col3:
        fbs = st.text_input("Enter your fbs", "0")
    with col1:
        restecg = st.text_input("Enter your restecg", "0")
    with col2:
        thalach = st.text_input("Enter your thalach", "0")
    with col3:
        exang = st.text_input("Enter your exang", "0")
    with col1:
        oldpeak = st.text_input("Enter your oldpeak", "0")
    with col2:
        slope = st.text_input("Enter your slope", "0")
    with col3:
        ca = st.text_input("Enter your ca", "0")
    with col1:
        thal = st.text_input("Enter your thal", "0")

    heart_pred = ''

    # Creating a button for prediction
    if st.button('Predict Heart Result'):
        try:
            # Convert inputs to floats
            input_hdata = [
                int(age), int(sex), int(cp), int(trestbps), int(chol),
                int(fbs), int(restecg), int(thalach), int(exang),
                float(oldpeak), int(slope), int(ca), int(thal)
            ]

            # Reshape input data for the model
            input_hdata = [input_hdata]

            heart_pred = heart_model.predict(input_hdata)

            if heart_pred[0] == 1:
                heart_pred = 'Heart Disease Detected'
            else:
                heart_pred = 'No Heart Disease Found'

        except ValueError:
            heart_pred = 'Please enter valid numerical values for all fields.'

    st.success(heart_pred)

if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of pregnancies", "0")
    with col2:
        Glucose = st.text_input("Glucose level", "0")
    with col3:
        BloodPressure = st.text_input("Enter your BP value", "0")
    with col1:
        SkinThickness = st.text_input("Enter your skin thickness value", "0")
    with col2:
        Insulin = st.text_input("Enter your insulin value", "0")
    with col3:
        BMI = st.text_input("Enter your BMI value", "0")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Enter your DiabetesPedigree value", "0")
    with col2:
        Age = st.text_input("Enter your Age value", "0")

    diab_pred = ''

    # Creating a button for prediction
    if st.button('Predict Diabetes Result'):
        try:
            # Convert inputs to floats
            input_data = [
                float(Pregnancies), float(Glucose), float(BloodPressure),
                float(SkinThickness), float(Insulin), float(BMI),
                float(DiabetesPedigreeFunction), float(Age)
            ]

            # Reshape input data for the model
            input_data = [input_data]

            diab_pred = diabetes_model.predict(input_data)

            if diab_pred[0] == 1:
                diab_pred = 'The Person is Diabetic'
            else:
                diab_pred = 'The Person is Not Diabetic'

        except ValueError:
            diab_pred = 'Please enter valid numerical values for all fields.'

    st.success(diab_pred)

if selected == 'Parkinson Prediction':
    st.title("Parkinson Prediction using ML")
    col1, col2, col3,col4 = st.columns(4)
    # Define valid variable names for the inputs
    with col1:
        MDVP_Fo_Hz = st.text_input("Enter your MDVP:Fo(Hz)", "0")
    with col2:
        MDVP_Fhi_Hz = st.text_input("Enter your MDVP:Fhi(Hz)", "0")
    with col3:
        MDVP_Flo_Hz = st.text_input("Enter your MDVP:Flo(Hz)", "0")
    with col4:
        MDVP_Jitter_percent = st.text_input("Enter your MDVP:Jitter(%)", "0")
    with col1:
        MDVP_Jitter_Abs = st.text_input("Enter your MDVP:Jitter(Abs)", "0")
    with col2:
        MDVP_RAP = st.text_input("Enter your MDVP:RAP", "0")
    with col3:
        MDVP_PPQ = st.text_input("Enter your MDVP:PPQ", "0")
    with col4:
        Jitter_DDP = st.text_input("Enter your Jitter:DDP", "0")
    with col1:
        MDVP_Shimmer = st.text_input("Enter your MDVP:Shimmer", "0")
    with col2:
        MDVP_Shimmer_dB = st.text_input("Enter your MDVP:Shimmer(dB)", "0")
    with col3:
        Shimmer_APQ3 = st.text_input("Enter your Shimmer:APQ3", "0")
    with col4:
        Shimmer_APQ5 = st.text_input("Enter your Shimmer:APQ5", "0")
    with col1:
        MDVP_APQ = st.text_input("Enter your MDVP:APQ", "0")
    with col2:
        Shimmer_DDA = st.text_input("Enter your Shimmer:DDA", "0")
    with col3:
        NHR = st.text_input("Enter your NHR", "0")
    with col4:
        HNR = st.text_input("Enter your HNR", "0")
    with col1:
        RPDE = st.text_input("Enter your RPDE", "0")
    with col2:
        DFA = st.text_input("Enter your DFA", "0")
    with col3:
        spread1 = st.text_input("Enter your spread1", "0")
    with col4:
        spread2 = st.text_input("Enter your spread2", "0")
    with col1:
        D2 = st.text_input("Enter your D2", "0")
    with col2:
        PPE = st.text_input("Enter your PPE", "0")

    parkinson_pred = ''

    # Creating a button for prediction
    if st.button('Predict Parkinson Result'):
        try:
            # Convert inputs to floats
            input_pdata = [
                float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),
                float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP),
                float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer),
                float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
                float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR),
                float(RPDE), float(DFA), float(spread1), float(spread2),
                float(D2), float(PPE)
            ]

            # Reshape input data for the model
            input_pdata = [input_pdata]

            parkinson_pred = parkinson_model.predict(input_pdata)

            if parkinson_pred[0] == 1:
                parkinson_pred = 'Parkinson Disease Detected'
            else:
                parkinson_pred = 'No Parkinson Disease Found'

        except ValueError:
            parkinson_pred = 'Please enter valid numerical values for all fields.'

    st.success(parkinson_pred)
