import pandas as pd
import numpy as np
from datetime import datetime

def clean_sales_data(file_path):
    """
    Clean and prepare sales data for analysis
    """
    # Read the dataset
    df = pd.read_csv(file_path)
    
    # Convert dates
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])
    
    # Clean numeric columns
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
    df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
    
    # Calculate profit margins
    df['ProfitMargin'] = (df['Profit'] / df['Sales'] * 100).round(2)
    
    # Handle missing values
    df = df.fillna(0)
    
    return df

if __name__ == "__main__":
    df = clean_sales_data('data/raw/sales_data.csv')
    df.to_csv('data/processed/cleaned_sales.csv', index=False)
    print("Data cleaning completed successfully!")
