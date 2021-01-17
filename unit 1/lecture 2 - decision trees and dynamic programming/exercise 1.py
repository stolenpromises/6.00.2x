# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 00:42:44 2021

@author: nathan.m
"""
def yieldAllCombos:
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list 
    of which item(s) are in each bag.
    """
if loadlist == []: # all items have been placed
    yield combo(1:2) # output list 1 and 2
else yieldAllCombos(loadlist) # recursive call on remaining items 