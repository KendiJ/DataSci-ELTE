import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

true_min = 15.0
true_max = 85.0
true_scale = true_max - true_min  


sample_data = uniform.rvs(loc=true_min, scale=true_scale, size=5000)


estimated_loc, estimated_scale = uniform.fit(sample_data)


estimated_min = estimated_loc
estimated_max = estimated_loc + estimated_scale


print("--- ACTUAL VALUES ---")
print(f"Actual Min: {true_min}")
print(f"Actual Max: {true_max}")

print("\n--- ESTIMATED VALUES FROM .fit() ---")
print(f"Estimated Min: {estimated_min:.4f}")
print(f"Estimated Max: {estimated_max:.4f}")


plt.figure(figsize=(8, 5))

plt.hist(sample_data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black', label='Sample Data')


x = np.linspace(0, 100, 1000)
y_estimated = uniform.pdf(x, loc=estimated_loc, scale=estimated_scale)
plt.plot(x, y_estimated, 'r-', lw=3, label='Estimated Uniform Fit')

plt.title("Recovering Parameters with uniform.fit()")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()