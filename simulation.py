import numpy as np
import pandas as pd

class SelectionSimulator:
    def __init__(self, num_candidates=100):
        self.num_candidates = num_candidates
        # Generate static skill scores (92-100 range for tight competition)
        self.skill_scores = np.random.normal(96, 1, num_candidates)
        # Clip scores to ensure they're between 92 and 100
        self.skill_scores = np.clip(self.skill_scores, 92, 100)
        # Create candidate IDs
        self.candidates = [f"Candidate-{i+1}" for i in range(num_candidates)]
        
    def generate_luck_scores(self):
        # Generate random luck scores (0-100)
        return np.random.uniform(0, 100, self.num_candidates)
    
    def run_simulation(self):
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

    def get_skill_scores_df(self):
        return pd.DataFrame({
            'Candidate': self.candidates,
            'Skill Score': self.skill_scores
        })
