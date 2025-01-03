import pandas as pd

# Load the cleaned data
data_scaled = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/cleaned_stock_data.csv")

# Print rows with NaN values in the Price column
nan_rows = data_scaled[data_scaled['Price'].isna()]
print(nan_rows)