# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib2
proxy = urllib2.ProxyHandler({'http': 'http://username:password@domain'})
auth = urllib2.HTTPBasicAuthHandler()
opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
urllib2.install_opener(opener)


import numpy as np
import pandas as pd
import pandas.io.data as web
goog = web.DataReader('GOOG', data_source='google', start='3/14/2009', end='4/14/2014')
goog.tail()

sp500 = web.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', end='4/14/2014')
sp500.info()