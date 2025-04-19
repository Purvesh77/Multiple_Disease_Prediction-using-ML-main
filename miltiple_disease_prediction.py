# # -*- coding: utf-8 -*-

# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Load the trained models
# diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
# heart_model = pickle.load(open('heart_prediction.sav', 'rb'))
# parkinson_model = pickle.load(open('parkinson_prediction.sav', 'rb'))

# # Create a sidebar
# with st.sidebar:
#     selected = option_menu('Multiple Disease Prediction System',
#                            ['Heart Disease Prediction', 'Diabetes Prediction', 'Parkinson Prediction'],
#                            icons=['heart', 'activity', 'person'],
#                            default_index=0)

# if selected == 'Heart Disease Prediction':
#     st.title("Heart Disease Prediction using ML")
    
#     col1,col2,col3=st.columns(3)
#     with col1:
#         age = st.text_input("Enter Your Age", "0")
#     with col2:
#         sex = st.text_input("Sex (1 for Male, 0 for Female)", "1")
#     with col3:
#         cp = st.text_input("Enter your Cp", "0")
#     with col1:
#         trestbps = st.text_input("Enter your trestbps", '0')
#     with col2:
#         chol = st.text_input("Enter your chol", "0")
#     with col3:
#         fbs = st.text_input("Enter your fbs", "0")
#     with col1:
#         restecg = st.text_input("Enter your restecg", "0")
#     with col2:
#         thalach = st.text_input("Enter your thalach", "0")
#     with col3:
#         exang = st.text_input("Enter your exang", "0")
#     with col1:
#         oldpeak = st.text_input("Enter your oldpeak", "0")
#     with col2:
#         slope = st.text_input("Enter your slope", "0")
#     with col3:
#         ca = st.text_input("Enter your ca", "0")
#     with col1:
#         thal = st.text_input("Enter your thal", "0")

#     heart_pred = ''

#     # Creating a button for prediction
#     if st.button('Predict Heart Result'):
#         try:
#             # Convert inputs to floats
#             input_hdata = [
#                 int(age), int(sex), int(cp), int(trestbps), int(chol),
#                 int(fbs), int(restecg), int(thalach), int(exang),
#                 float(oldpeak), int(slope), int(ca), int(thal)
#             ]

#             # Reshape input data for the model
#             input_hdata = [input_hdata]

#             heart_pred = heart_model.predict(input_hdata)

#             if heart_pred[0] == 1:
#                 heart_pred = 'Heart Disease Detected'
#             else:
#                 heart_pred = 'No Heart Disease Found'

#         except ValueError:
#             heart_pred = 'Please enter valid numerical values for all fields.'

#     st.success(heart_pred)

# if selected == 'Diabetes Prediction':
#     st.title("Diabetes Prediction using ML")
#     col1,col2,col3=st.columns(3)
#     with col1:
#         Pregnancies = st.text_input("Number of pregnancies", "0")
#     with col2:
#         Glucose = st.text_input("Glucose level", "0")
#     with col3:
#         BloodPressure = st.text_input("Enter your BP value", "0")
#     with col1:
#         SkinThickness = st.text_input("Enter your skin thickness value", "0")
#     with col2:
#         Insulin = st.text_input("Enter your insulin value", "0")
#     with col3:
#         BMI = st.text_input("Enter your BMI value", "0")
#     with col1:
#         DiabetesPedigreeFunction = st.text_input("Enter your DiabetesPedigree value", "0")
#     with col2:
#         Age = st.text_input("Enter your Age value", "0")

#     diab_pred = ''

#     # Creating a button for prediction
#     if st.button('Predict Diabetes Result'):
#         try:
#             # Convert inputs to floats
#             input_data = [
#                 float(Pregnancies), float(Glucose), float(BloodPressure),
#                 float(SkinThickness), float(Insulin), float(BMI),
#                 float(DiabetesPedigreeFunction), float(Age)
#             ]

#             # Reshape input data for the model
#             input_data = [input_data]

#             diab_pred = diabetes_model.predict(input_data)

#             if diab_pred[0] == 1:
#                 diab_pred = 'The Person is Diabetic'
#             else:
#                 diab_pred = 'The Person is Not Diabetic'

#         except ValueError:
#             diab_pred = 'Please enter valid numerical values for all fields.'

#     st.success(diab_pred)

# if selected == 'Parkinson Prediction':
#     st.title("Parkinson Prediction using ML")
#     col1, col2, col3,col4 = st.columns(4)
#     # Define valid variable names for the inputs
#     with col1:
#         MDVP_Fo_Hz = st.text_input("Enter your MDVP:Fo(Hz)", "0")
#     with col2:
#         MDVP_Fhi_Hz = st.text_input("Enter your MDVP:Fhi(Hz)", "0")
#     with col3:
#         MDVP_Flo_Hz = st.text_input("Enter your MDVP:Flo(Hz)", "0")
#     with col4:
#         MDVP_Jitter_percent = st.text_input("Enter your MDVP:Jitter(%)", "0")
#     with col1:
#         MDVP_Jitter_Abs = st.text_input("Enter your MDVP:Jitter(Abs)", "0")
#     with col2:
#         MDVP_RAP = st.text_input("Enter your MDVP:RAP", "0")
#     with col3:
#         MDVP_PPQ = st.text_input("Enter your MDVP:PPQ", "0")
#     with col4:
#         Jitter_DDP = st.text_input("Enter your Jitter:DDP", "0")
#     with col1:
#         MDVP_Shimmer = st.text_input("Enter your MDVP:Shimmer", "0")
#     with col2:
#         MDVP_Shimmer_dB = st.text_input("Enter your MDVP:Shimmer(dB)", "0")
#     with col3:
#         Shimmer_APQ3 = st.text_input("Enter your Shimmer:APQ3", "0")
#     with col4:
#         Shimmer_APQ5 = st.text_input("Enter your Shimmer:APQ5", "0")
#     with col1:
#         MDVP_APQ = st.text_input("Enter your MDVP:APQ", "0")
#     with col2:
#         Shimmer_DDA = st.text_input("Enter your Shimmer:DDA", "0")
#     with col3:
#         NHR = st.text_input("Enter your NHR", "0")
#     with col4:
#         HNR = st.text_input("Enter your HNR", "0")
#     with col1:
#         RPDE = st.text_input("Enter your RPDE", "0")
#     with col2:
#         DFA = st.text_input("Enter your DFA", "0")
#     with col3:
#         spread1 = st.text_input("Enter your spread1", "0")
#     with col4:
#         spread2 = st.text_input("Enter your spread2", "0")
#     with col1:
#         D2 = st.text_input("Enter your D2", "0")
#     with col2:
#         PPE = st.text_input("Enter your PPE", "0")

#     parkinson_pred = ''

#     # Creating a button for prediction
#     if st.button('Predict Parkinson Result'):
#         try:
#             # Convert inputs to floats
#             input_pdata = [
#                 float(MDVP_Fo_Hz), float(MDVP_Fhi_Hz), float(MDVP_Flo_Hz),
#                 float(MDVP_Jitter_percent), float(MDVP_Jitter_Abs), float(MDVP_RAP),
#                 float(MDVP_PPQ), float(Jitter_DDP), float(MDVP_Shimmer),
#                 float(MDVP_Shimmer_dB), float(Shimmer_APQ3), float(Shimmer_APQ5),
#                 float(MDVP_APQ), float(Shimmer_DDA), float(NHR), float(HNR),
#                 float(RPDE), float(DFA), float(spread1), float(spread2),
#                 float(D2), float(PPE)
#             ]

#             # Reshape input data for the model
#             input_pdata = [input_pdata]

#             parkinson_pred = parkinson_model.predict(input_pdata)

#             if parkinson_pred[0] == 1:
#                 parkinson_pred = 'Parkinson Disease Detected'
#             else:
#                 parkinson_pred = 'No Parkinson Disease Found'

#         except ValueError:
#             parkinson_pred = 'Please enter valid numerical values for all fields.'

#     st.success(parkinson_pred)
# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_prediction.sav', 'rb'))
parkinson_model = pickle.load(open('parkinson_prediction.sav', 'rb'))

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(195deg, #42424a 0%, #191919 100%);
        color: white;
    }
    .st-b7 {
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #f8f9fa;
    }
    .stButton>button {
        background: linear-gradient(to right, #4776E6 0%, #8E54E9  100%);
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 25px;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .css-1aumxhk {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .success {
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    .disease-title {
        color: #2c3e50;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Create a sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Heart Disease Prediction', 'Diabetes Prediction', 'Parkinson Prediction'],
                          icons=['heart-pulse', 'activity', 'person'],
                          default_index=0,
                          styles={
                              "container": {"padding": "5px", "background-color": "#1a1a1a"},
                              "icon": {"color": "white", "font-size": "18px"}, 
                              "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#4a4a4a"},
                              "nav-link-selected": {"background-color": "#6a5acd"},
                          })

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 class='disease-title'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age (years)", min_value=0, max_value=120, value=50)
        cp = st.selectbox("Chest Pain Type", 
                         ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120)
        restecg = st.selectbox("Resting ECG", 
                              ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
        ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
        
    with col2:
        sex = st.radio("Sex", ["Male", "Female"])
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=250, value=150)
        slope = st.selectbox("Slope of Peak Exercise ST Segment", 
                            ["Upsloping", "Flat", "Downsloping"])
        
    with col3:
        thal = st.selectbox("Thalassemia", 
                          ["Normal", "Fixed Defect", "Reversible Defect"])
        exang = st.radio("Exercise Induced Angina", ["No", "Yes"])
        
    # Convert inputs to model format
    sex = 1 if sex == "Male" else 0
    cp_mapping = {"Typical angina": 0, "Atypical angina": 1, "Non-anginal pain": 2, "Asymptomatic": 3}
    cp = cp_mapping[cp]
    fbs = 1 if fbs == "Yes" else 0
    restecg_mapping = {"Normal": 0, "ST-T wave abnormality": 1, "Left ventricular hypertrophy": 2}
    restecg = restecg_mapping[restecg]
    exang = 1 if exang == "Yes" else 0
    slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    slope = slope_mapping[slope]
    thal_mapping = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}
    thal = thal_mapping[thal]

    heart_pred = ''

    # Creating a button for prediction
    if st.button('Predict Heart Disease'):
        try:
            input_hdata = [
                age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
                oldpeak, slope, ca, thal
            ]
            input_hdata = [input_hdata]
            heart_pred = heart_model.predict(input_hdata)

            if heart_pred[0] == 1:
                st.error('⚠️ Heart Disease Detected. Please consult a cardiologist.')
            else:
                st.success('✅ No Heart Disease Found. Maintain a healthy lifestyle!')

        except Exception as e:
            st.error(f'An error occurred: {str(e)}')

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.markdown("<h1 class='disease-title'>🩸 Diabetes Prediction</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
        BloodPressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
        
    with col2:
        Glucose = st.number_input("Glucose Level (mg/dl)", min_value=0, max_value=300, value=100)
        SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
        Age = st.number_input("Age (years)", min_value=0, max_value=120, value=30)
        
    with col3:
        Insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=1000, value=80)
        BMI = st.number_input("BMI (kg/m²)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)

    diab_pred = ''

    if st.button('Predict Diabetes'):
        try:
            input_data = [
                Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                BMI, DiabetesPedigreeFunction, Age
            ]
            input_data = [input_data]
            diab_pred = diabetes_model.predict(input_data)

            if diab_pred[0] == 1:
                st.error('⚠️ Diabetes Detected. Please consult a doctor for proper management.')
            else:
                st.success('✅ No Diabetes Detected. Keep up with healthy habits!')

        except Exception as e:
            st.error(f'An error occurred: {str(e)}')

# Parkinson's Prediction Page
if selected == 'Parkinson Prediction':
    st.markdown("<h1 class='disease-title'>🧠 Parkinson's Disease Prediction</h1>", unsafe_allow_html=True)
    
    st.info("Please enter voice measurement parameters for Parkinson's prediction")
    
    tabs = st.tabs(["Basic Voice Measures", "Advanced Voice Measures"])
    
    with tabs[0]:
        col1, col2 = st.columns(2)
        with col1:
            MDVP_Fo_Hz = st.number_input("Average Vocal Fundamental Frequency (Hz)", min_value=0.0, value=150.0, step=0.1)
            MDVP_Jitter_percent = st.number_input("Jitter (%)", min_value=0.0, value=0.005, step=0.0001, format="%.4f")
            MDVP_Shimmer = st.number_input("Shimmer (dB)", min_value=0.0, value=0.03, step=0.001, format="%.3f")
            NHR = st.number_input("Noise-to-Harmonics Ratio", min_value=0.0, value=0.02, step=0.001, format="%.3f")
            
        with col2:
            MDVP_Fhi_Hz = st.number_input("Maximum Vocal Fundamental Frequency (Hz)", min_value=0.0, value=200.0, step=0.1)
            MDVP_Jitter_Abs = st.number_input("Absolute Jitter (μs)", min_value=0.0, value=0.00003, step=0.00001, format="%.5f")
            MDVP_Shimmer_dB = st.number_input("Shimmer (dB)", min_value=0.0, value=0.3, step=0.01)
            HNR = st.number_input("Harmonics-to-Noise Ratio (dB)", min_value=0.0, value=20.0, step=0.1)
    
    with tabs[1]:
        col1, col2 = st.columns(2)
        with col1:
            MDVP_Flo_Hz = st.number_input("Minimum Vocal Fundamental Frequency (Hz)", min_value=0.0, value=100.0, step=0.1)
            MDVP_RAP = st.number_input("Relative Amplitude Perturbation", min_value=0.0, value=0.003, step=0.0001, format="%.4f")
            Shimmer_APQ3 = st.number_input("3-point Amplitude Perturbation Quotient", min_value=0.0, value=0.015, step=0.001, format="%.3f")
            RPDE = st.number_input("Recurrence Period Density Entropy", min_value=0.0, value=0.5, step=0.01)
            
        with col2:
            MDVP_PPQ = st.number_input("5-point Period Perturbation Quotient", min_value=0.0, value=0.004, step=0.0001, format="%.4f")
            Jitter_DDP = st.number_input("Jitter: DDP", min_value=0.0, value=0.009, step=0.0001, format="%.4f")
            Shimmer_APQ5 = st.number_input("5-point Amplitude Perturbation Quotient", min_value=0.0, value=0.02, step=0.001, format="%.3f")
            DFA = st.number_input("Detrended Fluctuation Analysis", min_value=0.0, value=0.7, step=0.01)
    
    col1, col2 = st.columns(2)
    with col1:
        Shimmer_DDA = st.number_input("Shimmer: DDA", min_value=0.0, value=0.045, step=0.001, format="%.3f")
        spread1 = st.number_input("Spread 1", min_value=-10.0, value=-5.0, step=0.1)
    with col2:
        MDVP_APQ = st.number_input("11-point Amplitude Perturbation Quotient", min_value=0.0, value=0.025, step=0.001, format="%.3f")
        spread2 = st.number_input("Spread 2", min_value=-10.0, value=0.2, step=0.1)
    
    col1, col2 = st.columns(2)
    with col1:
        D2 = st.number_input("D2", min_value=0.0, value=2.0, step=0.1)
    with col2:
        PPE = st.number_input("Pitch Period Entropy", min_value=0.0, value=0.2, step=0.01)

    parkinson_pred = ''

    if st.button("Predict Parkinson's Disease"):
        try:
            input_pdata = [
                MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz,
                MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP,
                MDVP_PPQ, Jitter_DDP, MDVP_Shimmer,
                MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
                MDVP_APQ, Shimmer_DDA, NHR, HNR,
                RPDE, DFA, spread1, spread2,
                D2, PPE
            ]
            input_pdata = [input_pdata]
            parkinson_pred = parkinson_model.predict(input_pdata)

            if parkinson_pred[0] == 1:
                st.error('⚠️ Parkinson\'s Disease Detected. Please consult a neurologist for further evaluation.')
            else:
                st.success('✅ No Parkinson\'s Disease Detected. Regular exercise may help prevent neurological disorders.')

        except Exception as e:
            st.error(f'An error occurred: {str(e)}')

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 14px;">
        <p>This predictive tool is for informational purposes only and should not replace professional medical advice.</p>
    </div>
    """, unsafe_allow_html=True)