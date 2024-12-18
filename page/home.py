import os
import streamlit as st
import yfinance as yf
from datetime import date, datetime, timedelta

from src import visualize_data

directory = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="MarketData - Portfolio",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
    )

# Adjust top padding
st.markdown("""
        <style>
                .block-container {
                    padding-top: 4rem;
                    padding-bottom: 4rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

col1, col2, col3 = st.columns([6.5, 0.5, 2])


with col3:
    ticker = st.text_input(label='Ticker (; separator)', key='tick1')
    list_ticker = ticker.split(';')
    date_start = st.date_input(label='Start', key='tick2', format='YYYY-MM-DD')
    date_end = st.date_input(label='End', key='tick3', format='YYYY-MM-DD')
    interval = st.selectbox(label='Interval', key='tick4',
                            options=['1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo'])
    load_button = st.button(label='UPDATE', key='tick5', use_container_width=True)

    if load_button:
        for tick in list_ticker:
            fig = visualize_data(tick, date_start, date_end, interval)
            col1.plotly_chart(fig, use_container_width=True)
        
        df = yf.download(list_ticker, start=date_start, end=date_end, interval=interval)
        col1.dataframe(df.reset_index(), use_container_width=True)
    
