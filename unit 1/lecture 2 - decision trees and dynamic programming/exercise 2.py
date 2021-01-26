# -*- coding: utf-8 -*-
"""
An alternative solution to exercise 1 which uses the itertools module.

Created on Fri Jan 22 18:13:09 2021

@author: nathan.m
"""

import itertools

def combogenerator(inputlist):
    """
    Generates all combinations of N items into two bags, whereby each 
    item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list 
    of which item(s) are in each bag.
    """
    for l in range(len(inputlist)): # range over the length of the list
        combo1possibles = itertools.combinations(inputlist, l) # length combo limit
        # now we are working with list1 possibilities
        for combination in combo1possibles: # loop over all list1 possibilities
            list1 = list(combination) # convert list1 combo from tuple to list
            prunedlist = [] 
            for i in inputlist: # loop over items in the full list
                if i not in list1: # check that the item isn't in combo1
                    prunedlist.append(i) # append to the pruned list
            # now we are working with list2 possibilties
            for l in range(len(prunedlist)): # range over the length of the list
                combo2possibles = itertools.combinations(prunedlist, l) # length combo limit
                # build combo of list 1 and 2 into a tuple and yield
                for combination in combo2possibles: # for each list2 possibility
                    yield (list1, list(combination)) # combine with list1 and yield
testset = ['a','b','c']          
x = combogenerator(testset)
print(x.__next__())