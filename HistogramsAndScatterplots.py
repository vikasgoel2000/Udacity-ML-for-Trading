# -*- coding: utf-8 -*-
"""
Created on Sun Jun 05 18:23:51 2016

@author: Coffee
"""

import matplotlib.pyplot as plt
import os
import pandas as pd

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
      
def plot(df_data):
    ax = df_data.plot(title="daily returns",fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Returns")
    plt.show()

def daily_return(df):
    daily_returns = (df/df.shift(1)) -1 #pandas library
    daily_returns.ix[0,:] = 0        
    return daily_returns
    
def test_run():
    symbols = ['SPY']
    start = '2009-01-01'
    end = '2012-12-31'
    idx = pd.date_range(start,end)
    df_data = get_data(symbols,idx)    
    plot(df_data)
    daily_returns = daily_return(df_data)
    plot(daily_returns)
    
    
if __name__ == "__main__":
    test_run()