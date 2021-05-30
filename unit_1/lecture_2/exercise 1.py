# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 00:42:44 2021

@author: nathan.m
"""
def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list 
    of which item(s) are in each bag.

    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 0:
                bag1.append(str(items[j]))
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(str(items[j]))
        yield (bag1, bag2) 
items = ['a', 'b', 'c']
x = yieldAllCombos(items)
print(x.__next__())