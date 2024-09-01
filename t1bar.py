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

# Bar graph: Number of cars by make
plt.figure(figsize=(12, 6))
df['Make'].value_counts().plot(kind='bar')
plt.title('Number of Cars by Make')
plt.xlabel('Make')
plt.ylabel('Count')
plt.show()

#The bar graph titled “Number of Cars by Make” shows the distribution of cars across different manufacturers. Ford has the highest count, with nearly 600 cars, indicating its market dominance. Other manufacturers like Chevrolet, Volkswagen, and Toyota follow, but with significantly fewer cars. This graph highlights the varying market presence of different car brands, with Ford leading by a substantial margin.

