import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data as web
import time
import tkinter as tk
from tkinter import *

#########################################

heart_CAT = ['AMD' , 'AAPL' , 'MT']
rows = 2
cols = 3
inde = 1

fig = plt.subplots(figsize = (10,5))

for i in heart_CAT:
    plt.subplot(rows , cols , inde)
    plt.title('{}'.format(i))
    plt.xlabel(i)
    inde = inde + 1

plt.show()



#########################################
class FinCalc():
    def __init__(self):
        self.assets = []

        # weightings = np.array([1.0])

        self.stockStartDate = '2015-01-01'

        self.today = datetime.today().strftime('%Y-%m-%d')

        self.stockDataFrame= pd.DataFrame()


    #create and plot graph (loops through each column)
    def daily_returns(self):
        for stock in self.assets:
            self.stockDataFrame[stock] = web.DataReader(stock , data_source = 'yahoo' , start = self.stockStartDate , end = self.today)['Adj Close']

        stdev = self.stockDataFrame.std()

        title = 'Daily Percentage Change'

        plt.close()

        self.my_stocks = self.stockDataFrame   
        for columns in self.my_stocks.columns.values:
            self.my_stocks[columns] = self.my_stocks[columns].pct_change(periods = 1)
            plt.plot(self.my_stocks[columns] , label = self.my_stocks)


        plt.title(title)
        plt.xlabel('Data' , fontsize= 18)
        plt.ylabel('Daily Percentage Change' , fontsize= 18)
        plt.legend(self.my_stocks.columns.values, loc = 'upper left')
        plt.show()

    # def return_distribution():
