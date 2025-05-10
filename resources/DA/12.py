import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data from CSV and parse Date column
df = pd.read_csv('weather_data.csv', parse_dates=['Date'])

# Preprocessing
df['Day_of_Year'] = df['Date'].dt.dayofyear

# Predictive analytics
X = df[['Temperature', 'Humidity', 'Wind Speed', 'Day_of_Year']]
y = df['Precipitation']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Building the model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Visualization
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Precipitation')
plt.ylabel('Predicted Precipitation')
plt.title('Actual vs Predicted Precipitation')
plt.show()

# Outputting model performance
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
