import pandas as pd
from pandas import concat
from pandas import read_csv
from pandas import DataFrame
import datetime as dt
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

sales = read_csv("src/data/Bakery_Sales.csv")
sales = sales.rename(columns={'day of week': 'dayofweek'})

sales = sales.dropna(subset=['total'])
sales = sales.dropna(subset=['dayofweek'])
# sales_nonan2 = sales.dropna(how='all')
# sales_nonan3 = sales.dropna(thresh=5)

# Split first column in date and time and add as feature at the end
dateandtime = sales["datetime"]
sales[["date", "time"]] = dateandtime.str.split(pat=' ',  n=1, expand=True)

encoder = OneHotEncoder(sparse=False, categories=[['Mon','Tues','Wed','Thur','Fri','Sat','Sun']])
dayofweek_encoded =  encoder.fit_transform(sales[["dayofweek"]])
columns_name = encoder.get_feature_names_out()

print(columns_name)

dayofweek_encoded_pd = DataFrame(dayofweek_encoded, columns= ['Mon','Tues','Wed','Thur','Fri','Sat','Sun'])
sales = pd.concat([sales, dayofweek_encoded_pd], axis=1)

#print('rrr', sales['0  '])
#sales.rename(columns={sales.iloc[: , 29]: 'Mon'})#, '1': 'Tues', '2': 'Wed', '3': 'Thur', '4': 'Fri' ,'5': 'Sat','6': 'Sun'})

#print(sales)
#print(columns)
#for column in sales:
    #print(column)

print(sales)

print(type(sales))


sales = read_csv("src/data/Bakery_Sales.csv")
weather = read_csv("src/data/Seoul_weather.csv" , sep=";")
holidays = read_csv("src/data/public_holidays.csv", sep=";")

X=[sales,weather,holidays]

print(X[1])