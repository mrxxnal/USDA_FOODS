import streamlit as st
import pandas as pd

# Title for your app
st.title("USDA Food Analysis")

try:
    # Load cleaned data
    data = pd.read_csv("data/cleaned_data.csv")

    # Display the data
    st.subheader("Dataset Preview")
    st.write(data)

    # Display the visualization
    st.subheader("Visualization: Calories in Ultra-Processed Foods")
    st.image("visuals/calories_plot.png", caption="Calories in Ultra-Processed Foods")
except FileNotFoundError as e:
    st.error("Error: Required files are missing. Please make sure the data and visualizations are generated.")
    st.text(str(e))