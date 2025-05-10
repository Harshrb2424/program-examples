import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('product_sales_data.csv')

# Preprocessing
df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' to datetime
df['Day_of_Year'] = df['Date'].dt.dayofyear

# Predictive analytics
X = df[['Price', 'Advertising_Budget', 'Day_of_Year']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Building the model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Visualization
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Sales')
plt.ylabel('Predicted Sales')
plt.title('Actual vs Predicted Sales')
plt.show()

# Outputting model performance
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
