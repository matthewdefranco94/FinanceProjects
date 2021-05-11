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

#covariance matrix , 252 days in trading year
cov_matrix_annual = returns.cov() * 252
print(cov_matrix_annual) #diagonal matrix is our variance, all other are covariances

#calculate portolio variance
port_variance = np.dot(weightings.T , np.dot(cov_matrix_annual , weightings))
print("Portfolio variance " + str(port_variance))

#calculate portfolio volatility (st.dev)
port_volatility = np.sqrt(port_variance)
print("Portfolio volatility " + str(port_volatility))