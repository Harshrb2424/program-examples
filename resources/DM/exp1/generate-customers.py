# generate-customers.py

import pandas as pd
import numpy as np

np.random.seed(42)
n_customers = 10000

customer_ids = [f'C{str(i).zfill(4)}' for i in range(1, n_customers + 1)]
names = [f'Name_{i}' for i in range(1, n_customers + 1)]
emails = [f'22Q91A66{i}@mrce.in' if np.random.rand() > 0.1 else '' for i in range(1, n_customers + 1)]
locations = np.random.choice([
    'Hyderabad', 'Medchal', 'Secunderabad', 'Warangal', 'Vijayawada',
    'Karimnagar', 'Nizamabad', 'Visakhapatnam', 'Kerala', 'Guntur'
], size=n_customers)

# Generate ages as FLOAT to allow NaN
ages = np.random.randint(16, 28, size=n_customers).astype(float)  # Now float
# Randomly set ~500 missing values
missing_age_indices = np.random.choice(n_customers, size=500, replace=False)
ages[missing_age_indices] = np.nan

# Build DataFrame
customers_df = pd.DataFrame({
    'Customer ID': customer_ids,
    'Name': names,
    'Email': emails,
    'Age': ages,  # Now float (can hold NaN)
    'Location': locations
})

# Replace empty email strings with NaN, then later we'll fill with 'unknown'
customers_df['Email'] = customers_df['Email'].replace('', pd.NA)

# Save to CSV
customers_df.to_csv('Customers.csv', index=False)
print("✅ Customers.csv created with 10,000 rows (including missing Age and Email).")