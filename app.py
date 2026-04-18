import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("solar_model.pkl")

features = [
    'distance-to-solar-noon',
    'temperature',
    'wind-direction',
    'wind-speed',
    'sky-cover',
    'visibility',
    'humidity',
    'average-wind-speed-(period)',
    'average-pressure-(period)'
]

st.title("🌞 Solar Power Prediction App")

# Inputs
distance = st.number_input('Distance to Solar Noon', 0.0, 1.0)
temp = st.number_input('Temperature', -50.0, 150.0, 60.0)
wind_dir = st.number_input('Wind Direction', 0.0, 360.0, 180.0)
wind_speed = st.number_input('Wind Speed', 0.0, 50.0, 10.0)
sky = st.number_input('Sky Cover', 0.0, 8.0, 4.0)
vis = st.number_input('Visibility', 0.0, 10.0, 10.0)
hum = st.number_input('Humidity', 0.0, 100.0, 70.0)
avg_ws = st.number_input('Avg Wind Speed', 0.0, 20.0, 10.0)
avg_pr = st.number_input('Avg Pressure', 29.0, 31.0, 30.0)

if st.button("Predict"):
    input_df = pd.DataFrame([[distance, temp, wind_dir, wind_speed, sky, vis, hum, avg_ws, avg_pr]], columns=features)
    
    pred = model.predict(input_df)
    
    st.success(f"⚡ Predicted Power: {pred[0]:.2f} Joules")
