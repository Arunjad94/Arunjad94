import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Load a time series dataset
df = pd.read_csv(r'C:\Users\Akutty\Desktop\ARUN_Py/RAT_SET_POINT.csv')

# Convert 'Timestamp' column to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'].str.replace(' IST', ''), format='%d-%b-%y %I:%M:%S %p')

# Localize the datetime to a recognized timezone (assuming IST for now)
df['Timestamp'] = df['Timestamp'].dt.tz_localize('Asia/Kolkata')

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(df['Timestamp'], df['Value'], label='Original Time Series')
plt.title('Airline Passengers Time Series')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()

# Split the data into training and testing sets
train_size = int(len(df) * 0.8)
train, test = df.iloc[:train_size], df.iloc[train_size:]

# Fit an ARIMA model
order = (5, 1, 0)  # ARIMA(p, d, q) order
model = ARIMA(train['Value'], order=order)
fit_model = model.fit()

# Forecast future values
forecast_values = fit_model.predict(start=len(train), end=len(train) + len(test) - 1, typ='levels')

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(train['Timestamp'], train['Value'], label='Training Data')
plt.plot(test['Timestamp'], test['Value'], label='Test Data')
plt.plot(test['Timestamp'], forecast_values, label='ARIMA Forecast', color='red')
plt.title('ARIMA Forecasting')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.legend()
plt.show()



