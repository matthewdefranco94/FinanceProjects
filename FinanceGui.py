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
# from FinProject import *



#########################################
#Some user input here , possibly a GUI for selecting stocks#
class StockSim():
    def __init__( self , width = 900 , height = 400 , instruction = ''):
        self.Interface = tk.Tk()

        self.Interface.title("Daily Returns")
        self.Interface.geometry(str(width) + 'x' + str(height)) #WxH

        self.instructions = tk.Label(self.Interface , text = instruction)
        self.instructions.pack()

        self.input_label = tk.Label(self.Interface , text = 'Stock Ticker: ')
        self.input_label.pack()
        self.input_label = tk.Entry(self.Interface)
        self.input_label.pack()


        self.user_input = self.input_label.get()

        print(self.user_input)


        self.input_button = tk.Button(self.Interface , text = 'Return Results')
        self.input_button.bind("<ButtonRelease>" , self.stock_input)
        self.input_button.pack()
        

        self.Interface.mainloop()



    def stock_input(self , event):
        return self.input_label.get()
        

        # self.figure = self.plt.Figure(figsize = (6,5) , dpi = 100)
        # self.chart_type = FigureCanvasTkAgg(figure , Interface)
        # self.chart_type.get_tk_widget().pack()



        
    # def plots():
    #     break

Gui = StockSim()
