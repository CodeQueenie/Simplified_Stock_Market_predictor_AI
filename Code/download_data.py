import yfinance as yf
import pandas as pd
import os

def download_stock_data(ticker, start_date, end_date, output_file):
    """
    Downloads historical stock data from Yahoo Finance and saves it to a CSV file.

    Args:
        ticker (str): Stock ticker symbol.
        start_date (str): Start date in the format 'YYYY-MM-DD'.
        end_date (str): End date in the format 'YYYY-MM-DD'.
        output_file (str): Path to the output CSV file.
    """
    try:
        print(f"Current working directory: {os.getcwd()}")
        full_output_path = os.path.abspath(output_file)
        print(f"Full path to output file: {full_output_path}")

        stock_data = yf.download(ticker, start=start_date, end=end_date)
        stock_data.to_csv(full_output_path)
        print(f"Data for {ticker} saved to {full_output_path}")
    except Exception as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    download_stock_data("AAPL", "2018-01-01", "2023-01-01", "MarketMind-AI/Data/stock_data.csv")

# Generated by Nicole LeGuern.