import pandas as pd
import numpy as np

def calculate_performance_metrics(df):
    """
    Calculate detailed performance metrics
    """
    # Sales by region
    regional_sales = df.groupby('Region').agg({
        'Sales': ['sum', 'mean', 'count'],
        'Profit': ['sum', 'mean'],
        'Quantity': 'sum'
    }).round(2)
    
    # Top performing products
    product_performance = df.groupby('ProductName').agg({
        'Sales': 'sum',
        'Quantity': 'sum',
        'ProfitMargin': 'mean'
    }).sort_values('Sales', ascending=False).head(10)
    
    # Generate summary
    return regional_sales, product_performance

if __name__ == "__main__":
    df = pd.read_csv('data/processed/cleaned_sales.csv')
    regional, products = calculate_performance_metrics(df)
    
    # Save results
    regional.to_csv('data/processed/regional_performance.csv')
    products.to_csv('data/processed/top_products.csv')
