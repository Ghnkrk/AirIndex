import streamlit as st
st.set_page_config(
    page_title="Air Quality Index Predictor", 
    page_icon=":evergreen_tree:", 
    layout="centered"
)

import pickle 
import time
import pandas as pd
import numpy as np
import logging
from logging.handlers import RotatingFileHandler
import os

# Configure Logging
LOG_FILE = os.path.abspath(os.path.join("..", "log", "app.log"))
LOG_DIR = os.path.dirname(LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

handler = RotatingFileHandler(LOG_FILE, "a", maxBytes=5000, backupCount=5)
logging.basicConfig(
    handlers=[handler],
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
        font-family: 'Arial', sans-serif;
    }
    .login-container {
        max-width: 400px;
        margin: auto;
        padding: 40px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        background-color: #ecf0f1;
        border: 1.5px solid #3498db;
        border-radius: 5px;
        color: #2c3e50;
    }
    .stButton > button {
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }
    .result-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model
with open('model.pkl', 'rb') as file:
    logging.info("Loading the model from .pkl format")
    model = pickle.load(file)

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Login Page
def login_page():
    st.markdown('<h1 class="title">🌍 Air Quality Predictor</h1>', unsafe_allow_html=True)
    
    # Username and password inputs (no validation for this example)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        # Always allow login for this example
        st.session_state.logged_in = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Main Prediction Page
def prediction_page():
    # Title with custom styling
    st.markdown('<h1 class="title">🌍 Air Quality Index Predictor</h1>', unsafe_allow_html=True)

    # Sidebar Navigation
    menu = ["Predict AQI", "AQI Description", "Logout"]
    choice = st.sidebar.radio("Navigation", menu)

    if choice == "Predict AQI":
        # Input columns
        col1, col2 = st.columns(2)
        with col1:
            co_aqi = st.number_input("CO AQI Value:", min_value=0, placeholder='Enter CO AQI Value', key='co')
            ozone_aqi = st.number_input("OZONE AQI Value:", min_value=0, placeholder='Enter OZONE AQI Value', key='ozone')
        with col2:
            no2_aqi = st.number_input("NO2 AQI Value:", min_value=0, placeholder='Enter NO2 AQI Value', key='no2')
            pm_aqi = st.number_input("PM2.5 AQI Value:", min_value=0, placeholder='Enter PM2.5 AQI Value', key='pm')

        # Prediction button and results
        col3, col4 = st.columns(2)
        if st.button("Predict Air Quality"):
            data = pd.DataFrame([[co_aqi, ozone_aqi, no2_aqi, pm_aqi]], 
                                 columns=["CO AQI Value","Ozone AQI Value","NO2 AQI Value","PM2.5 AQI Value"])
            
            logging.info("Predicting with model")
            
            start_time = time.time()
            pred = model.predict(data)
            end_time = time.time()
            
            logging.info("Inference completed")
            
            elapsed = end_time - start_time
            
            # Determine AQI Category
            def get_aqi_category(pred):
                if 0 <= pred <= 50:
                    return 'Good', '#4CAF50'
                elif 51 <= pred <= 100:
                    return 'Moderate', '#FFEB3B'
                elif 101 <= pred <= 150:
                    return 'Unhealthy for Sensitive Groups', '#FF9800'
                elif 151 <= pred <= 200:
                    return 'Unhealthy', '#F44336'
                elif 201 <= pred <= 300:
                    return 'Very Unhealthy', '#9C27B0'
                else:
                    return 'Hazardous', '#B71C1C'
            
            aqi_category, color = get_aqi_category(pred[0])
            
            st.write("**Air Quality Category**")
            st.markdown(f'<h2 style="color:{color};">{aqi_category}</h2>', unsafe_allow_html=True)
            logging.info("AQI Category displayed")
            
            st.write(f'Elapsed Prediction Time: {elapsed:.7f} seconds')

    elif choice == "AQI Description":
        st.markdown('## 📊 Understanding Air Quality Index (AQI)')
        description = """
        The Air Quality Index (AQI) is a standardized system used to measure and report the quality of air in a specific area. 
        It provides an easy-to-understand scale that indicates how polluted the air is and what the associated health effects might be for the general public.

        **AQI Categories Breakdown:**
        - **0-50 (Good):** Air quality is satisfactory, with minimal pollution risk.
        - **51-100 (Moderate):** Air quality is acceptable, with potential concerns for sensitive individuals.
        - **101-150 (Unhealthy for Sensitive Groups):** Health risks for children, elderly, and those with respiratory conditions.
        - **151-200 (Unhealthy):** General population may experience health effects.
        - **201-300 (Very Unhealthy):** Significant health warnings for everyone.
        - **301+ (Hazardous):** Emergency conditions affecting the entire population.

        The AQI considers key pollutants like PM2.5, carbon monoxide (CO), ozone (O₃), and nitrogen dioxide (NO₂).
        
        **Health Recommendations:**
        - Monitor air quality regularly
        - Limit outdoor activities during poor air quality
        - Use air purifiers indoors
        - Consult healthcare providers for specific health concerns
        """

        st.write(description)
        logging.info("Comprehensive description displayed")

    elif choice == "Logout":
        st.session_state.logged_in = False
        st.rerun()

# Main App Logic
def main():
    if not st.session_state.logged_in:
        login_page()
    else:
        prediction_page()

# Run the app
if __name__ == "__main__":
    main()
