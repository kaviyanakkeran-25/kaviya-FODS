import pandas as pd

# Read stock data
data = pd.read_csv("stock_data.csv")  # CSV must have 'Date' and 'Close' columns

# Calculate variability
mean_price = data['Close'].mean()
std_dev = data['Close'].std()
price_range = data['Close'].max() - data['Close'].min()

print("Mean Closing Price:", mean_price)
print("Standard Deviation:", std_dev)
print("Price Range:", price_range)
