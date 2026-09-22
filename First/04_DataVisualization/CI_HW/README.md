# Confidence Interval Calculator

**Course:** Introduction to Data Science  
**By:** Kendi  

## Overview
This module calculates the Confidence Interval (CI) for a given sample dataset. Before applying the mathematical formulas, the script utilizes `scipy.stats.probplot` to generate a probability plot. This visual check ensures our assumption of Normality holds true, which is a prerequisite for these specific CI methods.

## Methodological Breakdown

To find the most computationally efficient and statistically sound approach, I exploited three different methods to calculate the 95% Confidence Interval:

### 1. The Manual Formula Calculation
* **Logic:** I explicitly coded the formula $\bar{x} \pm Z \frac{s}{\sqrt{n}}$. I used `norm.ppf` to fetch the exact Z-score corresponding to the confidence level.
* **Pros:** Demonstrates a fundamental understanding of the underlying mathematics.
* **Cons:** Prone to typos, requires manual calculation of the Standard Error.

### 2. The `scipy.stats.norm.interval` Method
* **Logic:** This is the optimized, built-in function for calculating the interval using the Z-distribution.
* **Pros:** Extremely lightweight and fast. The best choice for large datasets ($n \ge 30$) where the Central Limit Theorem heavily applies.

### 3. The `scipy.stats.t.interval` Method (Student's T-Distribution)
* **Logic:** This method uses the T-distribution, which accounts for the Degrees of Freedom ($n-1$). 
* **Pros:** This is universally the safest and most robust method. If the sample size is small ($n < 30$), the Z-distribution is too narrow and assumes we know the population variance. The T-distribution artificially widens the interval to account for the uncertainty of a small sample. As $n$ approaches infinity, the T-distribution naturally becomes identical to the Z-distribution.

## Conclusion & Recommendation
While all three methods yield almost identical results for large datasets, **Method 3 (`scipy.stats.t.interval`)** is the optimal, most robust choice for a generalized function, as it safely handles both large and critically small sample sizes without failing or providing over-confident estimates.