import streamlit as st
import pandas as pd
import numpy as np

raw_data = pd.read_csv("https://raw.githubusercontent.com/hadimaster65555/dataset_for_teaching/main/dataset/50_startups/50_Startups.csv")

st.title("Simple Streamlit Apps")

st.header("Showing Startup 50 Dataset")
st.dataframe(raw_data)
