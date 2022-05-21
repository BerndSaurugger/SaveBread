import pandas as pd
import datetime as dt


def time_in_secs(timestring):
    pt = dt.datetime.strptime(timestring, '%H:%M')
    total_seconds = pt.minute*60 + pt.hour*3600
    return total_seconds


def preprocess_datasets(sales, weather, holidays):
    # looking at different ways to get rid of "no a number"-Values
    # dropna subset, drops every row where subset-Value is NaN
    # dropna(how='all'), drops row if all values are NaN
    # dropna(thresh = m), drops row if at least m Values are NaN
    # nonan = no not a number (values)
    sales = sales.dropna(subset=['total'])
    # sales_nonan2 = sales.dropna(how='all')
    # sales_nonan3 = sales.dropna(thresh=5)

    # Split first column in date and time and add as feature at the end
    dateandtime = sales["datetime"]
    sales[["date", "time"]] = dateandtime.str.split(pat=' ',  n=1, expand=True)

    # add weekday column starting from 0 = Monday to 6 = Sunday
    sales['weekday'] = pd.to_datetime(sales['date']).apply(lambda x: x.weekday())
    sales = sales.rename(columns={'day of week': 'dayofweek'})

    # drop datetime and place, only date is important not datetime
    sales_inprogress = sales.drop(['datetime', 'place'], axis=1)

    # convert time in seconds, so its easier to calculate with it
    # and set specific times

    time_col = sales['time']
    # time.strptime('00:00:00,000','%I:%M:%S')

    # set daytime borders
    sales_inprogress['daytime'] = time_col

    for i in range(len(time_col)):
        if 39600 >= time_in_secs(time_col[i]) >= 25200:
            sales_inprogress['daytime'][i] = 0
        elif 54000 >= time_in_secs(time_col[i]) > 39600:
            sales_inprogress['daytime'][i] = 1
        elif 64800 >= time_in_secs(time_col[i]) > 54000:
            sales_inprogress['daytime'][i] = 2
        else:
            sales_inprogress['daytime'][i] = 3

    # looking if there are rows with morning sales or night sales
    important_cols = sales_inprogress[['weekday', 'daytime']].copy()

    zero_daytime = []
    for i in range(len(important_cols['daytime'])):
        if important_cols['daytime'][i] == 0:
            zero_daytime.append(i)

    for i in zero_daytime:
        sales_inprogress = sales_inprogress.drop(zero_daytime)

    # drop unnecessary columns
    sales_bproducts = sales_inprogress.drop(['dayofweek', 'time', 'total'], axis=1)  # 'daytime' 'weekday'

    # rename weather for case_sensitive name
    # date needs to be written exactly the same in every merging dataframe
    weather.rename(columns={'datetime': 'date'}, inplace=True)
    holidays.rename(columns={'Date': 'date', 'type ': 'type'}, inplace=True)
    main_bakery = sales_bproducts.groupby(['date', 'daytime', 'weekday']).sum().reset_index()
    bakery = main_bakery.merge(weather, on="date", how='left')
    bakery = bakery.merge(holidays, on="date", how="left")
    bakery = bakery.drop(
        ['sunrise', 'sunset', 'conditions', 'description', 'Title', 'name'],
        axis=1
    )

    bakery['type'] = bakery['type'].astype('category').cat.codes
    bakery['type'] = bakery['type'] + 1

    # make list with 1 if it is a holiday and 0 if it isnt
    # add list to dataframe as column

    holiday = []
    for i in range(len(bakery)):
        if bakery['type'][i] != 0:
            holiday.append(1)
        else:
            holiday.append(0)

    bakery['holiday'] = holiday

    # icons into cat.codes
    bakery['icon'] = bakery['icon'].astype('category').cat.codes
    bakery.rename(columns={'icon': 'weather', 'type': 'h_type'}, inplace=True)

    return bakery
