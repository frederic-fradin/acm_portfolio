import os
import streamlit as st
import yfinance as yf
from datetime import date, timedelta
from src.data_loading import visualize_data

def main():
    directory = os.path.dirname(os.path.abspath(__file__))

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

    st.header("Portfolio summary", divider="gray")

    col1, col2, col3 = st.columns([6.75, 0.25, 1.50])

    with col3:
        st.write('')
        st.write('')
        ticker = st.text_input(label='Ticker (; separator)', key='tick1')
        list_ticker = ticker.split(';')
        default_start = date.today() - timedelta(days=90)
        date_start = st.date_input(label='Start', key='tick2', format='YYYY-MM-DD', value=default_start)
        date_end = st.date_input(label='End', key='tick3', format='YYYY-MM-DD')
        load_button = st.button(label='UPDATE', key='tick5', use_container_width=True)

        if load_button:
            col1.write('')
            col1.write('')
            col_metric = col1.columns(len(list_ticker))
            for tick in list_ticker:
                ticker = yf.Ticker(tick)
                ticker_target = ticker.analyst_price_targets
                ticker_index = list_ticker.index(tick)
                col_metric[ticker_index].metric(label=tick, value=round(ticker_target['current'],2))

            for tick in list_ticker:
                fig, markdown_content, ticker_target, data = visualize_data(tick, date_start, date_end, '1d')
                
                with col1.container():
                    cola, colb, colc = st.columns([4, 0.25, 2.50])    
                    cola.plotly_chart(fig, use_container_width=True)
                    colc.write('')
                    colc.write('')
                    colc.write('**NEWS**')
                    colc.markdown(markdown_content)

                    with st.expander('Data'):
                        st.dataframe(data.reset_index(), use_container_width=True)

    
if __name__ == "__main__":
    main()