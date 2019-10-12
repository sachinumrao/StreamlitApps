import datetime
import numpy as np
import pandas as pd
import streamlit as st
import yfinance as yf 
import plotly.figure_factory as ff
import matplotlib.pyplot as plt


# create title of page
st.title("Stocks Price Chart")

# create dropdown for selecting stocks
list_stocks = ['Apple', 'Microsoft', 'Tesla', 'Nvidia']

# the selected entry is stored in stock variable
st.subheader('Choose your stock')
stock = st.selectbox('', list_stocks)

# get the stock data
# first we need a dictionary for stock to ticker mapping

stock_ticker_map = {'Apple' : 'AAPL',
                    'Microsoft' : 'MSFT',
                    'Tesla' : 'TSLA',
                    'Nvidia' : 'NVDA'}


# set start and end date for which price to fetch
start_date = '2015-01-01'

# use yahoo finance to fecth data
@st.cache(ignore_hash=True)
def get_stock_data(stock):
    df = yf.download(stock, start_date)
    return df

# Preprocessing
df = get_stock_data(stock_ticker_map[stock])
df['Date'] = pd.to_datetime(df.index)
df = df.reset_index(drop=True)

# create heading above the plot
st.subheader('Closing price of %s' % stock)

# creating matplotlib plot
fig, ax = plt.subplots(1, 1)
ax.plot(df['Date'], df['Close'], color='#33adff', LineWidth=0.5)
ax.fill_between(df['Date'], 0, df['Close'], 
    facecolor='#33adff', alpha=0.4, interpolate=True)
plt.ylabel("Share Price in $")
plt.grid(True)
st.pyplot()

#st.area_chart(df[['Close']])
