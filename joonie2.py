import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load your time series data
file_path = r'C:\Users\Hariharan\OneDrive\AirPassengers.csv'
df = pd.read_csv(file_path, parse_dates=["Month"], index_col="Month")

# Ensure the data is numeric
df['#Passengers'] = pd.to_numeric(df['#Passengers'], errors='coerce')

# Perform seasonal decomposition
result = seasonal_decompose(df['#Passengers'], model="additive", period=12)

# Deseasonalize the time series
deseasonalized = df['#Passengers'] - result.seasonal

# Plot the deseasonalized time series
plt.figure(figsize=(10, 6))
plt.plot(deseasonalized, label="Deseasonalized")
plt.xlabel("Time")
plt.ylabel("Deseasonalized Values")
plt.title("Deseasonalized Time Series")
plt.grid(True)
plt.legend()
plt.show()
