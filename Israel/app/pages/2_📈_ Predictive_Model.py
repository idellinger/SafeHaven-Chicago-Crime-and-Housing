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

neighborhoods = pd.read_csv(NB_file_path, header=None)
neighborhoods = neighborhoods.rename(columns={0: 'Neighborhood'})
neighborhoods = neighborhoods.drop(columns=1)

neighborhood_select = pd.DataFrame({
    'Neighborhood': neighborhoods['Neighborhood'],
    'bool': 0
})
neighborhood_dict = neighborhoods.to_dict(orient='index')


val1 = st.number_input("Longitude:")
val2 = st.number_input("Latitude:")
val3 = st.number_input("Year built:", min_value= 1700, step=1)
val4 = st.number_input("Sold price:", step=1)
val5 = st.selectbox("Neighborhood:",neighborhoods)

"""if st.button("Predict"):
    inputs = 
    prediction = model.predict(inputs)
    st.write("Predicted Crime count is:", prediction)
"""

