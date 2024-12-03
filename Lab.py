# IMPORTING THE REQUIRED LIBRARIES -->

import pandas as pd
import numpy as np

# INCLUDING THE FILE 

df = pd.read_csv('AQI_Data.csv')

# 1. Displaying the first 5 Rows

print(df.head(5))

# 2. Displaying the last 6 rows

print(df.tail(6))

# 3. Displaying the summary statistics for all NUMERIC columns

print(df.describe())

# 4. Using Numpy to compute the mean AQI, PM2.5, and PM10 values for each city

cities = df['City'].unique()

mean_values_np = {
    city: {
        'AQI': np.mean(df.loc[df['City'] == city, 'AQI']),
        'PM2.5': np.mean(df.loc[df['City'] == city, 'PM2.5']),
        'PM10': np.mean(df.loc[df['City'] == city, 'PM10'])
    }
    for city in cities
}

data = pd.DataFrame(mean_values_np).T # .T is for transposing
print(data)

# 5. Display all rows where the city is 'Delhi'

Delhi_Rows = df[df['City'] == 'Delhi']
print(Delhi_Rows)

# 6. Display the first 10 rows, showing only the columns City, AQI, and PM2.5

print(Delhi_Rows[['City', 'AQI', 'PM2.5']].head(10))

# 7. Using NumPy to filter out and display rows where AQI > 300 and PM10 > 200

aqi_filter = np.logical_and(Delhi_Rows['AQI'] > 300, Delhi_Rows['PM10'] > 200)
print(Delhi_Rows[aqi_filter])