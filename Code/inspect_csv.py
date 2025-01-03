import pandas as pd

def inspect_csv(input_path):
    """
    Inspects the CSV file to understand the structure.

    Parameters:
    input_path (str): The path to the input CSV file.
    """
    try:
        # Load the CSV file without skipping rows
        data = pd.read_csv(input_path, header=None)
        
        print("First few rows of the data:")
        print(data.head())
        
        # Print the number of columns
        print("\nNumber of columns:", len(data.columns))
        
        # Print the columns for further analysis
        print("\nColumns in the data:")
        print(data.columns)
    except Exception as e:
        print(f"Error inspecting CSV: {e}")

# Define the input path
input_path = "C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/stock_data.csv"

# Inspect the CSV file
inspect_csv(input_path)