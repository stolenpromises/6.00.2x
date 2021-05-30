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
    # enumerate the 3**N possible combinations
    for i in range(3**N): # each integer represents a bag1/2 configuration
        bag1 = []
        print('bag1 is ,', bag1)
        bag2 = []
        print('bag2 is ,', bag2)
        if i == 0: # a special case for 0
            ternary = '0'
        else:
            ternary = find_ternary(i) # call for the ternary of the integer
        print('ternary is ', ternary)
        print('for j beginning')
        for j in range(N): # progress down the item list
            print('jloop beginning... j is', j)
            if ternary[j] == 1: # bit for item being in bag1
                bag1.append(items[j])
                print('appending ', items[j], 'to bag1')
            if ternary[j] == 2: # bit for item being in bag2
                bag2.append(items[j])
                print('appending ', items[j], 'to bag2')
            print('j loop ending')
        yield (bag1,bag2) # generate the bag1/2 configuration
def find_ternary(num):
    """
    Converts base 10 integers into a string of it's base 3 equivalent.

    Parameters
    ----------
    num : int - natural numbers only

    Returns
    -------
    str

    """
    quotient = num/3    #3
    remainder = num%3
    if quotient == 0:   #4
        return ""
    else:
        return find_ternary(int(quotient)) + str(int(remainder))    #5  

items = ['a', 'b', 'c']
x = yieldAllCombos(items)
print(x.__next__())
