"""
 Start with
 streamlit run ./src/streamlit_app.py
 """
import datetime
import logging

import streamlit as st
import models.train_model as tm
import numpy as np
import altair as alt
import visualization.visualize as vis
import pandas as pd


st.set_page_config(layout="wide")


def main():
    """
    Inserts a dropdown menu to select period of interest: Tomorrow / Next week
    Shows 2 tables with products and sales per period
    Shows 2 graphs with products and sales per period
    """
    today = '2020-03-01'
    dummy_data = tm.get_data_with_predictions_from_dummy_data()
    time_window = st.selectbox('Which timeframe do you want to show', (
        "Tomorrow",
        "Next Week"
    ))

    col1, col2 = st.columns([3, 5])
    with col1:
        st.header("Aggregated Predictions")
        df_input = articles_per_timeframe(dummy_data, today, time_window, True)
        st.dataframe(data=df_input, width=None)
        st.text('Visualization Descending')
        df_input_vis = articles_per_timeframe(dummy_data, today, time_window)
        bars = alt.Chart(df_input_vis).mark_bar().encode(x='amount:Q',y=alt.Y('products:O', sort='-x'))
        text = bars.mark_text(color='white').encode(text = 'amount:Q')
        rule = alt.Chart(df_input_vis).mark_rule(color = 'red').encode(x='mean(amount):Q')
        st.altair_chart(bars+text+rule, use_container_width=True)

    with col2:
        df_input = articles_per_timeframe(dummy_data, today, time_window, False)
        if time_window == "Tomorrow":
            st.header("predictions for tomorrow")
            df_daytime = df_input.drop(['date', 'weekday', 'holiday', 'h_type', 'weather', 'temp'], axis=1)
            df_daytime.set_index('daytime', inplace=True)
            df_daytime = df_daytime.apply(np.floor)
            df_daytime = df_daytime.transpose().reset_index(level=0)
            df_daytime.rename(columns={'index': 'products', 1: 'morning', 2: 'afternoon'}, inplace=True)
            df_daytime['sum'] = df_daytime['morning'] + df_daytime['afternoon']
            st.dataframe(data=df_daytime, width=None)
            # Add Chart for aggregated view 
            st.text('Visualization Tomorrow')
            bars = alt.Chart(df_daytime).transform_fold(
                ['morning', 'afternoon'],
                as_=['daytime', 'sum_of_sales']).mark_bar().encode(
                    x=alt.X('sum_of_sales:Q',
                        stack = 'zero',
                        scale= alt.Scale(domain=(0, 15), clamp= True)),
                    y=alt.Y('products:O', sort = '-x'),
                    color='daytime:N').interactive()
            st.altair_chart(bars, use_container_width=True)

        elif time_window == 'Next Week':
            st.header("predictions for next week")
            df_week = df_input.drop(['date', 'daytime', 'holiday', 'h_type', 'weather', 'temp'], axis=1)
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
            df_week['sum']= df_week.iloc[:,1:].sum(axis=1)
            st.dataframe(data=df_week, width=None)
            # Add Chart for aggregated view 
            st.text('Visualization next week')
            weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            bars = alt.Chart(df_week).transform_fold([
                'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
              as_=['weekday', 'sum_of_sales']).mark_bar().encode(
                  x=alt.X('sum_of_sales:Q',
                  stack = 'zero',
                  sort= weekday_order,
                  scale= alt.Scale(domain=(0, 100), clamp= True)),
                  y=alt.Y('products:O', sort= '-x'),
                  color= alt.Color('weekday:N', sort= weekday_order)).interactive()
            st.altair_chart(bars, use_container_width=True)


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
        df = filtered_df.drop(['date', 'daytime', 'weekday', 'holiday', 'h_type', 'weather', 'temp'], axis=1)
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
