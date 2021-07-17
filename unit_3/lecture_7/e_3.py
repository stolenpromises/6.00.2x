# -*- coding: ut==f-8 -*-
"""
Created on Sat Jul 17 01:38:07 2021

@author: nathan.m
"""

import numpy as np
import math


def stdDevOfLengths(L):
    """Take in a list of strings and outputs the std dev of their lengths.

    Parameters
    ----------
    L : list
        a list of strings

    Returns
    -------
    the std dev of the lengths of the strings

    or

    float('NaN')
    """
    if len(L) == 0:  # check for a blank list
        return float('Nan')
    elements = len(L)  # number of elements in the list of strings
    stringarray = np.array(L)  # convert list to array
    lengtharray = np.empty(0)  # initiate blank array of lengths
    for e in stringarray:  # iterate over the strings
        lengtharray = np.append(lengtharray, len(e))  # append string lengths
    mew = np.mean(lengtharray)  # mean of the string lengths
    var = 0  # variance
    for e in lengtharray:  # iterate over the array
        var += (e - mew)**2  # sum into variance
    var = var/elements  # variance result
    return math.sqrt(var)  # return the square root of the variance


# TEST CASES
L = ['a', 'z', 'p']
#L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))
