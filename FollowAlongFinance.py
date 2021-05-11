#attemps to optimize user portfolio 

from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

#stocks
assets = [  'FB' , 'AMZN' , 'NFLX' , 'GOOG' , 'AAPL' , 'AMD' , 'CX' ]


#weightings
weights = 1 / len(assets)
weightings = np.array([weights for x in range(len(assets))])


#get the stock / portfolio starting date 
stockStartDate = '2014-01-01'

#ending date (today)
today = datetime.today().strftime('%Y-%m-%d')

#Create dataframe to store adjusted close price
df = pd.DataFrame()

#store the adjusted close price into dataframe
for stock in assets:
    df[stock] = web.DataReader(stock , data_source = 'yahoo' , start = stockStartDate , end = today)['Adj Close']

#visully show stock / portfolio
title = 'Portfolio Adj. Close Price History'

#get stocks
my_stocks = df

#create and plot
for c in my_stocks.columns.values:
    plt.plot(my_stocks[c] , label = c)

plt.title(title)
plt.xlabel('Date')
plt.ylabel('Adj. Close Price')
plt.legend(my_stocks.columns.values , loc = 'upper left')
plt.show()

returns = df.pct_change()
print(returns)

print(weightings)