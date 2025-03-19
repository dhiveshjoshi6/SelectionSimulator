# Basic test to verify Streamlit functionality
import streamlit as st

st.title("Test Application")
st.write("If you can see this message, Streamlit is working correctly!")

# Add a simple button to test interactivity
if st.button("Click me"):
    st.write("Button clicked!")