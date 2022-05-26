"""
This module allows to encapsulate visualization methods. This visualization methods
are solely used in the UI of the savebread project.
"""
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Table View
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

def line_chart(dataframe):
    """
    TODO: Docstring
    """
  


def histogram(dataframe):
    """
    TODO: Docstring
    """
    pass


