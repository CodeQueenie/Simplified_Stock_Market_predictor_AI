import pandas as pd

def fix_headers(input_path, output_path):
    """
    Fixes the headers of the CSV file.

    Parameters:
    input_path (str): The path to the input CSV file.
    output_path (str): The path to the output CSV file with fixed headers.
    """
    try:
        # Read the CSV file, skipping the first row with incorrect headers
        df = pd.read_csv(input_path, skiprows=1, header=None)

        # Define the correct headers without the 'Ticker' column
        headers = ["Date", "Price", "Close", "High", "Low", "Open", "Volume"]

        # Check the number of columns
        print(f"Number of columns in data: {len(df.columns)}")
        
        # Fix the headers and add the 'Ticker' column if the number of columns matches
        if len(df.columns) == len(headers):
            df.columns = headers
            # Insert 'Ticker' column
            df.insert(1, 'Ticker', 'AAPL')

            # Save the fixed CSV file
            df.to_csv(output_path, index=False)
            print(f"Headers fixed and saved to {output_path}")
        else:
            print(f"Header length mismatch: Expected {len(headers)}, but got {len(df.columns)}")
    except Exception as e:
        print(f"Error fixing headers: {e}")

# Define the input and output paths
input_path = "C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/stock_data.csv"
output_path = "C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/fixed_stock_data.csv"

# Fix the headers
fix_headers(input_path, output_path)