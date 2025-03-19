import streamlit as st
import plotly.express as px
import pandas as pd
from simulation import SelectionSimulator

# Page configuration
st.set_page_config(
    page_title="Selection Simulation",
    layout="wide"
)

# Initialize session state
if 'simulator' not in st.session_state:
    st.session_state.simulator = SelectionSimulator()
    st.session_state.simulation_history = []

st.title("Selection Simulation: Impact of Luck")

st.markdown("""
This simulation demonstrates how a small luck component (5%) can affect selection outcomes
even when skill differences are minimal. The simulation uses:
- 95% weight for skill scores
- 5% weight for luck scores
- 100 candidates competing for 10 positions
""")

# Display static skill scores
st.subheader("Static Skill Distribution")
skill_df = st.session_state.simulator.get_skill_scores_df()
fig_skill = px.histogram(skill_df, x="Skill Score", 
                        title="Distribution of Skill Scores",
                        nbins=20)
st.plotly_chart(fig_skill)

# Run simulation button
if st.button("Run New Simulation"):
    results = st.session_state.simulator.run_simulation()
    st.session_state.simulation_history.append(results.head(10)['Candidate'].tolist())

    # Display current simulation results
    st.subheader("Current Simulation Results (Top 10)")
    st.dataframe(results.head(10))

    # Show score distribution
    fig_total = px.scatter(results, x="Skill Score", y="Luck Score", 
                          color="Total Score",
                          title="Score Distribution",
                          hover_data=["Candidate"])
    st.plotly_chart(fig_total)

# Reset button
if st.button("Reset Simulation"):
    st.session_state.simulator = SelectionSimulator()
    st.session_state.simulation_history = []
    st.rerun()