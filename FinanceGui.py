import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data as web
import time
import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg , NavigationToolbar2Tk)
from FinProject import FinCalc
import csv



#########################################
#Some user input here , possibly a GUI for selecting stocks#
class StockSim():
    def __init__( self , width = 900 , height = 500 , instruction = ''):
        self.FinCalcs = FinCalc()

        self.Interface = tk.Tk()

        self.Interface.title("Daily Returns")
        self.Interface.geometry(str(width) + 'x' + str(height)) #WxH

        self.instructions = tk.Label(self.Interface , text = instruction)
        self.instructions.pack()

        self.asset_text_box = tk.Label(self.Interface , text = 'Stock Ticker: ')
        self.asset_text_box.pack()
        self.asset_text_box = tk.Entry(self.Interface)
        self.asset_text_box.pack()


        self.user_input = self.asset_text_box.get()

        print(self.user_input)


        self.input_button = tk.Button(self.Interface , text = 'Return Results')
        self.input_button.bind("<ButtonRelease>" , self.OnReturnResults)
        self.input_button.pack()
        

        self.Interface.mainloop()



    def OnReturnResults(self , event):
        input_list = self.asset_text_box.get()
        input_list = input_list.replace(' ' , "")
        input_list = input_list.split(",")

        self.FinCalcs.assets = input_list
        self.FinCalcs.daily_returns()
        

        # self.figure = self.plt.Figure(figsize = (6,5) , dpi = 100)
        # self.chart_type = FigureCanvasTkAgg(figure , Interface)
        # self.chart_type.get_tk_widget().pack()

        
    # def plots():
    #     break

Gui = StockSim()


