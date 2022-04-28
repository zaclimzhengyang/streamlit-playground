import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
shown are the stock **closing price** and ***volume*** of XPeng!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
ticker_symbol = 'XPEV'

# get data on this ticker
ticker_data = yf.Ticker(ticker_symbol)

#get the historical prices for this ticker
ticker_df = ticker_data.history(period='id', start='2021-10-01', end='2022-04-27')

st.write("""
## Closing Price
""")
st.line_chart(ticker_df.Close)

st.write("""
## Volume of Stock Traded 
""")
st.line_chart(ticker_df.Volume)

st.write("""
##  Upcoming Events
""")
st.write(ticker_data.calendar)


# having more # will result in the heading becoming smaller
# having the first # will result in the wording become bold
# having ** will result in wording becoming bold
