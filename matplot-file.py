import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
from matplotlib.finance import candlestick_ohlc
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

#data frame
df = web.DataReader('MSFT', 'google', dt.datetime(2012, 1, 1), dt.datetime(2017, 6, 6))

#resampling the data
df_ohlc = df[['Open', 'High', 'Low', 'Close']].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

#resetting date index
df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

#subplotting
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.xaxis_date()

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

plt.show()