import pandas as pd
import numpy as np
import json
import sqlite3
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def load_data(file_path, file_type):
    """
    Load data from various file types.
    
    Args:
        file_path (str): Path to the data file.
        file_type (str): Type of the data file ('csv', 'json', 'excel', 'database').

    Returns:
        pd.DataFrame: Loaded data.
    """
    if file_type == "csv":
        return pd.read_csv(file_path)
    elif file_type == "json":
        return pd.read_json(file_path)
    elif file_type == "excel":
        return pd.read_excel(file_path)
    elif file_type == "database":
        engine = create_engine(f"sqlite:///{file_path}")
        return pd.read_sql_table("data", con=engine)
    else:
        raise ValueError("Unsupported file type. Use 'csv', 'json', 'excel', or 'database'.")

def residual_analysis(y_true, y_pred):
    """
    Perform residual analysis and plot residuals distribution.
    
    Args:
        y_true (pd.Series): Actual values.
        y_pred (pd.Series): Predicted values.
    """
    residuals = y_true - y_pred
    mse = mean_squared_error(y_true, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True)
    plt.title("Residuals Distribution")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.show()

def main():
    """
    Main function to execute the residual analysis.
    """
    try:
        # Load data
        file_path = "c:/Projects/Simplified_Stock_Market_predictor_AI/data/stock_data.csv"  # Update with your data file path
        file_type = "csv"  # Update with your data file type
        data = load_data(file_path, file_type)
        
        # Assuming the data has columns 'actual' and 'predicted'
        y_true = data["actual"]
        y_pred = data["predicted"]
        
        # Perform residual analysis
        residual_analysis(y_true, y_pred)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

# Generated by Nicole LeGuern