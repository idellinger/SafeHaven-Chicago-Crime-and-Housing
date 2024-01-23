import streamlit as st
import pandas as pd
from pickle import load
import matplotlib.pyplot as plt
import numpy as np
import joblib

st.title("Predictive Model")

model = joblib.load(r'C:\Data Science\chicago-crime-property-analysis\Israel\app\nb_modelneb.sav','r')
st.title("CrimePredict")

NB_file_path = r'C:\Data Science\chicago-crime-property-analysis\Israel\app\neighborhoods.txt'
year_built_file_path = r'C:\Data Science\chicago-crime-property-analysis\Israel\app\year_built.txt'

# Getting the neighborhood feature into a form that works as model input #
neighborhoods = pd.read_csv(NB_file_path, header=None)
neighborhoods = neighborhoods.rename(columns={0: 'Neighborhood'})
neighborhoods = neighborhoods.drop(columns=1)

neighborhood_select = pd.DataFrame({'Neighborhood': neighborhoods['Neighborhood']})

# Getting the year built feature into a form that works as model input #
year_built_data = pd.read_csv(year_built_file_path, header=None)
year_built_data = year_built_data.rename(columns={0: 'YearBuilt'})
year_built_data = year_built_data.drop(columns=1)

year_built_select = pd.DataFrame({'YearBuilt': year_built_data['YearBuilt']})

val1 = st.number_input("Longitude:")
val2 = st.number_input("Latitude:")
val3 = st.number_input("Year built:", min_value= 1700, step=1)
val4 = st.number_input("Sold price:", step=1)
val5 = st.selectbox("Neighborhood:",neighborhoods)

chosen_year_built = val3

year_built_select['YearBuilt'] = np.where(year_built_select['YearBuilt'] == 
                                               chosen_year_built, chosen_year_built, 0)

chosen_neighborhood = val5

neighborhood_select['Neighborhood'] = np.where(neighborhood_select['Neighborhood'] == chosen_neighborhood, 1, 0)
#neighborhood_select['Neighborhood'] = np.where(neighborhood_select['Neighborhood'] == 
                                               #chosen_neighborhood, chosen_neighborhood, 0)

if st.button("Predict"):
    feature_array = np.concatenate([
    np.array([[val1]]),       
    np.array([[val2]]),         
    year_built_select['YearBuilt'].values.reshape(1, -1),  # Add values from year_built_select
    np.array([[val4]]), 
    neighborhood_select['Neighborhood'].values.reshape(1, -1)  # Add values from neighborhood_select
], axis=1) 
    
    prediction = model.predict(feature_array)
    st.write("Predicted Crime count is:", prediction)


