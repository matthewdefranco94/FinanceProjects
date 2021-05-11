#attemps to optimize user portfolio 

from pandas_datareader import data as web
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
plt.style.use('fivethirtyeight')



#stocks
assets = [  'FB' , 'AMZN' , 'NFLX' , 'GOOG' , 'AAPL' , 'MT' , 'CX' , 'RACE' ]


#weightings
weights = 1 / len(assets)
weightings = np.array([weights for x in range(len(assets))]) #would apply the weightings to each element of the list above


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


#calculate portfolio volatility (st.dev)
port_volatility = np.sqrt(port_variance)


#calculate annual portfolio return
portfolioSimpleAnnualReturn = np.sum(returns.mean() * weights) * 252

#manual Shapre Ratio (Rp - Rf / StdevPort)
sharpe = portfolioSimpleAnnualReturn / port_volatility

print('Sharpe ratio : ' + str(round(sharpe)))


#Expected annual return , volatility (risk) , variance
percent_var = str(round(port_variance , 2)*100) + '%'
percent_vols = str(round(port_volatility , 2)*100) + '%'
percent_returns = str(round(portfolioSimpleAnnualReturn , 2 )*100) + '%'

print('Expected variance: ' + percent_var)
print('Expected volatility: ' + percent_vols)
print('Expected return: ' + percent_returns)

#portfolio optimization !
#expected returns and annualized sample covariance matrix of asset returns

mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

#get max sharpe ratio -- performance of an investment vs a 'risk-free' investment
eff = EfficientFrontier( mu , S )
weights = eff.max_sharpe()
clean_weights = eff.clean_weights()
print(clean_weights)
print(eff.portfolio_performance(verbose = True))

#get discrete allocation of each share per stock
from pypfopt.discrete_allocation import DiscreteAllocation , get_latest_prices

latest_prices = get_latest_prices(df)
weights = clean_weights
discreate_allo = DiscreteAllocation(weights , latest_prices , total_portfolio_value = 10000)
allocation , leftover = discreate_allo.lp_portfolio()
print('Discreate allocation: ' , allocation)
print('Leftover: ${:.2f}'.format(leftover))
