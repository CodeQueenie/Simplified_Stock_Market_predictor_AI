import pandas as pd

# Load the cleaned data
data_scaled = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/cleaned_stock_data.csv")

# Handle NaN values by filling them with the mean of the Price column
data_scaled = data_scaled.assign(Price=data_scaled['Price'].fillna(data_scaled['Price'].mean()))

# Save the updated data
data_scaled.to_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/cleaned_stock_data.csv", index=False)
print("Updated cleaned data saved with NaN values filled with the mean.")