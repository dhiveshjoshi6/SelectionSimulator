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
This simulation demonstrates how luck can affect outcomes even when skill differences are minimal:
- Each candidate has a **fixed skill score** (92-100 range) that doesn't change between runs
- A **random luck score** (0-100) is generated for each candidate in every new simulation
- Final score: 95% skill + 5% luck

Try running the simulation multiple times to see how luck can change the outcomes!
""")

# Display static skill scores
st.subheader("Fixed Skill Distribution")
st.info("These skill scores remain constant across all simulation runs")
skill_df = st.session_state.simulator.get_skill_scores_df()
fig_skill = px.histogram(skill_df, x="Skill Score", 
                        title="Distribution of Static Skill Scores (92-100 range)",
                        nbins=20)
st.plotly_chart(fig_skill)

# Run simulation button
if st.button("Run New Simulation"):
    results = st.session_state.simulator.run_simulation()
    st.session_state.simulation_history.append(results.head(10)['Candidate'].tolist())

    # Display current simulation results
    st.subheader("Current Simulation Results (Top 10)")
    st.info("Notice how rankings can change between runs due to random luck scores")
    st.dataframe(results.head(10))

    # Show score distribution
    st.subheader("Score Relationships")
    fig_total = px.scatter(results, x="Skill Score", y="Luck Score", 
                          color="Total Score",
                          title="Skill vs Luck Scores (Latest Simulation)",
                          hover_data=["Candidate"])
    st.plotly_chart(fig_total)

    # Show how many times the simulation has been run
    st.markdown(f"**Total simulations run:** {len(st.session_state.simulation_history)}")

# Reset button
if st.button("Reset Simulation"):
    st.warning("This will generate new fixed skill scores for all candidates")
    st.session_state.simulator = SelectionSimulator()
    st.session_state.simulation_history = []
    st.rerun()