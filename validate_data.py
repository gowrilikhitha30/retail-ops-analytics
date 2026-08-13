import pandas as pd
import sys

def run_data_audit():
    print("🔍 INITIATING SUPPLY CHAIN DATA AUDIT...")
    try:
        df = pd.read_csv('retail_operations_data.csv')
    except FileNotFoundError:
        print("❌ Audit Failed: Source data file 'retail_operations_data.csv' missing. Run app.py first.")
        sys.exit(1)
        
    # Assertion 1: Total Record Schema Integrity
    assert len(df) == 1000, f"❌ Data Integrity Alert: Record count is {len(df)}, expected 1000."
    
    # Assertion 2: Financial Outliers & Revenue Integrity
    negative_sales = df[df['Sales'] < 0]
    assert len(negative_sales) == 0, f"❌ Financial Anomaly: Found {len(negative_sales)} records with negative revenue."
    
    # Flag 3: Log Logical Contradictions (Returns on Cancelled Orders)
    invalid_returns = df[(df['DeliveryStatus'] == 'Cancelled') & (df['ReturnRequested'] == 'Yes')]
    if len(invalid_returns) > 0:
        print(f"⚠️ OPERATIONAL WARNING: Found {len(invalid_returns)} records where cancelled orders requested returns. Flagging data anomaly for upstream audit.")
    else:
        print("✅ Order log status logic verified successfully.")
        
    print("✅ DATA INTEGRITY METRICS ASSIGNED: Data is clear for dashboard consumption.")

if __name__ == "__main__":
    run_data_audit()
