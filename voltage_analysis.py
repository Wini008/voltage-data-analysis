import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Load the data into a DataFrame
df = pd.read_csv(
    r"C:\Users\Tejaswini\OneDrive\Desktop\Greencell Assign-Tejaswini\data\Sample_Data.csv"
)

# Convert Timestamp column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True)

# Show first few rows (proof of import)
print(df.head())


# Plot Voltage vs Timestamp 

plt.figure(figsize=(12, 5))
plt.plot(df['Timestamp'], df['Values'], label='Voltage')
plt.xlabel('Timestamp')
plt.ylabel('Voltage')
plt.title('Voltage vs Time')
plt.legend()
plt.show()


#Create 5-point moving average and plot

df['MA_5'] = df['Values'].rolling(window=5).mean()

plt.figure(figsize=(12, 5))
plt.plot(df['Timestamp'], df['Values'], label='Voltage', alpha=0.5)
plt.plot(df['Timestamp'], df['MA_5'], label='5-point Moving Average')
plt.xlabel('Timestamp')
plt.ylabel('Voltage')
plt.title('Voltage with 5-point Moving Average')
plt.legend()
plt.show()


# Find local peaks and lows

peaks, _ = find_peaks(df['Values'])
lows, _ = find_peaks(-df['Values'])

peaks_df = df.iloc[peaks][['Timestamp', 'Values']]
lows_df = df.iloc[lows][['Timestamp', 'Values']]

print("\nLocal Peaks:")
print(peaks_df.head())

print("\nLocal Lows:")
print(lows_df.head())


#  Find instances where Voltage < 20

below_20 = df[df['Values'] < 20][['Timestamp', 'Values']]

print("\nVoltage below 20:")
print(below_20)


# BONUS: Find downward slope acceleration


# First derivative (slope)
df['slope'] = df['Values'].diff()

# Second derivative (acceleration)
df['acceleration'] = df['slope'].diff()

# Downward acceleration: slope < 0 AND acceleration < 0
downward_accel = df[(df['slope'] < 0) & (df['acceleration'] < 0)]

print("\nDownward slope acceleration points:")
print(downward_accel[['Timestamp', 'Values']].head())
