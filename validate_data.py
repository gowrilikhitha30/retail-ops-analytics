import pandas as pd
import sys

def run_data_audit():
    print("🔍 INITIATING SUPPLY CHAIN DATA AUDIT...")
    try:
        df = pd.read_csv('retail_operations_data.csv')
    except FileNotFoundError:
        print("❌ Audit Failed: Source data file 'retail_operations_data.csv' missing. Run app.py first.")
        sys.exit(1)
        
    # Check 1: Record Integrity
    assert len(df) == 1000, f"❌ Data Integrity Alert: Record count is {len(df)}, expected 1000."
    
    # Check 2: Financial Outliers & Integrity
    negative_sales = df[df['Sales'] < 0]
    assert len(negative_sales) == 0, f"❌ Financial Anomaly: Found {len(negative_sales)} records with negative revenue."
    
    # Check 3: Logical Status Mapping
    invalid_returns = df[(df['DeliveryStatus'] == 'Cancelled') & (df['ReturnRequested'] == 'Yes')]
    if len(invalid_returns) > 0:
        print(f"⚠️ Operational Warning: Found {len(invalid_returns)} records where cancelled orders requested returns.")
        
    print("✅ DATA INTEGRITY VERIFIED: All core logistics records conform to schema constraints.")

if __name__ == "__main__":
    run_data_audit()
