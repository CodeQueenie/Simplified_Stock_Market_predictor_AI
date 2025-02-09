import pandas as pd

def fix_headers(input_file, output_file):
    """
    Fixes the headers in the stock market dataset.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    try:
        # Load data
        data = pd.read_csv(input_file)
        print("Data loaded successfully.")
        
        # Fix headers (example: renaming columns)
        data.columns = ["price", "close", "high", "low", "open", "volume"]
        print("Headers fixed.")
        
        # Save the fixed data to the specific path
        data.to_csv(output_file, index=False)
        print(f"Fixed data saved to {output_file}")

    except Exception as e:
        print(f"Error fixing headers: {str(e)}")  # Ensure error message is a string

# Specify the input and output file paths
input_file = "C:/Projects/Simplified_Stock_Market_Predictor_AI/Sandbox/test_stock_data.csv"
output_file = "C:/Projects/Simplified_Stock_Market_Predictor_AI/Sandbox/fixed_test_stock_data.csv"

# Fix the headers
fix_headers(input_file, output_file)

# Generated by Nicole LeGuern