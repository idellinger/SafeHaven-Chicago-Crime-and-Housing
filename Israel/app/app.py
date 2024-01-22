import streamlit as st

st.set_page_config(page_title="Real eSafe",initial_sidebar_state="collapsed")

css_file_path = r"C:\Data Science\chicago-crime-property-analysis\Israel\app\style.css"

with open(css_file_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown("# Predictive Modeling for Neighborhood Safety")
st.markdown("Seth K, Rashid B, and Israel D")
import pandas as pd
from pickle import load
import matplotlib.pyplot as plt
import numpy as np

# Frontpage #
@st.cache_data
def load_data_head(filepath):
    df = pd.read_csv(filepath)
    return df
df = load_data_head(r'C:\Data Science\chicago-crime-property-analysis\Israel\app\resources\data\df_head.csv')
st.write("City of Chicago Crime Database")
st.dataframe(df)

st.sidebar.markdown('## Pages go here')

st.button("Rerun") # Reloads the page to check if cache is working