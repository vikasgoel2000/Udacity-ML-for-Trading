# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:48:08 2016
CHapter 1 of udacity course - Machine Learning for Trading
@author: Coffee
"""
import pandas as pd

def test_run():
    df =  pd.read_csv("data/AAPL.csv")
    print df # print entire dataframe
    print df.head() # view top 5 lines of csv  
    print df.tail() # view last 5 row     
    print df[10:21] #  rows between 10 and 20, last one is exclusive
    
    
# Maximum Closing values for some stocks data
    
def get_max_close(symbol):
    df2 = pd.read_csv("data/{}.csv".format(symbol)) # read in data
    return df2['Close'].max() # compute maximum closing price
    
def test_run2():
    for symbol in ['AAPL', 'IBM']:
        print "Max Close"
        print symbol, get_max_close(symbol)
        
        
if __name__ == "__main__":
    test_run()
    test_run2()