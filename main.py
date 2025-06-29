import streamlit as st
import pandas as pd
from EDA import run_EDA
from Description import run_Description
from app import run_PREDICTION

st.set_page_config(page_title="Smart Nutrition Planner", layout="wide")

st.sidebar.title("📌 Navigation")
choice = st.sidebar.radio("Go to", ["📘 Description", "📊 EDA", "🤖 Prediction"])

if choice == "📘 Description":
    run_DESCRIPTION()

elif choice == "📊 EDA":
    df = pd.read_csv("fitness_data.csv")
    run_EDA(df)

elif choice == "🤖 Prediction":
    run_PREDICTION()

