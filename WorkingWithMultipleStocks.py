# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:33:51 2016

@author: Coffee
"""

import pandas as pd

def test_run():
    #Define date range
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates=pd.date_range(start_date,end_date)
    print dates
    print dates[0]
    
    #Create an empty dataframe with date as index
    df1 = pd.DataFrame(index=dates)
    print df1
    
    #Read SPY data into tempprary dataframe
    #Use index_col to change the index and parse_dates to convert date 
    #into DateTimeIndex object
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date",
                        parse_dates=True,
                        usecols=['Date','Adj Close'],na_values=['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})    
    print dfSPY
   
    #Join the two datafranes using DataFrame.join()
    df1 = df1.join(dfSPY) #LEFT JOIN by default
    # Drop NaN values
    df1=df1.dropna()
    # It can be done in one step by using Inner Joint  
    #i.e, set how = 'inner' in df1.join
    print df1
    
    #Read in more stocks
    symbols = ['GOOG','IBM','GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol),
                              index_col='Date',parse_dates=True,
                              usecols=['Date','Adj Close'],na_values=['nan'])
        #rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close':symbol})   
        print df_temp
        df1=df1.join(df_temp)
    
    print df1
    
def test_run2():
      #Define date range
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    dates=pd.date_range(start_date,end_date)
    print dates
    print dates[0]
    
    #Create an empty dataframe with date as index
    df1 = pd.DataFrame(index=dates)
    print df1
    
    #Read SPY data into tempprary dataframe
    #Use index_col to change the index and parse_dates to convert date 
    #into DateTimeIndex object
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date",
                        parse_dates=True,
                        usecols=['Date','Adj Close'],na_values=['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})    
    print dfSPY
   
    #Join the two datafranes using DataFrame.join()
    df1 = df1.join(dfSPY) #LEFT JOIN by default
    # Drop NaN values
    df1=df1.dropna()
    # It can be done in one step by using Inner Joint  
    #i.e, set how = 'inner' in df1.join
    print df1
    
    #Read in more stocks
    symbols = ['GOOG','IBM','GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol),
                              index_col='Date',parse_dates=True,
                              usecols=['Date','Adj Close'],na_values=['nan'])
        #rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close':symbol})   
        print df_temp
        df1=df1.join(df_temp)
    
    #SLice by row using Dataframe.ix[] selector
    print df1.ix['2010-01-01':'2010-01-31'] # january
    #Slice by columns
    print df1['GOOG']
    # slice by multiple columns
    print df1[['IBM','GLD']]
    
    #SLice using both row and column
    print df1.ix['2010-03-10':'2010-03-15',['SPY','IBM']] 


    
    
if __name__ == "__main__":
    test_run()
    test_run2()