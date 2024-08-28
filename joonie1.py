import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load your time series data (replace with your actual data)
# Example: df = pd.read_csv("your_time_series_data.csv", parse_dates=["Date"], index_col="Date")

# Perform seasonal decomposition
file_path = r'C:\Users\Hariharan\OneDrive\AirPassengers.csv'
df = pd.read_csv(file_path, parse_dates=["Month"], index_col="#Passengers")

result = seasonal_decompose(df["Month"], model="additive", period=12)  # Chosen "additive" decomposition

# Plot the components
plt.figure(figsize=(10, 6))
plt.subplot(411)
plt.plot(df.index, result.observed, label="Observed")
plt.legend()
plt.subplot(412)
plt.plot(df.index, result.trend, label="Trend")
plt.legend()
plt.subplot(413)
plt.plot(df.index, result.seasonal, label="Seasonal")
plt.legend()
plt.subplot(414)
plt.plot(df.index, result.resid, label="Residual")
plt.legend()
plt.tight_layout()
plt.show()
