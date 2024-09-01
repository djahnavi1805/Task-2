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

# Pair plot: Relationships between multiple features
sns.pairplot(df, vars=['Engine HP', 'MSRP', 'Engine Cylinders'])
plt.suptitle('Pair Plot of Engine HP, MSRP, and Engine Cylinders', y=1.02)
plt.show()

'''The image displays a series of scatter plots and histograms arranged in a 3x2 grid format, showing the relationships and distributions of ‘Engine HP’, ‘MSRP’, and ‘Engine Cylinders’.

Top Row:
The first plot is a histogram showing the frequency distribution of ‘Engine HP’, with most cars having lower horsepower.
The second plot is a scatter plot of ‘Engine HP’ vs. ‘MSRP’, indicating a positive correlation where higher horsepower generally corresponds to higher prices.
The third plot is a scatter plot of ‘Engine HP’ vs. ‘Engine Cylinders’, showing that cars with more cylinders tend to have higher horsepower.
Middle Row:
The first plot mirrors the second plot of the top row but with axes swapped.
The middle plot is a histogram showing the frequency distribution of ‘MSRP’, with most cars priced lower.
The last plot shows ‘MSRP’ vs. ‘Engine Cylinders’, indicating that cars with more cylinders tend to be more expensive.
Bottom Row:
The first plot mirrors the third plot of the top row but with axes swapped.
The final plot is a histogram showing the frequency distribution of ‘Engine Cylinders’, with most cars having fewer cylinders.
