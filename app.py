import pickle 
import time
import streamlit as st
import pandas as pd
import numpy as np



with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Air Quality Index Prediction')
col1 , col2 = st.columns(2)
with col1:
    co_aqi = st.number_input("CO AQI Value:", min_value=0, placeholder='Enter CO AQI Value')
    ozone_aqi = st.number_input("OZONE AQI Value:", min_value=0, placeholder='Enter OZONE AQI Value')
with col2:
    no2_aqi = st.number_input("NO2 AQI Value:", min_value=0, placeholder='Enter NO2 AQI Value')
    pm_aqi = st.number_input("PM2.5 AQI Value:", min_value=0, placeholder='Enter PM2.5 AQI Value')


col3, col4 = st.columns(2)
if st.button("Predict"):
    data = pd.DataFrame([[co_aqi, ozone_aqi, no2_aqi, pm_aqi]], columns=["CO AQI Value","Ozone AQI Value","NO2 AQI Value","PM2.5 AQI Value"])
    start_time = time.time()
    pred = model.predict(data)
    end_time = time.time()
    elapsed = end_time - start_time
    with col1:
        st.write('**Air Quality Index** ')
        st.write(int(pred[0]))
        aqi_category = 0
        match pred:
            case _ if 0 <= pred <=50:
                aqi_category = 'Good'
            case _ if 51 <= pred <=100:
                aqi_category = 'Moderate'
            case _ if 101 <= pred <=150:
                aqi_category = 'Unhealthy for Sensitive groups'
            case _ if 151 <= pred <=200:
                aqi_category = 'Unhealthy'
            case _ if 201 <= pred <=300:
                aqi_category = 'Very Unhealthy'
            case _ if 301 <= pred:
                aqi_category = 'Hazardous'

    with col4:
        st.write("**Air Quality Index Category** ")
        st.write(aqi_category)
    st.write(f'Elapsed time : {elapsed :.5f} seconds')


    description = """
    About the Air Quality Index (AQI)
    The Air Quality Index (AQI) is a standardized system used to measure and report the quality of air in a specific area. It provides an easy-to-understand scale that indicates how polluted the air is and what the associated health effects might be for the general public. The AQI ranges from 0 to 500, with higher values indicating greater air pollution and higher potential health risks.

    AQI Categories: \n 
    0-50 (Good): Air quality is considered satisfactory, and air pollution poses little or no risk. \n 
    51-100 (Moderate): Air quality is acceptable; however, some pollutants may be a concern for sensitive individuals. \n 
    101-150 (Unhealthy for Sensitive Groups): Members of sensitive groups, such as children, elderly, and individuals with respiratory or heart conditions, may experience health effects. \n 
    151-200 (Unhealthy): Everyone may begin to experience health effects; members of sensitive groups may experience more serious effects. \n 
    201-300 (Very Unhealthy): Health alert: Everyone may experience more serious health effects. \n 
    301-500 (Hazardous): Health warnings of emergency conditions. The entire population is likely to be affected. \n 
    The AQI considers key pollutants such as PM2.5, PM10, carbon monoxide (CO), ozone (O₃), nitrogen dioxide (NO₂), and sulfur dioxide (SO₂). This information helps individuals make informed decisions to protect their health, such as limiting outdoor activities during poor air quality days.

    For more information, refer to your local environmental agency or the World Health Organization (WHO) guidelines on air quality.
    """

    def stream_data():
        for word in description.split(" "):
            yield word + " "
            time.sleep(0.005)
    
    st.write_stream(stream_data)

