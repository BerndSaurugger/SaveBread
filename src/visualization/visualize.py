"""
This module allows to encapsulate visualization methods. This visualization methods
are solely used in the UI of the savebread project.
"""
import streamlit as st
import altair as alt


def line_chart(df_input_vis):
    """
    Table creates a simple chart displaying products & sales
    using input data from a dataframe.
    :param dataframe: dataframe with result predictions
    """
    bars = alt.Chart(df_input_vis).mark_bar().encode(
        x='amount:Q',
        y=alt.Y('products:O', sort='-x'))
    text = bars.mark_text(color='white').encode(text='amount:Q')
    rule = alt.Chart(
        df_input_vis).mark_rule(
        color='red').encode(x='mean(amount):Q')
    st.altair_chart(bars+text+rule, use_container_width=True)


def bar_chart_day(df_daytime):
    """
    Creates a simple bar chart displaying sales predictions per tomorrow
    using input data from dataframe.
    :param dataframe: dataframe with result predictions
    """
    bars = alt.Chart(df_daytime).transform_fold(
        ['morning', 'afternoon'], as_=['daytime', 'sum_of_sales']).mark_bar().encode(
        x=alt.X('sum_of_sales:Q',
                stack='zero',
                scale=alt.Scale(domain=(0, 15), clamp=True)),
        y=alt.Y('products:O', sort='-x'),
        color='daytime:N').interactive()
    st.altair_chart(bars, use_container_width=True)


def bar_chart_week(df_week):
    """
    Creates a simple bar chart displaying sales predictions per next week
    using input data from dataframe.
    :param dataframe: dataframe with result predictions
    """
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                     'Friday', 'Saturday', 'Sunday']
    bars = alt.Chart(df_week).transform_fold(
        ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        as_=['weekday', 'sum_of_sales']).mark_bar().encode(
            x=alt.X('sum_of_sales:Q', stack='zero',
                    sort=weekday_order,
                    scale=alt.Scale(domain=(0, 100), clamp=True)),
            y=alt.Y('products:O', sort='-x'),
            color=alt.Color('weekday:N', sort=weekday_order)).interactive()
    st.altair_chart(bars, use_container_width=True)
