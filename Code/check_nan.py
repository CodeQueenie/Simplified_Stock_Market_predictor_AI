import pandas as pd

# Load the cleaned data using the absolute path
data_scaled = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/cleaned_stock_data.csv")

# Check for any remaining NaN values
nan_columns = data_scaled.columns[data_scaled.isna().any()].tolist()
if nan_columns:
    print(f"Columns with remaining NaN values: {nan_columns}")
    for col in nan_columns:
        print(f"Number of NaN values in {col}: {data_scaled[col].isna().sum()}")
else:
    print("No NaN values remaining in the cleaned data.")