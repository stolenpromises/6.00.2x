# -*- coding: utf-8 -*-
"""
How would you randomly generate an even number x, 0 <= x < 100? Fill out the
definition for the function genEven(). Please generate a uniform distribution
over the even numbers between 0 and 100 (not including 100).

Created on Sun Feb 21 12:17:23 2021

@author: nathan.m
"""

import random


def genEven():
    """Return a random integer within 0-99."""
    return random.randrange(0, 99, 2)  # step by 2, for only even integers


def deterministicNumber():
    """Deterministically return an even number between 9-21."""
    return 10  # by definition, just requires that the return is non-random

def stochasticNumber():
    """
    Stochastically return a uniformly distributed even number between 9-21.
    """
    x = random.randint(9, 21)
    if x % 2 == 0:  # we got an even number as a result
        return x
    else:
        return stochasticNumber()  # recursive call to attain an even result
