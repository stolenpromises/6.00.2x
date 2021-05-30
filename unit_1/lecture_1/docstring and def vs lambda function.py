# -*- coding: utf-8 -*-
"""
Practice code written while reviewing pep257
docstring convention and def vs lambda functions.

Created on Wed Dec 30 04:30:57 2020

@author: nathan.m
"""

def is_even(i):
    """Evaluate if an integer is even.
    
    Keyword arguments:    
    i -- a positive integer
    
    Return defintions:
        
    True -- if i is even
    False -- otherwise
    """
    if i%2 == 0:
        return True
    else:
        return False