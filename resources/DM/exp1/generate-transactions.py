# generate-transactions.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_transactions = 50000

# Recreate customer IDs (must match Customers.csv)
n_customers = 10000
customer_ids = [f'C{str(i).zfill(4)}' for i in range(1, n_customers + 1)]

# Generate transaction data
transaction_ids = [f'T{str(i).zfill(5)}' for i in range(1, n_transactions + 1)]
customer_choices = np.random.choice(customer_ids, size=n_transactions)

start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
date_range = (end_date - start_date).days
dates = [
    (start_date + timedelta(days=np.random.randint(0, date_range))).strftime('%Y-%m-%d')
    for _ in range(n_transactions)
]

# Randomly set some dates to empty string (simulate missing)
mask_missing_dates = np.random.rand(n_transactions) < 0.05  # 5% missing
dates = ["" if missing else date for missing, date in zip(mask_missing_dates, dates)]

# Amounts: 5% missing (set to NaN)
amounts = np.random.uniform(10, 1000, size=n_transactions)
mask_missing_amounts = np.random.rand(n_transactions) < 0.05
amounts[mask_missing_amounts] = np.nan

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam',
            'Headphones', 'Speaker', 'Desk', 'Chair', 'Cable']
product_names = np.random.choice(products, size=n_transactions)

# Create DataFrame
transactions_df = pd.DataFrame({
    'Transaction ID': transaction_ids,
    'Customer ID': customer_choices,
    'Date': dates,
    'Amount': amounts,
    'Product': product_names
}

# Save to CSV
transactions_df.to_csv('Transactions.csv', index=False)
print("✅ Transactions.csv created with 50,000 rows (with missing Date and Amount).")