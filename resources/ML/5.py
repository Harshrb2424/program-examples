# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load dataset
df = pd.read_csv('Real estate.csv')
df.drop('No', inplace=True, axis=1)

# Print dataset information
print(df.head())
print(df.columns)

# Visualize data with a scatterplot
sns.scatterplot(x='X4 number of convenience stores', y='Y house price of unit area', data=df)

# Prepare feature variables
X = df.drop('Y house price of unit area', axis=1)
y = df['Y house price of unit area']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
print('Mean Squared Error:', mean_squared_error(y_test, predictions))
print('Mean Absolute Error:', mean_absolute_error(y_test, predictions))