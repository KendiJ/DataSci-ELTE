# Simple Linear Regression – Diabetes Dataset

**Course:** Introduction to Data Science  
**Student:** Kendi  

## Overview
This project applies simple linear regression to predict diabetes progression using individual features: `bmi`, `bp`, `s5`, and `s6`. The goal is to compare how well each feature performs on its own.

## Method
- The dataset is split into 80% training and 20% testing data.
- A separate linear regression model is trained for each feature.
- Models are evaluated on the test set using:
  - RMSE (Root Mean Squared Error)
  - R² score (Coefficient of Determination)

## Results
Model performance ranked from best to worst:

1. `s5` – lowest RMSE and highest R²  
2. `bmi` – strong performance  
3. `bp` – moderate performance  
4. `s6` – weakest predictor  

## Conclusion
`s5` is the best single feature for predicting disease progression in this dataset. However, the relatively low R² scores indicate that a single feature is not sufficient, and combining multiple features would likely improve performance.