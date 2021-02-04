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
    cargo_history : list
        A list of lists. Each inner list represents a round trip transport
        operation. Payloads are identified via unique_payload parameter passed
        in at runtime. Each trip orders heavier payloads first. Arbitrary
        tiebreak and trip order.
            example:
                cargo_history = [[pl1, pl2], [pl3, pl4]]
    """
    # helper function to allow for sorting the dictionary by value
    def valuetarget(x):
        return x[1]

    # convert the input dictionary into a dictionary sorted by weight
    sorted_dict = {key: value for (key, value) in sorted(input_dict.items(), key = valuetarget, reverse=True)}
    print('transport beginning. sorted_dict is ', sorted_dict)
    cargo_history = []  # initiate the list of lists
    # run a takeoff loop as long as there is remaining payload
    # iterations = 0
    while sorted_dict != {}:
    # while iterations <3:
        # iterations += 1
        # plane landed empty
        cargo = []
        cargo_weight = cargo_limit
        dict_trash_que = []  # prep a trash que for payload that we load
        # load payload biggest to smallest and don't exceed the cargo limit
        print('load payload loop begins')
        print()
        for i in sorted_dict:  # loop over remaining payload
            print('remaining payload loop beginning on ', i)
            if sorted_dict[i] <= cargo_weight:  # cargo room for payload
                print('there is cargo room')
                cargo.append(i)  # add the payload to cargo
                print('cargo appended. cargo is now ', cargo)
                cargo_weight -= sorted_dict[i]  # add the payload weight
                print('payload weight is added. cargo_weight is now ', cargo_weight)
        print('sorted dict removal loop beginning')
        for i in cargo:  # remove loaded payload
            print('dict_trash_que working on ', i)
            del(sorted_dict[str(i)])  # payload accounted for... remove
        print('trash que ending and sorted dict now is ', sorted_dict)
        cargo_history.append(cargo)  # record the delivery
        print('cargo_history now is ', cargo_history)

# sample dictionary for testing
sample = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
samplelimit = 10
print(greedy_cow_transport(sample, samplelimit))

#temp
cargo_weight = 10
test = ('Callie', 2)