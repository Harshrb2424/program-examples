import pandas as pd

customers = pd.read_csv("Customers.csv")
transactions = pd.read_csv("Transactions.csv")

print(customers.head())
print(transactions.head())


## *Step 2: Data Cleaning*

### a) Handle Missing Values

# Check for missing values
print(customers.isnull().sum())
print(transactions.isnull().sum())


# Fill missing emails with 'unknown'
customers['Email'].fillna('unknown', inplace=True)

# Drop transactions with missing amount
transactions.dropna(subset=['Amount'], inplace=True)


### b) Remove Duplicates

customers.drop_duplicates(inplace=True)
transactions.drop_duplicates(inplace=True)


### c) Data Type Corrections

transactions['Date'] = pd.to_datetime(transactions['Date'])
transactions['Amount'] = transactions['Amount'].astype(float)

## *Step 3: Data Transformation (Normalization)*

### Normalize the transaction amount using Min-Max Scaling:


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
transactions['Amount_Normalized'] = scaler.fit_transform(transactions[['Amount']])


## *Step 4: Data Integration*

### Merge datasets on Customer ID:


merged_data = pd.merge(transactions, customers, on='Customer ID', how='inner')
print(merged_data.head())


## *Step 5: Save Cleaned and Integrated Data*

merged_data.to_csv("Cleaned_Integrated_Data.csv", index=False)