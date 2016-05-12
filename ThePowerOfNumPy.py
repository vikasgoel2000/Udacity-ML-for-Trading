# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:27:55 2016

@author: Coffee
"""

# Creating th NumPy arrays

import numpy as np

def test_run():
    # 1D array
    print np.array([2,3,4])
    # 2D array
    print np.array([(2,3,4),(5,6,7)])
    # empty array
    print np.empty(5)
    print np.empty((5,4)) #default is float
    print np.ones((5,4), dtype=np.int)
    
def random_numbers(): #generate number [0.0,1.0) 
    print np.random.random((5,4))
    print np.random.rand(5,4) #without using a tuple
    #from std. normal distribution
    print np.random.normal(size = (2,3))
    # with different mean and std. deviation
    print np.random.normal(50,10,size=(2,3))
    # random integers
    print np.random.randint(10) # a single integer in [0,10)
    print np.random.randint(0,10) # same aa above
    print np.random.randint(0,10, size =5) #5 random as 1D array
    # 2 D array    
    print np.random.randint(0,10, size=(3,4)) 
    
def array_attributes():
    a = np.random.random((5,4))
    print a
    print a.shape
    print a.shape[0] # no. of rows
    print a.shape[1] # no. of columns
    print len(a.shape) # dimension of shape tuple
    print a.size # no. of values in array
    print a.dtype
    
def array_operations():
    np.random.seed(693)  #seed the random no.
    a = np.random.randint(0,10,size=(5,4))
    print "Array: \n", a
    #Sum of all elements
    print "Sum of all the elements:", a.sum()   
    #Sum along rows or column, Axis =1:rows, Axis =0 :column
    print "Sum along rows", a.sum(axis=1)
    print "Sum along column", a.sum(axis=0)
    
    #Min,Max and Mean
    print "Minimum of each column:", a.min(axis=0)
    print "Maximum of each row:", a.max(axis=1)
    print "Mean of all elements:", a.mean()
    
if __name__ == "__main__":
    test_run()
    random_numbers()
    array_attributes()
    array_operations()