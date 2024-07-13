import yfinance as yf
import streamlit as st
import datetime



col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter the start date", datetime.date(2019, 1, 1))
with col2:
    end_date = st.date_input("Enter the end date", datetime.date(2020, 1, 1))

ticket_symbol = st.text_input("Enter the Stock Symbol", "AAPL", key="placeholder")
ticker_data = yf.Ticker(ticket_symbol)

ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

st.write(f"""{ticket_symbol}'s EOD Price""")
st.dataframe(ticker_df)
st.write(f"""{ticket_symbol}'s Daily Closing Price Chart""")
st.line_chart(ticker_df.Close)




