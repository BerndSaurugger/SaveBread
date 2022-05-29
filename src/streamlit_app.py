"""
 Start with
 streamlit run ./src/streamlit_app.py
 """
import datetime
import logging
from matplotlib.pyplot import axis
import streamlit as st
import models.train_model as tm
import numpy as np
# import visualization.visualize as vis


st.set_page_config(layout="wide")


def main():
    """
    TODO: Docstring
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
        st.text('Visualization 1')
        # df_inp_vis = articles_per_timeframe(dummy_data, today, time_window)
        # visualization.line_chart(df_inp_vis)
        # st.dataframe(data=df_input, width=None)

    with col2:
       #  st.header("Week predictions")
        df_input = articles_per_timeframe(dummy_data, today, time_window, False)
        if time_window == "Tomorrow":
            st.header("predictions for tomorrow")
            df_daytime = df_input.drop(['date', 'weekday', 'holiday', 'h_type', 'weather', 'temp'], axis=1)
            df_daytime.set_index('daytime', inplace=True)
            st.dataframe(data=df_daytime.transpose(), width=None)
            st.text('Visualization 2')
           # st.bar_chart(data=df_daytime,height=550)
        elif time_window == 'Next Week':
            st.header("predictions for next week")
            df_week = df_input.drop(['date', 'daytime', 'holiday', 'h_type', 'weather', 'temp'], axis=1)
            df_week = df_week.apply(np.floor)
            df_week = df_week.groupby('weekday').sum()
            st.dataframe(data=df_week.transpose(), width=None)
            # st.dataframe(data=df_week.transpose().apply(np.ceil), width=None)
            st.text('Visualization 2')
            # st.bar_chart(data=df_week,height=550)
        

def articles_per_timeframe(data, today, tw, agg=True):
    """
    TODO: Docstring
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
