import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

np.random.seed(42)
X = np.linspace(0, 100, 100)
Y = 3 * X + 5 + np.random.normal(0, 15, 100)

cov_matrix = np.cov(X, Y)
pearson_corr, _ = pearsonr(X, Y)

print(f"Covariance (Hard to interpret): {cov_matrix[0,1]:.2f}")
print(f"Pearson Correlation (Before Outlier): {pearson_corr:.4f}")

X_outlier = np.append(X, [10000])
Y_outlear = np.append(Y, [10000])

pearson_outlier, _ = pearsonr(X_outlier, Y_outlear)
print(f"Pearson Correlation (After Outlier): {pearson_outlier:.4f}")

plt.scatter(X_outlier, Y_outlear)
plt.show()