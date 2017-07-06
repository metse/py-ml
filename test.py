import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start = dt.datetime(2016,1,1)
end = dt.datetime(2017,1,1)
source = 'google'

tickers = ['AAPL', 'SPY','MSFT']

df = web.DataReader(tickers, source, start, end)

def get_data():
    
    pass
    
def convert_to_time_series(ticker):
    close = df.ix['Close']
    
    weekdays = pd.date_range(start=start, end=end, freq='B')
    
    close = close.reindex(weekdays)
    
    close = close.fillna(method='ffill')
    
    result = close.ix[:, ticker]
    
    return result
    
def get_bands(rm, rstd):
    upper = rm + rstd * 2
    lower = rm - rstd * 2
    
    return upper, lower
    
def get_rolling_mean(ticker, window):
    return pd.rolling_mean(ticker, window=window)

def get_rolling_std(ticker, window):
    return pd.rolling_std(ticker, window=window)
    
def plot_data():
    
    aapl = convert_to_time_series(tickers[0])
    
    ma = get_rolling_mean(aapl, window=20)
    
    dev = get_rolling_std(aapl, window=20)
    
    upper_band, lower_band = get_bands(ma, dev)
    
    #We are plotting the time series
    ax = aapl.plot(title='Statistical Analysis of Apple Stock', label='AAPL')
    
    #first
    ma.plot(label='Rolling Mean', ax=ax)
    
    #second
    upper_band.plot(label='Upper Band', ax=ax)
    
    #third
    lower_band.plot(label='Lower Band', ax=ax)
    
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    
    ax.legend(loc='upper left')
    
    plt.show()

plot_data()