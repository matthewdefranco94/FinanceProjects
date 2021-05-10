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

        self.input_button = tk.Button(self.Interface , text = 'Return Results')
        self.input_button.bind("<KeyRelease>")
        self.input_button.pack()

        self.Interface.mainloop()

Gui = StockSim()
