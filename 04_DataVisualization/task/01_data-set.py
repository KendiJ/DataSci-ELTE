# import numpy as np
# import matplotlib.pyplot as plt

# from scipy.stats import uniform

# continuous_vector = np.random.uniform(low=0.0, high=10.0, size=1000)
# print("First 5 continuous values:", continuous_vector[:5])

# discrete_vector = np.random.randint(low=1, high=7, size=1000)

# print("First 5 discrete values:", discrete_vector[:5])

# plt.hist(continuous_vector, bins=20, color='skyblue', edgecolor='black')
# plt.title("Histogram of Continuous Uniform Distribution")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()

from scipy.stats import uniform

data1 = uniform.rvs(loc=0.0, scale=10.0, size=1000)

print(data1[:5])