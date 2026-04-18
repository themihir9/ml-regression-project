import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv("solarpowergeneration.csv")


Q1 = np.percentile(df["distance-to-solar-noon"],25)
Q3 = np.percentile(df["distance-to-solar-noon"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['distance-to-solar-noon'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'distance-to-solar-noon'])<LW:
        df.loc[i,'distance-to-solar-noon']=LW
        s=s+1
    elif (df.loc[i,'distance-to-solar-noon'])>UW: # Added condition for upper outliers
        df.loc[i,'distance-to-solar-noon']=UW
        s=s+1
   
Q1 = np.percentile(df["temperature"],25)
Q3 = np.percentile(df["temperature"],75)
IQR = Q3-Q1

UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['temperature'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'temperature'])<LW:
        df.loc[i,'temperature']=LW
        s=s+1
    elif (df.loc[i,'temperature'])>UW: # Added condition for upper outliers
        df.loc[i,'temperature']=UW
        s=s+1
      


import numpy as np
Q1 = np.percentile(df["wind-direction"],25)
Q3 = np.percentile(df["wind-direction"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['wind-direction'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'wind-direction'])<LW:
        df.loc[i,'wind-direction']=LW
        s=s+1
    elif (df.loc[i,'wind-direction'])>UW: # Added condition for upper outliers
        df.loc[i,'wind-direction']=UW
        s=s+1

import numpy as np
Q1 = np.percentile(df["wind-speed"],25)
Q3 = np.percentile(df["wind-speed"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['wind-speed'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'wind-speed'])<LW:
        df.loc[i,'wind-speed']=LW
        s=s+1
    elif (df.loc[i,'wind-speed'])>UW: # Added condition for upper outliers
        df.loc[i,'wind-speed']=UW
        s=s+1
      


import numpy as np
Q1 = np.percentile(df["sky-cover"],25)
Q3 = np.percentile(df["sky-cover"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR

c=len(df['sky-cover'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'sky-cover'])<LW:
        df.loc[i,'sky-cover']=LW
        s=s+1
    elif (df.loc[i,'sky-cover'])>UW: # Added condition for upper outliers
        df.loc[i,'sky-cover']=UW
        s=s+1



import numpy as np
Q1 = np.percentile(df["visibility"],25)
Q3 = np.percentile(df["visibility"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['visibility'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'visibility'])<LW:
        df.loc[i,'visibility']=LW
        s=s+1
    elif (df.loc[i,'visibility'])>UW: # Added condition for upper outliers
        df.loc[i,'visibility']=UW
        s=s+1


import numpy as np
Q1 = np.percentile(df["humidity"],25)
Q3 = np.percentile(df["humidity"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['humidity'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'humidity'])<LW:
        df.loc[i,'humidity']=LW
        s=s+1
    elif (df.loc[i,'humidity'])>UW: # Added condition for upper outliers
        df.loc[i,'humidity']=UW
        s=s+1
      


Q1 = np.percentile(df["average-wind-speed-(period)"],25)
Q3 = np.percentile(df["average-wind-speed-(period)"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['average-wind-speed-(period)'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'average-wind-speed-(period)'])<LW:
        df.loc[i,'average-wind-speed-(period)']=LW
        s=s+1
    elif (df.loc[i,'average-wind-speed-(period)'])>UW: # Added condition for upper outliers
        df.loc[i,'average-wind-speed-(period)']=UW
        s=s+1
      


Q1 = np.percentile(df["average-pressure-(period)"],25)
Q3 = np.percentile(df["average-pressure-(period)"],75)
IQR = Q3-Q1
##("IQRvalue",IQR)
UW = Q3+1.5*IQR
LW = Q1-1.5*IQR


c=len(df['average-pressure-(period)'])
s=0
for i in range(0,c):
    
    
    if (df.loc[i,'average-pressure-(period)'])<LW:
        df.loc[i,'average-pressure-(period)']=LW
        s=s+1
    elif (df.loc[i,'average-pressure-(period)'])>UW: # Added condition for upper outliers
        df.loc[i,'average-pressure-(period)']=UW
        s=s+1
      


target_col = "power-generated"

X = df.drop(target_col, axis=1)
y = df[target_col]

# Impute missing values in X before splitting
X = X.fillna(X.mean(numeric_only=True))


SS = StandardScaler()
SS_cont = SS.fit_transform(X)
X_scaled = pd.DataFrame(SS_cont, columns=X.columns)



X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
 






from sklearn.linear_model import LinearRegression, Ridge


#
from sklearn.ensemble import GradientBoostingRegressor

gb_model = GradientBoostingRegressor(random_state=42)

# Fit model on scaled training data
gb_model.fit(X_train, y_train)

train_pred = gb_model.predict(X_train)
test_pred  = gb_model.predict(X_test)
##("BOOSTING MODEL")
##("\nTrain RMSE:", np.sqrt(mean_squared_error(y_train, train_pred)))
##("Te# %%
print("\nTrain R2  :", r2_score(y_train, train_pred))

print("Test  R2  :", r2_score(y_test, test_pred))


import streamlit as st


import streamlit as st
st.markdown( """
    <style>
    .stApp {
        background-color: #DFFFDE;
    };
    }
    </style>
    """,
    unsafe_allow_html=True)

st.markdown("""
           <p style="text-align: center; font-family: 'Open Sans'; color: green; font-size: 40px;">Welcome to the Solar Energy Prediction Application    </p>""", unsafe_allow_html=True)
##st.markdown("""
        ##    <p  style="font-family: 'Open Sans'; color: green; font-size: 20px;">Please enter the below values  </p>""", unsafe_allow_html=True)
##
st.subheader('Please enter below  Feature Values:')
# Input fields for features

distance_to_solar_noon = st.number_input('Enter Distance to Solar Noon', min_value=0.0, max_value=1.0, step=0.01)
temperature = st.number_input(' Enter Temperature', min_value=-50.0, max_value=150.0, value=60.0, step=1.0)
wind_direction = st.number_input('Enter Wind Direction', min_value=0.0, max_value=360.0, value=180.0, step=1.0)
wind_speed = st.number_input('Enter Wind Speed', min_value=0.0, max_value=50.0, value=10.0, step=0.1)
sky_cover = st.number_input('enter Sky Cover (0-8, e.g., 0=Clear, 8=Overcast)', min_value=0.0, max_value=8.0, value=4.0, step=1.0)
visibility = st.number_input('Enter Visibility', min_value=0.0, max_value=10.0, value=10.0, step=0.1)
humidity = st.number_input('Enter Humidity', min_value=0.0, max_value=100.0, value=70.0, step=1.0)
average_wind_speed_period = st.number_input('Average Wind Speed (Period)', min_value=0.0, max_value=20.0, value=10.0, step=0.1)
average_pressure_period = st.number_input('Average Pressure (Period)', min_value=29.0, max_value=31.0, value=30.0, step=0.01)
 

# Display input values (for debugging/verification)
st.subheader('Entered Feature Values:')
st.write(f'Distance to Solar Noon: {distance_to_solar_noon}')
st.write(f'Temperature: {temperature}')
st.write(f'Wind Direction: {wind_direction}')
st.write(f'Wind Speed: {wind_speed}')
st.write(f'Sky Cover: {sky_cover}')
st.write(f'Visibility: {visibility}')
st.write(f'Humidity: {humidity}')
st.write(f'Average Wind Speed (Period): {average_wind_speed_period}')
st.write(f'Average Pressure (Period): {average_pressure_period}')

# Prediction button
if st.button('Predict Power Generated', key='predict_button'):
    # Create a DataFrame for the input features, in the same order as trained
    input_data = pd.DataFrame([[distance_to_solar_noon, temperature, wind_direction, wind_speed, sky_cover, visibility, humidity, average_wind_speed_period, average_pressure_period]],
                              columns=['distance-to-solar-noon', 'temperature', 'wind-direction', 'wind-speed', 'sky-cover', 'visibility', 'humidity', 'average-wind-speed-(period)', 'average-pressure-(period)'])

    # Scale the input features using the loaded StandardScaler
    # The scaler object is named 'scaler' in cell e3370b08
    scaled_input_array = SS.transform(input_data)
    scaled_input = pd.DataFrame(scaled_input_array, columns=X.columns)

    # Make prediction using the trained Gradient Boosting model
    predicted_power = gb_model.predict(scaled_input)

    st.success(f'Predicted Power Generated: {predicted_power[0]:.2f} Joules')


# %%
