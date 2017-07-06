import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as dt

#statistical analysis of time-series data

def plot_data(msft, short_rolling, long_rolling):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    ax.plot(msft.index, msft, label='MSFT Stock')
    ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
    ax.plot(long_rolling.index, long_rolling, label='100 days rolling')
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    
    ax.legend()
    
    plt.show()
    
def convert_to_time_series(data, ticker, start, end):
    close = data.ix['Close']
    
    weekdays = pd.date_range(start=start, end=end, freq='B')
    
    close = close.reindex(weekdays)
    
    close = close.fillna(method='ffill')
    
    #time series
    result = close.ix[:, ticker]
    
    return result
    
    
def get_rolling_mean(values, window):
    #return rolling mean for given values
    return pd.rolling_mean(values, window=window)
    
def get_rolling_std(values, window):
    #return rolling deviation for given values
    return pd.rolling_std(values, window=window)
    
def get_bollinger_bands(rm, rstd):
    #return upper and lower band
    upper_band = rm + rstd * 2
    lower_band = rm - rstd * 2
    
    return upper_band, lower_band
    
def calculate_ma(ticker, start, end):
    
    #calculate moving averages of the closing prices
    short_rolling_ticker = ticker.rolling(window=100).mean()
    long_rolling_ticker = ticker.rolling(window=100).mean()
    
    plot_data(ticker, short_rolling_ticker, long_rolling_ticker)

def test_run():
    tickers = ['AAPL', 'MSFT', 'SPY']
    start = dt.datetime(2015,1,31)
    end = dt.datetime(2016,1,1)
    data = web.DataReader(tickers, 'google', start, end)
    
    #time series
    msft = convert_to_time_series(data, 'MSFT', start, end)
    
    rm_msft = get_rolling_mean(msft, window=20)
    
    rstd_msft = get_rolling_std(msft, window=20)
    
    upper, lower = get_bollinger_bands(rm_msft, rstd_msft)
    
    ax = msft.plot(title='Bollinger Bands', label='MSFT')
    rm_msft.plot(label='Rolling Mean', ax=ax)
    upper.plot(label='Upper band', ax=ax)
    lower.plot(label='Lower band', ax=ax)
    
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    
    ax.legend(loc='upper left')
    plt.show()

test_run()
    