import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Set page title
st.title("Selection Simulation Demo")

# Add a basic counter to test state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Display basic interactive elements
st.write("Testing basic functionality")

if st.button("Increment Counter"):
    st.session_state.counter += 1

st.write(f"Counter value: {st.session_state.counter}")

# Test data visualization
test_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

st.write("Test Plot")
st.plotly_chart(px.scatter(test_data, x='x', y='y'))