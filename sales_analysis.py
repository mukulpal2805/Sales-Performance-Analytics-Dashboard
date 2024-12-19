import pandas as pd
import numpy as np

def analyze_sales(df):
    """
    Perform sales analysis and calculate KPIs
    """
    # Monthly sales analysis
    monthly_sales = df.groupby(df['OrderDate'].dt.strftime('%Y-%m')).agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Quantity': 'sum',
        'OrderID': 'count'
    }).round(2)
    
    # Product category performance
    category_performance = df.groupby('Category').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'ProfitMargin': 'mean'
    }).round(2)
    
    # Calculate KPIs
    kpis = {
        'total_sales': df['Sales'].sum(),
        'total_profit': df['Profit'].sum(),
        'avg_order_value': (df['Sales'] / df['OrderID'].nunique()).round(2),
        'profit_margin': (df['Profit'].sum() / df['Sales'].sum() * 100).round(2)
    }
    
    return monthly_sales, category_performance, kpis

if __name__ == "__main__":
    # Load cleaned data
    df = pd.read_csv('data/processed/cleaned_sales.csv')
    
    # Perform analysis
    monthly, category, kpis = analyze_sales(df)
    
    # Save results
    monthly.to_csv('data/processed/monthly_sales.csv')
    category.to_csv('data/processed/category_performance.csv')
    
    print("\nAnalysis Results:")
    print(f"Total Sales: ${kpis['total_sales']:,.2f}")
    print(f"Total Profit: ${kpis['total_profit']:,.2f}")
    print(f"Average Order Value: ${kpis['avg_order_value']:,.2f}")
    print(f"Overall Profit Margin: {kpis['profit_margin']}%")
