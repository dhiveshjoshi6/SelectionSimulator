import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from simulation import SelectionSimulator

# Debug logging
st.write("Debug: Application initialization started")

# Initialize session state
if 'simulator' not in st.session_state:
    st.session_state.simulator = SelectionSimulator()
    st.session_state.simulation_history = []
    st.write("Debug: Session state initialized")

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

# Analysis of multiple simulations
if st.session_state.simulation_history:
    st.subheader("Multiple Simulation Analysis")
    
    # Calculate selection frequencies
    all_selections = [item for sublist in st.session_state.simulation_history for item in sublist]
    selection_freq = pd.Series(all_selections).value_counts()
    
    # Display selection statistics
    total_simulations = len(st.session_state.simulation_history)
    st.markdown(f"**Total Simulations Run:** {total_simulations}")
    
    # Show selection frequency
    st.markdown("### Selection Frequency")
    fig_freq = px.bar(selection_freq, 
                      title="Number of Times Each Candidate Was Selected",
                      labels={'index': 'Candidate', 'value': 'Times Selected'})
    st.plotly_chart(fig_freq)
    
    # Calculate and display interesting statistics
    most_selected = selection_freq.index[0]
    never_selected = len(set(st.session_state.simulator.candidates) - set(selection_freq.index))
    
    st.markdown(f"""
    ### Key Insights
    - Most frequently selected: **{most_selected}** ({selection_freq.iloc[0]} times)
    - Number of candidates never selected: **{never_selected}**
    - Selection variability shows the impact of the 5% luck factor
    """)

# Reset button
if st.button("Reset Simulation"):
    st.session_state.simulator = SelectionSimulator()
    st.session_state.simulation_history = []
    st.rerun()