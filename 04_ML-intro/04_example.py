from sklearn.datasets import load_diabetes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

# 1. Load the data
diabetes_ds = load_diabetes()
df = pd.DataFrame(diabetes_ds.data, columns=diabetes_ds.feature_names)
y = diabetes_ds.target

# 2. Features to check
features_to_check = ['bmi', 'bp', 's5', 's6']

# Lists to store the scores for our plot later
pearson_scores = []
spearman_scores = []

print("--- Spearman Correlation with Disease Progression (y) ---")

# 3. The Loop
for _key in features_to_check:
    if _key != "y":
        # Calculate both to compare
        p_corr, _ = pearsonr(df[_key], y)
        s_corr, s_p_value = spearmanr(df[_key], y)
        
        # Save scores for plotting
        pearson_scores.append(p_corr)
        spearman_scores.append(s_corr)
        
        # Print Spearman results
        print(f"Feature: {_key:>4} | Spearman r: {s_corr:.4f} | p-value: {s_p_value:.4e}")

# ==========================================
# 4. Plotting the Comparison with PyPlot
# ==========================================
# Setup the X-axis positions
x = np.arange(len(features_to_check))
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(8, 6))

# Draw the two sets of bars
ax.bar(x - width/2, pearson_scores, width, label='Pearson (Linear)', color='skyblue', edgecolor='black')
ax.bar(x + width/2, spearman_scores, width, label='Spearman (Ranked)', color='coral', edgecolor='black')

# Formatting the plot
ax.set_ylabel('Correlation Score')
ax.set_title('Pearson vs. Spearman Correlation\n(Detecting Non-Linear Relationships)', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(features_to_check)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of the bars for exact reading
for i in range(len(features_to_check)):
    ax.text(x[i] - width/2, pearson_scores[i] + 0.01, f'{pearson_scores[i]:.2f}', ha='center', fontsize=9)
    ax.text(x[i] + width/2, spearman_scores[i] + 0.01, f'{spearman_scores[i]:.2f}', ha='center', fontsize=9)

plt.tight_layout()
plt.show()