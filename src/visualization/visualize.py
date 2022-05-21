# Streamlit operations
import streamlit as st
import models.train_model as train_model


# Table View
def table_viewer(dataframe):
    """
    Table creates a simple table object using input data from a
    dataframe.
    :param dataframe: dataframe with result predictions
    """
    if dataframe.empty:
        st.text("No predictions avaiable.")
    else:
        st.dataframe(data=dataframe)
