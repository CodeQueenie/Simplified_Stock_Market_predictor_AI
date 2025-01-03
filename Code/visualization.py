import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_predictions(actual, predicted):
    """
    Plots the actual vs. predicted stock prices.

    Parameters:
    actual (pd.Series): The actual stock prices.
    predicted (pd.Series): The predicted stock prices.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(actual.index, actual, label="Actual Prices", color="blue")
    plt.plot(predicted.index, predicted, label="Predicted Prices", color="orange")
    plt.title("Actual vs Predicted Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.grid()
    plt.show()

def plot_moving_average(data, window):
    """
    Plots the moving average of stock prices.

    Parameters:
    data (pd.Series): The stock prices.
    window (int): The window size for the moving average.
    """
    moving_avg = data.rolling(window=window).mean()
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data, label="Stock Prices", color="blue")
    plt.plot(moving_avg.index, moving_avg, label=f"{window}-Day Moving Average", color="red")
    plt.title(f"{window}-Day Moving Average of Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.legend()
    plt.grid()
    plt.show()

# Load the actual and predicted stock prices
data = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/featured_stock_data.csv")
predicted = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/predictions.csv")

# Assuming 'Date' is a column in the CSVs, set it as the index for plotting
data['Date'] = pd.to_datetime(data['Date'])
predicted['Date'] = pd.to_datetime(predicted['Date'])
data.set_index('Date', inplace=True)
predicted.set_index('Date', inplace=True)

# Call the plotting functions
plot_predictions(data['Price'], predicted['Predicted_Price'])
plot_moving_average(data['Price'], window=20)