"""
 Start with
 streamlit run ./src/streamlit_app.py
 """
import datetime
import logging

import streamlit as st
import numpy as np
from models import train_model as tm
import visualization.visualize as vis


st.set_page_config(layout="wide")


def main():
    """
    Inserts a dropdown menu to select period of interest: Tomorrow / Next week
    Shows 2 tables with products and sales per period
    Shows 2 graphs with products and sales per period
    """
    today = '2020-03-01'
    dummy_data = tm.get_data_with_predictions_from_dummy_data()

    # setup logo and header
    col1, mid, col2 = st.columns([1, 1, 20])
    with col1:
        st.image('SAveBreadLogo.png', width=100)
    with col2:
        st.header('SaveBread Planning Tool')
        st.write('The SaveBread Planning Tool shows a prediction '
                 'of sales per product for tomorrow or next week. '
                 'This helps the bakery manager to plan the production '
                 'of the products according to the market demands. '
                 'The target of this tool is to show the predicted sales per product'
                 ' with the purpose to save bread from being wasted due to over-production.')

    time_window = st.selectbox('Which timeframe do you want to show', (
        "Tomorrow",
        "Next Week"
    ))

    col1, col2 = st.columns([3, 5])
    with col1:
        st.header("Aggregated predictions")
        df_input = articles_per_timeframe(dummy_data, today, time_window, True)
        st.dataframe(data=df_input, width=None)
        st.text('Visualization Descending')
        df_input_vis = articles_per_timeframe(dummy_data, today, time_window)
        vis.line_chart(df_input_vis)

    with col2:
        df_input = articles_per_timeframe(dummy_data, today, time_window, False)
        if time_window == "Tomorrow":
            st.header("Predictions for tomorrow")
            df_daytime = df_input.drop(['date', 'weekday', 'holiday', 'h_type',
                                        'weather', 'temp'], axis=1)
            df_daytime.set_index('daytime', inplace=True)
            df_daytime = df_daytime.apply(np.floor)
            df_daytime = df_daytime.transpose().reset_index(level=0)
            df_daytime.rename(columns={'index': 'products',
                                       1: 'morning',
                                       2: 'afternoon'}, inplace=True)
            df_daytime['sum'] = df_daytime['morning'] + df_daytime['afternoon']
            st.dataframe(data=df_daytime, width=None)
            st.text('Visualization Tomorrow')
            vis.bar_chart_day(df_daytime)
        elif time_window == 'Next Week':
            st.header("Predictions for next week")
            df_week = df_input.drop(['date', 'daytime', 'holiday', 'h_type',
                                     'weather', 'temp'], axis=1)
            df_week = df_week.apply(np.floor)
            df_week = df_week.groupby('weekday').sum()
            df_week = df_week.transpose().reset_index(level=0)
            df_week.rename(columns={'index': 'products',
                                    0.0: 'Monday',
                                    1.0: 'Tuesday',
                                    2.0: 'Wednesday',
                                    3.0: 'Thursday',
                                    4.0: 'Friday',
                                    5.0: 'Saturday',
                                    6.0: 'Sunday'}, inplace=True)
            df_week['sum'] = df_week.iloc[:, 1:].sum(axis=1)
            st.dataframe(data=df_week, width=None)
            st.text('Visualization next week')
            vis.bar_chart_week(df_week)


def articles_per_timeframe(data, today, tw, agg=True):
    """
    Shows a df with products and sales per selected period: Tomorrow / Next Week
    """
    df_after_today = data[data.date > today]
    time_window = tw

    if time_window == "Tomorrow":
        filtered_df = df_after_today[df_after_today.date == '2020-03-02']
    elif time_window == 'Next Week':
        filtered_df = df_after_today[df_after_today.date <= '2020-03-09']
    if agg:
        df = filtered_df.drop(['date', 'daytime', 'weekday', 'holiday',
                               'h_type', 'weather', 'temp'], axis=1)
        df = df.transpose()
        df = df.apply(np.floor)
        df = df.sum(axis=1)
        df = df.reset_index(level=0)
        df.rename(columns={'index': 'products'}, inplace=True)
        df.columns = ['products', 'amount']
    else:
        df = filtered_df
    return df


@st.cache
def first_execution_date():
    """ Used so that reloading the web app doesn't create a new log file every time """
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")


def setup_logger():
    """
    TODO: Docstring
    """
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

    file_handler = logging.FileHandler(
        f'src/logs/savebread-{first_execution_date()}.log'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


if __name__ == '__main__':
    logger = setup_logger()
    main()
