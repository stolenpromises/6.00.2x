# -*- coding: utf-8 -*-
"""
Problem set 1 covering lectures 1-3.

A three part problem set involving the transport of items via competing
optimization models.

Part 1: a greedy algorithm
Part 2: a brute force algorithm
Part 3: algorithm comparison

Created on Sat Jan 30 20:29:33 2021

@author: nathan.m
"""
import itertools


def greedy_cow_transport(input_dict, cargo_limit):
    """
    Optimizes a multi-part transport operation.

    Parameters
    ----------
    input_dict : dict
        dictionary matching payload item names to weights(in tons).
            example entry/types/max values:
                {unique_payload: 100}
                {str: int}
                {n/a: 0-100}
    cargo_limit : int
        weight limit per transport operation

    Returns
    -------
    list_of_lists : list
        A list of lists. Each inner list represents a round trip transport
        operation. Payloads are identified via unique_payload parameter passed
        in at runtime. Each trip orders heavier payloads first. Arbitrary
        tiebreak and trip order.
            example:
                list_of_lists = [[pl1, pl2], [pl3, pl4]]
    """


    # convert the input dictionary into a dictionary sorted by weight
    sorted_dict = input_dict.
    itertools.combinations(input_dict, r)
    dict.items
    sorted()
    
# sample dictionary for testing
sample = {'lpha': 550, 'beta': 1000}
print(sorted(sample))
print(sample['beta'])
for i in sample:
    print(i)
print(sample.values())
sample.items()

sorted_dict = {key:value for (key,value) in sorted(sample.items())}

PyDict_Copy(sample)
sample.copy
sorted(sample, key=sample.__getitem__)
sorted_dict[key, value for (key, value) in sorted(sample.items())]
[[key, value] for (key, value) in sorted(sample.items())]

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
print(double_dict1)

{'e': 10, 'a': 2, 'c': 6, 'b': 4, 'd': 8}

