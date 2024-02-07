import statsmodels.api as sm
import pandas as pd

# Create a DataFrame with time series data
path = r'C:\Users\Dell\Downloads\RAT_SET_POINT.csv'
df = pd.read_csv(path)

# Fit an ARIMA model
model = sm.tsa.ARIMA(df['Value'], order=(1, 1, 1)).fit()

# Make predictions
forecast = model.forecast(steps=1)  # Adjust the number of steps as needed

print("Forecast:", forecast)


order = (1, 1, 1)  # Replace with appropriate order values
seasonal_order = (1, 1, 1, 12)  # Replace with appropriate seasonal order values
model = sm.tsa.statespace.SARIMAX(df['Value'], order=order, seasonal_order=seasonal_order)
results = model.fit()

# Make predictions
forecast_steps = 12  # Replace with the number of steps you want to forecast
forecast = results.get_forecast(steps=forecast_steps)
predictions = forecast.predicted_mean

merge_data = pd.concat([df,predictions], axis=1)
#merge_data.to_csv(r'C:\Users\Dell\Downloads\pridict_RAT_SET_POINT.csv', index=True)

print(predictions)
from datetime import datetime 
merge_data['Timestamp'] = merge_data['Timestamp'].str[:-6]
#TimeStamp
start_timestamp = merge_data.at[627, 'Timestamp']
start_timestamp = start_timestamp.replace('Dec', '12')
print(start_timestamp)
pandas_timestamp = pd.to_datetime(start_timestamp, format='%d-%m-%Y %H:%M:%S')
print(pandas_timestamp)

no_of_stamp = 10
dff = pd.DataFrame({'Timestamp':[start_timestamp + pd.Timedelta(minutes=15 * i)for i in range(no_of_stamp)]})
print(dff)

