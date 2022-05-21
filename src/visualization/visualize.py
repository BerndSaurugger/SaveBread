# Imports for plotting
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit operations
import streamlit as st


# Table View
def Table_Viewer(dataframe):
    """
    Table creates a simple table object using input data from a
    dataframe.
    
    :param dataframe: dataframe with predictions
    """
    if dataframe.empty:
        st.text("No predictions avaiable.")
    else:
        st.dataframe(data=dataframe)