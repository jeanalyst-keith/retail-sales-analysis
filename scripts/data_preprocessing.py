import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Load and clean the retail sales dataset."""
    df = pd.read_csv(file_path)
    
    # Basic cleaning
    df = df.drop_duplicates()
    df = df.dropna()
    
    # Convert date column
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Feature Engineering
    df['Month'] = df['Date'].dt.month
    df['Day_of_Week'] = df['Date'].dt.day_name()
    df['Revenue'] = df['Quantity'] * df['Price per Unit']
    df['Age_Group'] = pd.cut(df['Age'], bins=[0, 25, 35, 50, 100], 
                             labels=['18-25', '26-35', '36-50', '51+'])
    
    print(f"Dataset shape: {df.shape}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    return df

if __name__ == "__main__":
    df = load_and_clean_data('data/raw/retail_sales_dataset.csv')
    df.to_csv('data/processed/cleaned_sales.csv', index=False)
    print("✅ Data cleaned and saved to data/processed/cleaned_sales.csv")
    print(df.head())
