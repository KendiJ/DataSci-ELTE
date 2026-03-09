import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


true_mean = 75.0
true_std = 10.0


sample_data = np.random.normal(loc=true_mean, scale=true_std, size=5000)
mean = np.mean(sample_data)
std = np.std(sample_data)

print(f"Estimated std: {std}")
print(f"Estimated mean: {mean}")

estimated_mean, estimated_std = norm.fit(sample_data)

print("\n--- ESTIMATED PARAMETERS ---")
print(f"Estimated Mean (Expected Value): {estimated_mean:.2f} (True was {true_mean})")
print(f"Estimated Standard Deviation:    {estimated_std:.2f} (True was {true_std})")


plt.figure(figsize=(8, 5))


plt.hist(sample_data, bins=30, density=True, alpha=0.5, color='mediumpurple', edgecolor='black', label='Raw Data')


x = np.linspace(40, 110, 1000)
y_pdf = norm.pdf(x, loc=estimated_mean, scale=estimated_std)

plt.plot(x, y_pdf, 'k-', lw=2, label=f'Fitted Normal Curve\n$\mu={estimated_mean:.1f}, \sigma={estimated_std:.1f}$')

plt.title("Normal Distribution: Data vs. Estimated Fit")
plt.xlabel("Value")
plt.ylabel("Frequency (Density)")
plt.legend()
plt.show()