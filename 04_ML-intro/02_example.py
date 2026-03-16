import pandas as pd
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, scr

# 1. Load the data
diabetes_ds = load_diabetes()
df = pd.DataFrame(diabetes_ds.data, columns=diabetes_ds.feature_names)
df["y"] = diabetes_ds.target

# 2. Set up the Matplotlib Figure (2 rows, 5 columns to hold exactly 10 plots)
fig, axes = plt.subplots(nrows=2, ncols=5, figsize=(20, 8))
axes = axes.flatten() # Flattens the 2x5 grid into a simple 1D list so we can loop through it easily

# 3. Loop through all 10 features
for i, feature in enumerate(diabetes_ds.feature_names):
    x = df[feature]
    y = df['y']
    
    # Calculate the Pearson correlation between the feature and the target
    correlation, p_value = pearsonr(x, y)
    
    # Draw the scatter plot on the current subplot
    axes[i].scatter(x, y, alpha=0.5, color='royalblue', edgecolor='w')
    
    # Add titles and labels so we know what we are looking at
    axes[i].set_title(f"Feature: {feature}\nCorrelation: {correlation:.2f}", fontweight='bold')
    axes[i].set_xlabel(f"{feature} (Normalized)")
    axes[i].set_ylabel("Disease Progression (y)")
    axes[i].grid(True, linestyle='--', alpha=0.6)

# 4. Clean up the layout and show the plots
plt.tight_layout()
plt.show()