# from sklearn.datasets import load_diabetes

# import pandas as pd

# if __name__ == '__main__':
#     diabetes_ds = load_diabetes
#     df = pd.DataFrame(diabetes_ds.data, columns=diabetes_ds.feature_names)
#     df["y"] = diabetes_ds.target
#     print(df.head())

from sklearn.datasets import load_diabetes
import pandas as pd

# Set Pandas to display all columns
pd.set_option('display.max_columns', None)
# Optional: Set the width of the display so it doesn't wrap awkwardly
pd.set_option('display.width', 1000)

if __name__ == '__main__':
    # Add () to actually call the function and load the data
    diabetes_ds = load_diabetes() 
    
    # Create the DataFrame
    df = pd.DataFrame(diabetes_ds.data, columns=diabetes_ds.feature_names)
    
    # Add the target variable 'y'
    df["y"] = diabetes_ds.target
    
    # Print the first 5 rows
    print(df.head())