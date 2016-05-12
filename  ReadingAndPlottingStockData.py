# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:48:08 2016
CHapter 1 of udacity course - Machine Learning for Trading
@author: Coffee
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read csv file and print some of the rows
def test_run():
    df =  pd.read_csv("data/AAPL.csv")
    print df # print entire dataframe
    print df.head() # view top 5 lines of csv  
    print df.tail() # view last 5 row     
    print df[10:21] #  rows between 10 and 20, last one is exclusive
    
    
# Function to find maximum Closing values for some stocks data
def get_max_close(symbol):
    df2 = pd.read_csv("data/{}.csv".format(symbol)) # read in data
    return df2['Close'].max() # compute maximum closing price
    
def test_run2():
    for symbol in ['AAPL', 'IBM']:
        print "Max Close"
        print symbol, get_max_close(symbol)
    
# Function to calculate average volume transfer during the period
def get_mean_volume(symbol):
    df3 = pd.read_csv("data/{}.csv".format(symbol))
    return df3['Volume'].mean() # calculate the avergae using mean()
        
def test_run3():
    for symbol in ['AAPL', 'IBM']:
        print "Mean Volume"
        print symbol, get_mean_volume(symbol)


# Function to plot the data
def test_run4():
    df4 = pd.read_csv("data/AAPL.csv")
    print df4['Adj Close']
    df4['Adj Close'].plot()
    plt.show() # called to show plot
    # as data is in reverse order the data is in deacreasing
    
# Function to plot High Prices of IBM
def test_run5():
    df5 = pd.read_csv("data/IBM.csv")
    df5['High'].plot()
    plt.show()
    
# Function to plot two variables    
def test_run6():
    df6 = pd.read_csv("data/AAPL.csv")
    df6[['Close','Adj Close']].plot()
    plt.show()
    
# Main function 
if __name__ == "__main__":
    test_run()
    test_run2()
    test_run3()
    test_run4()
    test_run5()
    test_run6()