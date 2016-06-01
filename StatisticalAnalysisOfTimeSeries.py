# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 22:10:40 2016
01-04 Statistical analysis of time series Videos
@author: Coffee
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def test_run():
       #Define date range
    start_date = '2010-01-01'
    end_date = '2012-12-31'
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
    df1.plot()
    plt.show()
    
    #Print Mean
    print "\n Mean\n",df1.mean()
    print "\n Standard Deviaton\n", df1.std()
    print "\n Median\n", df1.median()
    
    df3 = df1.ix['2012-01-01':'2012-12-31','SPY']
    print df3
    ax = df3.plot(title = "SPY rolling mean", label ='SPY')
    rm_spy = pd.rolling_mean(df3, window =20)
    rm_spy.plot(label="Rolling mean",ax=ax)
    
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')
    plt.show()

    
if __name__ == "__main__":
    test_run()