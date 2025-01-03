import pandas as pd

# Load the raw data
data = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/raw_stock_data.csv")

# Print the first few rows of the raw data
print("First few rows of raw data:")
print(data.head())

# Print the summary statistics of the Price column
print("\nSummary statistics of the Price column:")
print(data['Price'].describe())

# Check for NaN values in the Price column
nan_rows = data[data['Price'].isna()]
print("\nRows with NaN values in the Price column:")
print(nan_rows)