import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


true_lambda = 4.0

sample_data = np.random.poisson(lam=true_lambda, size=5000)

print(f"First 10 minutes of API pings: {sample_data[:10]}")


estimated_lambda = np.mean(sample_data)

print("\n--- ESTIMATED PARAMETERS ---")
print(f"Estimated Lambda (Rate): {estimated_lambda:.4f} (True was {true_lambda})")


plt.figure(figsize=(8, 5))


bins = np.arange(0, max(sample_data) + 1.5) - 0.5
plt.hist(sample_data, bins=bins, density=True, alpha=0.5, color='lightgreen', edgecolor='black', label='Raw Data (Observed)')


x_values = np.arange(0, max(sample_data) + 1)
y_pmf = poisson.pmf(x_values, mu=estimated_lambda)

plt.plot(x_values, y_pmf, 'ko-', lw=2, markersize=8, label=f'Fitted Poisson PMF\n$\lambda={estimated_lambda:.2f}$')

plt.title("Poisson Distribution: Data vs. Estimated Fit")
plt.xlabel("Number of Events (e.g., API Pings per minute)")
plt.ylabel("Probability")
plt.xticks(x_values) 
plt.legend()
plt.show()