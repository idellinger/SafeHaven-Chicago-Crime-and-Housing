import streamlit as st
import pandas as pd
from pickle import load
import matplotlib.pyplot as plt
import numpy as np

st.title("Interactive Crime Map")

crime_map_data = pd.read_csv(r'C:\Data Science\chicago-crime-property-analysis\Israel\app\resources\data\map_data.csv')


st.map(data = crime_map_data, color='#da1919')