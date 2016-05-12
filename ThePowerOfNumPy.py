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

if __name__ == "__main__":
    test_run()