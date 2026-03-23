import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes()
X_full = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

features = ['bmi', 'bp', 's5', 's6']
results = []

fig, axes = plt.subplots(1, 4, figsize=(20, 5))

for i, f in enumerate(features):
    X = X_full[[f]]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    train_rmse = np.sqrt(mean_squared_error(y_train, y_pred_train))
    test_rmse = np.sqrt(mean_squared_error(y_test, y_pred_test))
    r2 = r2_score(y_test, y_pred_test)
    
    results.append([f, train_rmse, test_rmse, r2])
    
    axes[i].scatter(X_test, y_test)
    axes[i].plot(X_test, y_pred_test)
    axes[i].set_title(f"{f} | R²: {r2:.3f}")
    axes[i].set_xlabel(f)
    axes[i].set_ylabel("Target")

plt.tight_layout()
plt.show()

df_results = pd.DataFrame(results, columns=["Feature", "Train RMSE", "Test RMSE", "Test R2"])
df_results = df_results.sort_values(by="Test RMSE")

print(df_results)