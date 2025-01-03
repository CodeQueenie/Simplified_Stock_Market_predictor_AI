import pandas as pd

def calculate_sma(data, window):
    """
    Calculates the Simple Moving Average (SMA) for the given data.

    Args:
        data (pd.DataFrame): DataFrame containing stock market data.
        window (int): Window size for calculating SMA.
    """
    return data["Close"].rolling(window=window).mean()

def calculate_rsi(data, window):
    """
    Calculates the Relative Strength Index (RSI) for the given data.

    Args:
        data (pd.DataFrame): DataFrame containing stock market data.
        window (int): Window size for calculating RSI.
    """
    delta = data["Close"].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window).mean()
    avg_loss = loss.rolling(window).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def extract_features(input_file, output_file):
    """
    Extracts technical indicators from the stock market data.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
    """
    try:
        # Load data
        data = pd.read_csv(input_file)

        # Calculate technical indicators
        data["SMA"] = calculate_sma(data, 20)
        data["RSI"] = calculate_rsi(data, 14)

        # Save data with features
        data.to_csv(output_file, index=False)
        print(f"Data with features saved to {output_file}")
    except Exception as e:
        print(f"Error extracting features: {e}")

if __name__ == "__main__":
    extract_features("../Data/cleaned_stock_data.csv", "../Data/featured_stock_data.csv")

# Generated by Nicole LeGuern.