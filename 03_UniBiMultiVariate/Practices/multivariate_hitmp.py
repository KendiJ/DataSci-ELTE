import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
years_exp = np.random.randint(1, 11, 100)
salary = years_exp * 10000 + np.random.normal(0, 5000, 100)
age = years_exp + 22 + np.random.normal(0, 2, 100)
random_metric = np.random.rand(100) * 100

df = pd.DataFrame({
    'Years_Eperience': years_exp,
    'Salary': salary,
    'Age': age,
    'Random_Metric': random_metric
})

missing_indicies = np.random.choice(df.index, size=10, replace=False)
df.loc[missing_indicies, 'Salary'] = np.nan

df['Salary'] = df['Salary'].fillna(df['Salary'].median())

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

corr_matrix = df_scaled.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Multivariate Correlation Heatmap")
plt.tight_layout()
plt.show()