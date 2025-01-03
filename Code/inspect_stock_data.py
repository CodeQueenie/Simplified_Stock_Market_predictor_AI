import pandas as pd

# Load the stock data
data = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/stock_data.csv")

# Print the first few rows of the data
print("First few rows of stock data:")
print(data.head())

# Print the columns to see if 'Date' and 'Ticker' exist
print("\nColumns in the data:")
print(data.columns)