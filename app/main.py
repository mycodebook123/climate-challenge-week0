import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data

st.set_page_config(page_title="African Climate Dashboard", layout="wide")
st.title("🌍 African Climate Dashboard")

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filters")

# 1. Country Selector
countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=df['Country'].unique())

# 2. Year Range Slider (The missing requirement!)
min_year = int(df['YEAR'].min())
max_year = int(df['YEAR'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# --- DATA FILTERING ---
# We filter by BOTH country and the selected year range
filtered_df = df[
    (df['Country'].isin(countries)) & 
    (df['YEAR'].between(year_range[0], year_range[1]))
]

# --- CHARTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Temperature Trends")
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    sns.lineplot(data=filtered_df, x='Date', y='T2M', hue='Country', ax=ax1)
    plt.xticks(rotation=45)
    st.pyplot(fig1)

with col2:
    st.subheader("Precipitation Distribution")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x='Country', y='PRECTOTCORR', hue='Country', ax=ax2)
    st.pyplot(fig2)