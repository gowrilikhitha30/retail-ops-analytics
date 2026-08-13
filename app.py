import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta

# 1. Generate Synthetic Retail Operations Data
np.random.seed(42)
num_orders = 1000
start_date = datetime(2026, 1, 1)
date_list = [start_date + timedelta(days=int(np.random.randint(0, 90))) for _ in range(num_orders)]

data = {
    'OrderID': [f"ORD-{10000+i}" for i in range(num_orders)],
    'OrderDate': date_list,
    'Category': np.random.choice(['Electronics', 'Apparel', 'Home', 'Books'], num_orders, p=[0.3, 0.3, 0.2, 0.2]),
    'Sales': np.random.uniform(10.0, 500.0, num_orders).round(2),
    'Quantity': np.random.randint(1, 5, num_orders),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], num_orders),
    'DeliveryStatus': np.random.choice(['On-Time', 'Delayed', 'Cancelled'], num_orders, p=[0.85, 0.10, 0.05]),
    'ReturnRequested': np.random.choice(['Yes', 'No'], num_orders, p=[0.08, 0.92])
}

df = pd.DataFrame(data)
df.to_csv('retail_operations_data.csv', index=False)
print("✅ Success: 'retail_operations_data.csv' created with 1,000 operational records!")

# 2. Relational Database Integration via SQLite
print("\n🗄️ Initializing Local Relational Database Engine...")
conn = sqlite3.connect(':memory:')  # Creates an in-memory SQL database
df.to_sql('orders', conn, index=False, if_exists='replace')

# 3. Read and Execute queries.sql File Natively
try:
    with open('queries.sql', 'r') as f:
        sql_script = f.read()
    
    # Split queries by semicolon to execute sequentially
    queries = [q.strip() for q in sql_script.split(';') if q.strip()]
    
    print("\n--- RUNNING SQL METRICS EXTRACTION ENGINE ---")
    titles = [
        "1. EXECUTIVE METRICS BY PRODUCT CATEGORY",
        "2. REGIONAL SHIPPING EFFICIENCY & TRAFFIC BOTTLENECKS",
        "3. DEEP DIVE: CRITICAL RETURN ANOMALIES"
    ]
    
    for i, query in enumerate(queries[:3]):
        print(f"\n🔹 Executing: {titles[i]}")
        result_df = pd.read_sql_query(query, conn)
        print(result_df.to_string(index=False))
        
except FileNotFoundError:
    print("⚠️ Warning: 'queries.sql' file not found locally. Skipping direct SQL execution test.")

conn.close()
