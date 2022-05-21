import pandas as pd
from pandas import read_csv
import datetime as dt

def time_in_secs(timestring):
    pt = dt.datetime.strptime(timestring,'%H:%M')
    total_seconds = pt.minute*60 + pt.hour*3600
    return total_seconds

def get_dataset():
    #read in csv
    sales = read_csv("src/data/Bakery_Sales.csv")
    #sales.info

    #read in csv, needs separation by semicolon to read in
    weather = read_csv("src/data/Seoul_weather.csv" , sep=";")

    #read in csv, needs separation by semicolon to read in
    holidays = read_csv("src/data/public_holidays.csv", sep=";")
    #holidays

    #looking at different ways to get rid of "no a number"-Values
    #dropna subset, drops every row where subset-Value is NaN
    #dropna(how='all'), drops row if all values are NaN
    #dropna(thresh = m), drops row if at least m Values are NaN
    #nonan = no not a number (values)
    sales_nonan = sales.dropna(subset=['total'])
    sales_nonan2 = sales.dropna(how='all')
    sales_nonan3 = sales.dropna(thresh=5)
    sales = sales_nonan

    # Split first column in date and time and add as feature at the end
    dateandtime = sales_nonan["datetime"]
    sales_nonan[["date", "time"]] = dateandtime.str.split(pat = ' ',  n=1, expand = True)

    # add weekday column starting from 0 = Monday to 6 = Sunday 
    sales_nonan['weekday'] = pd.to_datetime(sales_nonan['date']).apply(lambda x: x.weekday())
    sales_nonan = sales_nonan.rename(columns = {'day of week':'dayofweek'})

    #drop datetime and place, only date is important not datetime
    sales_inprogress1 = sales_nonan.drop(['datetime','place'], axis=1)

    #convert time in seconds, so its easier to calculate with it
    #and set specific times

    time_col = sales_nonan['time']
    #time.strptime('00:00:00,000','%I:%M:%S')


    #set daytime borders
    sales_inprogress1['daytime']=time_col
    for i in range(len(time_col)):
        if 39600 >= time_in_secs(time_col[i]) >= 25200:
            sales_inprogress1['daytime'][i] = 0
        elif 54000 >= time_in_secs(time_col[i]) > 39600:
            sales_inprogress1['daytime'][i] = 1
        elif 64800 >= time_in_secs(time_col[i]) > 54000:
            sales_inprogress1['daytime'][i] = 2
        else:
            sales_inprogress1['daytime'][i] = 3
        

    #looking if there are rows with morning sales or night sales
    important_cols = sales_inprogress1[['weekday','daytime']].copy()

    zero_daytime=[]
    for i in range(len(important_cols['daytime'])):
        if important_cols['daytime'][i]==0:
            zero_daytime.append(i)

    for i in zero_daytime:
        sales_inprogress1 = sales_inprogress1.drop(zero_daytime)

    #drop unnecessary columns
    sales_bproducts = sales_inprogress1.drop(['dayofweek', 'time', 'total'], axis=1) #'daytime' #'weekday'

    #rename weather for case_sensitive name
    #date needs to be written exactly the same in every merging dataframe
    weather.rename(columns = {'datetime' : 'date'}, inplace = True)
    holidays.rename(columns = {'Date' : 'date', 'type ': 'type'}, inplace = True)
    main_bakery = sales_bproducts.groupby(['date','daytime','weekday']).sum().reset_index()
    bakery_finished = pd.merge(main_bakery, weather, on="date", how='left')
    bakery_finished2 = pd.merge(bakery_finished, holidays, on="date", how="left")
    bakery_finished2_dropped = bakery_finished2.drop(['sunrise', 'sunset', 'conditions', 'description', 'Title', 'name'], axis=1)

    # bakery_finished2_dropped_type_finished = []
    # for i in range(len(bakery_finished2_dropped)):
    #     if bakery_finished2_dropped['type'][i] == "Season":
    #         bakery_finished2_dropped_type_finished.append(i)

    #bakery_finished2_dropped
    # for i in bakery_finished2_dropped_type_finished:
    #     bakery_finished2_dropped.drop(bakery_finished2_dropped.iloc[bakery_finished2_dropped_type_finished], inplace=True, axis=0)

    #into catcodes +1 so its from 0 to 6
    bakery_finished2_dropped = bakery_finished2.drop(['sunrise', 'sunset', 'conditions', 'description', 'Title', 'name'], axis=1)
    dummy = bakery_finished2_dropped
    dummy['type'] = dummy['type'].astype('category').cat.codes
    dummy['type'] = dummy['type'] + 1


    #make list with 1 if it is a holiday and 0 if it isnt
    #add list to dataframe as column

    holiday=[]
    for i in range(len(dummy)):
        if dummy['type'][i] !=0:
            holiday.append(1)
        else:
            holiday.append(0)

    dummy['holiday'] = holiday

    #icons into cat.codes
    dummy2 = dummy
    dummy2['icon'] = dummy2['icon'].astype('category').cat.codes

    dummy3= dummy2
    dummy3.rename(columns = {'icon' : 'weather', 'type': 'h_type'}, inplace = True)
    baker_sales_dataset = dummy3
    return baker_sales_dataset


