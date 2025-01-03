import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_model(X_train, y_train, model_type="linear_regression"):
    """
    Trains a machine learning model using the provided training data.

    Parameters:
    X_train (array-like): The input features for training.
    y_train (array-like): The target variable for training.
    model_type (str): The type of model to train ("linear_regression" or "decision_tree").

    Returns:
    model: The trained machine learning model.
    """
    from sklearn.linear_model import LinearRegression
    from sklearn.tree import DecisionTreeRegressor

    if model_type == "linear_regression":
        model = LinearRegression()
    elif model_type == "decision_tree":
        model = DecisionTreeRegressor()
    else:
        raise ValueError("Invalid model type. Choose 'linear_regression' or 'decision_tree'.")

    model.fit(X_train, y_train)
    return model

def predict(model, X_test):
    """
    Makes predictions using the trained model.

    Parameters:
    model: The trained machine learning model.
    X_test (array-like): The input features for prediction.

    Returns:
    array: The predicted values.
    """
    return model.predict(X_test)

def evaluate_model(y_true, y_pred):
    """
    Evaluates the performance of the model using Mean Absolute Error (MAE) and Mean Squared Error (MSE).

    Parameters:
    y_true (array-like): The true target values.
    y_pred (array-like): The predicted values.

    Returns:
    dict: A dictionary containing MAE and MSE.
    """
    from sklearn.metrics import mean_absolute_error, mean_squared_error

    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)

    return {"MAE": mae, "MSE": mse}

# Load the feature-extracted data
data = pd.read_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/featured_stock_data.csv")

# Define features and target
features = ['SMA', 'RSI', 'Volume']
target = 'Price'

X = data[features]
y = data[target]

# Diagnose NaN values in y
nan_rows = y[y.isna()]
print("Rows with NaN values in y:")
print(nan_rows)

# Handle NaN values by dropping rows with NaN values in both X and y
data_dropped = data.dropna(subset=features + [target])
X = data_dropped[features]
y = data_dropped[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = train_model(X_train, y_train, model_type="linear_regression")

# Make predictions
y_pred = predict(model, X_test)

# Save the predictions to a CSV file
predictions = pd.DataFrame({'Date': data.iloc[X_test.index].index, 'Predicted_Price': y_pred})
predictions.to_csv("C:/Projects/Simplified_Stock_Market_Predictor_AI/MarketMind-AI/Data/predictions.csv", index=False)

# Evaluate the model
evaluation_results = evaluate_model(y_test, y_pred)
print(f"Mean Absolute Error: {evaluation_results['MAE']}")
print(f"Mean Squared Error: {evaluation_results['MSE']}")