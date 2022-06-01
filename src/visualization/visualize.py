"""
This module allows to encapsulate visualization methods. This visualization methods
are solely used in the UI of the savebread project.
"""
import streamlit as st


def table_viewer(dataframe):
    """
    Table creates a simple table object using input data from a
    dataframe.
    :param dataframe: dataframe with result predictions
    """
    if dataframe.empty:
        st.text("No predictions available.")
    else:
        st.dataframe(data=dataframe)

def line_chart(df_input_vis):
    """
    Table creates a simple chart displaying products & sales 
    using input data from a dataframe.
    :param dataframe: dataframe with result predictions
    """
    if dataframe.empty:
        st.text("No predictions available.")
    else:
        st.dataframe(data=df_input_vis) 

def bar_chart_day(df_daytime):
    """
    Creates a simple bar chart displaying sales predictions per tomorrow
    using input data from dataframe.
    :param dataframe: dataframe with result predictions
    """
    if dataframe.empty:
        st.text("No predictions available.")
    else:
        st.dataframe(data=df_daytime)  

def bar_chart_week(df_week):
    """
    Creates a simple bar chart displaying sales predictions per next week
    using input data from dataframe.
    :param dataframe: dataframe with result predictions
    """
    if dataframe.empty:
        st.text("No predictions available.")
    else:
        st.dataframe(data=df_week) 

