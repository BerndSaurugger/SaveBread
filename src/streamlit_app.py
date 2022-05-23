# Start with
# streamlit run ./src/streamlit_app.py
import streamlit as st
import models.train_model as train_model
import numpy as np

st.set_page_config(layout="wide")


def articles_per_timeframe():
    st.text('Data Frame 1')
    df_after_today = dummy_data[dummy_data.date > today]

    time_window = st.selectbox('Which timeframe do you want to show', (
        "Tomorrow",
        "Next Week",
        "Next 4 Weeks"
    ))
    if time_window == "Tomorrow":
        filtered_df = df_after_today[df_after_today.date == '2020-03-02']
    elif time_window == 'Next Week':
        filtered_df = df_after_today[df_after_today.date <= '2020-03-09']
    elif time_window == 'Next 4 Weeks':
        filtered_df = df_after_today[df_after_today.date < '2020-03-30']

    # filtered_df = filtered_df.sum()
    df = filtered_df.drop(['date', 'daytime', 'weekday', 'holiday', 'h_type', 'weather', 'temp'], axis=1)
    df = df.sum().T
    df = df.apply(np.ceil)
    st.dataframe(df)


col1, col2 = st.columns(2)
today = '2020-03-01'

dummy_data = train_model.get_data_with_predictions_from_dummy_data()
with col1:
    articles_per_timeframe()

    st.text('Data Frame 2')
    st.dataframe(dummy_data)

with col2:
    st.text('Data Frame 3')
    st.dataframe(dummy_data)
    st.text('Data Frame 4')
    st.dataframe(dummy_data)
