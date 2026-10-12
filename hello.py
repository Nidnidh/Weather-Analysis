import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

date_range = pd.date_range(start='2021-01-01', end='2023-12-31')

temperature = np.random.normal(loc=20, scale=10, size=len(date_range))
humidity = np.random.uniform(30, 100, size=len(date_range))
precipitation = np.random.exponential(scale=3, size=len(date_range))

temperature[np.random.choice(len(temperature),10, replace=False)]= np.nan
humidity[np.random.choice(len(humidity) , 10, replace=False)] = np.nan
precipitation[np.random.choice(len(precipitation) , 10 , replace=False)] = np.nan

raw_df = pd.DataFrame({
    'Date': date_range,
    'Temperature_C': np.round(temperature, 1),
    'Humidity_Pct': np.round(humidity, 1),
    'Precipitation_mm': np.round(precipitation, 1)
})


raw_df.to_csv('weather_data.csv', index=False)
df = pd.read_csv('weather_data.csv')
df = df.dropna()
df['Date']=pd.to_datetime(df['Date'])

temperature = df['Temperature_C'].values
humidity = df['Humidity_Pct'].values
precip = df['Precipitation_mm'].values

print("Temperature - Mean:", np.mean(temperature) , "Median:" , np.median(temperature), "Std:" , np.std(temperature))
print("Humidity-Mean:" , np.mean(humidity))
print("Precipitation-Std Dev:" , np.std(precip))

df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')[['Temperature_C' , 'Humidity_Pct' , 'Precipitation_mm']].mean()
print(monthly_avg)

monthly_avg['Temperature_C'].plot(kind='line' , title='Average Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature')
plt.show()

monthly_avg['Precipitation_mm'].plot(kind='line' , title='Average Monthly Precipitation')
plt.xlabel('Month')
plt.ylabel('Precipitation')
plt.show()

plt.hist(df['Temperature_C'], bins=20, color='skyblue' , edgecolor='black')
plt.title('Temperature Dritribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.show()