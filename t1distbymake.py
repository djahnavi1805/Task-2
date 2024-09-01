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

# Box plot: MSRP distribution by make
plt.figure(figsize=(12, 6))
sns.boxplot(x='Make', y='MSRP', data=df)
plt.title('MSRP Distribution by Make')
plt.xlabel('Make')
plt.ylabel('MSRP')
plt.xticks(rotation=90)
plt.show()

#The box plot titled “MSRP Distribution by Make” shows the distribution of car prices for various manufacturers. Each box represents the interquartile range (IQR) of MSRP, with the line inside the box indicating the median price. Brands like Ferrari and Lamborghini have higher median prices and wider IQRs, indicating more variability in their prices. Outliers are shown as individual points beyond the whiskers, highlighting extreme values. This graph helps compare the price ranges and variability across different car makes.

