import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Sidebar for user input
st.sidebar.header("User Input")

def get_user_input():
    num = st.sidebar.number_input("Select a number", value=10, min_value=0)
    return num

# Get user input
user_number = get_user_input()

# Create a DataFrame based on user input
data = pd.DataFrame({
    'Numbers': np.arange(1, user_number + 1),
    'Squares': np.square(np.arange(1, user_number + 1))
})

# Display DataFrame in main area
st.subheader("Data Preview")
st.write(data)

# Plotting the data
st.subheader("Plot of Numbers and Squares")
st.line_chart(data.set_index('Numbers'))