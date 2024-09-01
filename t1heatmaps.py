# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('C:\\Users\\Hariharan\\OneDrive\\data.csv')

# Data cleaning and preprocessing
df = df.dropna()  # Alternatively, you can use df.fillna(df.mean()) or other methods

# Basic information
print(df.info())
print(df.head())

# Number of instances of each class
print(df['Make'].value_counts())

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Interpretations
'''This heatmap shows the correlation coefficients between various features of cars, such as ‘Year’, ‘Engine HP’, ‘Engine Cylinders’, ‘Number of Doors’, ‘highway MPG’, ‘city mpg’, ‘Popularity’, and ‘MSRP’. The color gradient ranges from dark blue (negative correlation) to dark red (positive correlation), with white representing no correlation.

Key Observations:
Engine HP and MSRP:
Correlation Coefficient: 0.81
Interpretation: There is a strong positive correlation between Engine HP and MSRP, indicating that cars with higher engine horsepower tend to have higher prices.
Engine Cylinders and Engine HP:
Correlation Coefficient: 0.81
Interpretation: There is a strong positive correlation between the number of engine cylinders and engine horsepower, suggesting that cars with more cylinders generally have higher horsepower.
Engine Cylinders and highway MPG:
Correlation Coefficient: -0.60
Interpretation: There is a strong negative correlation between the number of engine cylinders and highway MPG, indicating that cars with more cylinders tend to have lower fuel efficiency on the highway.
Engine Cylinders and city mpg:
Correlation Coefficient: -0.62
Interpretation: Similarly, there is a strong negative correlation between the number of engine cylinders and city mpg, suggesting that cars with more cylinders are less fuel-efficient in city driving.
highway MPG and city mpg:
Correlation Coefficient: 0.82
Interpretation: There is a strong positive correlation between highway MPG and city mpg, indicating that cars that are fuel-efficient on the highway are also fuel-efficient in the city.
Popularity and MSRP:
Correlation Coefficient: 0.13
Interpretation: There is a weak positive correlation between popularity and MSRP, suggesting that more popular cars tend to be slightly more expensive, but the relationship is not very strong.
Practical Insights:
Performance vs. Efficiency: The negative correlations between engine cylinders and both highway MPG and city mpg highlight the trade-off between performance (more cylinders, higher horsepower) and fuel efficiency.
Pricing Strategy: The strong positive correlation between Engine HP and MSRP can inform pricing strategies, emphasizing performance features for higher-priced models.
Fuel Efficiency: The strong positive correlation between highway MPG and city mpg suggests that improvements in fuel efficiency will likely benefit both city and highway driving.
By analyzing these correlations, you can gain valuable insights into the relationships between different features of cars, which can inform decision-making in areas such as product development, marketing, and pricing strategies.


