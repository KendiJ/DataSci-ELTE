# Practical Assignment: Probability & Distributions Simulations

**Course:** Introduction to Data Science  
**Student:** Kendi J (C5CDDZ)

## Overview
This repository contains Python simulations exploring foundational probability concepts and statistical distributions discussed in our lectures. The script uses `numpy`, `matplotlib`, and `scipy.stats` to empirically demonstrate uniform distributions, normal distributions, permutations, combinations, and formal statistical hypothesis testing.

## Code Breakdown & My Understanding

### 1. Binary Output, Uniform Distribution (Coin Toss)
In this section, I simulated a simple coin toss. Since a fair coin has two outcomes with equal probabilities, it follows a discrete uniform distribution. 
* **The Code:** I used a list comprehension to simulate 1,000 tosses. To visualize the Law of Large Numbers, I ran this 1,000-toss simulation 30 separate times. 
* **The Result:** The plotted line shows the probability of getting Heads constantly hovering around the $0.50$ mark, proving the theoretical probability empirically.

### 2. 6-Class Output, Uniform Distribution (Die Roll)
Similar to the coin toss, a fair 6-sided die follows a uniform distribution where each outcome ($1$ through $6$) has a $1/6$ probability. 
* **The Code:** I simulated 1,000 die rolls and calculated the probability of rolling an odd number (which theoretically should be $0.50$). 
* **The Result:** The generated histogram displays 6 bins of roughly equal height, which is the visual signature of a uniform distribution.

### 3. Permutations and Combinations
This section translates the mathematical formulas for arrangements into code using the `math.factorial` function.
* **Permutations ($nPr$):** Used when the order of the outcomes *does* matter.
* **Combinations ($nCr$):** Used when the order of the outcomes *does not* matter.

### 4. Normal Distribution
I used `np.random.normal(0, 1, 1000)` to generate 1,000 continuous data points. The parameters $0$ and $1$ define a Standard Normal (Gaussian) Distribution with a mean ($\mu$) of $0$ and a standard deviation ($\sigma$) of $1$. The resulting histogram perfectly visualizes the classic "bell curve" shape.

## Homework Solution: Normality Testing
The homework required testing whether the `die_results` and `data` variables follow a normal distribution. 

**Methodology:** To solve this, I utilized the **Shapiro-Wilk Test** (`scipy.stats.shapiro`), which we covered in Lecture 2. This test evaluates the null hypothesis that the data was drawn from a normal distribution. A $p$-value $> 0.05$ indicates we fail to reject the null hypothesis (meaning the data appears normal).

**Results:**
1. **`die_results`:** The Shapiro-Wilk test returned a $p$-value significantly less than $0.05$. Therefore, I rejected the null hypothesis. This aligns perfectly with the theory, as the die rolls follow a *Uniform* distribution, not a Normal one.
2. **`data`:** The test returned a $p$-value greater than $0.05$. Therefore, I failed to reject the null hypothesis, confirming that the `data` variable is indeed normally distributed (which makes sense, as it was explicitly generated using `np.random.normal`).