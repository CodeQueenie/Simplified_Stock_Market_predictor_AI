# Simplified Stock Market Predictor AI

## Overview
Simplified Stock Market Predictor AI is a project that uses machine learning techniques to forecast stock prices based on historical data. The goal is to demonstrate various machine learning techniques, such as data cleaning, feature extraction, model development, prediction evaluation, and visualization.

## Project Structure
```
Simplified_Stock_Market_Predictor_AI
├── Code
│   ├── check_nan.py
│   ├── data_cleaning.py
│   ├── download_data.py
│   ├── feature_extraction.py
│   ├── fix_headers.py
│   ├── handle_nan_values_updated.py
│   ├── handle_nan_values.py
│   ├── inspect_csv.py
│   ├── inspect_raw_data.py
│   ├── inspect_source_data.py
│   ├── inspect_stock_data.py
│   ├── model_development.py
│   ├── prediction_evaluation.py
│   ├── print_nan_rows.py
│   ├── residual_analysis.py
│   ├── verify_cleaned_data.py
│   └── visualization.py
├── Data
│   ├── cleaned_stock_data.csv
│   ├── featured_stock_data.csv
│   └── stock_data.csv
├── Documentation
│   └── report.md
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/CodeQueenie/Simplified_Stock_Market_predictor_AI.git
   ```

2. **Navigate to the project directory**:
   ```sh
   cd Simplified_Stock_Market_Predictor_AI
   ```

3. **Create a conda environment**:
   ```sh
   conda create --name stock_predictor_ai python=3.8
   ```

4. **Activate the environment**:
   ```sh
   conda activate stock_predictor_ai
   ```

5. **Install required packages**:
   ```sh
   conda install pandas numpy matplotlib seaborn scikit-learn
   ```

## Usage Guidelines

1. **Fix Headers**: Run `fix_headers.py` to correct the headers in the stock market dataset.
   ```sh
   python Code/fix_headers.py
   ```

2. **Data Cleaning**: Run `data_cleaning.py` to preprocess the stock market dataset.
   ```sh
   python Code/data_cleaning.py
   ```

3. **Feature Extraction**: Execute `feature_extraction.py` to calculate technical indicators.
   ```sh
   python Code/feature_extraction.py
   ```

4. **Model Development**: Use `model_development.py` to train the machine learning model and perform feature importance analysis.
   ```sh
   python Code/model_development.py
   ```

5. **Prediction Evaluation**: Run `prediction_evaluation.py` to make predictions and evaluate model performance.
   ```sh
   python Code/prediction_evaluation.py
   ```

6. **Residual Analysis**: Execute `residual_analysis.py` to perform residual analysis.
   ```sh
   python Code/residual_analysis.py
   ```

7. **Visualization**: Execute `visualization.py` to visualize the actual vs. predicted stock prices.
   ```sh
   python Code/visualization.py
   ```

## License
This project is licensed under the MIT License.