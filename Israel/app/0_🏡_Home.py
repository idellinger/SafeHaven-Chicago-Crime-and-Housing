import streamlit as st
import pandas as pd
from pickle import load
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Real eSafe", page_icon = "🏡", initial_sidebar_state="collapsed")

css_file_path = r"C:\Data Science\chicago-crime-property-analysis\Israel\app\style.css"

with open(css_file_path) as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.markdown("# Predictive Modeling for Neighborhood Safety")
st.markdown("Seth K, Rashid B, and Israel D")

# Home page #
@st.cache_data # Cached the DataFrame so it only has to load once
def load_data_head(filepath):
    df = pd.read_csv(filepath)
    return df
df = load_data_head(r'C:\Data Science\chicago-crime-property-analysis\Israel\app\resources\data\df_head.csv')
st.markdown("City of Chicago Crime Database")
st.dataframe(df)

# Images on the Home page #
tab1, tab2, tab3 = st.tabs(["Crime by Neighborhood","Kernel Density Plot","Correlation Heatmap"]) # Image tabs

with tab1:
    st.header("Breakdown of crime by neighborhood")
    st.image("./resources/images/CrimeNeighborhood.png")

with tab2:
    st.header("Relationship beween Crime and Property value")
    st.image("./resources/images/KDE.png")

with tab3:
    st.header("Heatmap of feature correlation")
    st.image("./resources/images/Heatmap.png")

st.button("Rerun") # Reloads the page to check if cache is working