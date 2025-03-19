import streamlit as st

print("Debug: Starting minimal Streamlit app")

st.set_page_config(
    page_title="Selection Simulation",
    layout="wide"
)

st.title("Selection Simulation")
st.write("Basic test to verify server functionality")

if st.button("Test Button"):
    st.success("Button clicked!")