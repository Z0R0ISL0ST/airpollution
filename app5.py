import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("air_pollution_model.pkl")

st.title("Air Pollution Prediction")
st.write("Predict PM2.5 levels based on environmental factors.")

# User input
temperature = st.slider("Temperature (°C)", 0, 40, 20)
humidity = st.slider("Humidity (%)", 10, 90, 50)
wind_speed = st.slider("Wind Speed (km/h)", 0, 20, 5)
traffic_density = st.slider("Traffic Density (vehicles/hr)", 50, 500, 200)
industrial_emissions = st.slider("Industrial Emissions", 10, 500, 100)

# Make prediction
if st.button("Predict"):
    input_data = np.array([[temperature, humidity, wind_speed, traffic_density, industrial_emissions]])
    prediction = model.predict(input_data)
    st.write(f"Predicted PM2.5 Level: **{prediction[0]:.2f} µg/m³**")