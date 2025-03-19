I was watching this video by veritasium - https://youtu.be/3LopI4YeC4I?si=IAt5RrrRVYWESY9I. it was essentially about the role of skill vs luck in success. 
so, he suggested he ran simulation for the same. I took the idea and first thought how to make simple calculator for the same with data analytics. 
and, replit came handy. so in just 13 instruction it is ready.

Files details:
1. app.py:
Main Streamlit application file
Creates the web interface for the simulation
Handles the visualization of results using Plotly
Manages the simulation state and controls
Displays histograms, scatter plots, and statistics

2. simulation.py:
Contains the core SelectionSimulator class
Handles the logic for generating skill scores (92-100 range)
Manages luck scores (0-100 range)
Calculates final scores using the 95% skill + 5% luck formula
Provides methods for running simulations and getting results

3. .pyproject.toml:
Python project configuration file
Lists project dependencies:
numpy: for numerical operations
pandas: for data manipulation
plotly: for interactive visualizations
streamlit: for the web interface
twilio: for notifications (though not currently used)

4. .streamlit/config.toml:
Streamlit configuration file
Sets up the server to run on port 5000
Configures server address to 0.0.0.0 for external access
Disables CORS and XSRF protection for development

5. .replit:
Replit-specific configuration file
Defines how the project runs in Replit
Sets up the run button and workflows
Configures deployment settings
Maps port 5000 to external port 80

6. replit.nix:
Nix package configuration for Replit
Specifies system-level dependencies
Sets up locale settings

7. uv.lock:
Lock file for Python package dependencies
Ensures consistent package versions across installations
This project is a simulation system that demonstrates how a small luck factor (5%) can influence outcomes in competitive scenarios where candidates have similar high skill levels (92-100 range).

Assistant mode




Formula used : Final Score = (0.95 × Skill Score) + (0.05 × Luck Score) where during each iteration skill score is kept constant and luck score is generated randomly. 
based on variation caused by luck score which accounts to only 5% of overall score the top 10 changes heavily. despite skill score kept constant which is 95% of overall score.
