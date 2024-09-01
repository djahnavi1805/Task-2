# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:\\Users\\Hariharan\\OneDrive\\data.csv')

# Print column names to check for 'MSRP' and 'Engine HP'
print("Columns in the dataset:", df.columns)

# Data cleaning and preprocessing
# Drop rows with missing values
df = df.dropna()

if 'Engine HP' in df.columns and 'MSRP' in df.columns:
    df['Engine HP'] = pd.to_numeric(df['Engine HP'], errors='coerce')
    df['MSRP'] = pd.to_numeric(df['MSRP'], errors='coerce')
else:
    print("Columns 'Engine HP' or 'MSRP' not found in the dataset.")

# Drop rows with NaN values after conversion
df = df.dropna(subset=['Engine HP', 'MSRP'])

# Basic information
print(df.info())
print(df.head())

# Number of instances of each class
print(df['Make'].value_counts())
numeric_df = df.select_dtypes(include=[np.number])

# Scatter plot: MSRP vs. Engine HP
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Engine HP', y='MSRP', data=df)
plt.title('MSRP vs. Engine HP')
plt.xlabel('Engine HP')
plt.ylabel('MSRP')
plt.show()

#The scatter plot titled “MSRP vs. Engine HP” shows the relationship between a car’s engine horsepower (HP) and its manufacturer’s suggested retail price (MSRP). Most data points are clustered at the lower end of both axes, indicating that cars with lower horsepower tend to have lower prices. As engine horsepower increases, MSRP also tends to increase, but higher-powered cars are less common. This suggests a positive correlation between engine HP and MSRP, meaning that more powerful cars generally cost more.


