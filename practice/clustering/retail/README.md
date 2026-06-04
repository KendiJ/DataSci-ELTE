# Unsupervised Learning Blueprint: Clustering Retail Customer Profiles

This guide outlines the conceptual roadmap for detecting hidden customer segments within a raw, imperfect retail activity dataset. It emphasizes an end-to-end engineering mindset, ensuring data integrity, reproducibility, and business interpretability.

---

## Phase 1: Project Architecture & Reproducibility Setup
Before performing any data science, establish a clean development environment and an intuitive project structure. This prevents configuration errors and guarantees that another engineer can reproduce your results identically.

### 1. Environment and Folder Structure
Organize your workspace using a strict directory layout:
* `data/raw/` – Stores the immutable original dataset. Never overwrite these files.
* `data/interim/` – Holds data at intermediate cleaning stages.
* `data/processed/` – Stores the final analysis-ready and clustered outputs.
* `notebooks/` – For exploratory research and structured experimentation.
* `configs/` – For centralized hyperparameter and path management.
* `reports/figures/` & `reports/tables/` – For exporting visual assets and metrics.

### 2. Configuration Management
Create a centralized `config.json` file inside the `configs/` directory. Store parameters such as relative file paths, feature selection lists, scaling choices, PCA variance thresholds, the chosen random seed, and K-Means parameters. 

### 3. Setting the Deterministic Anchor
Fix a global random seed across all libraries that utilize stochastic (randomized) algorithms. In this workflow, a fixed seed ensures that the initialization of PCA components and K-Means centroids remains identical across different machine executions.

---

## Phase 2: Workflow, Data Audit, & Cleaning (Part A)
Raw corporate data is inherently noisy. The primary objective here is to systematically identify quality issues and standardize fields for numerical modeling.

### 1. The Initial Data Audit
Load the raw data using relative paths. Programmatically inspect the shape, column data types, missing value counts per feature, and duplicated row frequencies.

### 2. Strategic Cleaning Actions
Address at least four explicit data anomalies without mutating the raw file:
* **Currency Parsing:** Strip currency symbols (e.g., `$`) and commas from monetary text fields, converting them to floating-point numbers.
* **Percentage Conversion:** Parse percentage strings, stripping the `%` symbol and dividing by 100 to yield a clean decimal fraction.
* **Temporal Standardization:** Identify rows with mixed date formats in the signup column and parse them into a unified, clean datetime object.
* **Missing Values and Duplicates:** Drop or impute missing entries based on statistical relevance, and explicitly remove duplicated observations, resetting the dataframe index afterward.

### 3. Feature Engineering & Validation
* **Derived Feature Creation:** Build a new, business-focused metric from existing columns (e.g., dividing annual spend by visit frequency to calculate average spend per visit).
* **Defensive Checks:** Implement explicit verification rules (assertions or conditional tests) to ensure data logic holds true—such as confirming that no item quantities are negative and that dates fall within a valid historical range.
* **Pipeline Export:** Write out the partially cleaned data to the `interim/` folder and the final model-ready file to the `processed/` folder.

---

## Phase 3: Exploratory Data Analysis (Parts B & C)
Before modeling, use statistical and visual tools to understand individual distributions and multi-variable interactions.

### 1. Univariate Analysis Strategy
Select a primary feature of interest to analyze in isolation. 
* Calculate four key descriptive statistics: a measure of central tendency (mean or median), dispersion (variance or standard deviation), and distribution shape (skewness and kurtosis).
* Visualize the feature using a histogram or boxplot to identify skewness, modalities, or clear outliers.

### 2. Bivariate and Correlation Matrix Strategy
* **Targeted Pair Investigation:** Choose a pair of continuous variables with an expected behavioral relationship (e.g., customer satisfaction score vs. loyalty index). 
* Generate a scatter plot to visually assess linearity or clustering.
* Compute four metrics for the pair: Covariance (directional relationship), Pearson $r$ (linear correlation), Spearman $\rho$ (monotonic rank correlation), and the Coefficient of Determination ($R^2$) to evaluate variance explanation.
* **Multivariate Mapping:** Construct a global correlation matrix across all numerical attributes. Isolate the absolute strongest positive and absolute strongest negative correlation pairs to identify potential redundancies.
* **Robustness Verification:** Perform a quick validation check by recalculating your key correlation metrics after dropping outlier rows or changing your missing-value strategy. This checks whether your insights are stable or overly sensitive to a few anomalies.

---

## Phase 4: Feature Engineering & Dimensionality Reduction (Part D)
K-Means depends entirely on geometric distance calculations. If features are on different scales, variables with larger absolute values will distort the algorithm.

### 1. Feature Standardization
Apply a feature scaling pipeline to center the numerical variables around a mean of zero with a standard deviation of one. 

### 2. Principal Component Analysis (PCA)
* Fit PCA on the scaled feature matrix to project the data into an orthogonal space of uncorrelated components.
* Plot the cumulative explained variance ratio against the number of principal components.
* Determine the smallest number of dimensions required to preserve at least 85% of the data's original variance. 
* Evaluate if PCA is a necessary step before clustering for this specific dataset by analyzing whether it effectively compresses dense, highly correlated features down to a simpler set of components.

---

## Phase 5: K-Means Clustering Optimization (Part E)
With a clean, compressed feature space, run the unsupervised clustering engine to define distinct customer segments.

### 1. Hyperparameter Iteration
Execute the K-Means algorithm repeatedly across an array of cluster counts, typically iterating $k$ from 2 through 9. For every value of $k$, compute and log the following internal cluster quality metrics into a structured comparison table:
* **Cluster Size Distributions:** Check if any configurations yield empty, tiny, or single-sample clusters.
* **Silhouette Score:** Measures how well-separated the clusters are and how cohesive each cluster is internally.
* **Calinski-Harabasz Index:** Evaluates the ratio of between-cluster variance to within-cluster variance (higher is generally better).
* **Davies-Bouldin Index:** Measures the average similarity between each cluster and its most similar peer (lower signifies better separation).

### 2. Selection, Visualization, and Persona Profiling
* **Optimal $k$ Selection:** Choose the final cluster count by finding where the evaluation metrics align (e.g., peaks in Silhouette score, elbows in variance, and manageable cluster sizes). Update your central `config.json` with this choice.
* **Geometric Projection:** Visualize your final clusters by drawing a 2D scatter plot using the first two principal components from Phase 4, color-coding each data point by its assigned K-Means cluster label.
* **Centroid Profile Analysis:** Calculate the mean values of the original unscaled features across each cluster to construct a profile table. 
* **Operational Reflection:** Conclude the workflow by documenting the business utility of these clusters. Are these groups highly interpretable? Are they robust enough to drive personalized marketing strategies, or do they overlap too heavily to be actionable?