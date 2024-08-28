import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace with your actual file path)
file_path = r'C:\Users\Hariharan\OneDrive\AirPassengers.csv'
df = pd.read_csv(file_path, parse_dates=["Month"], index_col="#Passengers")

# Create a line plot
plt.figure(figsize=(10, 6))
plt.plot(df["Month"], df.index, label="#Passengers")  # Swap x and y
plt.xlabel("Year")  # Reflect X and Y axes
plt.ylabel("Number of Passengers")  # Reflect X and Y axes
plt.title("Air Passenger Counts (1949-1960)")
plt.grid(True)
plt.legend()
plt.show()

