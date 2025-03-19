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

        # Calculate consistency metrics
        consistent_top10 = selection_freq[selection_freq >= total_simulations * 0.8].count()
        avg_appearances = selection_freq.mean()

        st.markdown(f"""
        ### Selection Consistency
        - Candidates appearing in >80% of simulations: **{consistent_top10}**
        - Average times a candidate appears: **{avg_appearances:.1f}**
        - Probability of same exact top 10: Very low due to luck factor
        """)

    # Show how many times the simulation has been run
    st.markdown(f"**Total simulations run:** {len(st.session_state.simulation_history)}")

# Reset button
if st.button("Reset Simulation"):
    st.warning("This will generate new fixed skill scores for all candidates")
    st.session_state.simulator = SelectionSimulator()
    st.session_state.simulation_history = []
    st.rerun()