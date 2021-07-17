# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 12:28:20 2021

@author: nathan.m
"""

def solveit(test):
    """Find the abs value smallest int solution to a function.

    Test, a function that takes an int parameter and returns a Boolean

    Assumes there exists an int, x, such that test(x) is True

    Returns an int, x, with the smallest absolute value such that test(x) is
    True. In case of ties, return any one of them.
    """
    # begin counting from 0
    count = 0
    if test(0) is True:
        return 0
    count = 1
    while test(count) is not True:  # keep counting till we break or solve
        if test(count*-1) is True:  # check for a negative solution
            count = count*-1  # apply the negative
            break  # break out if the negative works
        count += 1  # add to the count
    return count
#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))