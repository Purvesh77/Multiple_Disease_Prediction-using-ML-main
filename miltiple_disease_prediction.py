# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('heart_prediction.sav', 'rb'))
parkinson_model = pickle.load(open('parkinson_prediction.sav', 'rb'))

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

# Function to toggle theme
def toggle_theme():
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
    st.rerun()  # Use st.rerun() instead of st.experimental_rerun()

# Apply theme CSS
def apply_theme():
    if st.session_state.theme == 'dark':
        st.markdown("""
        <style>
        .main {
            background-color: #1a1a1a;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #2d2d2d;
            color: white;
            border-right: 1px solid #444;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input, 
        .stSelectbox>div>div>select, .stTextArea>div>div>textarea {
            background-color: #2d2d2d;
            color: white;
            border: 1px solid #444;
        }
        .stRadio>div {
            color: white;
        }
        .css-1aumxhk {
            background-color: #2d2d2d;
            border: 1px solid #444;
        }
        .st-b7 {
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .main {
            background-color: white;
            color: black;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            color: black;
            border-right: 1px solid #ddd;
        }
        .stTextInput>div>div>input, .stNumberInput>div>div>input, 
        .stSelectbox>div>div>select, .stTextArea>div>div>textarea {
            background-color: white;
            color: black;
            border: 1px solid #ced4da;
        }
        .stRadio>div {
            color: black;
        }
        .css-1aumxhk {
            background-color: white;
            border: 1px solid #ddd;
        }
        </style>
        """, unsafe_allow_html=True)

# Common CSS for both themes
st.markdown("""
    <style>
    .stButton>button {
        background: linear-gradient(to right, #4776E6 0%, #8E54E9 100%);
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
    .success {
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    .disease-title {
        text-align: center;
        margin-bottom: 30px;
    }
    .theme-toggle-btn {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
        border-radius: 50%;
        width: 40px;
        height: 40px;
        font-size: 20px;
        cursor: pointer;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        border: none;
    }
    .input-label {
        font-weight: bold;
        margin-bottom: 5px;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Apply the theme
apply_theme()

# Theme toggle button
st.markdown(f"""
    <button class="theme-toggle-btn" onclick="window.parent.document.querySelector('section.main').firstElementChild.click()" 
        style="background: {'#333' if st.session_state.theme == 'light' else '#f8f9fa'}; 
               color: {'white' if st.session_state.theme == 'light' else 'black'}">
        {'🌙' if st.session_state.theme == 'light' else '☀️'}
    </button>
    """, unsafe_allow_html=True)

# Create a sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                         ['Heart Disease Prediction', 'Diabetes Prediction', 'Parkinson Prediction'],
                         icons=['heart-pulse', 'activity', 'person'],
                         default_index=0,
                         styles={
                             "container": {"padding": "5px", "background-color": "#f8f9fa" if st.session_state.theme == 'light' else "#2d2d2d"},
                             "icon": {"color": "black" if st.session_state.theme == 'light' else "white", "font-size": "18px"}, 
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "color": "black" if st.session_state.theme == 'light' else "white", "--hover-color": "#4a4a4a"},
                             "nav-link-selected": {"background-color": "#6a5acd"},
                         })
    
    # Add theme toggle in sidebar
    st.markdown("---")
    if st.button(f"Switch to {'Dark' if st.session_state.theme == 'light' else 'Light'} Mode"):
        toggle_theme()

# [Rest of your disease prediction pages remain exactly the same...]
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 class='disease-title'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age (years)", min_value=0, max_value=120, value=50, step=1)
        cp = st.selectbox("Chest Pain Type", 
                         ["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120, step=1)
        restecg = st.selectbox("Resting ECG", 
                              ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
        ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0, step=1)
        
    with col2:
        sex = st.radio("Sex", ["Male", "Female"])
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, value=200, step=1)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=250, value=150, step=1)
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

    if st.button('Predict Heart Disease', key='heart_predict'):
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
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0, step=1)
        BloodPressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70, step=1)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
        
    with col2:
        Glucose = st.number_input("Glucose Level (mg/dl)", min_value=0, max_value=300, value=100, step=1)
        SkinThickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20, step=1)
        Age = st.number_input("Age (years)", min_value=0, max_value=120, value=30, step=1)
        
    with col3:
        Insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=1000, value=80, step=1)
        BMI = st.number_input("BMI (kg/m²)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)

    diab_pred = ''

    if st.button('Predict Diabetes', key='diabetes_predict'):
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

    if st.button("Predict Parkinson's Disease", key='parkinson_predict'):
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
    <div style="text-align: center; font-size: 14px;">
        <p>Desined by Purvesh Patil with ❤️</p>
        
    </div>
    """, unsafe_allow_html=True)