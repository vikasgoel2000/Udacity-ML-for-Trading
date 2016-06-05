# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 17:00:34 2016

@author: Coffee
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

def symbol_to_path(symbol,base_dir="data"):
     return os.path.join(base_dir, "{}.csv".format(str(symbol)))
 
def get_data(symbollist, dates):
     df_final = pd.DataFrame(index = dates)
     if "SPY" not in symbollist:
         symbollist.insert(0,"SPY")      
     for symbol in symbollist:
         file_path =  symbol_to_path(symbol)
         df_temp = pd.read_csv(file_path, index_col='Date', parse_dates = True, usecols=['Date','Adj Close'], na_values=['nan'])
         df_temp = df_temp.rename(columns = {'Adj Close': symbol})
         df_final = df_final.join(df_temp)
         if symbol == "SPY":
             df_final = df_final.dropna(subset=["SPY"])             
     return df_final
      
def test_run():
    #symbols = ["PSX","FAKE1","FAKE2"]
    symbols = ['FAKE2']
    start = '2005-12-31'
    end = '2014-12-07'
    idx = pd.date_range(start,end)
    df_data = get_data(symbols,idx)
    #to fill missing data
    df_data.fillna(method="ffill",inplace="TRUE")
    df_data.fillna(method="bfill",inplace="TRUE")
    df_data.plot()
    plt.show()
    
def quiz():
    symbols = ["JAVA","FAKE1","FAKE2"]
    start = '2005-12-31'
    end = '2014-12-07'
    idx = pd.date_range(start,end)
    df_data = get_data(symbols,idx)
    #to fill missing data
    df_data.fillna(method="ffill",inplace="TRUE")
    df_data.fillna(method="bfill",inplace="TRUE")
    df_data.plot()
    plt.show()

def plot(df_data):
    ax = df_data.plot(title="incomplete data",fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    
if __name__ == "__main__":
    test_run()
    quiz()