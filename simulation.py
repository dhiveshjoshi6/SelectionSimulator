# Pre-startup verification
print("Debug: Testing simulation imports...")
try:
    import numpy as np
    import pandas as pd
    print("Debug: Simulation imports successful")
except Exception as e:
    print(f"Debug: Simulation import error - {str(e)}")
    raise

class SelectionSimulator:
    def __init__(self, num_candidates=100):
        try:
            print("Debug: Initializing SelectionSimulator")
            self.num_candidates = num_candidates
            # Generate static skill scores (92-100 range for tight competition)
            # These scores remain fixed for each candidate throughout all simulations
            self.skill_scores = np.random.normal(96, 1, num_candidates)
            # Clip scores to ensure they're between 92 and 100
            self.skill_scores = np.clip(self.skill_scores, 92, 100)
            # Create candidate IDs
            self.candidates = [f"Candidate-{i+1}" for i in range(num_candidates)]
            print("Debug: SelectionSimulator initialized successfully")
        except Exception as e:
            print(f"Debug: Error in SelectionSimulator initialization: {str(e)}")
            raise

    def generate_luck_scores(self):
        try:
            # Generate new random luck scores (0-100) for each simulation run
            # These scores change with every simulation
            return np.random.uniform(0, 100, self.num_candidates)
        except Exception as e:
            print(f"Debug: Error generating luck scores: {str(e)}")
            raise

    def run_simulation(self):
        try:
            # Generate new luck scores for this simulation run
            luck_scores = self.generate_luck_scores()

            # Calculate weighted scores (95% skill, 5% luck)
            total_scores = (0.95 * self.skill_scores) + (0.05 * luck_scores)

            # Create DataFrame with all scores
            df = pd.DataFrame({
                'Candidate': self.candidates,
                'Skill Score': self.skill_scores,
                'Luck Score': luck_scores,
                'Total Score': total_scores
            })

            # Sort by total score and get top 10
            return df.sort_values('Total Score', ascending=False).reset_index(drop=True)
        except Exception as e:
            print(f"Debug: Error in run_simulation: {str(e)}")
            raise

    def get_skill_scores_df(self):
        try:
            return pd.DataFrame({
                'Candidate': self.candidates,
                'Skill Score': self.skill_scores
            })
        except Exception as e:
            print(f"Debug: Error in get_skill_scores_df: {str(e)}")
            raise