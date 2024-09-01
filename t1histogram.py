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

# Histogram: Distribution of Engine HP
plt.figure(figsize=(10, 6))
sns.histplot(df['Engine HP'], bins=30, kde=True)
plt.title('Distribution of Engine HP')
plt.xlabel('Engine HP')
plt.ylabel('Frequency')
plt.show()

#The histogram titled “Distribution of Engine HP” shows the frequency of cars with different engine horsepower (HP). Most cars have engine horsepower in the range of 100 to 200 HP, as indicated by the peak in the histogram. The frequency decreases significantly as horsepower increases, with very few cars having horsepower above 600 HP. This distribution suggests that lower horsepower engines are more common in the dataset.

