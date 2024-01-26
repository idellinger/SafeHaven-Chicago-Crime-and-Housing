import streamlit as st
import pandas as pd
from pickle import load
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Real eState", layout = "wide", page_icon = "🏡", initial_sidebar_state="expanded")


developers_markdown = """
Seth Kulow ([GitHub](https://github.com/Skcodingacademy))\n
Israel Dellinger ([GitHub](https://github.com/idellinger))\n 
Rashid Baset ([GitHub](https://github.com/rbaset5))\n
"""
st.sidebar.title("Developers")
st.sidebar.info(developers_markdown)
st.title("Real eState:")
st.subheader("A predictive model for neighborhood safety", divider="grey")

# Home page #
@st.cache_data # Cached the DataFrame so it only has to load once
def load_data_head(filepath):
    df = pd.read_csv(filepath)
    return df
df = load_data_head(r'C:\Data Science\chicago-crime-property-analysis\Israel\app\resources\data\df_head.csv')

intro_markdown = """
Using publicly accessable data from the City of Chicago and Zillow (via HomeHarvest), we developed machine learning models to demonstrate the relationships between neighborhoods, housing, and crime.
"""
st.write(intro_markdown)


with st.expander("City of Chicago Crime Database"):
    st.dataframe(df)

# Images on the Home page #
tab1, tab2, tab3 = st.tabs(["Days on Market","Kernel Density Plot","Correlation Heatmap"]) # Image tabs

with tab1:
    st.header("Average days on market by neighborhood")
    st.image("./resources/images/daysonmarket.png")

with tab2:
    st.header("Relationship beween Crime and Property value")
    st.image("./resources/images/KDE.png")

with tab3:
    st.header("Heatmap of feature correlation")
    st.image("./resources/images/Heatmap.png")

st.button("Rerun") # Reloads the page to check if cache is working