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
class FinCalc():
    def __init__(self):
        self.assets = []

        # weightings = np.array([1.0])

        self.stockStartDate = '2015-01-01'

        self.today = datetime.today().strftime('%Y-%m-%d')

        self.df = pd.DataFrame()

        for stock in self.assets:
            self.df[stock] = web.DataReader(stock , data_source = 'yahoo' , start = self.stockStartDate , end = self.today)['Adj Close']


        self.title = 'Daily Percentage Change'

        self.my_stocks = self.df

        # self.stdev = self.df.std()
        # print(self.stdev)

    #create and plot graph (loops through each column)
    def daily_returns(self):
        for columns in self.my_stocks.columns.values:
            self.my_stocks[columns] = self.my_stocks[columns].pct_change(periods = 1)
            plt.plot(self.my_stocks[columns] , label = self.my_stocks)


        plt.title(self.title)
        plt.xlabel('Data' , fontsize= 18)
        plt.ylabel('Daily Percentage Change' , fontsize= 18)
        plt.legend(self.my_stocks.columns.values , loc = 'upper left')
        plt.show()

    # def return_distribution():