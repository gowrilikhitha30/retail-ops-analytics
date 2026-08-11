import pandas as pd
import numpy as np
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

print("\n--- EXECUTIVE OPERATIONS SUMMARY ---")
summary = df.groupby('Category').agg(
    Total_Orders=('OrderID', 'count'),
    On_Time_Deliveries=('DeliveryStatus', lambda x: (x == 'On-Time').sum()),
    Total_Returns=('ReturnRequested', lambda x: (x == 'Yes').sum())
).reset_index()

summary['On_Time_Delivery_Rate_%'] = ((summary['On_Time_Deliveries'] / summary['Total_Orders']) * 100).round(2)
summary['Return_Rate_%'] = ((summary['Total_Returns'] / summary['Total_Orders']) * 100).round(2)

print(summary[['Category', 'Total_Orders', 'On_Time_Delivery_Rate_%', 'Return_Rate_%']].to_string(index=False))
