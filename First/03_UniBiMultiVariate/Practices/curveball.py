import numpy as np
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt

X = np.arange(1, 51)
Y = np.exp(X / 10)

pearson_corr, _  =  pearsonr(X, Y)
spearman_corr, _ = spearmanr(X, Y)

print(f"Pearson (Measures exact linear fit): {pearson_corr:.4f}")
print(f"Spearman (Measures ranked order): {spearman_corr:.4f}")

plt.plot(X, Y, 'o')
plt.show()