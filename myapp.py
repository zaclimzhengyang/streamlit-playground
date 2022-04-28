import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
shown are the stock **closing price** and ***volume*** of XPeng!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'XPEV'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2021-10-01', end='2022-04-27')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume of Stock Traded 
""")
st.line_chart(tickerDf.Volume)

st.write("""
##  Upcoming Events
""")
st.write(tickerData.calendar)


# having more # will result in the heading becoming smaller
# having the first # will result in the wording become bold
# having ** will result in wording becoming bold
