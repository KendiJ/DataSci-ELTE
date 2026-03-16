from sklearn.datasets import load_diabetes
import pandas as pd
from scipy.stats import pearsonr

# 1. Load the data
diabetes_ds = load_diabetes()
df = pd.DataFrame(diabetes_ds.data, columns=diabetes_ds.feature_names)
y = diabetes_ds.target  # Extract the target variable

# 2. The specific features you identified
features_to_check = ['bmi', 'bp', 's5', 's6']

print("--- Pearson Correlation with Disease Progression (y) ---")

# 3. The precise loop you requested
for _key in features_to_check:
    # Safety check to ensure we don't correlate y with itself if it was in the list
    if _key != "y": 
        # Calculate Pearson correlation (returns the r-score and the p-value)
        corr_score, p_value = pearsonr(df[_key], y)
        
        # Print the results neatly aligned
        print(f"Feature: {_key:>4} | Pearson r: {corr_score:.4f} | p-value: {p_value:.4e}")