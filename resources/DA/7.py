import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Generate synthetic data
np.random.seed(42)
data = np.random.randn(100).cumsum()
time_series = pd.Series(data, index=pd.date_range(start='1/1/2000', periods=100, freq='M'))

# Plot original data
time_series.plot(title='Sample Time Series Data')
plt.show()

# Fit ARIMA(2,1,2)
model = ARIMA(time_series, order=(2, 1, 2))
model_fit = model.fit()

# Print summary and forecast
print(model_fit.summary())
forecast = model_fit.forecast(steps=10)
print("Forecasted Values:\n", forecast)

# Plot forecast
plt.plot(time_series, label='Original')
plt.plot(forecast, label='Forecast', color='red')
plt.title('ARIMA Forecast')
plt.legend()
plt.show()