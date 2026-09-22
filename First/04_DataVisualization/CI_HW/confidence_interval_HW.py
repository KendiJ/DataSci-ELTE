# need a function which will generate / calculates the confidence interval. Any method is acceptable.
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t, probplot


# 1. Simple Data

# simulating weight of 50 elements
np.random.seed(42)
sample_data = np.random.normal(loc=150.0, scale=15.0, size=50)

# the prob plot (Q-Q Plot) to make sure the data is Norma before any CI
plt.figure(figsize=(6, 4))
probplot(sample_data, dist="norm", plot=plt)
plt.title("Prob Plot")
plt.tight_layout()
plt.show()


# 2. Confidence Interval fun
confidence_level = 0.95
n = len(sample_data)
sample_mean = np.mean(sample_data)
sample_std = np.std(sample_data, ddof=1)
standard_error = sample_std / np.sqrt(n)


# Method 1: Manual Maths way
def ci_manual(mean, std_err, conf_level):
    alpha = 1 - conf_level
    z_score = norm.ppf(1 - alpha / 2)
    margin_of_error = z_score * std_err
    return mean - margin_of_error, mean + margin_of_error

# Method 2: Z-Distrib way 
def ci_z_distrib(mean, std_err, conf_level):
    return norm.interval(confidence=conf_level, loc=mean, scale=std_err)

# Method 3: T-Distrib way
def ci_t_distrib(mean, std_err, n, conf_level):
    degrees_of_freedom = n - 1
    return t.interval(confidence=conf_level, df=degrees_of_freedom, loc=mean, scale=std_err)

print(f"Sample mean: {sample_mean:.2f}")
print(f"-" * 40)

lower1, upper1 = ci_manual(sample_mean, standard_error, confidence_level)
print(f"M1(Manual Maths):    [{lower1:.2f}, {upper1:.2f}]")

lower2, upper2 = ci_z_distrib(sample_mean, standard_error, confidence_level)
print(f"M2(Z-Interval): [{lower2:.2f}, {upper2:.2f}]")

lower3, upper3 = ci_t_distrib(sample_mean, standard_error, n, confidence_level)
print(f"M3(T-Interval): [{lower3:.2f}, {upper3:.2f}]")