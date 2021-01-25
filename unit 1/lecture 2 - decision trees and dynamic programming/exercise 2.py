# -*- coding: utf-8 -*-
"""
An alternative solution to exercise 1 which uses the itertools module.

Created on Fri Jan 22 18:13:09 2021

@author: nathan.m
"""

import itertools

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = iterable
    return itertools.chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for it in iterables:
        for element in it:
            yield element

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

return chain.from_iterable

set = ['a','b','c']



def rangeiterate(list):
    '''
    Iteratively ranges over the length of a list, returning said length
    '''
    for l in range(len(list)):
        return l

# build tuple combo 1
def firstlist(list):
    """
    Iteratively generates all tuple combinations of a list
    """
    for l in range(len(list)): # range over the length of the list
        lengthtuple = itertools.combinations(list, l) # create a tuple of that length
        for item in lengthtuple: # loop over the objects in that tuple
            yield item

# build tuple combo 2, excluding items found in combo 1
def secondlist(tuplecombo1, list):
    prunedlist = []
    for i in list: # loop over items in the original list
        if i not in tuplecombo1: # check that the item isn't in combo 1
            prunedlist.append(i) # append to the pruned list
    return firstlist(prunedlist)
        
# combine tuple combo 1 and 2 into a generated result
def combothelists():
            
        
    
    
    for l in range(len(list)): # range over the length of the list
        lengthtuple = itertools.combinations(set, l) # create a tuple of that length
        for item in lengthtuple: # loop over the objects in that tuple
            yield item