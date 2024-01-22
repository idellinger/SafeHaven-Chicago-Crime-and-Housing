import streamlit as st
import pandas as pd
from pickle import load
import matplotlib.pyplot as plt
import numpy as np

st.title("Predictive Model")

model = pickle.load(open('','rb'))