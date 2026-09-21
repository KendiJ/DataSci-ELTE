import random
from matplotlib import pyplot as plt
import numpy as np

# coin toss
def flip_coin():
    return random.choice(['H', 'T'])

# coin toss many times
def simulate_coin_tosses(n):
    results = [flip_coin() for _ in range(n)] 
    return results

# Probs of getting heads
def probability_of_heads(results):
    heads_count = results.count('H')
    return heads_count / len(results)

# 1K coin tosses with uniform distrib
n_tosses = 1000
n_simulations = 30
_res = []

for i in range(n_simulations):
    _res.append(probability_of_heads(simulate_coin_tosses(n_tosses)))
    plt.plot(_res)
plt.show()

# simulate rolling a die
def roll_die():
    return random.randint(1, 6)

# roll die many times
def simulate_die_rolls(n):
    results = [roll_die() for _ in range(n)]
    return results

def probability_of_odd(results):
    odd_count = len([x for x in results if x % 2 != 0])
    return odd_count / len(results)

# simulate 1K die
n_rolls = 1000
die_results = simulate_die_rolls(n_rolls)
prob_odd = probability_of_odd(die_results)

plt.hist(die_results, bins=6)
plt.show()


from math import factorial

# calculate permutations (nPr)
def num_Permutation(n, r):
    return factorial(n) // factorial (n - r)

# calculate combinations (nCr)
def num_combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
n = 5
r = 3
perms = num_Permutation(n, r)
combs = num_combination(n, r)
print(f'The number of ways to arrange {r} items from {n} items is {perms} (permutations).')
print(f'The number of ways to choose {r} items from {n} items is {combs} (combination).')


# Normal Distribution
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Data")
plt.show()

# -------------------------
# HOMEWORK SOLUTION
# -------------------------
from scipy.stats import shapiro

stat_die, p_die = shapiro(die_results)

print(f"\n1. Variable 'die_results':")
print(f"  shapiro-Wilk Test p-value = {p_die:.5f}")

if p_die > 0.05:
    print("   Conclusion: The data looks Normal (Gaussian).")
else:
    print("   Conclusion: The data does not look normal")

stat_data, p_data = shapiro(data)
print(f"\n2. Variable 'data':")
print(f"   Shapiro-Wilk Test p-value = {p_data:.5f}")

if p_data > 0.05:
    print("   Conclusion: The data looks Normal (Gaussian).")
else:
    print("   Conclusion: The data does NOT look Normal.")
